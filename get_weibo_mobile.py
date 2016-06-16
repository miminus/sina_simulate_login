# -*- coding: utf-8 -*-
import requests
import json
import chardet
from bs4 import BeautifulSoup
import sys,time
# from __future__ import unicode_literals


s = requests.session()

headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Encoding": "gzip,deflate",
	"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Connection": "keep-alive",
	"Cache-Control":"max-age=0",
	"DNT":"1",
	"Host":"login.weibo.cn",
    "Referer": "http://login.weibo.cn/login/",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
}

headers1 = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Encoding": "gzip,deflate",
	"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Connection": "keep-alive",
	"DNT":"1",
	"Host":"weibo.cn",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
}

login_url = "http://login.weibo.cn/login/"

r1 = s.get(login_url)
# with open('d:/2.html','wb') as f:
    # f.write(r1.text)
    
all_content = BeautifulSoup(r1.text,'html5lib')

# vk = all_content.find_all('input')
# print len(vk)
form_action = all_content.find_all('form')[0].get('action')
vk = all_content.find_all('input',attrs={"name":"vk"})[0].get('value').strip()
capId = all_content.find_all('input',attrs={"name":"capId"})[0].get('value').strip()
img_url = all_content.find_all('img')[0].get('src')
passwd_id = all_content.find_all('input',attrs={'type':"password"})[0].get('name')

print form_action
print vk
print capId
print img_url
print passwd_id

# reload(sys)
# sys.setdefaultencoding('utf-8')

code = raw_input('input code:')
print chardet.detect(code)

data1 = {"backTitle":"ÊÖ»úÐÂÀËÍø",
         "backURL" : "http%3A%2F%2Fweibo.cn",
         "capId" : capId,
         "code" : code,
         "mobile" : "robbersun@sohu.com",
         passwd_id : "897fgCKdf",
         "submit" : "µÇÂ¼",
         "tryCount" : "",
         "vk" : vk,
         }
        
login_post_url = "http://login.weibo.cn/login/" + form_action
r2 = s.post(login_post_url,headers=headers,data=data1)
print r2.text
print r2.cookies
with open('d:/222.txt','wb') as f:
    f.write(r2.text)

page_num = 300
 
while page_num:
    weibo_url = "http://weibo.cn/chiaotunguniv?page=" + str(page_num) + "&vt=4&PHPSESSID="
    r3 = s.get(weibo_url, headers = headers1)
    
    file_path = 'E:/Own_things/weibo_sjtu/' + str(page_num) + '.html'
    with open(file_path,'wb') as f:
        f.write(r3.text)
    print 'got page' 
    page_num -=1
    # time.sleep(5)
    