# -*- encoding: utf-8 -*-
"""
@file: maximalSquare.py
@time: 2020/12/29 下午3:53
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 221. 最大正方形
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4

示例 2：
输入：matrix = [["0","1"],["1","0"]]
输出：1

示例 3：
输入：matrix = [["0"]]
输出：0

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] 为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
"""


def maximal_square(matrix):
    """
    动态规划. 时间复杂度 O(m * n), 空间复杂度 O(n)
    dp[i][j] 中存放的为当前正方形的边长

    dp 方程：
        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
    :param matrix: (list[list[str]])
    :return: (int)
    """
    m, n = len(matrix), len(matrix[0])
    max_square = 0
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_square = max(max_square, dp[i][j])

    return max_square * max_square


def test(matrix, answer):
    outputs = maximal_square(matrix)
    print("Inputs:{}, Outputs:{}, Except:{}".format(matrix, outputs, answer))
    assert outputs == answer


def main():
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    test(matrix, 4)

    matrix = [["0", "1"], ["1", "0"]]
    test(matrix, 1)

    matrix = [["0"]]
    test(matrix, 0)


if __name__ == '__main__':
    main()
