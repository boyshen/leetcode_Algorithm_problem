# -*- encoding: utf-8 -*-
"""
@file: robotSim.py
@time: 2020/9/21 下午4:51
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  874.模拟行走机器人
机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

-2：向左转 90 度
-1：向右转 90 度
1 <= x <= 9：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物。

第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。

示例 1：
输入: commands = [4,-1,3], obstacles = []
输出: 25
解释: 机器人将会到达 (3, 4)

示例 2：
输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
输出: 65
解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处 

提示：
0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
答案保证小于 2 ^ 31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/walking-robot-simulation
"""


def robot_sim1(commands, obstacles):
    """
    情景描述
    :param commands: (list)
    :param obstacles: (list[list[int]])
    :return: (int)
    """
    # 移动坐标。分别是 北、东、南、西
    direction_x = [0, 1, 0, -1]
    direction_y = [1, 0, -1, 0]

    # direction 为方向。 0：北、 1：东、 2：南、 3：西
    (x, y), direction = (0, 0), 0
    obstacles = set(map(tuple, obstacles))
    res = 0

    for cmd in commands:
        # right
        if cmd == -1:
            direction = (direction + 1) % 4
        # left
        elif cmd == -2:
            direction = (direction - 1) % 4
        else:
            for _ in range(cmd):
                if (x + direction_x[direction], y + direction_y[direction]) in obstacles:
                    break
                x = x + direction_x[direction]
                y = y + direction_y[direction]

            res = max(res, pow(x, 2) + pow(y, 2))
    return res


def robot_sim(commands, obstacles):
    """
    情景描述
    :param commands: (list[int])
    :param obstacles: (list[tuple])
    :return:
    """
    robot = ['n', (0, 0)]
    res = 0
    obstacles = set(map(tuple, obstacles))

    for command in commands:
        if command == -1 or command == -2:
            robot[0] = rotate(command, robot[0])
        else:
            robot = move(command, robot, obstacles)

        _, (x, y) = robot
        res = max(res, pow(x, 2) + pow(y, 2))
    return res


def rotate(cmd, direction):
    update = direction
    if cmd == -1:
        if direction == 'e':
            update = 's'
        elif direction == 's':
            update = 'w'
        elif direction == 'w':
            update = 'n'
        elif direction == 'n':
            update = 'e'

    elif cmd == -2:
        if direction == 'e':
            update = 'n'
        elif direction == 'n':
            update = 'w'
        elif direction == 'w':
            update = 's'
        elif direction == 's':
            update = 'e'
    return update


def move(cmd, robot, obstacles):
    direction, (x, y) = robot
    # 东 x += cmd
    if direction == 'e':
        for _ in range(cmd):
            if (x + 1, y) in obstacles:
                break
            x += 1

    # 南 y -= cmd
    elif direction == 's':
        for _ in range(cmd):
            if (x, y - 1) in obstacles:
                break
            y -= 1

    # 西  x -= cmd
    elif direction == 'w':
        for _ in range(cmd):
            if (x - 1, y) in obstacles:
                break
            x -= 1

    # 北 y += cmd
    elif direction == 'n':
        for _ in range(cmd):
            if (x, y + 1) in obstacles:
                break
            y += 1

    return [direction, (x, y)]


def test(cmd, obstacles, answer):
    outputs = robot_sim(cmd, obstacles)
    print("Inputs:command={}, obstacles={}, Outputs:{}, Except:{}".format(cmd, obstacles, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    cmd, obstacles, answer = [4, -1, 3], [], 25
    test(cmd, obstacles, answer)

    cmd, obstacles, answer = [4, -1, 4, -2, 4], [[2, 4]], 65
    test(cmd, obstacles, answer)


if __name__ == '__main__':
    main()
