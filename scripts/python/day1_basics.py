#!/usr/bin/env python3

#-*- coding: utf-8 -*-

"""
基础练习
"""
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} 是偶数"
    else:
        return f"{number} 是奇数"

def print_list_items(items):
    print("列表内容:")
    for item in items:
        print (f"-{item}")

def count_positive_numbers(numbers):
    count = 0
    i = 0
    while i < len(numbers):
        if numbers[i] > 0:
            count += 1
        i += 1
    return f"正数个数：{count}"


def get_student_grade(student_dict,name):
    if name in student_dict:
        return f"{name}的成绩:{student_dict[name]}"
    else:
        return f"未找到学生{name}的成绩"

def generate_multiplcation_table(n):
    print(f"\n{n}x{n}乘法表")
    for i in range(1,n + 1):
        row = []
        for j in range(1,i + 1):
            row.append(f"{j}x{i}={j*i}")
        print(" ".join(row))


if __name__ == "__main__":
    print(check_even_odd(15))
    print(check_even_odd(16))

    fruits = ['苹果','香蕉','橘子','梨']
    print_list_items(fruits)

    numbers = [-3,0,2,5,6,7]
    print(count_positive_numbers(numbers))

    grades = {"张三":85,"李四":79,"王五":92,"赵六":69}
    print(get_student_grade(grades,"张三"))
    print(get_student_grade(grades,"李子明"))

    generate_multiplcation_table(9)
