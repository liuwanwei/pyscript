#coding=gbk
#from sys import exit
from re import findall
#from sys import exit

from GetContent import getHtml
from WebApi import WebApi

webApi = WebApi()

def updateRanks(rankUrl, tournamentId):
    content = getHtml(rankUrl)
    pattern = ' target="_blank">(.*?)</a></font>'
    matches = findall(pattern, content)
    for i in range(len(matches)):
        print matches[i]
        global webApi
        webApi.updateTeamRank(tournamentId, matches[i], i + 1)            

if __name__ == "__main__":
    tournaments = [('http://sports.sina.com.cn/global/score/Germany/index.shtml', 17),
                   ('http://sports.sina.com.cn/global/score/Italy/index.shtml', 18),
                   ('http://sports.sina.com.cn/global/score/France/index.shtml', 19),
                   ('http://sports.sina.com.cn/global/score/Spain/index.shtml', 20),
                   ('http://sports.sina.com.cn/global/score/England/index.shtml', 21)]
    for i in range(len(tournaments)):
        updateRanks(tournaments[i][0], tournaments[i][1])
    webApi.updateParam('updateRankTime', '')