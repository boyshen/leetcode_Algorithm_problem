# -*- encoding: utf-8 -*-
"""
@file: minimumTotal.py
@time: 2020/10/8 下午5:59
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  120.三角形最小路径和

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle/
"""


def minimum_total1(triangle):
    """
    动态规划。 top-down. 时间复杂度 O(N^2) 空间复杂度 O(N)
    f(n) = {
        f[0] + c[i][0]           if j = 0
        f[i-1] + c[i][i]         if j = i
        min(f[j], f[j-1]) + c[i][j]   other
    }

    :param triangle: (list[list[int]])
    :return: (int)
    """
    if not triangle and not triangle[0]:
        return

    n = len(triangle)
    res = [0] * n
    res[0] = triangle[0][0]

    for i in range(1, n):
        # 三角形右
        res[i] = res[i - 1] + triangle[i][i]
        # 三角形中间
        for j in range(i - 1, 0, -1):
            res[j] = min(res[j], res[j - 1]) + triangle[i][j]
        # 三角形左
        res[0] = res[0] + triangle[i][0]

    return min(res)


def minimum_total2(triangle):
    """
     动态规划。 bottom-up. 时间复杂度 O(N^2) 空间复杂度 O(N)
    :param triangle: (list[list[int]])
    :return: (int)
    """
    if not triangle and not triangle[0]:
        return

    n = len(triangle)
    res = triangle[-1]

    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            res[j] = min(res[j], res[j + 1]) + triangle[i][j]
    return res[0]


def minimum_total(triangle):
    """
    动态规划。时间复杂度 O(n^2)，空间复杂度 O(n^2)
    :param triangle: (list[list[int]])
    :return: (int)
    """
    n = len(triangle)
    state = [[0] * n for _ in range(n)]
    state[0][0] = triangle[0][0]

    for i in range(1, n):
        state[i][0] = state[i - 1][0] + triangle[i][0]
        for j in range(1, i):
            state[i][j] = min(state[i - 1][j - 1], state[i - 1][j]) + triangle[i][j]
        state[i][i] = state[i - 1][i - 1] + triangle[i][i]
    return min(state[-1])


def test(inputs, answer):
    outputs = minimum_total(inputs)
    print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    assert outputs == answer


def main():
    inputs = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]]
    test(inputs, 11)


if __name__ == '__main__':
    main()
