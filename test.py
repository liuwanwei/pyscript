#coding=gbk
import re

def substring():
    string="�й�ְҵ���򳬼�������1��"
    print string[:-5]
    
    
def readfile():
    file="sina.htm"
    contents=open(file).read()
    print contents

if __name__ == "__main__":
    #substring()
    readfile()