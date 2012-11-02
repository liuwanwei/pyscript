from GamesFromSina import GamesFromSina
from WebPageFunction import getHtml

#http://data.sports.sina.com.cn/yingchao/calendar/?action=round&league_id=418&round=1
#通过依次改变上方url中league_id的值，生成不同url，获取url代表哪项赛事信息。

if __name__ == "__main__":
    sina = GamesFromSina()
    leagueId = 400
    while leagueId <= 450:
        url = sina.getRoundUrl(leagueId, 1)
        html = getHtml(url)
        sina.getTournament(html)
        leagueId = leagueId + 1
