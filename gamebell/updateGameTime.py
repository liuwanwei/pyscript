import json
import string
import time

from WebApi import WebApi
from GamesFromSina import GamesFromSina

class UpdateSoccerGameTime(object):
    def __init__(self):
        self._thisRound = dict()
        
        # soccer id_in_db : id_in_url
        self._tourId2UrlId = {17:327, 18:326, 20:329, 21:325}
        self._weekBegin = ''
        self._weekEnd = ''
        self.getWeekSpan()
    
    def getWeekSpan(self):
        nowTime = time.localtime()
        nowSeconds = time.mktime(nowTime)
        #print nowTime        
        
        elapsed = nowTime.tm_hour * 3600 + nowTime.tm_min * 60 + nowTime.tm_sec
        dayBeginSeconds = nowSeconds - elapsed
        dayBeginTime = time.localtime(dayBeginSeconds)
        #print dayBeginTime 
        
        weekBeginSeconds = dayBeginSeconds - nowTime.tm_wday * 3600 * 24
        weekBeginTime = time.localtime(weekBeginSeconds)
        self._weekBegin = time.strftime('%Y-%m-%d %H:%M:%S', weekBeginTime)
        print "Week begin at: " + self._weekBegin
        
        weekEndSeconds = dayBeginSeconds + (7 - nowTime.tm_wday) * 3600 * 24
        weekEndSeconds += 3600 * 6  # Game weekend finished by monday morning
        weekEndTime = time.localtime(weekEndSeconds)
        self._weekEnd = time.strftime('%Y-%m-%d %H:%M:%S', weekEndTime)
        print "Week   end at: " + self._weekEnd
        


    def storeData(self, tournamentId, round):        
        tournamentId = string.atoi(tournamentId)
        round = string.atoi(round)    
    
        # Does the key exist?
        if None == self._thisRound.get(tournamentId):
            self._thisRound[tournamentId] = [round]
        else:
            try:
                # Does the value exist?
                self._thisRound[tournamentId].index(round)
            except ValueError:
                self._thisRound[tournamentId].append(round)

    def getGamesOfThisWeek(self):        
        api = WebApi()
        ret=api.getGamesOfWeek(self._weekBegin, self._weekEnd)
        data = json.loads(ret)['data']
        data = json.loads(data)
        for i in range(len(data)):
            #print data[i]['round'] + " " + data[i]['tournamentId']
            self.storeData(data[i]['tournamentId'], data[i]['round'])
        print self._thisRound;
    

    def updateGames(self):
        sina = GamesFromSina()        
            
        self.getGamesOfThisWeek()    
        
        # After query, self._thisRound's value would like this:    
        # {17: [17], 18: [16], 19: [18], 20: [16, 17], 21: [16]}
        keys = self._thisRound.keys()
        for i in range(len(keys)):
            tourId = keys[i]
            rounds = self._thisRound[keys[i]]
            for j in range(len(rounds)):
                leagueId = self._tourId2UrlId.get(tourId)
                if None != leagueId:
                    print leagueId, rounds[j]
                    sina.getRoundGames(leagueId, rounds[j])
                    sina.uploadRoundGames()
        
    
if __name__ == "__main__":
        updater = UpdateSoccerGameTime()
        updater.updateGames()
        
        webApi = WebApi()
        webApi.updateParam('updateGameTime', '')
                