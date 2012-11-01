#coding=utf-8

from json import loads
from urllib import urlencode
from time   import localtime

from WebPageFunction import getHtml


class WebApi(object):
    def __init__(self):
        #self._domain='http://localhost/index.php?'
        self._domain='http://lingling1.sinaapp.com/index.php?'
        
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
        tour=self.GBK2UTF8(tournament)
        host=self.GBK2UTF8(hostTeam)
        guest=self.GBK2UTF8(guestTeam)
        param=[('tournament',tour), 
               ('hostTeam',host), 
               ('guestTeam',guest), 
               ('dateTime',dateTime),
               ('round',round)]
        encoded=urlencode(param)                
        url=self._domain+'m=game&f=addGame&'+encoded+'&t=json'            
        #print url
        ret=getHtml(url)        
        print 'add %s VS %s ON %s, ret %s' % (hostTeam, guestTeam, dateTime, ret)
        return self.checkResult(ret)
    
    def getGamesOfWeek(self, begin, end):
        param = [ ('begin', begin), ('end', end)]
        encoded = urlencode(param)
        url=self._domain+'m=game&f=getGamesOfWeek&'+encoded+'&t=json'
        ret=getHtml(url)
        return ret
    
    def updateTeamRank(self, tournamentId, teamName, rank):
        teamName = self.GBK2UTF8(teamName)        
        param = [('tournamentId', tournamentId), ('teamName', teamName), ('rank', rank)]
        encoded = urlencode(param)
        url = self._domain + "m=game&f=updateRank&" + encoded + '&t=json'
        return getHtml(url)

    def updateParam(self, key, value):        
        param = "key=%s&val=%s&t=json" % (key, value)
        param = [('key', key), ('val', value)]
        encoded = urlencode(param)
        url = self._domain + "m=param&f=update&" + encoded + '&t=json'
        return getHtml(url)

    def addTvB(self, team, date, time, tvb):
        tm = localtime()
        year = tm.tm_year
        dateTime = "%s-%s %s" % (year, date, time)
        
        print team + " " + dateTime + " " + tvb
        team=self.GBK2UTF8(team)
        tvb=self.GBK2UTF8(tvb)
        param = [('teamName', team), ('dateTime', dateTime), ('tvb', tvb)]
        encoded = urlencode(param)
        url = self._domain + "m=game&f=addTvB&" + encoded + '&t=json'
        print url
        print getHtml(url)
