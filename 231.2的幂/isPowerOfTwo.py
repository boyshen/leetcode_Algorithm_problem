# -*- encoding: utf-8 -*-
"""
@file: isPowerOfTwo.py
@time: 2020/10/23 下午4:02
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  231.2的幂

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
输入: 1
输出: true
解释: 2^0 = 1

示例 2:
输入: 16
输出: true
解释: 2^4 = 16

示例 3:
输入: 218
输出: false
"""


def is_power_of_two1(n):
    """
    位运算。解题思路：2的幂即二进制中的只有一个 1 。
    例如：0001 --> 1
         0010 --> 2
         0100 --> 4
         1000 --> 8

    时间复杂度O(1), 空间复杂度O(1)
    判断 n & (n - 1) == 0.
        n & (n - 1) 表示清零最低位的 1 。
        例如 n = 4 -> 0100. 4 - 1 = 3 -> 0011.
            0100 & 0011 = 0
        如果是 12 则：
            12 -> 1100
            11 -> 1011
            1100 & 1011 = 1000
    :param n: (int)
    :return: (int)
    """
    return n > 0 and n & (n - 1) == 0


def is_power_of_two(n):
    """
    位运算。n & -n == n
    n & -n 是通过补码进行运算。例如 4 原码、补码、反码都是它本身。0 0100. -4 补码为 1 1110
    0 0100 & 1 1110 == 0 0100
    :param n: (int)
    :return: (bool)
    """
    return 0 < n == n & (-n)


def test(n, answer):
    outputs = is_power_of_two(n)
    print("Inputs:{}, Outputs:{}, Except:{}".format(n, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test(1, True)
    test(16, True)
    test(218, False)


if __name__ == '__main__':
    main()
