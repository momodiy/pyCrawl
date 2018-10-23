# Author: Steven Lee
# Date: 2018/10/22
# Time: 22:40
# Description: get stock info

import csv
import tushare as ts

def getSingleStockInfo(num):
    # excel 文件保存
    res =ts.get_h_data(num, start='2018-01-16', end='2018-01-18')
# print(res)
    # for p in res.find_all('p', class_=''):
    #     print(p)

    # for letter in 'Python':
    # for x in res(6):
    #     print(eval("res" + str(x)))

    print('=======')
    # json.dumps(res)
    print(res)
    print('=======')

    for v in res:
        print(222222)
        # print(res[v])
        # print(v)

    try:
        writer=csv.writer(coupondata)
        writer.writerow('1','2','555')
        for i in range(10):
            print(i)
            writer.writerow( (i,i+2,i*2))
    finally:
        coupondata.close()

    return res



coupondata = open('stock.csv', 'w+')

getSingleStockInfo('000651')

# print(''.join(getSingleStockInfo('000651')))
# coupondata.write(getSingleStockInfo('000651'))
#
# coupondata.close()


# obj = [[1, 2, 3], 123, 123.123, 'abc', {'key1': (1, 2, 3), 'key2': (4, 5, 6)}]
# encodedjson = json.dumps(obj)
# print(repr(obj))
# print(encodedjson)