#!/usr/bin/env python3
# -*- coding:utf8 -8-

"""
定义函数
引入模块
"""

import os,sys,time

# 全局变量
# 注意：在函数内修改 GLOBAL_MESSAGE 需要使用 global 关键字
GLOBAL_MESSAGE = "这是全局变量"

def get_current_time():
    return time.strftime('%Y-%m-%d %M:%H:%S',time.localtime())

def join_path(*parts):
    return os.path.join(*parts)

def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    avg = total / len(numbers)
    return round(avg,2)

if __name__ == "__main__":
    print(f"python 版本：{sys.version}")

    current_time = get_current_time()
    print(f"当前时间:{current_time}")

    path = join_path("home","user","projects","day2")
    print(f"拼接路径:{path}")

    scores = [85,90,77,62,100]
    avg_score = calculate_average(scores)
    print(f"成绩平均分:{avg_score}")

    print(f"全局变量:{GLOBAL_MESSAGE}")
