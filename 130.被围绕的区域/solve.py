# -*- encoding: utf-8 -*-
"""
@file: solve.py
@time: 2020/10/15 下午2:43
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  130.被围绕的区域

给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
"""

from collections import deque


class Solution1(object):
    """
    DFS. 时间复杂度 O(m * n). m、n 分别为board的行和列。空间复杂度为 O(m * n). 主要是递归栈的压缩
    """

    def solve(self, board):
        """
        :param board: (list[list[str]])
        :return: (list[list[str]])
        """
        if len(board) == 0 or len(board[0]) == 0:
            return

        row, col = len(board), len(board[0])
        for i in range(row):
            self.dfs(board, i, 0)
            self.dfs(board, i, col - 1)

        for j in range(col):
            self.dfs(board, 0, j)
            self.dfs(board, row - 1, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        return board

    def dfs(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
            return

        board[i][j] = '#'
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)


class Solution2(object):
    """
    BFS. 时间复杂度 O(m * n). m、n 分别为board的行和列。空间复杂度为 O(m * n).
    """

    def solve(self, board):
        if len(board) == 0 or len(board[0]) == 0:
            return

        row, col = len(board), len(board[0])
        queue = [(i, j) for i in range(row) for j in (0, col - 1) if board[i][j] == 'O']
        queue += [(r, c) for c in range(1, col - 1) for r in (0, row - 1) if board[r][c] == 'O']
        d_queue = deque(queue)

        while d_queue:
            r, c = d_queue.popleft()
            board[r][c] = '#'
            for (x, j) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dx, dy = r + x, c + j
                if 0 <= dx < row and 0 <= dy < col and board[dx][dy] == 'O':
                    d_queue.append((dx, dy))

        for i in range(row):
            for j in range(col):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board


class Solution(object):
    """
    并查集
    """

    def solve(self, board):
        if len(board) == 0 or len(board[0]) == 0:
            return

        row, col = len(board), len(board[0])
        uf = UnionFind(row * col)
        dumpy = (row * col) - 1

        for i in range(row):
            for j in range(col):
                if board[i][j] != 'O':
                    continue
                if i == 0 or j == 0 or i == row - 1 or j == col - 1:
                    uf.union(i * col + j, dumpy)
                else:
                    for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        dx, dy = x + i, y + j
                        if 0 <= dx < row and 0 <= dy < col and board[dx][dy] == 'O':
                            uf.union(i * col + j, dx * col + dy)

        for i in range(row):
            for j in range(col):
                if board[i][j] != 'O':
                    continue
                if uf.find(i * col + j) == uf.find(dumpy):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return board


class UnionFind(object):
    def __init__(self, total):
        self.parent = [i for i in range(total)]

    def union(self, node1, node2):
        p1 = self.find(node1)
        p2 = self.find(node2)
        if self.parent[p1] != p2:
            self.parent[p1] = p2

    def find(self, node):
        root = node
        while root != self.parent[root]:
            root = self.parent[root]
        while self.parent[node] != node:
            x = node
            node = self.parent[node]
            self.parent[x] = root
        return root


def test(board, answer):
    print('Input board: ')
    for val in board:
        print(' '.join(val))
    print()

    outputs = Solution().solve(board)
    string = ['Outputs: ', 'Except answer: ']
    res = [outputs, answer]
    for i in range(len(res)):
        print(string[i])
        for val in res[i]:
            print(' '.join(val))
        print()

    # assert outputs == answer, print("Answer Failed")


def main():
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'x', 'X']]
    answer = [['X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X'],
              ['X', 'O', 'x', 'X']]
    test(board, answer)

    print("-----" * 5)
    board = [['O', 'X', 'X', 'X'],
             ['O', 'O', 'X', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'x', 'X']]
    answer = [['O', 'X', 'X', 'X'],
              ['O', 'O', 'X', 'X'],
              ['X', 'X', 'X', 'X'],
              ['X', 'O', 'x', 'X']]
    test(board, answer)


if __name__ == '__main__':
    main()
