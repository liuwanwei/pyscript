#Coding:utf-8

import os
import sys, getopt

actionId=''

# Find yii script's full directory
def getBaseCmdPath():
	scriptPath = os.path.split(os.path.realpath(__file__))[0]
	yiiPath = scriptPath + "/../../yii"	
	return os.path.realpath(yiiPath)

def getAction():
	return actionId

def getNeatCommand():
	yiiPath = getBaseCmdPath()
	action = getAction()
	return "%s %s" % (yiiPath, action)

def getCommand():
	neatCommand = getNeatCommand();
	command = "%s 2>&1 >/dev/null &" % neatCommand
	return command

def getOldProcess():
	neatCommand = getNeatCommand()
	cmd = "ps ax|grep '%s' | grep -v grep | awk '{print $1;}'" % neatCommand
	output = os.popen(cmd)
	pids = output.read().split('\n')

	# remove empty process names
	while '' in pids:
		pids.remove('')
	return pids


def killOldProcess():
	pids = getOldProcess()

	if not pids:
		print 'nothing to kill: process not exist'

	# When killed main process, child processes will  close automatically
	while pids:
		cmd = 'kill -9 ' + pids[0]
		print cmd
		os.system(cmd)
		pids = getOldProcess()

def startNewProcess():
	cmd = getCommand()
	print "Execute: [ %s ]" % cmd
	os.system(cmd)

def usage():
	print "%s -a <actionId> [-k] [-r]" % sys.argv[0]
	sys.exit(2)

def main(argv):
	global actionId

	try:
		opts, args = getopt.getopt(argv,"hkra:",["action="])
	except getopt.GetoptError:
		usage()
	for opt, arg in opts:
		if opt == '-h':
			usage()
		elif opt == '-k':
			killOldProcess()
			sys.exit(0)
		elif opt == '-r':
			killOldProcess()
		elif opt in ("-a", "--action"):
			actionId = arg

	if actionId == '':
		usage()

	pids = getOldProcess()
	if not pids:
		startNewProcess()
		print 'restart processes ok'
	else:
		print 'old processes already exist with Pid: ' + ' '.join(pids)

if __name__ == "__main__":	
	main(sys.argv[1:])
			
