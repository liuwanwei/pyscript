#coding=utf-8
import re
from json import loads
from urllib import urlencode
import GetContent

# 从新浪体育某个页面获取比赛信息
class GamesFromSina(object):
    def __init__(self):
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
            self._tournament=ret.group(key)
            self._tournament=self._tournament[:-5]
    
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
        return url    
                
    def getGames(self, url):
        """获取赛事某轮次的所有比赛信息
        """
        #TODO html=GetContent.getHtml(url)
        html=open("sina.htm").read()
        self.getTournament(html)
        self.getTeams(html)
        self.getGameDates(html)
        
    def getRoundGames(self, leagueId, round):
        """公共接口，获取赛事某轮次的所有比赛信息
        """
        self._leagueId = leagueId
        self._round = round
        url=self.getRoundUrl()
        self.getGames(url)    

class WebApi(object):
    def __init__(self):
        self._domain='http://localhost/index.php?'
        
    def GBK2UTF8(self, string):
        return string.decode('cp936').encode('utf8')
    
    def checkResult(self, ret):
        """在对下一级的json.loads结果处理前，仍要调用json.loads
        """
        jsonData=loads(ret)
        jsonData=jsonData['data']
        jsonData=loads(jsonData)
        id=jsonData['id']
        if(id != False):
            return True
        else:
            return False
    
    def addGame(self, tournament, hostTeam, guestTeam, dateTime, round):        
        tournament=self.GBK2UTF8(tournament)
        hostTeam=self.GBK2UTF8(hostTeam)
        guestTeam=self.GBK2UTF8(guestTeam)
        param=[('tournament',tournament), 
               ('hostTeam',hostTeam), 
               ('guestTeam',guestTeam), 
               ('dateTime',dateTime),
               ('round',round)]
        encoded=urlencode(param)                
        url=self._domain+'m=game&f=addGame&'+encoded+'&t=json'            
        #print url
        ret=GetContent.getHtml(url)        
        print ret
        return self.checkResult(ret)

if __name__ == '__main__':
    leagueId=318
    round=1
    obj=GamesFromSina()
    obj.getRoundGames(leagueId, round)
    #obj.printGames()
    webApi=WebApi()
    count=len(obj._hosts)
    for i in range(0, count):
        if(False == webApi.addGame(obj._tournament, 
        obj._hosts[i], obj._guests[i], obj._times[i], round)):
            break
        
