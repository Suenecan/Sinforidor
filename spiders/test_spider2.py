import requests
from lxml import etree
import time
import datetime


class Spider_2():
    """汪丁丁的博客"""

    s_name = 'wangdingding'

    def __init__(self):
        self.url = 'http://wangdingding.blog.caixin.com/'
        self.today = datetime.date.today()
        self.yesterday = str(self.today - datetime.timedelta(days=1))

    def start(self):

        d = {}
        ret = requests.get(self.url)
        root = etree.HTML(ret.text)
        for _ in range(1,6):
            title = str(root.xpath('/html/body/div[2]/div[2]/div[1]/div[{}]/div/h2/a/text()'.format(_))[0])
            date = str(root.xpath('/html/body/div[2]/div[2]/div[1]/div[{}]/div/span[1]/text()'.format(_))[0])
            link = str(root.xpath('/html/body/div[2]/div[2]/div[1]/div[{}]/div/h2/a/@href'.format(_))[0])
            date = date.split(" ")[0]
            date = date.replace("年", '-')
            date = date.replace("月", '-')
            publish_data = date.replace("日", '')
            if publish_data == self.yesterday:
                d[title] = link
            
        return d


class Spider_3():

    s_name = 'spider3'

    def __init__(self):
        self.url = 'http://wangdingding.blog.caixin.com/'
        self.today = datetime.date.today()
        self.yesterday = str(self.today - datetime.timedelta(days=1))

    def start(self):
        d = {
            "title3": "content3"
        }
        # ret = requests.get(self.url)
        # root = etree.HTML(ret.text)
        # for _ in range(0):
        #     title = str(root.xpath('/html/body/div[2]/div[2]/div[1]/div[{}]/div/h2/a/text()'.format(_))[0])
        #     date = str(root.xpath('/html/body/div[2]/div[2]/div[1]/div[{}]/div/span[1]/text()'.format(_))[0])
        #     link = str(root.xpath('/html/body/div[2]/div[2]/div[1]/div[{}]/div/h2/a/@href'.format(_))[0])
        #     date = date.split(" ")[0]
        #     date = date.replace("年", '-')
        #     date = date.replace("月", '-')
        #     publish_data = date.replace("日", '')
        #     if publish_data == self.yesterday:
        #         d[title] = link
            
        return d


if __name__ == "__main__":
    
    S = Spider_2()
    ret = S.start()
    print(ret)
