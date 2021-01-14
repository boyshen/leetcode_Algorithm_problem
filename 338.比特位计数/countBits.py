# -*- encoding: utf-8 -*-
"""
@file: countBits.py
@time: 2020/10/27 下午2:50
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 338.338.比特位计数

给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:
输入: 2
输出: [0,1,1]

示例 2:
输入: 5
输出: [0,1,1,2,1,2]

进阶:
给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits
"""


def count_bits(num):
    """
    DP + 位运算。时间复杂度 O(N), 空间复杂度 O(N)
    DP 方程： P[i] = P[i & (i-1)] + 1 ==> i & (i-1) 对最低位的1清零
    DP 转移表
    num     bits      result
    0        00         0
    1        01         1
    2        10         1
    3        11         2
    4        100        1
    :param num: (int)
    :return: (list[int])
    """
    res = [0] * (num + 1)
    for i in range(1, num + 1):
        res[i] = res[i & (i - 1)] + 1
    return res


def test(num, answer):
    outputs = count_bits(num)
    print("Inputs:{}, Outputs:{}, Except:{}".format(num, outputs, answer))


def main():
    test(0, [0])
    test(1, [0, 1])
    test(2, [0, 1, 1])
    test(5, [0, 1, 1, 2, 1, 2])


if __name__ == '__main__':
    main()
