#!/usr/local/bin/python3

# 微拍视频下载器
# 将别人分享到新浪微波的微拍视频下载下来
# 使用方法 crawl.py shared_video_url

import os
import sys
import urllib.request
import re
import shutil
import datetime
import getopt

# User-Agent 必须指定成移动设备，否则获取到的是其它页面
user_agent_iphone4 = '[Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7]'

def merge(ts_filenames):
    now = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    output = 'output_video_'+now+'.ts'
    print('合并到：%s' % output)
    with open (output, 'wb') as merged:
        for ts_file in ts_filenames:
            with open(ts_file, 'rb') as mergefile:
                shutil.copyfileobj(mergefile, merged)

def get_video_url(content):
    video_urls = []
    lines = content.split('\n')
    for i in range(len(lines)):
        result = re.match(r'http://aliv.weipai.cn.+\.ts$', lines[i])
        if result:
            video_urls.append(lines[i])

    return video_urls

def download_videos(video_urls):
    downloaded_files = []
    for i in range(len(video_urls)):
        temp_local_name = 'downloaded_%d.tmp' % (i+1)
        print('下载[%d/%d]' % (i+1, len(video_urls)))
        download_file(video_urls[i], temp_local_name)
        downloaded_files.append(temp_local_name)

    return downloaded_files

def download_file(url, local_filename):
    print('下载到 %s : [%s]' %  (local_filename, url))
    with urllib.request.urlopen(url) as response, open(local_filename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)



def get_video_list_url(shared_video_url):
    request = urllib.request.Request(shared_video_url, data=None, headers={'User-Agent':user_agent_iphone4})
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    result = re.search(r'src="(http://aliv3.weipai.cn.+?)" webkit-playsinline', content)
    if result == None:
        result = re.search(r'src="(http://.+?\.m3u8)" webkit-playsinline', content)
        if result == None:
            print('video list not found')
            return None
        else:
            print('get video list in postion 2')

    step2_url = result.group(1)
    print(step2_url)
    print('得到视频列表地址，获取...')
    return step2_url

def get_video_list_content(video_list_url):
    request = urllib.request.Request(video_list_url, data=None, headers={'User-Agent':user_agent_iphone4})
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def usage():
    print('Usage:%s -u shared_video_url' % sys.argv[0])
    print('\t -u, --url  分享到微博的视频播放页的 url')

if __name__ == '__main__':
    shared_video_url = 'http://share.weipai.cn/video/uuid/B97C3ADA-AE8B-4585-9B55-24DEE8002BE6?type=third_publish_sina&platform=sina'
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'u:', ['url'])
        for opt, arg in opts:
            if opt in ('-u', '--url='):
                shared_video_url = arg
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    video_list_url = get_video_list_url(shared_video_url)
    if video_list_url != None:
        content = get_video_list_content(video_list_url)
        video_urls = get_video_url(content)

        print('得到视频列表，下载视频文件...')
        downloaded = download_videos(video_urls)

        print('合并文件...')
        merge(downloaded)
        print('完成')


