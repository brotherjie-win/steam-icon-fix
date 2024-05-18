# Steam圖標修復 (Python)
## 說明文檔
[English](https://github.com/brotherjie-win/steam-icon-fix/blob/main/README.md) | [簡體中文](https://github.com/brotherjie-win/steam-icon-fix/blob/main/README_SC.md) | 繁體中文
## 功能
修復Steam創建的桌面快捷方式丟失的異常情況，在重裝系統或將已有遊戲遷移到新電腦上時非常有用。
## Usage
### ⚠ 警告: 如果將Steam安裝在了程序提供的C盤默認路徑中("C:\Program Files (x86)\Steam" or "C:\Program Files\Steam"), 就必須使用管理員權限運行本程序或python.exe, 否則會被系統UAC權限控製阻止並報錯：PermissionError: [Errno 13]。  
### ℹ 說明: 目前正在試驗使用一種無需更改代碼的外置翻譯的模塊以使得翻譯工作更加簡單，該模塊會盡快上線。
### 1. 直接使用打包後的程序文件（普通用戶推薦）
1. 從[Releases](https://github.com/brotherjie-win/steam-icon-fix/releases/latest)下載打包好的程序文件，解壓到適當的文件夾下。
2. 進入程序目錄後運行"steam-icon-fix.exe"等待程序自動掃描Steam安裝目錄和庫目錄，然後自動下載圖標。
3. 運行"rebuild_icon_cache.bat"重建圖標緩存以使得所有圖標都能夠正確顯示。運行註意保存所有的文件和進度，因為該操作會重啟資源管理器進程。
### 2. 開發者和翻譯人員
1. 確保在本地搭建好Python開發環境, 目前用於開發和測試該程序使用了Python 3.9和3.12版本。
2. 切換到代碼目錄下, 使用Conda, Virtualenv等工具創建開發用的虛擬環境。
3. 激活上面創建的虛擬環境, 在代碼目錄下運行"pip install -r requirements.txt"安裝程序所需的依賴項。
4. 如需改變核心功能，請修改main.py文件, 修改iputils.py文件可以改變檢測IP地址的方式和返回的顯示語言類型, 翻譯人員可以修改icon_translations.py來添加或修改翻譯。  
5. 修改完成後運行"python main.py"測試效果。
6. 如果需要的話，運行"rebuild_icon_cache.bat"重建圖標緩存以使得所有圖標都能夠正確顯示。運行註意保存所有的文件和進度，因為該操作會重啟資源管理器進程。
## 原理
### ℹ Info: 開始修復前, 程序會利用IP地址查詢的API(優先使用國內服務器/使用國外服務器作為回退)來檢測你的公共IPv4地址所在的大概的國家或地區, 然後根據規則使用不同的顯示語言。 
目前支持的語言: 簡體中文(中國大陸地區), 繁體中文(中國香港/澳門特別行政區和中國臺灣地區) and 英語(其他國家和地區)。
1、程序首先自動按盤符字母順序掃描默認的Steam安裝目錄(每個盤符下的"Program Files (x86)/Steam", "Program Files/Steam", "Steam"文件夾)有無steam.exe文件，有則作為Steam的安裝目錄。
2、若程序未在默認目錄下發現Steam安裝，需要用戶手動指定Steam的安裝目錄，即steam.exe文件所在文件夾，並進行校驗直到找到steam.exe文件。
3、程序會自動掃描Steam安裝目錄下steamapps文件夾中的Steam庫配置文件libraryfolders.vdf（保存Steam庫的位置和遊戲的APPID），並讀取所有遊戲的APPID，若該文件損壞則無法修復。
4、掃描完成後程序會自動按照APPID檢測Steam安裝目錄下steam/games文件夾中對應的遊戲圖標是否已經存在，若存在則跳過，否則在Steam網站上查詢遊戲的客戶端圖標並下載，下載完成後會提示狀態，每個程序最多嘗試5次。
## 特別註意
1. 當前版本僅支持Windows系統。
2. 有些遊戲在Steam商店上架時沒有提供對應的本地化名稱翻譯，因此這些遊戲將直接顯示英文名稱。
3. Steam常見再發行文件不提供任何圖標，因此會被自動跳過且沒有提示。
## 代理服務器用戶註意事項
### ❌ 錯誤: 如果不按照下列步驟修改Python urllib庫使用的代理服務器地址，你可能會在基於urllib訪問網站的任何Python程序上遇到 SSLEOFError(8, 'EOF occurred in violation of protocol')錯誤。
### ℹ 問題原因 
如果你使用的代理服務器軟件在設置系統代理時沒有明確標明其使用的協議類型, urllib會默認代理服務器使用的協議類型和訪問時提供的URI的協議相同. 例如, 訪問HTTP網站時(URI開頭是http://), 此時使用的代理服務器地址就是"http://<proxy_ip>:<proxy_port>". 相應的，會使用"https://<proxy_ip>:<proxy_port>"(URI開頭是https://)或者"ftp://<proxy_ip>:<proxy_port>"(sites starting with ftp://)作為訪問HTTPS和FTP站點時所用的代理服務器地址。因而如果你的代理服務器軟件並不支持HTTPS和FTP代理協議的話，訪問HTTPS和FTP網站的請求必然會因為握手失敗而無法發送到代理服務器。
### ℹ 解決方法 
如果不需要代理服務器就能很容易的訪問Steam的話，可以臨時退出代理服務器軟件以清除系統代理設置，然後重新運行程序即可解決問題。  
但是，如果依賴於代理服務器來訪問Steam，請按照下列方法指定代理服務器的協議類型：
1. 前往"高級系統設置"模塊，可以在運行(Win+R->Run)或命令行工具(如CMD/PowerShell)中輸入SystemPropertiesAdvanced來打開。
2. 點擊"環境變量"打開環境變量設置的選項卡。
3. 這裏建議只需要添加用戶變量就可以了, 因此點擊上面一個"新建"按鈕。
4. 如果用HTTP協議的代理服務器，需要添加以下三組用戶變量（變量名:變量值）:    
(1)HTTP_PROXY:http://<proxy_ip>:<proxy_port>  
(2)HTTPS_PROXY:http://<proxy_ip>:<proxy_port>  
(3)FTP_PROXY:http://<proxy_ip>:<proxy_port>  
5. 在上面打開的窗口中一直點擊"確定"，應用代理設置，然後重新運行程序即可解決問題。  
