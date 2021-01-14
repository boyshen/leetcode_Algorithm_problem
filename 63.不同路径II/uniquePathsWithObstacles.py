# -*- encoding: utf-8 -*-
"""
@file: uniquePathsWithObstacles.py
@time: 2020/9/29 下午6:07
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 63.不同路径 II

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。

示例 1:
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
"""


def unique_paths_with_obstacles(obstacle_grid):
    """
    动态规划。时间复杂度 O(m * n), 空间复杂度 O(n)
    :param obstacle_grid: (list[list[int]])
    :return: (int)
    """
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    state = [0] * n
    state[0] = 1 if obstacle_grid[0][0] == 0 else 1

    for i in range(m):
        for j in range(n):
            if obstacle_grid[i][j] == 1:
                state[j] = 0
            elif j > 0:
                state[j] = state[j] + state[j - 1]

    return state[-1]


def test(inputs, answer):
    outputs = unique_paths_with_obstacles(inputs)
    print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    assert outputs == answer


def main():
    inputs = [[0, 0, 0],
              [0, 1, 0],
              [0, 0, 0]]
    test(inputs, 2)

    inputs = [[0, 0]]
    test(inputs, 1)

    inputs = [[1, 0]]
    test(inputs, 0)


if __name__ == '__main__':
    main()
