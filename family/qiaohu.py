#!/usr/bin/python
#coding=utf-8
#指示python用utf-8方式来处理代码，2.X版本默认非utf-8。

import re
from BeautifulSoup import BeautifulSoup

categories = []
pattern_list = [u'宝宝版', u'幼幼版', u'快乐版', u'成长版', u'学习版']

def add_category(name):
	categories.append({'name' : name, 'result' : []})

def parse_a_tag(a):
	matched = False
	for category in categories:
		m=re.search(category['name'], a['title'])
		if m != None:
			category['result'].append({'url' : a['href'], 'title' : a['title']})
			matched = True
			break

	if matched == False:
		print(a['title'] + '- not matched')

def show_result():
	for category in categories:
		print category['name']
		for matched in category['result']:
			print(matched['title'])

# 准备视频分类数组
for  name in pattern_list:
	add_category(name)

html_doc = open('tongtongde.html').read()
soup = BeautifulSoup(html_doc)
divs = soup.findAll('div', {'id':'movie_title',})
for tag in divs:
        for a in tag('a'):
        	parse_a_tag(a)

# 输出结果看看：）
show_result()
