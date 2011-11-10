#coding=utf-8
import re
import GetContent
from WebApi import WebApi
from time import sleep

# 从新浪体育某个页面获取比赛信息
class GamesFromSina(object):
    def __init__(self):        
        self._webApi=WebApi()
        self.clear()
        
    def clear(self):
        self._leagueId=0    # 联赛名称
        self._round=0       # 联赛轮次        
        self._tournament=""
        self._hosts = []
        self._guests= []
        self._times = []
        
        
    def printGames(self):
        print "%s 第%s轮" % (self._tournament, self._round)
        for i in range(0, len(self._times)):
            print "%s VS %s" % (self._hosts[i], self._guests[i])
            print "                         Date: "+self._times[i]
        
    def trimRoundString(self, string):
        """删除赛事名称后面的’第N轮’信息
        文件采用utf-8编码，要从搜索结果（gbk）中删除最后的“第几轮”
        信息，要先把搜索模式串的编码改成gbk。
        """
        di='第'.decode('utf8').encode('cp936')
        lun='轮'.decode('utf8').encode('cp936')
        key='round'
        pattern='.+?(?P<%s>%s.+?%s)' % (key, di, lun)
        ret=re.search(pattern, string)
        if None == ret:
            print "%s not found" % pattern
            return False
        else:
            count=len(ret.group(key))
            return string[:-count]        
        
    def getTournament(self, html):
        """获取赛事名称
        """
        key='tournament'
        pattern="<font color=\"2677AF\"> *(?P<%s>.+?)</font>" % key
        ret=re.search(pattern, html)
        if None == ret:
            print "%s not found" % pattern
            return None
        else:
            ret=self.trimRoundString(ret.group(key))
            if(False == ret):
                return False
            else:
                self._tournament = ret            
                print ret
                return True
                
    
    def getTeams(self, html):
        """获取该轮次所有比赛主队和客队
        """
        pattern="class=\"a02\" target=_blank>.+?</a>"
        ret=GetContent.findAll(pattern, html)
        key="team"
        for i in range(0, len(ret)):
            pattern=">(?P<%s>.+?)<" % key
            team=re.search(pattern, ret[i])
            team=team.group(key)
            if i % 2 == 0:
                self._hosts.append(team)
            else:
                self._guests.append(team)
                        
    def getGameDates(self, html):
        """获取该轮次所有比赛开始时间
        """
        pattern="<font color=\"#333333\">[0-9-:]+?</font>"
        ret=GetContent.findAll(pattern, html)
        key="time"
        for i in range(0, len(ret)):
            pattern=">(?P<%s>.+?)<" % key
            time=re.search(pattern, ret[i])
            time=time.group(key)
            if i % 2 == 0:
                date=time
            else:
                time=date+" "+time
                self._times.append(time)
    
    def getRoundUrl(self):
        """根据轮次、赛事id，获取该轮次比赛信息的URL
        """
        baseUrl="http://data.sports.sina.com.cn/yingchao/calendar/"
        params="?action=round&league_id=%s&round=%s" % (self._leagueId, self._round)
        url=(baseUrl+params)
        print url
        return url    
                
    def getGames(self, url):
        """获取赛事某轮次的所有比赛信息
        """
        html=GetContent.getHtml(url)
        #html=open("sina.htm").read()
        if(False == self.getTournament(html)):
            return False
        self.getTeams(html)
        self.getGameDates(html)
        
    def getRoundGames(self, leagueId, round):
        """公共接口，获取赛事某轮次的所有比赛信息
        """
        self.clear()
        self._leagueId = leagueId
        self._round = round
        url=self.getRoundUrl()
        return self.getGames(url) 
        
    def uploadRoundGames(self):        
        count=len(obj._hosts)
        for i in range(0, count):
            if(False == self._webApi.addGame(obj._tournament, 
                obj._hosts[i], obj._guests[i], obj._times[i], self._round)):
                break
        
        
    def getGamesInLeague(self, leagueId, maxRound):
        for i in range(1, maxRound + 1):        
            if( False == self.getRoundGames(leagueId, i)):
                break
            
            self.uploadRoundGames()        
            sleep(2)
        

if __name__ == '__main__':
    obj=GamesFromSina()
    leagueId=318
    maxRound=30
    obj.getGamesInLeague(leagueId, maxRound)
    #obj.printGames()    
        
