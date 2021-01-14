# -*- encoding: utf-8 -*-
"""
@file: hammingWeight.py
@time: 2020/10/23 下午3:26
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 191.位1的个数

编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

示例 1：
输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

示例 2：
输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。

示例 3：
输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。

提示：
请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，
并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-1-bits/
"""


def hamming_weight1(n):
    """
    位运算。 时间复杂度O(1), 空间复杂度O(1)
    n & 1. 判断奇偶。n & 1 == 1 奇数
    n >> 1. 右移一位
    :param n: (int)
    :return: (int)
    """
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1

    return count


def hamming_weight2(n):
    """
    位运算。
    依次对n的最低位1清零 n = n & (n - 1)
    :param n: (int)
    :return: (int)
    """
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count


def hamming_weight3(n):
    """
    使用 bin 库函数
    :param n: (int)
    :return: (int)
    """
    return bin(n).count('1')


def hamming_weight(n):
    """
    :param n: (int)
    :return: (int)
    """
    count = 0
    while n > 0:
        res = n % 2
        if res == 1:
            count += 1
        n = n >> 1
    return count


def test(n, answer):
    outputs = hamming_weight(n)
    print("Inputs:{}, Outputs:{}, Except:{}".format(n, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test(11, 3)
    test(128, 1)


if __name__ == '__main__':
    main()
