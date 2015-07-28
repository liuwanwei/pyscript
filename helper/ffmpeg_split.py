#!/usr/local/bin/python3

import sys
import subprocess
import datetime

if __name__ == "__main__":

    if (len(sys.argv) < 4):
        print('至少需要三个参数')
        print('1, 输入文件名字')
        print('2, 开始截取时间，00:00:00 格式')
        print('3, 截取时间长度，00:00:00 格式，或以秒为单位的数字')
        sys.exit(1)


    sourceFile = sys.argv[1] 
    startTime = sys.argv[2]
    substractLength = sys.argv[3]

    dotPosition = sourceFile.rfind(".")
    if (dotPosition == -1):
        print("文件名没有后缀？")
        sys.exit(2)
        
    nowTime = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    output = sourceFile[:dotPosition] + '-' + nowTime + sourceFile[dotPosition:]
    print(output)

    subprocess.call(['ffmpeg', '-i', sourceFile, '-vcodec', 'copy', '-acodec', 'copy', '-ss', startTime, '-t', substractLength, output])
    # ffmpeg -i $sourceFile -vcodec copy -acodec copy -ss $start_time -t $length output.mp4
