# -*- encoding: utf-8 -*-
"""
@file: mySqrt.py
@time: 2020/9/21 下午2:48
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 69.x的平方根

实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
"""


def my_sqrt1(x):
    """
    二分查找法
    :param x: (int)
    :return: (int)
    """
    if x == 0:
        return 0

    left, right, res = 0, x, -1
    while left <= right:
        mid = int(left + (right - left) / 2)
        value = mid * mid
        if value <= x:
            res = mid
            left = mid + 1
        elif value > x:
            right = mid - 1
    return res


def my_sqrt(x):
    """
    牛顿迭代法
    :param x: (int)
    :return: (int)
    """
    if x == 0:
        return 0

    c, x0 = float(x), float(x)
    while True:
        xi = (x0 + c / x0) / 2
        if abs(xi - x0) < 1e-7:
            break
        x0 = xi
    return int(x0)


def test(inputs, answer):
    outputs = my_sqrt(inputs)
    print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))


def main():
    x, answer = 4, 2
    test(x, answer)

    x, answer = 8, 2
    test(x, answer)


if __name__ == '__main__':
    main()
