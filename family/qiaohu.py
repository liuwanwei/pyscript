#!/usr/bin/python
#coding=utf-8
#指示python用utf-8方式来处理代码，2.X版本默认非utf-8。

import re
from bs4 import BeautifulSoup

g_categories = []
g_patter_list = [u'宝宝版', u'幼幼版', u'快乐版', u'成长版', u'学习版']

def add_category(name):
	g_categories.append({'name' : name, 'result' : []})

def parse_a_tag(a):
	matched = False
	print(a['title'])
	for category in g_categories:
		m=re.search(category['name'], a['title'])
		if m != None:
			category['result'].append({'url' : a['href'], 'title' : a['title']})
			matched = True
			break

	if matched == False:
		print(a['title'] + '- not matched')

def show_result():
	for category in g_categories:
		print category['name']
		for matched in category['result']:
			print(matched['title'])

def generate_category():
	for category in g_categories:
		for result in category['result']:
			h.a()

# 准备视频分类数组
for  name in g_patter_list:
	add_category(name)

html_doc = open('tongtongde.html').read()
soup = BeautifulSoup(html_doc, 'lxml')

# aes = soup.find_all('a', {'title':re.compile(u'成长版')})
# print(len(aes))
# for  a in aes:
	# parse_a_tag(a)

divs = soup.find_all('div', {'id':'movie_title'})
for tag in divs:
        for a in tag('a'):
        	parse_a_tag(a)

# 输出结果看看：）
# show_result()
