# -*- encoding: utf-8 -*-
"""
@file: isPerfectSquare.py
@time: 2020/9/21 下午4:18
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  367.有效的完全平方数

给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
说明：不要使用任何内置的库函数，如  sqrt。

示例 1：
输入：16
输出：True

示例 2：
输入：14
输出：False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-perfect-square
"""


def is_perfect_square1(num):
    """
    二分法
    :param num: (int)
    :return: (bool)
    """
    if num < 2:
        return True

    left, right = 1, num // 2
    while left <= right:
        mid = int(left + (right - left) / 2)
        value = mid * mid
        if value == num:
            return True
        elif value < num:
            left = mid + 1
        else:
            right = mid - 1

    return False


def is_perfect_square(num):
    """
    牛顿迭代法. xi = (x0 + C / x0) / 2
    :param num: (int)
    :return: (bool)
    """
    if num < 2:
        return True

    x0, c = num / 2, num
    while x0 * x0 > num:
        x0 = (x0 + c // x0) // 2
    return x0 * x0 == num


def test(inputs, answer):
    outputs = is_perfect_square(inputs)
    print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    inputs, answer = 16, True
    test(inputs, answer)

    inputs, answer = 14, False
    test(inputs, answer)


if __name__ == '__main__':
    main()
