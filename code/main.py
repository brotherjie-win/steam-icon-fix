import string
import os
import vdf
from steam.client import SteamClient
from urllib.request import urlretrieve

steam_client_icon_base_url = "https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/apps/"
default_steam_install_folder_list = ["Program Files (x86)/Steam", "Program Files/Steam", "Steam"]
steam_installation_folder = ""
steam_icon_folder = ""
all_game_id_list = []
max_retry = 5


def get_disklist():
    disk_list = []
    for ch in string.ascii_uppercase:
        disk = ch + ':/'
        if os.path.isdir(disk):
            disk_list.append(disk)
    return disk_list


def scan_steam_installation():
    global steam_installation_folder, steam_icon_folder
    if os.path.exists(os.path.join(steam_installation_folder, "steam.exe")):
        return True
    all_disk_list = get_disklist()
    for disk in all_disk_list:
        for install_folder in default_steam_install_folder_list:
            if os.path.exists(os.path.join(disk, install_folder, "steam.exe")):
                steam_installation_folder = os.path.join(disk, install_folder).replace("\\", "/")
                steam_icon_folder = os.path.join(steam_installation_folder, "steam/games").replace("\\", "/")
                return True
    print("未检测到Steam安装，请手动指定Steam安装目录")
    while not os.path.exists(os.path.join(steam_installation_folder, "steam.exe")):
        steam_folder = input("请输入Steam安装目录：")
        if not os.path.exists(os.path.join(steam_folder, "steam.exe")):
            print("输入的安装目录无效，请重新输入")
        else:
            steam_installation_folder = steam_folder
            steam_icon_folder = os.path.join(steam_installation_folder, "steam/games").replace("\\", "/")
    return True


def scan_steam_game_id():
    global all_game_id_list
    if not os.path.exists(os.path.join(steam_installation_folder, "steam.exe")):
        print("未设置Steam安装目录，开始主动扫描")
        scan_steam_installation()
    steam_lib_vdf = os.path.join(steam_installation_folder, "steamapps/libraryfolders.vdf").replace("\\", "/")
    if not os.path.exists(steam_lib_vdf):
        print("Steam游戏列表库文件损坏，无法继续")
        return False
    vdf_info_dict = vdf.load(open(steam_lib_vdf))
    for lib_id in vdf_info_dict['libraryfolders'].keys():
        current_lib_id_list = list(vdf_info_dict['libraryfolders'][lib_id]['apps'].keys())
        all_game_id_list.extend(current_lib_id_list)
    all_game_id_list = list(set(all_game_id_list))
    all_game_id_list = [int(gid) for gid in all_game_id_list]
    return True


def dl_all_game_icon():
    client = SteamClient()
    client.anonymous_login()
    assert client.logged_on
    for app_id in all_game_id_list:
        game_info = (client.get_product_info(apps=[app_id, ]))['apps'][app_id]['common']
        try:
            game_name = game_info["name_localized"]["schinese"]
        except KeyError:
            game_name = game_info["name"]
        if game_info["name"] == "Steamworks Common Redistributables":
            continue
        if "clienticon" in list(game_info.keys()):
            if os.path.exists(os.path.join(steam_icon_folder, game_info["clienticon"] + '.ico')):
                print("游戏 %s 程序图标已存在，跳过" % game_name)
                continue
            game_icon_url = steam_client_icon_base_url + str(app_id) + "/" + game_info["clienticon"] + '.ico'
            game_icon_filename = os.path.join(steam_icon_folder, game_info["clienticon"] + '.ico')
            trials = 0
            while trials < max_retry:
                try:
                    urlretrieve(game_icon_url, game_icon_filename)
                    break
                except:
                    trials += 1
                    print("游戏 %s 程序下载失败(第%d次)，重试中..." % (game_name, trials))
            if os.path.exists(game_icon_filename):
                print("游戏 %s 程序图标下载成功" % game_name)
            else:
                print("游戏 %s 程序下载失败" % game_name)
        else:
            print("游戏 %s 无程序图标，跳过" % game_name)
    return True


if __name__ == '__main__':
    scan_steam_installation()
    scan_steam_game_id()
    dl_all_game_icon()
