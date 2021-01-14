# -*- encoding: utf-8 -*-
"""
@file: coinChange.py
@time: 2020/9/18 下午3:17
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  322.零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
"""
import functools


def coin_change1(coins, amount):
    """
    DFS. 时间复杂度为 O(Sn) S = amount，n = len(coins). 空间复杂度为 O(S)
    :param coins: (list[int])
    :param amount: (int)
    :return: (int)
    """
    if amount < 1:
        return 0

    @functools.lru_cache(amount)
    def dfs(a_mount):
        if a_mount == 0:
            return 0
        if a_mount < 0:
            return -1
        mini = 1.0e9
        for coin in coins:
            res = dfs(a_mount - coin)
            if 0 <= res < mini:
                mini = res + 1

        return mini if mini < 1.0e9 else -1

    return dfs(amount)


def coin_change2(coins, amount):
    """
    动态规划。 时间复杂度为 O(Sn) S = amount，n = len(coins). 空间复杂度为 O(S)
    f[i] = min(i - c[i]) + 1
    动态转移表
    f[n],   数量
    f[0]    0
    f[1]    f[1] = min(f[1] - 1, f[1] - 2, f[1] - 5) + 1 = 1
    f[2]    f[2] = min(f[2] - 1, f[2] - 2, f[2] - 5) + 1 = 1
    f[3]    f[3] = min(f[3] - 1, f[3] - 2, f[3] - 5) + 1 = 2
    f[4]    f[4] = min(f[4] - 1, f[4] - 2, f[4] - 5) + 1 = 2

    :param coins: (list[int])
    :param amount: (int)
    :return: (int)
    """
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1


def coin_change(coins, amount):
    """
    DP. 解题思想同上。
    :param coins: (list[int])
    :param amount: (int)
    :return: (int)
    """
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
    return dp[-1] if dp[-1] != float('inf') else -1


def test(coins, amount, answer):
    outputs = coin_change(coins, amount)
    print("Inputs:coins={}, amount={}, Outputs:{}, Except:{}".format(coins, amount, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    coins, amount = [1, 2, 5], 11
    test(coins, amount, 3)

    coins, amount = [2], 3
    test(coins, amount, -1)

    coins, amount = [5, 3, 2], 54
    test(coins, amount, 12)


if __name__ == '__main__':
    main()
