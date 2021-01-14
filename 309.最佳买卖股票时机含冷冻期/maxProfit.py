# -*- encoding: utf-8 -*-
"""
@file: maxProfit.py
@time: 2020/10/31 下午4:39
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 309.最佳买卖股票时机含冷冻期

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
"""


def max_profit1(prices):
    """
    DP. 时间复杂度 O(N), 空间复杂度 O(NlogN)

    DP 方程：dp[index][status]
    dp[0][0]  ==> 第i天卖出
    dp[0][1]  ==> 第i天买入

    # 正常情况下的卖出。 前一天卖出的利润 vs 前一天买入的利润加当前股价
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])

    # 有冷冻期的买入。
    # dp[i-2][0] 表示 i-1 天是冷冻期，不能操作。所以只能用 i-2 卖出的利润减去当前的股价剩下的利润 vs 如果在 [i-1][1] 买入的股价。
    dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

    :param prices: (list[int])
    :return: (int)
    """
    if len(prices) < 2:
        return 0

    n = len(prices)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])

    for i in range(2, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

    return dp[-1][0]


def max_profit2(prices):
    """
    DP. 时间复杂度 O(N), 空间复杂度 O(NlogN)

    DP 方程。使用 dp[i][state] 表示
    dp[i][0]  ==>  卖出
    dp[i][1]  ==>  买入
    dp[i][2]  ==>  冷冻期

    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])  ==> 上一天卖出的价格 vs 上一次买入加当前股价所获取的收益
    dp[i][1] = max(dp[i-1][1], dp[i][2] - prices[i])    ==> 卖出之后的一天是冷冻期，所以用冷冻期之前的收益减去当前股价 vs 前一天买入
    dp[i][2] = dp[i][0]                                 ==> 冷冻期等于前一天卖出的股价

    :param prices: (list[int])
    :return: (int)
    """

    if not prices:
        return 0

    length = len(prices)
    # 初始化 DP
    dp = [[0] * 3 for _ in range(length)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[0][2] = 0

    for i in range(1, length):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] - prices[i])
        dp[i][2] = dp[i - 1][0]

    return max(dp[-1][0], dp[-1][2])


def max_profit(prices):
    """
    DP + 空间优化。 时间复杂度 O(N), 空间复杂度 O(1)

    DP 方程。 使用dp1、dp2、dp3 分别表示卖出、买入、冷冻期
    dp1 ==> 卖出
    dp2 ==> 买入
    dp3 ==> 冷冻期

    temp = dp1
    dp1 = max(dp1, dp2 + prices[i])  ==> 买入的最大利润：上一次买入的利润 vs 冷冻期减去当前股价利润（这里冷冻期保存卖出时候的收益）。
    dp2 = max(dp2, dp3 - prices[i])  ==> 卖出的最大利润：上一次卖出的利润 vs 买入的股价加当前股价
    dp3 = temp

    :param prices: (list[int])
    :return: (int)
    """

    if not prices:
        return 0

    dp1 = 0
    dp2 = -prices[0]
    dp3 = 0
    length = len(prices)
    for i in range(1, length):
        temp = dp1
        dp1 = max(dp1, dp2 + prices[i])
        dp2 = max(dp2, dp3 - prices[i])
        dp3 = temp

    return max(dp1, dp3)


def test(prices, answer):
    outputs = max_profit(prices)
    print("Inputs:{}, Outputs:{}, Except:{}".format(prices, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test([1, 2, 3, 0, 2], 3)


if __name__ == '__main__':
    main()
