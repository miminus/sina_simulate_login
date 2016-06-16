# -*- coding: utf-8 -*-

import requests
import json
s = requests.session()

headers = {
	"Accept": "*/*",
	"Accept-Encoding": "gzip,deflate",
	"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Connection": "keep-alive",
	"Cache-Control":"max-age=0",
	"DNT":"1",
	"Host":"www.dianping.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
    # "Referer": "http://www.dianping.com/account/iframeLogin?",
    # "X-Requested-With": 'XMLHttpRequest',
}

headers1 = {
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate",
	"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive",
	"DNT":"1",
	"Host":"www.dianping.com",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
	"Cookie":'cy=1; cye=shanghai; _hc.v="\"e7cb36cd-6094-4efe-828b-1695d340a726.1459240955\""; JSESSIONID=929A833CE27ED1BD076B6A6F2D2BB931; __utma=205923334.231696599.1459241083.1459241083.1459241083.1; __utmb=205923334.3.10.1459241083; __utmc=205923334; __utmz=205923334.1459241083.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHOENIX_ID=0a031c29-153c18c8fcc-43f9bbf'
}
headers2 = {
	"Accept": "*/*",
	"Accept-Encoding": "gzip,deflate",
	"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Connection": "keep-alive",
	"Content-Length" : "112",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"DNT":"1",
	"Host":"www.dianping.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
    "Referer": "http://www.dianping.com/account/iframeLogin?",
    "X-Requested-With": 'XMLHttpRequest',
}

headers3 = {
	"Accept": "*/*",
	"Accept-Encoding": "gzip,deflate",
	"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Connection": "keep-alive",
	"Content-Length" : "83",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"DNT":"1",
	"Host":"www.dianping.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
    "Referer": "http://www.dianping.com/account/iframeLogin?",
    "X-Requested-With": 'XMLHttpRequest',
}

headers4 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "DNT":"1",
    "Host":"t.dianping.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
}

r = s.post("http://www.dianping.com/account/ajax/getCaptcha",headers=headers1)
response_body = r.text
body_json = json.loads(response_body)
# print body_json
pic_url = body_json['msg']['url']
signature = body_json["msg"]["signature"]
print signature
print pic_url

pic_content = s.get(pic_url,stream=True).content
'''
将验证码保存下来
'''
with open('d:/pic.png','wb') as f:
    f.write(pic_content)
vcode = raw_input("input the code:")
#with open("pic1.jpg","wb") as f:
#    f.write(rr.text)
print vcode

checkChptcha_url = "http://www.dianping.com/account/ajax/checkCaptcha"
data = {"signature":signature,"vcode":vcode}
r2 = s.post(checkChptcha_url,data=data,headers=headers2)

print r2.text
body_json1 = json.loads(r2.text)
uuid = body_json1["msg"]["uuid"]
print uuid


UserVerify_url = "http://www.dianping.com/account/ajax/passwordLogin"
data_ = {"keepLogin":"on","password":"xxxx","username":"xxxxxxx","uuid":uuid}

r3 = s.post(UserVerify_url,data=data_,headers=headers3)
print r3.text

r4 = s.get('http://www.dianping.com/member/133518163',headers =headers )
with open('d:/123.txt','wb') as f:
    f.write(r4.text)
print 'got homepage'
    
    
    
r5 = s.get('http://www.dianping.com/search/category/1/30/g136o3p3',headers =headers )
with open('d:/1233.txt','wb') as f:
    f.write(r5.text)    
print 'got theator list'


r6 = s.get('http://www.dianping.com/shop/8435823',headers =headers )
with open('d:/12333.txt','wb') as f:
    f.write(r6.text) 
print 'got shop detail'
    

r7 = s.get('http://www.dianping.com/ajax/json/shop/movie/showlist?_nr_force=1459302409629&shopId=8435823&date=2016-04-01',headers =headers )
with open('d:/12333.txt','wb') as f:
    f.write(r6.text) 
print 'got one shop one day list'
    
    

r8 = s.get('http://t.dianping.com/movie/ajax/seatingPlan?movieShowId=80895052',headers=headers4)
with open('d:/123333.txt','wb') as f:
    f.write(r8.text) 
print 'got seated detail'









