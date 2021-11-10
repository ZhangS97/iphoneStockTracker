# coding: utf-8
import os
import time

import requests
import urllib3


def wxPusher(content, summary):
    url = "http://wxpusher.zjiecode.com/api/send/message"
    data = {
        "appToken": "AT_xxx",
        "content": content,
        "summary": summary,
        "contentType": 1,
        "uids": [
            "UID_xxxx"
        ]}
    res = requests.post(url=url, data=data)


urllib3.disable_warnings()

products = 'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/availability?iUP=N'
availability_url = 'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/availability.json'

# R643 虹悦城 在自取选店时可以看到店名
# R493 南京艾尚天地
# R703 玄武湖
stores = [('R643', '虹悦城'), ('R493', '南京艾尚天地'), ('R703', '玄武湖')]
# MLT93CH/A 13p 256 黑 产品型号在购物车里可以通过链接看到
# MLTE3CH/A 13p 256 蓝

products = [
    ('MLT93CH/A', 'iPhone 13 Pro 256GB 石墨色'),
    ('MLTE3CH/A', 'iPhone 13 Pro 256GB 远峰蓝色')
]

print('店铺：', stores)
print('型号：', products)

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0'

i = 0
while True:
    i += 1
    try:
        availability = s.get(availability_url, verify=False).json()
        for store in stores:
            for product in products:
                product_availability = availability['stores'][store[0]][product[0]]
                unlocked_state = product_availability['availability']['unlocked']
                if unlocked_state:
                    wxPusher(store[1] + product[1], store[1] + product[1])
                    print(i, '\t', store[1], '\t', product[1], '\t', product_availability)
                    os.system('say ' + store[1] + product[1])
    except Exception as e:
        print(i, '还没开始', e)

    time.sleep(10)
