#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-05-27 22:20:22
@LastEditors: steven
@LastEditTime: 2020-05-28 21:19:36
@Description:通过某个字段将记录分组
'''

from itertools import groupby
from operator import itemgetter
# Sort by the desired field first
things = [('2018-05-21', 11), ('2018-05-21', 3), ('2018-05-22', 10),
          ('2018-05-22', 4), ('2018-05-22', 22),('2018-05-23', 33)]
things.sort(key=itemgetter('date'))
for date, items in groupby(things, key=itemgetter(0)):
    print(date)
    for i in items:
        print(' ', i)
# for key, items in groupby(things, itemgetter(0)):
  # print(key)
  # print(items)

"""
2018-05-21
<itertools._grouper object at 0x0000029B85314B48>
2018-05-22
<itertools._grouper object at 0x0000029B85314B88>
2018-05-23
<itertools._grouper object at 0x0000029B85314B48>
"""

for subitem in items:
  print(subitem)
print('-' * 20)
