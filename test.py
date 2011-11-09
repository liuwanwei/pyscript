#coding=utf-8
import re
import base64
import urllib

def substring():
    string="中国职业足球超级联赛第1轮"
    print string[:-5]
    
    
def readfile():
    file="sina.htm"
    contents=open(file).read()
    print contents

def mergeString():
    url="http://localhost/index.php?m=game&f=addGame"+"&tournament="
    print url
    
def mergeUrl():
    aurl=[('tournament', '中国职业足球超级联赛'), ('hostTeam', '陕西人和'), ('dateTime', '2011-04-03 15:30:00')]
    ret=urllib.urlencode(aurl)
    print ret
    
def encodingBase64():
    aurl='陕西人和'
    #b=base64.encodestring(aurl)
    #print b
    c=urllib.urlencode(aurl)
    print c
    

if __name__ == "__main__":
    #substring()
    #readfile()
    #mergeString()
    mergeUrl()
    #encodingBase64()