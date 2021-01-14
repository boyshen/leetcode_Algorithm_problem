# -*- encoding: utf-8 -*-
"""
@file: climbStairs.py
@time: 2020/8/28 上午9:57
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 70.爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

example：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs/
"""
import math


def climb_stairs1(n):
    """
    递归方法实现
    :param n:  (int)
    :return:  (int)
    """
    dic = {3: 3}
    return helper(n, dic)


def helper(n, dic):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in dic:
        return dic[n]

    ret = helper(n - 2, dic) + helper(n - 1, dic)
    dic[n] = ret
    return ret


def climb_stairs2(n):
    """
    动态规划的方法
    :param n: (int)
    :return:  (int)
    """
    if n <= 2:
        return n
    f1, f2, f3 = 1, 2, 3
    for i in range(2, n):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f3


def climb_stairs3(n):
    """
    动态规划的方法
    :param n: (int)
    :return: (int)
    """
    f1, f2, f3 = 0, 0, 1
    for i in range(n):
        f1 = f2
        f2 = f3
        f3 = f1 + f2
    return f3


def climb_stairs4(n):
    """
    通项式，时间复杂度 O(logN)， 空间复杂度 O(1)。
    参考:https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
    :param n: (int)
    :return: (int)
    """
    sqrt5 = math.sqrt(5)
    fibn = math.pow((1 + math.sqrt(5)) / 2, n + 1) - math.pow((1 - math.sqrt(5)) / 2, n + 1)
    return int(fibn / sqrt5)


def climb_stairs(n):
    """
    矩阵快速幂。 [f(n-1), f(n)] = [[1,1],[1,0]]^n * [f(1), f(0)].
    时间复杂度 O(logN), 空间复杂度 O(N)
    :param n: (int)
    :return: (int)
    """
    matrix = [[1, 1],
              [1, 0]]
    res = matrix_pow(matrix, n)
    return res[0][0]


def matrix_pow(matrix, n):
    res = [[1, 0],
           [0, 1]]
    while n > 0:
        if (n & 1) == 1:
            res = dot(matrix, res)
        n = int(n / 2)
        matrix = dot(matrix, matrix)
    return res


def dot(m, n):
    a = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            a[i][j] = m[i][0] * n[0][j] + m[i][1] * n[1][j]
    return a


def test(inputs, answer):
    outputs = climb_stairs(inputs)
    print("Inputs: {}, Output:{}, Except:{}".format(inputs, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test(3, 3)
    test(5, 8)


if __name__ == '__main__':
    main()
