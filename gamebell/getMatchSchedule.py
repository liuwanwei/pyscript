#coding=utf-8
from GamesFromSina import GamesFromSina

def main():
    sinaAPI=GamesFromSina()
	# 两个数字，前面代表在新浪数据库里的league_id，后面代表赛季共多少轮比赛。
    leagues={'德甲':(418, 34),
			 '英超':(419, 38),
			 '西甲':(420, 38),  
             '意甲':(421, 38)}
    for i in leagues:
        print ("开始添加赛事 %s".decode('utf-8').encode('cp936')) % i        
        leagueId=leagues[i][0]
        maxRound=leagues[i][1]
        print "league %s , round %s" % (leagueId, maxRound)
        sinaAPI.getGamesInLeague(leagueId, maxRound)
    

def test():
    obj=GamesFromSina()
    obj.getGamesInLeague(329, 38)
    #obj.getRoundGames(329, 16)
    #obj.uploadRoundGames()
    #obj.printGames()
    
def printAllLeagues():
    obj=GamesFromSina()

if __name__ == '__main__':
    main()
    #test()
    #printAllLeagues()
