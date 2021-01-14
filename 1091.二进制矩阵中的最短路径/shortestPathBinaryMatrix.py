# -*- encoding: utf-8 -*-
"""
@file: shortestPathBinaryMatrix.py
@time: 2020/10/20 下午3:34
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 1091.二进制矩阵中的最短路径

在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。
一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：

相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
C_1 位于 (0, 0)（即，值为 grid[0][0]）
C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。


示例 1：

输入：[[0,1],
      [1,0]]
输出：2

示例 2：
输入：[[0,0,0],
      [1,1,0],
      [1,1,0]]
输出：4


提示：
1 <= grid.length == grid[0].length <= 100
grid[i][j] 为 0 或 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-path-in-binary-matrix
"""

from queue import PriorityQueue


def shortest_path_binary_matrix1(grid):
    """
    BFS. 时间复杂度 O(M * M) M 为 gird.length
         空间复杂度 O(M * M)
    :param grid: (list[list[int]])
    :return: (int)
    """

    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    if n <= 2:
        return n

    queue = [(0, 0, 2)]
    while queue:
        x, y, step = queue.pop(0)
        for i, j in [(1, 1), (-1, -1), (1, -1), (-1, 1), (0, 1), (1, 0), (0, -1), (-1, 0)]:
            dx, dy = i + x, j + y
            if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] != 1:
                if dx == dy == (n - 1):
                    return step
                queue.append((dx, dy, step + 1))
                grid[dx][dy] = 1
    return -1


def shortest_path_binary_matrix(grid):
    """
    A * 搜索
    :param grid: (list[list[int]])
    :return: (int)
    """
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1
    if n <= 2:
        return n

    p_queue = PriorityQueue()
    step = 1
    distance = heuristic((0, 0), (n - 1, n - 1))
    p_queue.put((step + distance + 1, (step, 0, 0)))
    grid[0][0] = step

    visit = set()
    while not p_queue.empty():
        _, (step, x, y) = p_queue.get()
        if (x, y) in visit:
            continue
        visit.add((x, y))

        for i, j in [(1, 1), (-1, -1), (1, -1), (-1, 1), (0, 1), (1, 0), (0, -1), (-1, 0)]:
            dx, dy = x + i, y + j
            if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] != 1:
                if dx == dy == (n - 1):
                    return step + 1
                # 相当于 grid[x][y] == 0 （说明没走过 且 可以走）
                # 或者 当前位置记录的步数大于前一步加一（说明之前走过这里 且 现在走比之前走更近一些）。
                if grid[dx][dy] != 0 and grid[dx][dy] <= step + 1:
                    continue
                grid[dx][dy] = step + 1
                distance = heuristic((dx, dy), (n - 1, n - 1))
                p_queue.put((distance + step + 1, (step + 1, dx, dy)))
    return -1


def heuristic(source, dist):
    x1, y1 = source
    x2, y2 = dist
    return max(abs(x1 - x2), abs(y1 - y2))


def test(gird, answer):
    print("Inputs:")
    for i in range(len(gird)):
        print(gird[i])
    outputs = shortest_path_binary_matrix(gird)
    print("Outputs:{}, Except:{}".format(outputs, answer))
    assert outputs == answer, print("Answer Failed")
    print()


def main():
    grid = [[0, 1], [1, 1]]
    test(grid, -1)

    grid = [[0]]
    test(grid, 1)

    grid = [[0, 1], [1, 0]]
    test(grid, 2)

    grid = [[0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]]
    test(grid, 4)

    grid = [[0, 0, 1],
            [1, 1, 1],
            [1, 1, 0]]
    test(grid, -1)

    grid = [[0, 0, 0, 0, 1, 1],
            [0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1],
            [0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0]]
    test(grid, 7)

    grid = [[0, 0, 0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0]]
    test(grid, 11)


if __name__ == '__main__':
    main()
