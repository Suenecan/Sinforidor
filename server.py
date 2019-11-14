"""
定时启动爬虫，发送爬取内容到指定邮箱
"""
import schedule
import time
from send_email import send
from dispatch import _spiders


def run():
    # 执行全部爬虫，将爬取到的信息进行对人友好的处理（可能是html？）
    ret = []
    for _ in _spiders:
        cur_s = _()
        per_ret = cur_s.start()
        for k, v in per_ret.items():
            ret.append(k+':'+v)
    ret = "\n".join(ret)
    # 将结构化数据发送到邮箱
    send(ret)


if __name__ == '__main__':

    schedule.every().day.at('17:00').do(run)
    while True:
        schedule.run_pending()

    # run()
