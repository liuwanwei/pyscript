import sys
import re

from WebApi import WebApi


date=None
time=None
guestTeam=None
hostTeam=None

matches = 0

webHandler = WebApi()

def getPage(file):    
    file=open(file)
    if not file:
        print "open %s error" % file
        sys.exit()
    line = file.readline()
    while line:      
        checkDate(line) # TODO if is date, then jump next 2
        checkTime(line)
        checkTeam(line)
        
        line = file.readline()
    global matches
    print matches + 1

def checkDate(line):
    # [<td width="90" height="25">]
    # start of all the match day, totally 128 days. 
    global date
    pat = '<td width="90" height="25">(.*?)</td>'
    #print line
    ret = re.search(pat, line)
    if None != ret:
        date = ret.group(1) # TODO why group 1?

def checkTime(line):
    # [<td height="25">]
    # 1021 match time.
    global date
    global time
    pat = '<td height="25">([0-9:]*).*?</td>'
    ret = re.search(pat, line)
    if None != ret:
        time = ret.group(1)
        #print date+time

def checkTeam(line):
    global guestTeam
    global hostTeam
    global date
    global time
    global matches
    # [<a href="team.php?]
    # 2042 match opponents, guest team for the first, host team for the second
    pat = '<a href="team.php?.*?>(.*?)</a>'
    ret = re.search(pat, line)
    if None != ret:
        if None == guestTeam:
            guestTeam = ret.group(1)
        else:
            hostTeam = ret.group(1)
            #print hostTeam + " vs " + guestTeam + " on " + date + time
            preAddGame(hostTeam, guestTeam, date, time)            
            matches += 1
            guestTeam = None

def preAddGame(hostTeam, guestTeam, date, time):    
    # format game date
    pat = '([0-9]+)'
    ret = re.findall(pat, date)
    month = ret[0]
    day   = ret[1]
    if month == '12' and day < '26':
        # pass NBA ji qian cai
        return False
    
    if month == '12':
        year = 2011
    else:
        year = 2012
    date = "%s-%s-%s " % (year, month, day)
    
    # format game time
    time = time + ":00"
    
    # generate datetime
    dateTime =  date + time
    
    # tournament name
    tournament = 'NBA 2011-2012'
    
    global webHandler
    ret = webHandler.addGame(tournament, hostTeam, guestTeam, dateTime, 0)
    if False == ret:
        print "error"
        sys.exit()

"""
def checkTeamOption(line):
    # [option value="" selected]
    # next line will find all the teams.
    pat = 'option value="" selected'
    ret = re.search(pat, line)
    if None != ret:
        global teamBlock
        teamBlock = 1

def getTeams(line):
    # From this field we got 31 teams, "super sonic" was not here.
    pat = '<option value=[0-9]*>(.*?)</option>'
    ret = re.findall(pat, line)
    print len(ret)
    for i in range(len(ret)):
        print "[%i]%s" % (i, ret[i])
    global teamBlock
    teamBlock = 2    
"""


if __name__ == "__main__":
    html = getPage('nba.htm')
    