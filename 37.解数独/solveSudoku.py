# -*- encoding: utf-8 -*-
"""
@file: solveSudoku.py
@time: 2020/10/18 下午5:36
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 37.解数独

编写一个程序，通过填充空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

提示：
给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
"""


class Solution1(object):
    """
    回溯。 方法一
    """

    def solve_sudo_ku(self, board):
        if len(board) == 0 or len(board[0]) == 0:
            return
        self.solve(board)

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    continue
                for num in range(1, 10):
                    if self.is_valid(board, i, j, str(num)):
                        board[i][j] = str(num)
                        if self.solve(board):
                            return True
                        else:
                            board[i][j] = '.'
                return False
        return True

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] != '.' and board[row][i] == num:
                return False
            if board[i][col] != '.' and board[i][col] == num:
                return False
            box_r = row // 3 * 3 + i // 3
            box_c = col // 3 * 3 + i % 3
            if board[box_r][box_c] != '.' and board[box_r][box_c] == num:
                return False
        return True


class Solution(object):
    """
    回溯。 方法二
    """

    def solve_sudo_ku(self, board):
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        box = [set(range(1, 10)) for _ in range(9)]

        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    num = int(board[i][j])
                    row[i].remove(num)
                    col[j].remove(num)
                    box[(i // 3 * 3) + (j // 3)].remove(num)

        def solve(item):
            if item == len(empty):
                return True
            r, c = empty[item]
            box_index = (r // 3) * 3 + (c // 3)
            for val in row[r] & col[c] & box[box_index]:
                row[r].remove(val)
                col[c].remove(val)
                box[box_index].remove(val)

                board[r][c] = str(val)
                if solve(item + 1):
                    return True

                row[r].add(val)
                col[c].add(val)
                box[box_index].add(val)
            return False

        solve(0)


def test(board):
    print("Inputs Board: ")
    for i in range(9):
        print(' '.join(board[i]))

    Solution().solve_sudo_ku(board)

    print("Outputs Board: ")
    for i in range(9):
        print(' '.join(board[i]))


def main():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    test(board)


if __name__ == '__main__':
    main()
