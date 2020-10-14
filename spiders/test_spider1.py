import requests
from lxml import etree
import time
import datetime

class Spider_1():
    """微软亚洲研究院"""
    s_name = 'microsoft'

    def __init__(self):
        self.url = 'https://www.msra.cn/zh-cn/news?wd&content-type=all'
        self.today = datetime.date.today()
        self.yesterday = str(self.today - datetime.timedelta(days=1))

    def start(self):

        d = {}
        ret = requests.get(self.url)
        root = etree.HTML(ret.text)
        for _ in range(1, 6):
            title = str(root.xpath('/html/body/div[2]/div/div[2]/div/div[2]/article[{}]/div[2]/p[1]/a/text()'.format(_))[0])
            desc = str(root.xpath('/html/body/div[2]/div/div[2]/div/div[2]/article[{}]/div[2]/p[2]/text()'.format(_))[0])
            link = str(root.xpath('/html/body/div[2]/div/div[2]/div/div[2]/article[{}]/div[2]/p[1]/a/@href'.format(_))[0])
            data = str(root.xpath('/html/body/div[2]/div/div[2]/div/div[2]/article[{}]/div[2]/p[3]/span[1]/text()'.format(_))[0])
            publish_data = data.split("：")[-1]
            # print(publish_data)
            if publish_data == self.yesterday:
                # print("好开心，成功了")
                d[title] = desc + "\n" + link
        return d


if __name__ == '__main__':
    S = Spider_1()
    ret = S.start()
    print(ret)

