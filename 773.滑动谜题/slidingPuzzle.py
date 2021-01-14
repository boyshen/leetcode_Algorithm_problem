# -*- encoding: utf-8 -*-
"""
@file: slidingPuzzle.py
@time: 2020/10/21 下午2:25
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  773.滑动谜题

在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。

示例：
输入：board = [[1,2,3],[4,0,5]]
输出：1
解释：交换 0 和 5 ，1 步完成

输入：board = [[1,2,3],[5,4,0]]
输出：-1
解释：没有办法完成谜板

输入：board = [[4,1,2],[5,0,3]]
输出：5
解释：
最少完成谜板的最少移动次数是 5 ，
一种移动路径:
尚未移动: [[4,1,2],[5,0,3]]
移动 1 次: [[4,1,2],[0,5,3]]
移动 2 次: [[0,1,2],[4,5,3]]
移动 3 次: [[1,0,2],[4,5,3]]
移动 4 次: [[1,2,0],[4,5,3]]
移动 5 次: [[1,2,3],[4,5,0]]

输入：board = [[3,2,4],[1,5,0]]
输出：14

提示：
board 是一个如上所述的 2 x 3 的数组.
board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-puzzle
"""
from queue import PriorityQueue


def sliding_puzzle1(board):
    """
    BFS. 时间复杂度 O(R * C * 3). R 和 C 为board的行数和列数，其中 3 为 move中最大值。
         空间复杂度 O(R * C). 主要是存放元素的队列
    :param board: (list[list[int]])
    :return: (int)
    """

    # 将board 看作是一维数组。key表示数字0所在的位置[0,1,2,3,5]。
    # value 表示当前0所在的位置可以跟那两几个位置进行交换.
    # 如当数字0在 1 整个位置上时，可以跟[0,2,4]位置上的元素进行交换。
    move = {0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]}

    s = ''.join([str(num) for row in board for num in row])
    queue = [(s, s.index('0'), 0)]
    visit = set()

    while queue:
        s, index, step = queue.pop(0)
        if s == '123450':
            return step

        if s in visit:
            continue
        visit.add(s)

        for m in move[index]:
            s_list = list(s)
            s_list[index], s_list[m] = s_list[m], s_list[index]
            queue.append((''.join(s_list), m, step + 1))
    return -1


def sliding_puzzle(board):
    """
    A*.
    :param board: (list[list[int]])
    :return: (int)
    """

    # 将board 看作是一维数组。key表示数字0所在的位置[0,1,2,3,5]。
    # value 表示当前0所在的位置可以跟那两几个位置进行交换.
    # 如当数字0在 1 整个位置上时，可以跟[0,2,4]位置上的元素进行交换。
    move = {0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]}

    score = get_score()
    p_queue = PriorityQueue()
    board_s = ''.join([str(num) for row in board for num in row])
    p_queue.put((0, (0, board_s, board_s.index('0'))))
    visit = set()

    while not p_queue.empty():
        distance, (step, board_s, index) = p_queue.get()

        if board_s == "123450":
            return step

        if board_s in visit:
            continue
        visit.add(board_s)

        for m in move[index]:
            board_l = list(board_s)
            board_l[index], board_l[m] = board_l[m], board_l[index]
            next_board = "".join(board_l)
            p_queue.put((step + score(board_l) + 1, (step + 1, next_board, m)))
    return -1


def get_score():
    scores = {}
    # 目标值，二维数组。0:[1,2] 中 0 表示数字 0 应在[1,2] 这个坐标中。1:[0,0] 表示数字 1 应在[0,0] 这个坐标下。
    goal_pos = {0: [1, 2], 1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1]}
    for num in range(6):
        # 计算曼哈顿距离。两级循环。如：假设 0 在 [0,0],[0,1],[0,2],[1,0],[1,1],[1,1] 这几个位置下与目标值得距离
        distance = [[abs(goal_pos[num][0] - i) + abs(goal_pos[num][1] - j) for j in range(3)] for i in range(2)]
        # 转换成一维。shape: [6,6]。 表示每个节点到目标节点的曼哈顿距离。
        scores[num] = distance[0] + distance[1]

    def manhattan_distances(board):
        score = 0
        for i in range(6):
            start = int(board[i])
            score += scores[start][i]
        return score

    return manhattan_distances


def test(board, answer):
    outputs = sliding_puzzle(board)
    print("Inputs:{}, Outputs:{}, Except:{}".format(board, outputs, answer))


def main():
    board = [[1, 2, 3], [4, 0, 5]]
    test(board, 1)

    board = [[4, 1, 2], [5, 0, 3]]
    test(board, 5)

    board = [[1, 2, 3], [5, 4, 0]]
    test(board, -1)


if __name__ == '__main__':
    main()
