# -*- encoding: utf-8 -*-
"""
@file: maxProfit.py
@time: 2020/10/30 下午3:53
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  123.买卖股票的最佳时机 III

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii

解答参考：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/wu-chong-shi-xian-xiang-xi-tu-jie-123mai-mai-gu-pi/
"""


def max_profit1(prices):
    """
    DFS + 记忆化搜索。时间复杂度 O(2^n)。 空间复杂度 O(N)
    :param prices: (list[int])
    :return: (int)
    """
    memory = {}

    def dfs(level, status, times):
        if (level, status, times) in memory:
            return memory[(level, status, times)]
        if level == len(prices) or times == 2:
            return 0

        # 定义 3 个变量。分别表示保持不动，买、 卖
        keep, buy, sell = 0, 0, 0
        keep = dfs(level + 1, status, times)

        if status == 0:
            # 处理买
            buy = dfs(level + 1, 1, times) - prices[level]
        else:
            # 处理卖
            sell = dfs(level + 1, 0, times + 1) + prices[level]

        memory[(level, status, times)] = max(keep, buy, sell)
        return memory[(level, status, times)]

    return dfs(0, 0, 0)


def max_profit2(prices):
    """
    DP.
    定义三种状态。[index][times][status].
    index： 第 i 天、
    times： 第 t 次
    status： 买入 1、卖出 0。

    dp[i][0][0]： 第 i 天第 0 次卖出后的最大利润
    dp[i][0][1]： 第 i 天第 0 次买入后的最大利润
    dp[i][1][0]： 第 i 天第 1 次卖出后的最大利润
    dp[i][1][1]： 第 i 天第 1 次买入后的最大利润
    dp[i][2][0]： 第 i 天第 2 次卖出后的最大利润
    dp[i][2][1]： 第 i 天第 2 次买入后的最大利润 （不需要考虑）

    :param prices: (list[int])
    :return: (int)
    """
    if not prices:
        return 0

    n = len(prices)
    dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n)]

    dp[0][0][0] = 0
    dp[0][0][1] = -prices[0]
    dp[0][1][0] = 0
    dp[0][1][1] = -prices[0]
    dp[0][2][0] = 0

    for i in range(1, n):
        # 处理第一次买入和卖出
        dp[i][0][1] = max(dp[i - 1][0][1], -prices[i])
        dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][1] + prices[i])

        # 处理第二次买入和卖出
        dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][1][0] - prices[i])
        dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][1][1] + prices[i])

    return max(dp[-1][0][1], dp[-1][1][0], dp[-1][1][1], dp[-1][2][0])


def max_profit3(prices):
    """
    DP + 二维数组. 使用 0，1，2，3 表示
    dp[i][0]  第 i 天 第1次买入
    dp[i][1]  第 i 天 第1次卖出
    dp[i][2]  第 i 天 第2次买入
    dp[i][3]  第 i 天 第2次卖出

    :param prices: (list[int])
    :return: (int)
    """
    if not prices:
        return 0

    n = len(prices)
    dp = [[0] * 4 for _ in range(n)]
    dp[0][0] = -prices[0]
    dp[0][1] = 0
    dp[0][2] = -prices[0]
    dp[0][3] = 0

    for i in range(1, n):
        # 第一次买入、卖出
        dp[i][0] = max(dp[i - 1][0], -prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

        # 第二次买入、卖出
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])
        dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])

    return max(dp[-1][0], dp[-1][1], dp[-1][2], dp[-1][3])


def max_profit(prices):
    """
    DP + 一维数组
    dp1 前一天第一次买入
    dp2 前一天第一次卖出
    dp3 前一天第二次买入
    dp4 前一天第二次卖出
    :param prices: (list[int])
    :return: (int)
    """
    if not prices:
        return 0

    n = len(prices)
    dp1 = -prices[0]
    dp2 = 0
    dp3 = -prices[0]
    dp4 = 0
    for i in range(1, n):
        dp1 = max(dp1, -prices[i])
        dp2 = max(dp2, dp1 + prices[i])

        dp3 = max(dp3, dp2 - prices[i])
        dp4 = max(dp4, dp3 + prices[i])

    return max(dp1, dp2, dp3, dp4)


def test(prices, answer):
    outputs = max_profit(prices)
    print("Inputs:{}, Outputs:{}, Except:{}".format(prices, outputs, answer))


def main():
    test([3, 3, 5, 0, 0, 3, 1, 4], 6)
    test([1, 2, 3, 4, 5], 4)
    test([7, 6, 4, 3, 1], 0)


if __name__ == '__main__':
    main()
