import time
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import io
import threading

def getLinks(soup):
    i=soup.findAll(href=re.compile("^https://e-hentai.org/g/"))

    arr=[]
    for line in i:
        arr.append(line.get("href"))
    return arr

def saveURL(URL,threadNo,pageNo,totalPage):
    with io.open("out.txt","a",encoding="UTF-8") as f:
        try:
            f.write(URL+'\n')
        except:
            f.write("None"+'\n')
    with io.open("log.txt","a",encoding="UTF-8") as f:
        ans=str(totalPage-pageNo)
        f.write(str(threadNo)+"號執行續 第"+str(pageNo)+"頁 還剩"+ans+"頁 save:"+URL+'\n')
        print(str(threadNo)+"號執行續 第"+str(pageNo)+"頁 還剩"+ans+"頁 save:"+URL)
        # try:
        #     f.write(str(threadNo)+"號執行續 第"+str(pageNo)+"頁 還剩"+ans+"頁 save:"+URL+'\n')
        #     print(str(threadNo)+"號執行續 第"+str(pageNo)+"頁 還剩"+ans+"頁 save:"+URL)
        # except:
        #     f.write("None"+'\n')
        #     print()
        #     print(str(threadNo)+"號執行續 第"+str(pageNo)+"頁 還剩"+ans+"頁 save:ERROR"+("!"*30))

def job(s,rs,re,threadNo):
    browser=webdriver.Chrome()
    for time2 in range(rs,re):
        if time2==0:
            browser.get("https://e-hentai.org/"+s)
        else:
            browser.get("https://e-hentai.org/"+s+"/"+str(time2))
        time2=time2+1
        for l in getLinks(BeautifulSoup(browser.page_source,"html.parser")):

            saveURL(l,threadNo,time2,re)

#-----------------------------------
#main
#-----------------------------------

p_cnt=int(input("一共有幾頁要抓?ex:4339"))-1
t_cnt=int(input("你要開幾個執行緒?ex:5"))
s=input("你要抓甚麼?ex:doujinshi")
k=int(p_cnt/t_cnt)
l=int(p_cnt%t_cnt)
print("每個執行續有"+str(k)+"頁(k)")
print("有"+str(l)+"頁(l)交給主執行續")

# 建立 t_cnt 個子執行緒
threads = []
for i in range(t_cnt):
  threads.append(threading.Thread(target = job, args = (s,k*i,k*(i+1)-2,i)))
  threads[i].start()

# 主執行緒繼續執行自己的工作
print("Main thread:")
job(s,p_cnt-l,p_cnt,-1)

# 等待所有子執行緒結束
for i in range(t_cnt):
  threads[i].join()

print("Done.")
