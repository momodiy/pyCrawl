# Author: Steven Lee
# Date: 2018/10/17
# Time: 23:27
# Description: tell me ...
import string
import random


def coupon_creator(digit):
    coupon = ''
    for word in range(digit):
        coupon += random.choice(string.ascii_uppercase + string.digits)
    return coupon


def two_hundred_coupons():
    data = ''
    count = 1
    for count in range(200):
        digit = 12
        count += 1
        data += 'coupon no.' + str(count) + ' ---  ' + coupon_creator(digit) + '\n'

    # print(data)
    return data


# 以只读方式打开txt文件
# coupondata = open('random.txt', 'w')
coupondata = open('random.txt', 'w')
print(coupondata.path)
print(111)
# 写入数据
coupondata.write(two_hundred_coupons())
# 关闭文件
coupondata.close()