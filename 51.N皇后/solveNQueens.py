# -*- encoding: utf-8 -*-
"""
@file: solveNQueens.py
@time: 2020/9/15 上午9:55
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  51.N皇后

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例：
输入：4
输出：[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

提示：
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
"""


def solve_n_queens1(n):
    """
    回溯。时间复杂度：O(N!)，其中 N 是皇后数量。空间复杂度：O(N)，其中 N 是皇后数量。
    由于使用位运算表示，因此存储皇后信息的空间复杂度是 O(1)，
    空间复杂度主要取决于递归调用层数和记录每行放置的皇后的列下标的数组，递归调用层数不会超过 N，数组的长度为 N。
    :param n: (int)
    :return: (list[list[str]])
    """
    res, queens = [], [-1] * n

    def backtrack(row):
        if row == n:
            board, r = [], ['.'] * n
            for q in queens:
                r[q] = 'Q'
                board.append("".join(r))
                r[q] = '.'
            res.append(board)

        for col in range(n):
            if is_ok(queens, row, col, n):
                queens[row] = col
                backtrack(row + 1)

    backtrack(0)
    return res


def is_ok(queens, row, column, n):
    left_diagonal, right_diagonal = column - 1, column + 1
    r = row - 1
    while r >= 0:
        if queens[r] == column:
            return False
        if 0 <= left_diagonal == queens[r]:
            return False
        if n > right_diagonal == queens[r]:
            return False
        left_diagonal -= 1
        right_diagonal += 1
        r -= 1
    return True


def solve_n_queens2(n):
    result = []

    def dfs(queen, xy_dif, xy_sum):
        p = len(queen)
        if p == n:
            result.append(queen)
            return None

        for q in range(n):
            if q not in queen and p - q not in xy_dif and p + q not in xy_sum:
                dfs(queen + [q], xy_dif + [p - q], xy_sum + [p + q])

    dfs([], [], [])
    return [['.' * i + 'Q' + '.' * (n - 1 - i) for i in queens] for queens in result]


def solve_n_queens(n):
    """
    位运算的回溯。 时间复杂度 O(n!), 空间复杂度 O(n)
    :param n: (int)
    :return: (list[list[str]])
    """
    def solve(row, col, left_diagonals, right_diagonal):
        if row == n:
            board = []
            for i in range(n):
                liner = ['.'] * n
                liner[queen[i]] = 'Q'
                board.append(''.join(liner))
            res.append(board)

        else:
            available_positions = ((1 << n) - 1) & (~(col | left_diagonals | right_diagonal))
            while available_positions:
                positions = available_positions & (-available_positions)
                available_positions = available_positions & (available_positions - 1)
                column = bin(positions - 1).count('1')
                queen[row] = column
                solve(row + 1, col | positions, (left_diagonals | positions) << 1, (right_diagonal | positions) >> 1)

    res = []
    queen = [-1] * n
    solve(0, 0, 0, 0)
    return res


def main():
    inputs = 4
    outputs = solve_n_queens(inputs)
    answer = [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
