"""
定时启动爬虫，发送爬取内容到指定邮箱
"""
# import schedule
import time
# from send_email import send
from dispatch import _spiders


def run():
    # 执行全部爬虫，将爬取到的信息进行对人友好的处理（可能是html？）
    ret = {}
    for _ in _spiders:
        cur_s = _()
        spider_ret = cur_s.start()
        per_site_info = []
        for title, descAndLink in spider_ret.items():
            per_site_info.append(title+'=>'+descAndLink)
        
        ret[cur_s.s_name] = per_site_info
    # 组织一下数据
    return ret


if __name__ == '__main__':

    print(run())
