# -*- encoding: utf-8 -*-
"""
@file: nthUglyNumber.py
@time: 2020/9/6 下午6:44
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 剑指 Offer 49. 丑数

把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

示例:
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chou-shu-lcof/
"""


def nth_ugly_number(n):
    """
    动态规划。时间复杂度 O(n), 空间复杂度 O(n)
    丑数的递推性质： 丑数只包含因子 2, 3, 5，因此有 “丑数 = 某较小丑数 × 某因子”
                （例如：[1,2] 中下一个丑数就是 使用 [1,2] * [2,3,5] = 结果：[2, 3, 5, 4, 6, 10] 中已经存在的 2 最小的一个数 ）。

    所以第 n + 1 个丑数可以看做是接近第 n 个的丑数a，b，c 与2，3，5相乘的最小值。
    即 min(a * 2, b * 3, c * 5).

    使用数组存储前 n 个丑数。假设 da, db, dc 为前 n 个丑数中任数的索引
    dp[n] = min(dp[da] * 2, dp[db] * 3, dp[dc] * 5)

    n   da,db,dc    dp
    1   0,0,0       [1]
    2   1,0,0       [1,2]
    3,  1,1,0       [1,2,3]
    4,  2,1,0       [1,2,3,4]
    5,  2,1,1       [1,2,3,4,5]
    6,  3,2,1       [1,2,3,4,5,6]
    """
    dp, da, db, dc = [1] * n, 0, 0, 0
    for i in range(1, n):
        n1, n2, n3 = dp[da] * 2, dp[db] * 3, dp[dc] * 5
        dp[i] = min(n1, n2, n3)
        if dp[i] == n1:
            da += 1
        if dp[i] == n2:
            db += 1
        if dp[i] == n3:
            dc += 1
    return dp[-1]


def main():
    inputs = 10
    answer = 12
    outputs = nth_ugly_number(inputs)
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except{}".format(inputs, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
