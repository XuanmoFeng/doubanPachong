#/usr/bin/env python
# coding=utf-8
import urllib2
import cookielib
import urllib
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
Posturl='https://accounts.douban.com/login'
capturl='https://www.douban.com/'
cookie =cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(handler)
username='18309220966'#登陆用户名
password='fengkai1314'#登陆密mZ
picture=urllib2.urlopen(capturl)
main_re=re.compile('https://www.douban.com/.+?size=s')
htm=main_re.findall(picture.read())
for j in htm:
    cc=re.compile('id=(.*?)&')
    htm1=cc.findall(j)
    for h1 in htm1:
        j1=h1
    o=urllib.urlopen(j)
    pi=o.read()
local=open('./image.jpg','wb')
local.write(pi)
local.close()
secretCode=raw_input('输入验证码')
postDate={
    'source': 'book',
    'redir': 'https://book.douban.com/',
    'form_email': username,
    'form_password': password,
    'captcha-solution':secretCode,
    'captcha-id':j1,
    'login':'登录',#unodecpe dasad
}
headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
}
data=urllib.urlencode(postDate)
request=urllib2.Request(Posturl,data,headers)
try:
    response=opener.open(request)
    zhanghao=re.compile('.*<span>.*号</span>')
    htm2=zhanghao.findall(response.read())
    for kk in htm2:
        print kk
except urllib2.HTTPError,e:
    print e.code














