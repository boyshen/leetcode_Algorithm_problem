# -*- encoding: utf-8 -*-
"""
@file: uniquePaths.py
@time: 2020/9/29 下午3:03
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  62.不同路径

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3
输出: 28
 
提示：
1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
"""
import math


def unique_paths1(m, n):
    """
    动态规划。时间复杂度 O(m * n), 空间复杂度 O(m * n)
    :param m: (int)
    :param n: (int)
    :return: (int)
    """
    state = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            state[i][j] = state[i - 1][j] + state[i][j - 1]

    return state[-1][-1]


def unique_paths2(m, n):
    """
    动态规划(优化)。 时间复杂度 O(m * n), 空间复杂度 O(n)
    :param m: (int)
    :param n: (int)
    :return: (int)
    """
    state = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            state[j] = state[j - 1] + state[j]
    return state[-1]


def unique_paths(m, n):
    """
    排列组合。从起点到终点，步数是固定的。步数 = (m + n) - 2。
    C(m+n-2, m-1/n-1)
    :param m: (int)
    :param n: (int)
    :return: (int)
    """
    return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))


def test(m, n, answer):
    outputs = unique_paths(m, n)
    print("Inputs:m={},n={}, Outputs:{}, Except:{}".format(m, n, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test(3, 2, 3)
    test(3, 3, 6)
    test(7, 3, 28)


if __name__ == '__main__':
    main()
