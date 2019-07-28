### 討論社群
FB:
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
        pip install re
        pip install selenium

    成功就會長這樣:
    ![Alt text](/doc/1.PNG)
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
- 修改`點我開始抓圖.bat`檔案，將`##你的帳號`及`##你的密碼`分別取代成你的帳號跟你的密碼。
 - xeHentai的[Repositories](https://github.com/fffonion/xeHentai):