# -*- encoding: utf-8 -*-
"""
@file: myPow.py
@time: 2020/9/14 上午11:40
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 50.Pow(x,n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:
输入: 2.00000, 10
输出: 1024.00000

示例 2:
输入: 2.10000, 3
输出: 9.26100

示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2^-2 = 1/2^2 = 1/4 = 0.25

说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
"""


def my_pow(x, n):
    """
    分治。时间复杂度为 O(logn), 空间复杂度 O(n)
    :param x: (int)
    :param n: (int)
    :return: (float)
    """

    def helper(xx, nn):
        if nn == 0:
            return 1.0
        y = helper(xx, nn // 2)
        return y * y if nn % 2 == 0 else y * y * xx

    # -n 表示由负数转换成正数
    return helper(x, n) if n >= 0 else helper(1 / x, -n)


def main():
    x = [2, 2.1, 2]
    n = [10, 3, -2]
    for i, (x1, n1) in enumerate(zip(x, n)):
        outputs = my_pow(x1, n1)
        print(outputs)


if __name__ == '__main__':
    main()
