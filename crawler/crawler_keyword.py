#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from urllib import request
import json


CITY = '360100'
KEY = '8cc6b267f72ad2d3fb72d9c92a799ede'
URL = "http://restapi.amap.com/v3/place/text?"
NUM = 100


if KEY == '':
    KEY = input("Enter your key: ")


def Get(page, keyword):
    url = URL + \
        "key=" + KEY + \
        '&extensions=all'+\
        '&city=' + CITY + \
        '&keywords=' + str(keyword) + \
        '&citylimit=true' + \
        '&offset=25' + \
        '&page=' + str(page) + \
        '&output=json'
    data = ''
    with request.urlopen(url) as fp:
        data = fp.read()
        data = data.decode('utf-8')
    print(data)
    return data


def PackAndWrite(keyword, file_name):
    pois_all = []
    times = 1
    for i in range(NUM):
        tmp = Get(i, keyword)
        res = json.loads(tmp)
        pois = res['pois']
        pois_all.extend(pois)
    for poi in pois_all:
        fp = open(str(file_name), 'a')
        lng, lat = poi['location'].split(',')
        name = poi['name']
        fp.write(lng)
        fp.write(',')
        fp.write(lat)
        fp.write(',')
        fp.write(name)
        fp.write('\n')
        print(times)
        times = times + 1
        

def Read(file_name):
    fp = open(str(file_name), mode='r', encoding='UTF-8')
    arr = []
    while True:
        tmp = fp.readline()
        if tmp == '':
            break
        arr.append(tmp[0:6])
    return arr


if __name__ == "__main__":
    # arr = Read('types_out.txt')
    # for i in arr:
    #     PackAndWrite(i, 'coordinates.txt')
    #     print('===================')
    PackAndWrite('bank', 'corrdinates_keyword.txt')
    
    
"""
踩了五个坑:
1. page;
2. VS Code 内置终端会保留状态;
3. 1000 次限制;
4. 使用关键词得到的数据不准确;
5. VS Code 内置终端的编码问题, 造成乱码.
最佳实践: 如上.
"""


"""
@author: chasehu
@github: chasehu123
@e-mail: chasehu123@outlook.com
"""