#coding=gbk
import re
import GetContent

class GamesFromSina:
    def __init__(self):
        self._url=''   
        self._leagueId=0
        self._round=0 
        
    # 获取赛事信息
    def getTournament(self, html):
        key='tournament'
        pattern="<font color=\"2677AF\"> *(?P<%s>.+?)</font>" % key
        ret=re.search(pattern, html)
        if None == ret:
            print "%s not found" % pattern
            return None
        else:
            tournament=ret.group(key)
            tournament=tournament[:-5]
            print tournament
        
    def getHostTeam(self, html):
        return 0
    
    def getGuestTeam(self, html):
        re=""
        
    def getDate(self, html):
        re=""
        
    def getTime(self, html):
        re=""
    
    # get round resource URL
    def getRoundUrl(self):
        baseUrl='http://data.sports.sina.com.cn/yingchao/calendar/'
        params="?action=round&league_id=%s&round=%s" % (self._leagueId, self._round)
        self._url=(baseUrl+params)
        print "url: %s" % self._url
        
    # get all games information from URL
    def getGames(self):
        html=GetContent.getHtml(self._url)
        self.getTournament(html)
        #self.getHostTeam(html)
        #self.getGuestTeam(html)
        #self.getDate(html)
        #self.getTime(html)
            
        
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
