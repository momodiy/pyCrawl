# Author: Steven Lee
# Date: 2018/10/18
# Time: 22:53
# Description: tell me ...

import string
print('Steven Lee')

from urllib.request import urlopen
from bs4 import  BeautifulSoup

html=urlopen('http://124.115.228.93/zfrgdjpt/xmgs.aspx?state=4')

bsObj=BeautifulSoup(html.read(),"html.parser")

str=bsObj.body
print(str)

coupondata = open('res.txt', 'w')
# 写入数据
coupondata.write(str.get_text('', strip=True))
# 关闭文件
coupondata.close()