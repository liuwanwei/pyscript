from GamesFromSina import GamesFromSina
from WebPageFunction import getHtml

if __name__ == "__main__":
    sina = GamesFromSina()
    leagueMax = 397
    for i in range(leagueMax):
        url = sina.getRoundUrl(i, 1)
        html = getHtml(url)
        sina.getTournament(html)
