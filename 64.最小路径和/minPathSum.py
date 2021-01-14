# -*- encoding: utf-8 -*-
"""
@file: minPathSum.py
@time: 2020/10/11 下午8:20
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  64.最小路径和

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum/
"""


def min_path_sum1(grid):
    """
    DP. 时间复杂度 O(N*M), 空间复杂度 O(N*M)
    DP 方程
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    :param grid: (list[list[int]])
    :return: (int)
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    state = [[0] * n for _ in range(m)]
    state[0][0] = grid[0][0]
    for i in range(1, m):
        state[i][0] = grid[i][0] + state[i - 1][0]

    for j in range(1, n):
        state[0][j] = grid[0][j] + state[0][j - 1]

    for i in range(1, m):
        for j in range(1, n):
            state[i][j] = min(state[i - 1][j], state[i][j - 1]) + grid[i][j]

    return state[-1][-1]


def min_path_sum(grid):
    """
    DP. 另一种实现方法
    :param grid: (list[list[int]])
    :return: (int)
    """
    m, n = len(grid), len(grid[0])
    state = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == j == 0:
                state[i][j] = grid[i][j]
            elif i == 0:
                state[i][j] = grid[i][j] + state[i][j - 1]
            elif j == 0:
                state[i][j] = grid[i][j] + state[i - 1][j]
            else:
                state[i][j] = min(state[i - 1][j], state[i][j - 1]) + grid[i][j]
    return state[-1][-1]


def test(grid, answer):
    outputs = min_path_sum(grid)
    print("Inputs:{}, Outputs:{}, Except:{}".format(grid, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    test(grid, 7)

    grid = [[1, 2, 5],
            [3, 2, 1]]
    test(grid, 6)


if __name__ == '__main__':
    main()
