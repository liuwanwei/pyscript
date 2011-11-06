#coding=gbk
import re

def substring():
    string="中国职业足球超级联赛第1轮"
    print string[:-5]
    
    
def readfile():
    file="sina.htm"
    contents=open(file).read()
    print contents

if __name__ == "__main__":
    #substring()
    readfile()