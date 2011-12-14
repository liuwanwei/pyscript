#coding=gbk
from re import search
from sys import exit
from string import split
from string import replace

from WebApi import WebApi
from GetContent import getHtml

class TVBroadCast(object):
    def __init__(self):
        self._tmp = 'tmp.html'
        self._date = ''
        self._time = ''
        self._webApi = WebApi()
    
    def saveTmp(self, str):
        fp = file(self._tmp, 'w')
        fp.write(str)
        fp.close()
        
    def getDate(self, line):
        pat = '<td class="link04"><strong>(.+?)</strong>'
        ret = search(pat, line)
        if None != ret:
            date = ret.group(1)  # TODO why group(0) matches full pat?
            # cut weekday suffix.
            date = date.split(' ')[0]
            pat = '([0-9]+).*?([0-9]+).*'
            ret = search(pat, date)
            #print ret.group(1) + " " + ret.group(2)
            self._date = ret.group(1) + "-" + ret.group(2)
            return True
    
    def getGame(self, line):
        # 先把时间和比赛分开
        pat = '<td class="link04">([0-9:]+) *(.+?)</td>'
        ret = search(pat, line)
        if None != ret:
            time = ret.group(1)
            desc = ret.group(2)
            self._time = time            
            self.getDetail(desc)
            
    def getDetail(self, desc):    
        desc = replace(desc, '<strong><font color="#ED1C24">CCTV-5</font></strong>', 'CCTV5')
        pat = '.+?VS +(.+?) +(.*)'
        ret = search(pat, desc)        
        if None != ret:
            guestTeam=ret.group(1)
            tvb=ret.group(2)        
            self._webApi.addTvB(guestTeam, self._date, self._time, tvb)            
        
    
    def start(self):
        fp = open(self._tmp)
        line = fp.readline()
        while line:      
            if True != self.getDate(line):
                self.getGame(line)
                
            line = fp.readline()
        
    
    def get(self, url):
        #html = getHtml(url)
        #self.saveTmp(html)
        self.start()
        

if __name__ == "__main__":
    tvb = TVBroadCast()
    tvb.get('http://sports.sina.com.cn/global/tvguide/')