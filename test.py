#coding=utf-8
import re
import base64
import urllib

def substring():
    string="中国职业足球超级联赛第1轮"
    print len('第1轮')
    print string
    num=7
    print string[:-num]
    
    
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
    
def testList():
    match = (221, 222, 223, 224)
    round = (30, 40, 50, 60)
    
    print len(match)
    for i in range(0, len(match)):
        print match[i]
        print round[i] 

def testMap():
    map={'zhongchao':(221, 30), 'dejia':(222, 40)}
    #print map['zhongchao']
    list=map['zhongchao']
    for i in map:
        print i
        print map[i][0]
        print map[i][1]
        """
        for i in map[i]:
            print j
        """
    
if __name__ == "__main__":
    #substring()
    #readfile()
    #mergeString()
    #mergeUrl()
    #encodingBase64()
    #testList()
    testMap()