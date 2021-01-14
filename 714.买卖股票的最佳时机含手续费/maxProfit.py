# -*- encoding: utf-8 -*-
"""
@file: maxProfit.py
@time: 2020/11/2 下午3:58
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  714.买卖股票的最佳时机含手续费

给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

注意:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
"""


def max_profit1(prices, fee):
    """
    DP. 时间复杂度 O(N), 空间复杂度 O(N * 2)
    DP 方程。 dp[index][state]
    dp[i][0]  ==> 卖出
    dp[i][1]  ==> 买入

    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)  ==> 前一天卖出的利润 vs 前一天买入的股价 + 当前股价 - 手续费
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])        ==> 前一天买入的利润 vs 前一天卖出利润 - 当前股价
    :param prices: (list[int])
    :param fee: (int)
    :return: (int)
    """
    if not prices:
        return 0

    length = len(prices)
    dp = [[0] * 2 for _ in range(length)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]

    for i in range(1, length):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

    return dp[-1][0]


def max_profit2(prices, fee):
    """
     DP + 空间优化。 时间复杂度 O(N), 空间复杂度 O(1)
     DP 方程。 dp1， dp2 表示卖出和买入
     dp1 ==> 卖出
     dp2 ==> 买入

     temp = dp1
     dp1 = max(dp1, dp2 + prices[i] - fee)
     dp2 = max(dp2, temp - prices[i])

    :param prices: (list[int])
    :param fee: (int)
    :return: (int)
    """

    if not prices:
        return 0

    dp1 = 0
    dp2 = -prices[0]
    length = len(prices)
    for i in range(1, length):
        temp = dp1
        dp1 = max(dp1, dp2 + prices[i] - fee)
        dp2 = max(dp2, temp - prices[i])

    return dp1


def max_profit(prices, fee):
    """
    递归 + 记忆化搜索。 时间复杂度 O(N), 空间复杂度O(N)
    :param prices: (list[int])
    :param fee: (int)
    :return: (int)
    """

    def dfs(index, status):
        if (index, status) in memory:
            return memory[(index, status)]

        if index >= length:
            return 0

        buy, sell, keep = 0, 0, 0
        keep = dfs(index + 1, status)
        if status == 1:
            sell = dfs(index + 1, 0) + prices[index] - fee
        else:
            buy = dfs(index + 1, 1) - prices[index]
        memory[(index, status)] = max(keep, sell, buy)

        return memory[(index, status)]

    length = len(prices)
    memory = {}
    if not prices:
        return 0
    else:
        return dfs(0, 0)


def test(prices, fee, answer):
    outputs = max_profit(prices, fee)
    print("Inputs:prices={}, fee={}, Outputs:{}, Except:{}".format(prices, fee, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test([1, 3, 2, 8, 4, 9], 2, 8)


if __name__ == '__main__':
    main()
