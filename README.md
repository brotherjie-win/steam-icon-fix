# Steam Icon Fix (Python)
## Documentation
English | [简体中文](https://github.com/brotherjie-win/steam-icon-fix/blob/main/README_SC.md) | [繁體中文](https://github.com/brotherjie-win/steam-icon-fix/blob/main/README_TC.md)
## Function
Fix missing icons for Steam games and apps, especially useful when you reinstall Windows or migrate Steam games and apps to another computer.
## Usage
### ⚠ Warning: If you have installed your Steam on the default location("C:\Program Files (x86)\Steam" or "C:\Program Files\Steam"), you must run our program or python.exe  with prompted privilege, otherwise you will be blocked by UAC and got a PermissionError: [Errno 13] notice.  
### ℹ Info: A more convenient method without requring to modify Python codes for translating is under developing and will be released soon.
### 1. For Bundled Windows Program
1. Download bundled program archive from Releases, then extract to a proper location.
2. Switch to the folder, and simply run "steam-icon-fix.exe" and wait for steam folders scanning and missing icons downloading to process.  
3. Click and run "rebuild_icon_cache.bat" to rebuild Windows icon cache in order for all icons to display correctly. Remember to save all your files and progress as it will restart explorer.exe, which may restart some/all explorer. 
### 2. For Developers/Translators
1. Make sure you have properly configurate your Python environment, I am using Python 3.9 and 3.12 for developing and testing this program.
2. Switch to the code folder, then create a virtual enviroment using Conda, Virtualenv or etc.
3. Activate your virtual enviroment, then switch to the code folder and run "pip install -r requirements.txt" to solve all dependencies.
4. Changing main.py for modifying core functions, or changing iputils.py for changing displaying language behaviors when detecting a public IPv4 address from a certain country, or changing icon_translations.py for adding or modifying translations.  
5. Testing modified codes by running "python main.py".
6. Click and run "rebuild_icon_cache.bat" to rebuild Windows icon cache in order for all icons to display correctly if necessary. Remember to save all your files and progress as it will restart explorer.exe, which may restart some/all explorer.
## Principles
### ℹ Info: Before fixing icons, now our program will use an IP-lookup api (Preferred API in China/Intl API for fallback) to detect your public IPv4 address to get your approximate country/region, then choosing properly language for you. 
Supported language: Simplified Chinese(China Mainland), Traditional Chinese(Hong Kong/Macau SAR and Taiwan, China) and English(other countries/regions).
1. The program will scan all default Steam installation folder("Program Files (x86)/Steam", "Program Files/Steam", "Steam" of each disk), if it found steam.exe within these folders, it will continue.
2. If these folders do not exist or no steam.exe found within these folders, we will ask you to specify a valid location containg the steam.exe file and determine whether your input is valid. It will not continue fixing until detecting correct steam.exe file.
3. It will read the Steam library configuration file(libraryfolders.vdf), which containing all locations of Steam library and all APPIDs of games and apps installed by Steam on your computer, so this file must not be broken otherwise fixing is impossible.
4. After getting all APPID info, the program will try get the clienticon(in .ico format) filename and download icons to a subfolder named steam/games in your Steam installation folder.
## Special Notice
1. This program currently supports Windows OS platform only.
2. If some game or app does not provide a localized name, it will be displayed in English.
3. Steamworks Common Redistributables does not have any icons and will be automatically ignored.
## For proxy users
### ❌ Error: You may encounter SSLEOFError(8, ‘EOF occurred in violation of protocol') on any Python programs using urllib if you do not follow these steps to configurate proxy settings for Python urllib on Windows.
### ℹ Reason 
If proxy program does not specify the exact protocol it uses, urllib will assign the same protocol according to the URI you provided. For example, when accessing a HTTP site(starting with http://), it will chosee "http://<proxy_ip>:<proxy_port>" as proxy server address. Correspondingly, it will prefer "https://<proxy_ip>:<proxy_port>"(sites starting with https://) or "ftp://<proxy_ip>:<proxy_port>"(sites starting with ftp://) when accessing HTTPS and FTP sites.
### ℹ Fixes 
If you do not encounter connectivity issues when accessing Steam, you may simply quit your proxy programs and it will be ok then.  
But if you rely on a proxy to access Steam, following these steps:  
1. Go to "Advanced System Properties" by running SystemPropertiesAdvanced using Run or CMD Tools(CMD/PowerShell).
2. Click "Environment Variables" to open a new settings panel.
3. Personally, We suggest you to add user variables for this purpose only, click "New" button on the top.
4. You should add three variables as following(Variable value:Variable name) if using HTTP proxy:  
(1)HTTP_PROXY:http://<proxy_ip>:<proxy_port>  
(2)HTTPS_PROXY:http://<proxy_ip>:<proxy_port>  
(3)FTP_PROXY:http://<proxy_ip>:<proxy_port>  
5. Click "OK" on all opened setting panels to apply proxy settings, then it will be ok then.  
