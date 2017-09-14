# restart_service.py 的说明

Yii2 控制台命令自动起停监控程序，支持三个参数：

- -a 指定要启动的控制台程序路由
- -k 杀掉已启动的控制台程序
- -r 杀掉并重新启动控制台程序

参数使用方式：

- -a 参数必须提供，-k -r 可选
- -k -r 都不存在时，只尝试启动控制台程序，如果程序已经运行，则不做任何动作

## 使用前准备

1. 在 console 目录下新建 bin 目录
2. 将 restart_service.py 拷贝到 bin 目录
3. 确保安装 python 2.7 版

## 使用方式一：命令行

```
// 后台运行 console 命令：queue/report
# python console/bin/restart_service.py -a queue/report

// 终止运行 console 命令：queue/report
# python console/bin/restart_service.py -a queue/report -k

// 关闭并重启 console 命令：queue/report
# python console/bin/restart_service.py -a queue/report -r
```

## 使用方式二：crontab

```
// 编辑定时任务控制表
# crontab -e

// 添加下面一行
*/1 * * * * /usr/bin/python /home/jobs/myproject/console/bin/restart_service.py -a queue/report
```

这样每隔一分钟，会检查一次控制台程序是否在后台运行，如果没有，会自动重新启动程序。