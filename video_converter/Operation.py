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
                (start, stop, name) = line.split(',')
                if rules == None:
                    rules = []
                rules.append((int(start), int(stop), name.strip('\n')))

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
        msg = '[%d-%d] %s' % (start, stop, name)
        
        video_clip = self.video_file_clip.subclip(start, stop)
        video_clip_name = '[%d-%d]%s%s' % (start, stop, name, self.video_file_extension)
        video_clip_path = '%s/%s' % (self.video_file_name, video_clip_name)
        print(video_clip_path)
        video_clip.write_videofile(video_clip_path)


if __name__ == '__main__':
    converter = VideoConverter('zwp.mp4', 'rule.conf')
    converter.convert()
    
