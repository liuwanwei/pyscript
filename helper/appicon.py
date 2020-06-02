#!/usr/bin/env python

import sys
import os
import subprocess

app_icon_dimentions = [20, \
                       29, 29*2, 29*3, \
                       40, 40*2, 40*3, \
                       #60*2 \ the same as 40*3
                       60, 60*3, \
                       76, 76*2, \
                       167
                       ]

def re_sample_app_icon(filename, subdir, width, height = None):
    if height == None:
        height = width

    (head, sep, suffix) = filename.rpartition('.')
    output = '%s/Icon-%d-%d.%s' % (subdir, width, height, suffix) 
    subprocess.call(['sips', '-z', str(width), str(height), filename, '--out', output])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage:\n\t./%s  the_path_of_file' % __file__)
        exit()
    else:
        print(sys.argv)
    
    file_path = sys.argv[1]
    
    if os.path.exists(file_path):
        filename = os.path.basename(file_path)
        (subdir_name, sep, tail) = filename.rpartition('.')
        print(subdir_name)
        subdir = os.path.join(os.getcwd(), subdir_name)
        print('subdir: %s' %  subdir)
        if os.path.exists(subdir):
            import shutil
            shutil.rmtree(subdir)

        os.mkdir(subdir)

        if os.path.exists(subdir):
            for width in app_icon_dimentions:
                re_sample_app_icon(file_path, subdir, width)
        else:
            print('can not create subdir: %s' % subdir)


