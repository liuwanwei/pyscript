#coding=gbk
import re
import GetContent

class GamesFromSina:
    def __init__(self):
        self._url=''   
        self._leagueId=0
        self._round=0 
        self._tournament=""
        self._hosts = []
        self._guests= []
        self._times = []
        
    def printGames(self):
        print "%s 第%s轮" % (self._tournament, self._round)
        for i in range(0, len(self._times)):
            print "%s VS %s" % (self._hosts[i], self._guests[i])
            print "                         Date: "+self._times[i]
        
    # 获取赛事信息
    def getTournament(self, html):
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
    
    # get round resource URL
    def getRoundUrl(self):
        baseUrl='http://data.sports.sina.com.cn/yingchao/calendar/'
        params="?action=round&league_id=%s&round=%s" % (self._leagueId, self._round)
        self._url=(baseUrl+params)
        print "url: %s" % self._url    
                
    # get all games information from URL
    def getGames(self):
        #FIXME html=GetContent.getHtml(self._url)
        html=open("sina.htm").read()
        self.getTournament(html)
        self.getTeams(html)
        self.getGameDates(html)
        
    # Public interface
    def getRoundGames(self, leagueId, round):
        self._leagueId = leagueId
        self._round = round
        self.getRoundUrl()
        self.getGames()    


leagueId=0
round=0

if __name__ == '__main__':
    obj=GamesFromSina()
    obj.getRoundGames(318, 1)
    obj.printGames()
