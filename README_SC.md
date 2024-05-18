# Steam图标修复 (Python)
## 说明文档
[English](https://github.com/brotherjie-win/steam-icon-fix/blob/main/README.md) | 简体中文 | [繁體中文](https://github.com/brotherjie-win/steam-icon-fix/blob/main/README_TC.md)
## 功能
修复Steam创建的桌面快捷方式丢失的异常情况，在重装系统或将已有游戏迁移到新电脑上时非常有用。
## Usage
### ⚠ 警告: 如果将Steam安装在了程序提供的C盘默认路径中("C:\Program Files (x86)\Steam" or "C:\Program Files\Steam"), 就必须使用管理员权限运行本程序或python.exe, 否则会被系统UAC权限控制阻止并报错：PermissionError: [Errno 13].  
### ℹ 说明: 目前正在试验使用一种无需更改代码的外置翻译的模块以使得翻译工作更加简单，该模块会尽快上线。
### 1. 直接使用打包后的程序文件（普通用户推荐）
1. 从[Releases](https://github.com/brotherjie-win/steam-icon-fix/releases/latest)下载打包好的程序文件，解压到适当的文件夹下。
2. 进入程序目录后运行"steam-icon-fix.exe"等待程序自动扫描Steam安装目录和库目录，然后自动下载图标。
3. 运行"rebuild_icon_cache.bat"重建图标缓存以使得所有图标都能够正确显示。运行注意保存所有的文件和进度，因为该操作会重启资源管理器进程。
### 2. 开发者和翻译人员
1. 确保在本地搭建好Python开发环境, 目前用于开发和测试该程序使用了Python 3.9和3.12版本。
2. 切换到代码目录下, 使用Conda, Virtualenv等工具创建开发用的虚拟环境。
3. 激活上面创建的虚拟环境, 在代码目录下运行"pip install -r requirements.txt"安装程序所需的依赖项。
4. 如需改变核心功能，请修改main.py文件, 修改iputils.py文件可以改变检测IP地址的方式和返回的显示语言类型, 翻译人员可以修改icon_translations.py来添加或修改翻译。  
5. 修改完成后运行"python main.py"测试效果。
6. 如果需要的话，运行"rebuild_icon_cache.bat"重建图标缓存以使得所有图标都能够正确显示。运行注意保存所有的文件和进度，因为该操作会重启资源管理器进程。
## 原理
### ℹ Info: 开始修复前, 程序会利用IP地址查询的API(优先使用国内服务器/使用国外服务器作为回退)来检测你的公共IPv4地址所在的大概的国家或地区, 然后根据规则使用不同的显示语言。 
目前支持的语言: 简体中文(中国大陆地区), 繁体中文(中国香港/澳门特别行政区和中国台湾地区) and 英语(其他国家和地区)。
1、程序首先自动按盘符字母顺序扫描默认的Steam安装目录(每个盘符下的"Program Files (x86)/Steam", "Program Files/Steam", "Steam"文件夹)有无steam.exe文件，有则作为Steam的安装目录。
2、若程序未在默认目录下发现Steam安装，需要用户手动指定Steam的安装目录，即steam.exe文件所在文件夹，并进行校验直到找到steam.exe文件。
3、程序会自动扫描Steam安装目录下steamapps文件夹中的Steam库配置文件libraryfolders.vdf（保存Steam库的位置和游戏的APPID），并读取所有游戏的APPID，若该文件损坏则无法修复。
4、扫描完成后程序会自动按照APPID检测Steam安装目录下steam/games文件夹中对应的游戏图标是否已经存在，若存在则跳过，否则在Steam网站上查询游戏的客户端图标并下载，下载完成后会提示状态，每个程序最多尝试5次。
## 特别注意
1. 当前版本仅支持Windows系统。
2. 有些游戏在Steam商店上架时没有提供对应的本地化名称翻译，因此这些游戏将直接显示英文名称。
3. Steam常见再发行文件不提供任何图标，因此会被自动跳过且没有提示。
## 代理服务器用户注意事项
### ❌ 错误: 如果不按照下列步骤修改Python urllib库使用的代理服务器地址，你可能会在基于urllib访问网站的任何Python程序上遇到 SSLEOFError(8, ‘EOF occurred in violation of protocol')错误。
### ℹ 问题原因 
如果你使用的代理服务器软件在设置系统代理时没有明确标明其使用的协议类型, urllib会默认代理服务器使用的协议类型和访问时提供的URI的协议相同. 例如, 访问HTTP网站时(URI开头是http://), 此时使用的代理服务器地址就是"http://<proxy_ip>:<proxy_port>". 相应的，会使用"https://<proxy_ip>:<proxy_port>"(URI开头是https://)或者"ftp://<proxy_ip>:<proxy_port>"(sites starting with ftp://)作为访问HTTPS和FTP站点时所用的代理服务器地址。因而如果你的代理服务器软件并不支持HTTPS和FTP代理协议的话，访问HTTPS和FTP网站的请求必然会因为握手失败而无法发送到代理服务器。
### ℹ 解决方法 
如果不需要代理服务器就能很容易的访问Steam的话，可以临时退出代理服务器软件以清除系统代理设置，然后重新运行程序即可解决问题。  
但是，如果依赖于代理服务器来访问Steam，请按照下列方法指定代理服务器的协议类型：
1. 前往"高级系统设置"模块，可以在运行(Win+R->Run)或命令行工具(如CMD/PowerShell)中输入SystemPropertiesAdvanced来打开。
2. 点击"环境变量"打开环境变量设置的选项卡。
3. 这里建议只需要添加用户变量就可以了, 因此点击上面一个"新建"按钮。
4. 如果用HTTP协议的代理服务器，需要添加以下三组用户变量（变量名:变量值）:    
(1)HTTP_PROXY:http://<proxy_ip>:<proxy_port>  
(2)HTTPS_PROXY:http://<proxy_ip>:<proxy_port>  
(3)FTP_PROXY:http://<proxy_ip>:<proxy_port>  
5. 在上面打开的窗口中一直点击"确定"，应用代理设置，然后重新运行程序即可解决问题。  

