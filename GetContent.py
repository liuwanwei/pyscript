#coding=gbk
import urllib2
import re 

# �Ӹ�����URL����ȡ��ҳ����
def getHtml(url):                
    user_agent='Mozilla/4.0 (compatible; MSIE 7.0; WindowsNT)'
    headers = {'User-Agent':user_agent}
        
    req = urllib2.Request(url, None, headers)
    retryTimes=0
    while retryTimes < 3:
        try:
            response = urllib2.urlopen(req)            
            html = response.read()
        except urllib2.URLError:
            print "urlopen error:" + url
            retryTimes+=1
        except:
            print "read error:" + url
            retryTimes+=1
        else:                
            return html
    
# ����Ŀ�괮�з���ģʽ�������н��
def findAll(pattern, model):
    rePattern=re.compile(pattern, re.S)
    results=rePattern.findall(model)
    return results
    