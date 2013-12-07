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
	# print(a['title'])
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

def create_head_tag(soup, category_info):
	head_tag = soup.new_tag('head')
	title_tag = soup.new_tag('title')
	title_tag.string = category_info['name']
	head_tag.append(title_tag)
	return head_tag

def create_a_tag(soup, tag_info):
	wrapper_tag = soup.new_tag('p')

	a_tag = soup.new_tag('a')
	a_tag['title'] = tag_info['title']
	a_tag['href'] = tag_info['url']
	a_tag.string = tag_info['title']

	wrapper_tag.append(a_tag)
	return wrapper_tag

def generate_category():
	for category in g_categories:
		print(u'生成URL：' + category['name'] + ' %d' % len(category['result']))
		soup = BeautifulSoup()
		html_tag = soup.new_tag('html')

		# html - head
		html_tag.append(create_head_tag(soup, category))

		# html - body
		body_tag = soup.new_tag('body')
		for result in category['result']:			
			body_tag.append(create_a_tag(soup, result))		
		html_tag.append(body_tag)

		soup.append(html_tag)

		output = '/Users/sungeo/www/public/' + category['name'] + '.html'
		open(output, 'w').write(soup.prettify().encode('UTF-8'))


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
generate_category()
