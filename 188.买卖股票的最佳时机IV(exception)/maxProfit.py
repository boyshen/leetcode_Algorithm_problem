# -*- encoding: utf-8 -*-
"""
@file: maxProfit.py
@time: 2020/11/2 下午4:43
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  188.买卖股票的最佳时机IV(exception)

给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1：
输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

示例 2：
输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

提示：
0 <= k <= 109
0 <= prices.length <= 104
0 <= prices[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
"""


def max_profit1(k, prices):
    """
    递归 + 记忆化搜索。 时间复杂度 O(N), 空间复杂度 O(N)
    (Time Limit Exceeded 超出时间限制)
    :param k: (int)
    :param prices: (list[int])
    :return: (int)
    """

    def dfs(index, status, count):
        if (index, status, count) in memory:
            return memory[(index, status, count)]
        if index >= length or count == k:
            return 0

        sell, buy, keep = 0, 0, 0
        keep = dfs(index + 1, status, count)
        if status == 1:
            sell = dfs(index + 1, 0, count + 1) + prices[index]
        else:
            buy = dfs(index + 1, 1, count) - prices[index]

        memory[(index, status, count)] = max(keep, sell, buy)
        return memory[(index, status, count)]

    def unlimited_max_profit():
        dp1 = 0
        dp2 = -prices[0]

        for i in range(1, length):
            temp = dp1
            dp1 = max(dp1, dp2 + prices[i])
            dp2 = max(dp2, temp - prices[i])
        return dp1

    memory = {}
    length = len(prices)
    if not prices:
        return 0

    if 2 * k > length:
        return unlimited_max_profit()
    else:
        return dfs(0, 0, 0)


def max_profit2(k, prices):
    """
    DP. 时间复杂度 O(N * k), 空间复杂度 O(N * k * 2) . N为 prices 的大小，k 为交易次数
    (Time Limit Exceeded 超出时间限制)
    DP 方程。
    dp[index][k][status]  ==>  第 i 天第k次的买入／卖出状态
    example:
    dp[i][0][1]  ==> 第 i 天第0次买入
    dp[i][1][0]  ==> 第 i 天第1次卖出

    dp[i][1][1]  ==> 第 i 天第1次买入
    dp[i][2][0]  ==> 第 i 天第2次卖出

    dp[i][2][1]  ==> 第 i 天第2次买入
    dp[i][3][0]  ==> 第 i 天第3次卖出
    其中 (k=0,1 时候为完成一次交易， k=1，2时候完成一次交易)

    初始化：
    # (k+1) 是因为需要在 k+1 完成交易。比如 k = 2 时候，如下在 2 次卖出。 所以需要用到
    #     dp[i][0][1]  ==> 第 i 天第0次买入
    #     dp[i][1][0]  ==> 第 i 天第1次卖出
    #
    #     dp[i][1][1]  ==> 第 i 天第1次买入
    #     dp[i][2][0]  ==> 第 i 天第2次卖出
    for t in range(k+1):
        dp[0][t][0] = 0
        dp[0][t][1] = -prices[0]

    计算
    for i in range(1, len(prices)):
        for t in range(1, k+1):
            # 卖出
            dp[i][t][0] = max(dp[i-1][t][0], dp[i-1][t-1][1] + prices[i])
            # 买入
            dp[i][t-1][1] = max(dp[i-1][t-1][1], dp[i-1][t-1][0] - prices[i])

    :param k: (int)
    :param prices: (list[int])
    :return: (int)
    """

    def unlimited_max_profit():
        dp1 = 0
        dp2 = -prices[0]

        for i in range(1, length):
            temp = dp1
            dp1 = max(dp1, dp2 + prices[i])
            dp2 = max(dp2, temp - prices[i])
        return dp1

    def k_max_profit():
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(length)]
        for t in range(k + 1):
            dp[0][t][0] = 0
            dp[0][t][1] = -prices[0]

        for i in range(1, length):
            for t in range(1, k + 1):
                dp[i][t][0] = max(dp[i - 1][t][0], dp[i - 1][t - 1][1] + prices[i])
                dp[i][t - 1][1] = max(dp[i - 1][t - 1][1], dp[i - 1][t - 1][0] - prices[i])
        return dp[-1][k][0]

    length = len(prices)
    if not prices:
        return 0
    # 优化操作。当交易次数 k * 2(一次买、一次卖) 大于交易的prices数量。则可以认为无限次交易，因为每天一次卖／买，遍历完成也没有达到 k 次。
    if 2 * k > length:
        return unlimited_max_profit()
    else:
        return k_max_profit()


def max_profit3(k, prices):
    def unlimited_max_profit():
        dp1 = 0
        dp2 = -prices[0]
        for i in range(1, length):
            temp = dp1
            dp1 = max(dp1, dp2 + prices[i])
            dp2 = max(dp2, temp - prices[i])
        return dp1

    def k_max_profit():
        dp = [[0, 0] for _ in range(k + 1)]
        for i in range(k + 1):
            dp[i][0] = 0
            dp[i][1] = -prices[0]
        for i in range(1, length):
            # 倒序
            for j in range(k, 0, -1):
                dp[j - 1][1] = max(dp[j - 1][1], dp[j - 1][0] - prices[i])
                dp[j][0] = max(dp[j][0], dp[j - 1][1] + prices[i])
        return dp[-1][0]

    if not prices:
        return 0

    length = len(prices)
    if 2 * k >= length:
        return unlimited_max_profit()
    else:
        return k_max_profit()


def max_profit(k, prices):
    def unlimited_max_profit():
        profit = 0
        for i in range(1, length):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    def k_max_profit():
        cost = [float('inf')] * (k + 1)
        profit = [0] * (k + 1)
        for i in range(length):
            for j in range(1, k + 1):
                cost[j] = min(cost[j], prices[i] - profit[j - 1])
                profit[j] = max(profit[j], prices[i] - cost[j])
        return profit[-1]

    if not prices:
        return 0

    length = len(prices)
    if 2 * k >= length:
        return unlimited_max_profit()
    else:
        return k_max_profit()


def test(k, prices, answer):
    outputs = max_profit(k, prices)
    print("Inputs:k={}, prices={}, Outputs:{}, Except:{}".format(k, prices, outputs, answer))


def main():
    test(2, [2, 4, 1], 2)
    test(2, [3, 2, 6, 5, 0, 3], 7)
    test(4, [3, 2, 6, 5, 0, 3], 7)


if __name__ == '__main__':
    main()
