#coding=utf-8
import re
import base64
import urllib
import time

def substring():
    string="中国职业足球超级联赛第1轮"
    print len('第1轮')
    print string
    num=7
    print string[:-num]
    
    
def readfile():
    file="nba.htm"
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
        
def getTime():
    nowTime = time.localtime()
    nowSeconds = time.mktime(nowTime)
    print nowTime
    print nowSeconds
    
    elapsed = nowTime.tm_hour * 3600 + nowTime.tm_min * 60 + nowTime.tm_sec
    dayBeginSeconds = nowSeconds - elapsed
    dayBeginTime = time.localtime(dayBeginSeconds)
    print dayBeginTime 
    
    weekBeginSeconds = dayBeginSeconds - nowTime.tm_wday * 3600 * 24
    weekBeginTime = time.localtime(weekBeginSeconds)
    print weekBeginTime
    
    weekEndSeconds = dayBeginSeconds + (7 - nowTime.tm_wday) * 3600 * 24
    weekEndTime = time.localtime(weekEndSeconds)
    print weekEndTime
   
def testTime():
    tm = time.localtime()
    print tm.tm_year
    
if __name__ == "__main__":
#testTime()
    #substring()
    #readfile()
    #mergeString()
    #mergeUrl()
    #encodingBase64()
    #testList()
    #testMap()
    #getTime()
