# -*- coding: utf-8 -*-
# from __future__ import absolute_import, division, print_function#, unicode_literals

import re
import json
import base64
import binascii

import rsa
import requests


headers1 = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection':'keep-alive',
    'DNT' : '1',
    'Host' : 'login.sina.com.cn',
    'Referer' : 'http://weibo.com/?',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
}
# import logging
# logging.basicConfig(level=logging.DEBUG)


WBCLIENT = 'ssologin.js(v1.4.18)'
user_agent = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"',
)
session = requests.session()
session.headers['User-Agent'] = user_agent
session.headers['DNT'] = '1'
session.headers['Connection'] = 'keep-alive'
session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
session.headers['Accept-Encoding']='gzip, deflate'


def encrypt_passwd(passwd, pubkey, servertime, nonce):
    key = rsa.PublicKey(int(pubkey, 16), int('10001', 16))
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(passwd)
    passwd = rsa.encrypt(message.encode('utf-8'), key)
    return binascii.b2a_hex(passwd)


def wblogin(username, password):
    resp = session.get(
        'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&&checkpin=0&client=%s' % (base64.b64encode(username.encode('utf-8')), WBCLIENT))

    pre_login_str = re.match(r'[^{]+({.+?})', resp.text).group(1)
    pre_login = json.loads(pre_login_str)

    pre_login = json.loads(pre_login_str)
    
    # door = raw_input("input code :")
    
    data = {
        # 'door' : door,
        # 'pcid' : pre_login['pcid'],
        'entry': 'weibo',
        'gateway': 1,
        'from': '',
        'savestate': 7,
        'userticket': 1,
        'ssosimplelogin': 1,
        'su': base64.b64encode(requests.utils.quote(username).encode('utf-8')),
        'service': 'miniblog',
        'servertime': pre_login['servertime'],
        'nonce': pre_login['nonce'],
        'vsnf': 1,
        'vsnval': '',
        'pwencode': 'rsa2',
        'sp': encrypt_passwd(password, pre_login['pubkey'],
                             pre_login['servertime'], pre_login['nonce']),
        'rsakv' : pre_login['rsakv'],
        'encoding': 'UTF-8',
        'prelt': '506',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.si'
               'naSSOController.feedBackUrlCallBack',
        'returntype': 'META',
        'pagerefer' : 'http://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=http%3A%2F%2Fweibo.com%2F&domain=.weibo.com&ua=php-sso_sdk_client-0.6.14',
    }
    resp = session.post(
        'http://login.sina.com.cn/sso/login.php?client=%s' % WBCLIENT,
        data=data,
    )

    login_url = re.search(r'replace\([\"\']([^\'\"]+)[\"\']',resp.text).group(1)
    print("-----")
    print(login_url)
    resp = session.get(login_url)
    with open("d:/m.txt","wb") as f:
        f.write(resp.text)
    login_str = re.match(r'[^{]+({.+?}})', resp.text).group(1)
    return json.loads(login_str)


if __name__ == '__main__':
    print(json.dumps(wblogin('losershen@sohu.com', '21334DFefdsf'), ensure_ascii=False))

    # timeline
    homepage = session.get('http://weibo.com/xjtuofficial?is_all=1').text
    with open("d:/mine.html","wb") as f:
    	f.write(homepage)