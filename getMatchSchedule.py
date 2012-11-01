import GamesFromSina

def main():
    obj=GamesFromSina()    
    leagues={'xijia':(329, 38), 
             'dejia':(327, 34), 
             'yijia':(326, 38),              
             'yingchao':(325, 38)}
             #'fajia':(328, 38)} discard FaJia because no broadcast in china.           
    for i in leagues:
        print ("开始添加赛事 %s".decode('utf-8').encode('cp936')) % i        
        leagueId=leagues[i][0]
        maxRound=leagues[i][1]
        print "league %s , round %s" % (leagueId, maxRound)
        obj.getGamesInLeague(leagueId, maxRound)
    

def test():
    obj=GamesFromSina()
    obj.getGamesInLeague(329, 38)
    #obj.getRoundGames(329, 16)
    #obj.uploadRoundGames()
    #obj.printGames()
    
def printAllLeagues():
    obj=GamesFromSina()

if __name__ == '__main__':
    #main()
    test()
    #printAllLeagues()
