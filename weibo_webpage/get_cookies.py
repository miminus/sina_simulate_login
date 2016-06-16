# encoding=utf-8
import json
import base64
import requests

"""
�������΢���˺ź����룬��ȥ�Ա���һԪ�߸���
������ʮ����΢�����Ƶ��ϣ�̫Ƶ���˻����302ת�ơ�
������Ҳ���԰�ʱ��������㡣
"""
myWeiBo = [
    {'no': 'c525558@trbvm.com ', 'psw': 'test123'},
    # {'no': 'shudieful3618@163.com', 'psw': 'a123456'},
]


def getCookies(weibo):
    """ ��ȡCookies """
    cookies = []
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    for elem in weibo:
        account = elem['no']
        password = elem['psw']
        username = base64.b64encode(account.encode('utf-8')).decode('utf-8')
        postData = {
            "entry": "sso",
            "gateway": "1",
            "from": "null",
            "savestate": "30",
            "useticket": "0",
            "pagerefer": "",
            "vsnf": "1",
            "su": username,
            "service": "sso",
            "sp": password,
            "sr": "1440*900",
            "encoding": "UTF-8",
            "cdult": "3",
            "domain": "sina.com.cn",
            "prelt": "0",
            "returntype": "TEXT",
        }
        session = requests.Session()
        r = session.post(loginURL, data=postData)
        jsonStr = r.content.decode('gbk')
        info = json.loads(jsonStr)
        if info["retcode"] == "0":
            print "Get Cookie Success!( Account:%s )" % account
            cookie = session.cookies.get_dict()
            cookies.append(cookie)
        else:
            print "Failed!( Reason:%s )" % info['reason']
    return cookies


cookies = getCookies(myWeiBo)
print cookies
print "Get Cookies Finish!( Num:%d)" % len(cookies)