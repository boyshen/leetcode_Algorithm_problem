# -*- encoding: utf-8 -*-
"""
@file: numLsLands.py
@time: 2020/9/18 上午10:17
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  200.岛屿数量

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1:
输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1

示例 2:
输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
"""


def num_is_lands1(grid):
    """
    BFS. 时间复杂度 O(N * M), 空间复杂度 O(min(M, N)). 最坏情况下可能整个都是陆地
    :param grid: (list[list[str]])
    :return: (int)
    """
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    nums = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                grid[r][c] = '0'
                nums += 1
                queue = [(r, c)]
                while queue:
                    x, y = queue.pop(0)
                    for row, col in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1':
                            queue.append((row, col))
                            grid[row][col] = '0'

    return nums


def num_is_lands2(grid):
    """
    DFS. 时间复杂度 O(N * M), 空间复杂度 O(M * N) 最坏情况下可能整个都是陆地
    :param grid: (list[list[str]])
    :return: (int)
    """
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    rows, cols = len(grid), len(grid[0])
    nums = 0

    def helper(r, c):
        grid[r][c] = '0'
        for row, col in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == '1':
                helper(row, col)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                helper(i, j)
                nums += 1

    return nums


def num_is_lands(grid):
    """
    并查集。时间复杂度 O(MN * MN). 其中前一个 MN 为遍历gird元素。 后一个 MN 是在最坏的情况下，即整个grid都是 '1'，每次需要遍历每个表格
    空间复杂度 O(MN)
    :param grid: (list[list[str]])
    :return: (int)
    """

    if not grid or not grid[0]:
        return 0

    row, col = len(grid), len(grid[0])
    uf = UnionFind(grid)

    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                for (x, y) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    dx, dy = i + x, j + y
                    if 0 <= dx < row and 0 <= dy < col and grid[dx][dy] == '1':
                        uf.union(i * col + j, dx * col + dy)
    return uf.count


class UnionFind(object):
    def __init__(self, grid):
        row, col = len(grid), len(grid[0])
        self.count, self.parent = 0, [0] * (row * col)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.parent[i * col + j] = i * col + j
                    self.count += 1

    def union(self, node1, node2):
        find1 = self.find(node1)
        find2 = self.find(node2)
        if find1 != find2:
            self.parent[find1] = find2
            self.count -= 1

    def find(self, node):
        root = node
        while root != self.parent[root]:
            root = self.parent[root]
        while self.parent[node] != node:
            x = node
            node = self.parent[node]
            self.parent[x] = root
        return root


def test(inputs, answer):
    outputs = num_is_lands(inputs)
    print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    # assert outputs == answer, print("Answer Failed")


def main():
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    test(grid, 1)

    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    test(grid, 3)

    grid = [['1'], ['1']]
    test(grid, 1)


if __name__ == '__main__':
    main()
