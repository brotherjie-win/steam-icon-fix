# Steam游戏图标修复
## 用途：修复Steam创建的桌面快捷方式丢失(白图标)的异常情况
## 用法：
### 方法一（内置环境，推荐）：
1、下载Release中的程序包压缩文件（当前仅支持Windows系统），并解压  
2、运行main.exe，程序会自动弹出命令窗口并扫描Steam安装目录/库目录，然后自动下载图标

### 方法二（编程方法）：
1、安装Python2.7以上或Python3.4以上的发行版本（推荐使用Python3）  
2、cd到代码文件夹所在目录下，运行pip install -r requirements.txt，安装依赖项steam[client]  
3、执行python main.py，程序会自动弹出命令窗口并扫描Steam安装目录/库目录，然后自动下载图标  

### 原理：
1、程序首先自动按盘符字母顺序扫描默认的Steam安装目录(每个盘符下的"Program Files (x86)/Steam", "Program Files/Steam", "Steam"文件夹)有无steam.exe文件，有则作为Steam的安装目录  
2、若程序未在默认目录下发现Steam安装，需要用户手动指定Steam的安装目录，即steam.exe文件所在文件夹，并进行校验直到找到steam.exe文件  
3、程序会自动扫描Steam安装目录下steamapps文件夹中的Steam库配置文件libraryfolders.vdf（保存Steam库的位置和游戏的APPID），并读取所有游戏的APPID，若该文件损坏则无法修复  
4、扫描完成后程序会自动按照APPID检测Steam安装目录下steam/games中对应的游戏图标是否已经存在，若存在则跳过，否则在Steam网站上查询游戏的客户端图标并下载，下载完成后会提示状态  

### 注意：
1、当前版本仅支持Windows系统  
2、有些游戏在Steam商店上架时没有提供对应的中文名称翻译，因此这些游戏将直接显示英文名称  
3、如果有些应用或游戏没有提供客户端图标（很罕见，几乎没有），下载时将会直接跳过并提示，Steam常见再发行文件会被自动跳过且不提示  
4、建议使用代理的用户手动配置环境变量，否则访问Steam网站时会出现SSL EOF错误8，设置方法：  
(1)Windows系统：在控制面板中打开高级系统设置（win8以上可以直接用搜索），选择环境变量，在用户变量中添加两条：变量名1：HTTP_PROXY，变量值1：包括协议的代理服务器地址；变量名2：HTTPS_PROXY，变量值2：包括协议的代理服务器地址  
(2)macOS/Linux系统：在终端中输入以下两条命令：命令1：export HTTP_PROXY="包括协议的代理服务器地址"；命令2：export HTTPS_PROXY="包括协议的代理服务器地址"；  
(3)注意：如果代理软件/服务器不支持HTTPS/FTP代理，只支持HTTP/SOCKS，请将协议设置为其中之一，如Clash(CFW)，设置为"http://" 或 "socks5://"开头的地址  

