# -*- encoding: utf-8 -*-
"""
@file: updateBoard.py
@time: 2020/9/22 下午4:07
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  529.扫雷游戏

让我们一起来玩扫雷游戏！
给定一个代表游戏板的二维字符矩阵。
'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，
数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：
1. 如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
2. 如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
3. 如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
4. 如果在此次点击中，若无更多方块可被揭露，则返回面板。

示例 1：
输入:
[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
Click : [3,0]
输出:
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

示例 2：
输入:
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
Click : [1,2]
输出:
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minesweeper
"""


def update_board1(board, click):
    """
    DFS.  时间复杂度为 O(m*n), 空间复杂度为 O(m*n)
    :param board: (list[list[str]])
    :param click: (list[int])
    :return: (list[list[str]])
    """

    direction = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    row, col = len(board), len(board[0])
    x, y = click[0], click[1]

    if 0 <= x < row and 0 <= y < col:
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            # 搜索周边是不是有地雷
            count = 0
            for (r, c) in direction:
                if 0 <= x + r < row and 0 <= y + c < col:
                    if board[x + r][y + c] == 'M':
                        count += 1

            # 如果周边有地雷，则更新。否则为 'B'
            if count != 0:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                for (r, c) in direction:
                    if 0 <= x + r < row and 0 <= y + c < col and board[x + r][y + c] == 'E':
                        update_board1(board, (x + r, y + c))
    return board


def update_board(board, click):
    """
    BFS. 时间复杂度为 O(m*n), 空间复杂度为 O(m*n)
    :param board: (list[list[str]])
    :param click: (list)
    :return: (list[list[str]])
    """
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    row, col = len(board), len(board[0])
    x, y = click[0], click[1]

    if 0 <= x < row and 0 <= y < col:
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            queue = [(x, y)]
            visit = [[False] * col for _ in range(row)]
            visit[x][y] = True
            while queue:
                x, y = queue.pop(0)
                count = 0
                for (r, c) in direction:
                    tx = x + r
                    ty = y + c
                    if 0 <= tx < row and 0 <= ty < col:
                        if board[x + r][y + c] == 'M':
                            count += 1

                if count:
                    board[x][y] = str(count)
                else:
                    board[x][y] = 'B'
                    for (r, c) in direction:
                        tx = x + r
                        ty = y + c
                        if 0 <= tx < row and 0 <= ty < col and not visit[tx][ty] and board[tx][ty] == 'E':
                            queue.append((tx, ty))
                            visit[tx][ty] = True

    return board


def test(board, click, answer):
    outputs = update_board(board, click)
    print("Inputs:board={}, click={}, Outputs:{}, Except:{}".format(board, click, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]
    answer = [['B', '1', 'E', '1', 'B'],
              ['B', '1', 'M', '1', 'B'],
              ['B', '1', '1', '1', 'B'],
              ['B', 'B', 'B', 'B', 'B']]
    test(board, click, answer)

    board = [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'M', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']]
    click = [1, 2]
    answer = [['B', '1', 'E', '1', 'B'],
              ['B', '1', 'X', '1', 'B'],
              ['B', '1', '1', '1', 'B'],
              ['B', 'B', 'B', 'B', 'B']]
    test(board, click, answer)


if __name__ == '__main__':
    main()
