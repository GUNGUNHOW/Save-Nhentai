### 注意!!!!!

 - 更詳細的版本說明:https://docs.google.com/document/d/1Ob0lBubVXhEaBD6LCTR3bBm1ztwhzq7JaIHbSDvH4Jc/edit?usp=sharing
 
 - 上面的4.7M的xeHentai-2.0.1.9.exe是舊版，又稱「xeHentai-2.0.1.9.nesl.1」，不用登入就能下載

 - 登陸後才能下載原圖的xeHentai-2.0.1.9.nesl.2，約234MB:https://drive.google.com/open?id=1dz8pSNuSmzfDb2igy5dPujr_4rrYrrhn

但你要把bat改成這樣:

`xeHentai-2.0.1.9.exe  -u 你的帳號 -k 你的密碼 https://e-hentai.org/g/1030706/2dc8913f4b/`

 - 可以瘋狂開執行序的xeHentai-2.0.1.9.nesl.3，約234MB:https://drive.google.com/open?id=1dz8pSNuSmzfDb2igy5dPujr_4rrYrrhn

 - xeHentai-2.0.1.9.nesl.4.exe是我個人為了要讓圖片跟專案資料夾放不同地方而製，他是nesl.3的延伸，所以執行序很多
載點:https://drive.google.com/open?id=1yCXJaUIVBh26v2gaSwzqusqwELhQXoTH

所有都在這裡:https://drive.google.com/drive/u/0/folders/1tdEmW94OhLYhb7h8OfZAq0Zd7kxdnCPi

### 討論社群
FB:
https://www.facebook.com/groups/650130698824997

FB粉專:
https://www.facebook.com/Ex%E8%AE%8A%E6%85%8B%E7%81%BD%E5%AE%B3%E7%B7%8A%E6%80%A5%E6%87%89%E8%AE%8A%E5%B0%8F%E7%B5%84-103592190979897

Discord:
https://discordapp.com/channels/604240020479541248/604255172050288660

主交流頻(kekeke):
https://kekeke.cc/%E6%8B%AF%E6%95%91ex%E8%AE%8A%E6%85%8B

GitHub:
https://github.com/neslxzhen/Save-Nhentai

### Language
 - Python 3.7

### Import Package
 - bs4
 - selenium
 - re

### What is it?
抓E-Henati整個網站的連結，這些連結未來可以做很多應用，例如批次抓圖。

### How To Use?
 - 下載Python 3.7
 - 在 `系統管理員CMD` 中輸入

        pip install bs4
        pip install selenium

    成功就會長這樣:
    ![Alt text](/doc/1.PNG)
-  將 `系統管理員CMD` `cd`至專案資料夾
-  在 `系統管理員CMD` 中輸入
    `python CatchPageUrl.py`

    然後他會問你：

    - 一共有幾頁要抓?ex:4339:
        
        你就輸入你有幾頁要抓

    - 你要開幾個執行緒?ex:5:
        
        你就輸入你要開幾個執行緒，你輸入5，就會有6個執行序，因為使用Chrome，很吃記憶體

    - 你要抓甚麼?ex:doujinshi:
        
        輸入你想抓甚麼，全小寫。主要是抓主網址後面的分支:

        ![Alt text](/doc/2.PNG)

    之後的輸出都放在out.txt裡面，而log是詳細版

### 還需要甚麼功能
 - 把標籤爬下來，存成xml

### how to catch IMG
- 修改`點我開始抓圖.bat`檔案

 xeHentai的[Repositories](https://github.com/fffonion/xeHentai)

如果你是Save E-hentai的一員，請看公告：
https://docs.google.com/document/d/116BYuP_gta44vgcEihb4wLbmsDhDsKlQ58j5YuD4pE0/edit?usp=drivesdk
所有更新都以公告為主，要不然我要兩頭修
