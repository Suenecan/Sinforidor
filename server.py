"""
定时启动爬虫，发送爬取内容到指定邮箱
"""
# import schedule
import time
# from send_email import send
from dispatch import _spiders

from simple.cache import have_list_key, iter_val, set_list_val, set_expr


def run():
    # 执行全部爬虫
    ret = {}
    for _ in _spiders:

        # 获取当前爬虫的名称
        cur_s = _()
        s_name = cur_s.s_name
        if have_list_key(s_name):
            print('从cache中拿的')
            per_site_info = get_cur_info_from_cache(s_name)
        else:
            print('现成爬取的')
            per_site_info = get_cur_info_from_sipder(cur_s, s_name)
        
        ret[s_name] = per_site_info
   
    return ret


def get_cur_info_from_cache(s_name):
    
    cur_info = []
    for line in iter_val(s_name):
        cur_info.append(line)
    return cur_info


def get_cur_info_from_sipder(cur_s, s_name):
   
    # 操纵当前爬虫去爬取数据
    spider_ret = cur_s.start()
    cur_info = []
    for title, descAndLink in spider_ret.items():
        cur_info.append(title+'=>'+descAndLink)
    if not cur_info:
        cur_info.append('nil')
    # 存入数据库并且设置过期时间
    set_list_val(s_name, cur_info)
    set_expr(s_name)
    return cur_info 


if __name__ == '__main__':

    print(run())
