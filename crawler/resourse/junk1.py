#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from urllib.parse import quote
from urllib import request
import json
import xlwt


KEY = '8cc6b267f72ad2d3fb72d9c92a799ede'
URL = "http://restapi.amap.com/v3/place/text?"
if KEY == '':
    KEY = input("Enter your key: ")

CITY = '南昌市'
AREAS = ['青云谱区']
TYPES = ['商场', '银行']
# 2 A 1 T: 1 and re and well
# 1 A 2 T: 2 and none-re and bad


def Get(type, page):
    url = URL + \
        "key=" + KEY + \
        '&extensions=all'+\
        '&keywords=' + quote(type) + \
        '&city=' + '360100' + \
        '&citylimit=true' + \
        '&offset=25' + \
        '&page=' + str(page) + \
        '&output=json'
    data = ''
    with request.urlopen(url) as fp:
        data = fp.read()
        data = data.decode('utf-8')
    return data
        


def TestGet(page):
    url = URL + \
        "key=" + KEY + \
        '&extensions=all'+\
        '&city=' + '360100' + \
        '&types=' + '010000' + \
        '&citylimit=true' + \
        '&offset=25' + \
        '&page=' + str(page) + \
        '&output=json'
    data = ''
    with request.urlopen(url) as fp:
        data = fp.read()
        data = data.decode('utf-8')
    return data



def Pack(type):
    page = 1
    pois = []
    while True:
        res = Get(type, page)
        print(res)
        res = json.loads(res)
        if res['count'] == str(0):
            print('=============')
            print("COUNT == 0!")
            print('=============')
            break
        tmp = res['pois']
        for i in range(len(tmp)):
            pois.append(tmp[i])
        page = page + 1
    return pois
        


def WriteToExcel(pois, type):
    wb = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = wb.add_sheet(type, cell_overwrite_ok=True)
    sheet.write(0, 0, 'lng')
    sheet.write(0, 1, 'lat')
    sheet.write(0, 2, 'name')
    j = 0
    for i in range(len(pois)):
        location = pois[i]['location']
        name = pois[i]['name']
        lng,lat = location.split(',')
        if lng[0:3] == '120':
            j = j + 1
            continue
        sheet.write(i + 1 - j, 0, lng)
        sheet.write(i + 1 - j, 1, lat)
        sheet.write(i + 1 - j, 2, name)
        # wb.save(r'' + CITY + "-" + str(type) + '.xls')
        wb.save(str(CITY) + "-" + str(type) + str('.xls')) # FIXME: wtf?






# def main():
#     for type in TYPES:
#         pois_type = []
#         for area in AREAS:
#             pois = Pack(type)
#             pois_type.extend(pois)
#             print("***[Area: " + str(area) + "]: " + str(len(pois)) + "***")
#             pois = []
#         print("***[Type: " + str(type) + "]: " + str(len(pois_type)) + "***")
#         WriteToExcel(pois_type, type)
#         print("Write finished!")
        
# if __name__ == "__main__":
#     for type in TYPES:
#         pois_type = []
#         for area in AREAS:
#             pois = []
#             pois = Pack(type)
#             pois_type.extend(pois)
#             print("***[Area: " + str(area) + "]: " + str(len(pois)) + "***")
#         print("***[Type: " + str(type) + "]: " + str(len(pois_type)) + "***")
#         WriteToExcel(pois_type, type)
#         print("Write finished!")





def TestPack():
    poiss = []
    for i in range(500):
        tmp = TestGet(i)
        res = json.loads(tmp)
        pois = res['pois']
        poiss.extend(pois)
    for poi in poiss:
        print(poi['name'])
        print(poi['location'])
        
    return len(poiss)
print(TestPack())