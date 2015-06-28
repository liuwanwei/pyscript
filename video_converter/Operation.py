#!/usr/bin/python

import os
from moviepy.editor import *

class VideoConverter:
    def __init__(self, video_file_path,rule_file_path):
        # 初始化原始视频文件名字和扩展名（生成视频片段时用）
        self.video_file_path = video_file_path
        filename = os.path.basename(video_file_path)
        rindex = filename.rfind('.')
        self.video_file_name = filename[0:rindex]
        self.video_file_extension = filename[rindex:]

        # 创建视频文件分割器对象
        self.video_file_clip = VideoFileClip(self.video_file_path)

        # 初始化视频分割规则
        self.rules = self._parse_rule_file(rule_file_path)

    def _parse_rule_file(self, rule_file_path):
        rules = None
        with open(rule_file_path, 'r') as fp:
            for line in fp:
                line = line.strip('\n').strip()
                array = line.split(',')
                length = len(array)
                if length == 3:
                    (start, stop, name) = array
                    if rules == None:
                        rules = []
                    rules.append( (start.strip(), stop.strip(), name.strip()) )

        return rules

    def convert(self):
        if self.video_file_clip == None:
            print('加载视频文件失败')
            return False

        if self.rules == None:
            print('解析规则文件失败')
            return False
        
        exist = os.path.exists(self.video_file_name)
        if not exist:
            # 创建同名目录作为视频片段存储位置
            os.mkdir(self.video_file_name)

        for (start, stop, name) in self.rules:
            self.split_file(start, stop, name)


    def split_file(self, start, stop, name):
        print('[%s-%s] %s' % (start, stop, name))
        #return
        
        video_clip = self.video_file_clip.subclip(start, stop)
        video_clip_name = '[%s-%s]%s%s' % (start, stop, name, self.video_file_extension)
        video_clip_path = '%s/%s' % (self.video_file_name, video_clip_name)
        print(video_clip_path)
        video_clip.write_videofile(video_clip_path)

def usage():
    print('Usage: %s -i input_video_file -r rule_file' % sys.argv[0])
    sys.exit(1)

if __name__ == '__main__':
    import getopt
    import sys

    input_file = 'zwp.mp4'
    rule_file = 'rule.conf'

    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'i:r:')
        for opt, arg in opts:
            if opt == '-i':
                input_file = arg
            elif opt == '-r':
                rule_file = arg
    except getopt.GetoptError:
        usage()

    if 'input_file' not in locals():
        print('\t请指定视频文件')
        usage()

    if 'rule_file' not in locals():
        print('\t请指定处理规则')
        usage()

    converter = VideoConverter(input_file, rule_file)
    converter.convert()
    
