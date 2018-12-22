# -*- coding:utf-8 -*-
"""
@author:Levy
@file:3_data.py
@time:2018/12/20 0020下午 9:44
"""
import pickle

# import pandas as pd

with open('data_1.pkl', 'rb') as f:
    data, label = pickle.load(f)
# print(label)

import numpy as np

features = []
for item in data:
    xs = np.array(item[0])
    ys = np.array(item[1])
    features.append((xs.mean(), xs.std(), xs.max(), xs.min(),
                     ys.mean(), ys.std(), ys.max(), ys.min()))

print([_[0] for _ in features])
# print(list(map(lambda 元素: 逻辑, 数组)))

print([np.array(_[0]).mean() for _ in data])
print(list(map(lambda _: np.array(_[0]).mean(), data)))

import pickle

with open('data_2.pkl', 'wb+') as f:
    pickle.dump(features, f)

# ////////////////////////只求含有x的平均值/////////////////////////////
# 提取所有的x放入一个all_x列表中
all_x = []
for i in data:
    # print(i[0])
    all_x.append(i[0])

# 求x的平均值
averge_x = []
for x in all_x:
    # x_sum = 0  # 这句应该放到此处，不应该放在下面for语句中
    # for j in x:
    #     x_sum += j
    averge_x.append(sum(x) / len(x))

print('对应每项x的平均值：', averge_x)
print('只有x平均的长度：', len(averge_x))

# # //////////////////////求含有x和y的平均值//////////////////////
# 先切去z坐标，存入dataXY的新列表中
dataXY = []
for points in data:
    point = points[:2]
    dataXY.append(point)

# 求含有x和y的平均值
avergeXY = []
for point_x, point_y in dataXY:
    x_sum = 0
    y_sum = 0
    # 注意这里for不能同时用for循环，需要用两个for循环
    for value_x in point_x:
        x_sum += value_x

    for value_y in point_y:
        y_sum += value_y

    t = (x_sum / len(point_x), y_sum / len(point_y))
    avergeXY.append(t)  # append只有一个参数
print('含有x和y的平均为：', avergeXY)
print('含有有x和y的平均值的长度为：', len(avergeXY))

# [mean_x_1,
#  mean_x_2,
#  ....]
#
#
# [(mean_x_1, mean_y_1),
#  ((mean_x_2, mean_y_2),
#   ...
# ]
#
# [(mean_x_1, std_x_1, max_x_1, min_x_1, mean_y_1, std_x_1, max_y_1, min_y_1),
#  (mean_x_2, std_x_2, max_x_2, min_x_2, mean_y_2, std_x_2, max_y_2, min_y_2),
#   ...
# ]
