"""
定时启动爬虫，发送爬取内容到指定邮箱
"""
import schedule
import time

current_time = str(time.strftime('%Y-%m-%d %H:%M'))


def task1():
    print("十秒执行一次任务1")


def task2():
    print("14:22执行一次，现在时间是：")
    print(current_time)


if __name__ == '__main__':
    schedule.every(10).seconds.do(task1)
    schedule.every().day.at('14:22').do(task2)
    while True:
        schedule.run_pending()
