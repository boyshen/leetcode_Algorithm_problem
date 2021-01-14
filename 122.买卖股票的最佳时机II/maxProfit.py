# -*- encoding: utf-8 -*-
"""
@file: maxProfit.py
@time: 2020/9/20 下午5:13
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  122.买卖股票的最佳时机 II

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

提示：
1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
"""


def max_profit1(prices):
    """
    峰谷法。参考中文官网题解
    max_profit = sum(height[peak] - height[valley])
    :param prices: (list[int])
    :return: (int)
    """
    m_profit = 0
    size = len(prices)

    i = 0
    while i < size - 1:
        # 找到谷
        while i < size - 1 and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]
        # 找到峰
        while i < size - 1 and prices[i] <= prices[i + 1]:
            i += 1
        peak = prices[i]
        m_profit += peak - valley
    return m_profit


def max_profit2(prices):
    """
    简单的一次遍历 (贪心), 在峰谷法的基础上进行改进。时间复杂度O(N), 空间复杂度O(1)
    :param prices: (list[int])
    :return: (int)
    """
    m_profit = 0
    size = len(prices)
    for i in range(1, size):
        if prices[i] > prices[i - 1]:
            m_profit += prices[i] - prices[i - 1]
    return m_profit


def max_profit3(prices):
    """
    贪心算法代码优化。时间复杂度O(N), 空间复杂度O(1)
    :param prices: (list[int])
    :return:(int)
    """
    return sum([max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1)])


def max_profit4(prices):
    """
    动态规划。时间复杂度为 O(n), 空间复杂度为 O(n*2)
    :param prices: (list[int])
    :return: (int)
    """
    n = len(prices)
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

    return dp[-1][0]


def max_profit(prices):
    """
    动态规划（优化）。时间复杂度为 O(n), 空间复杂度 O(1)
    :param prices: (list[int])
    :return: (int)
    """
    n = len(prices)
    profit1 = 0
    profit2 = -prices[0]
    for i in range(1, n):
        new_profit1 = max(profit1, profit2 + prices[i])
        new_profit2 = max(profit2, profit1 - prices[i])
        profit1 = new_profit1
        profit2 = new_profit2
    return profit1


def test(inputs, answer):
    outputs = max_profit(inputs)
    print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))


def main():
    prices, answer = [7, 1, 5, 3, 6, 4], 7
    test(prices, answer)

    prices, answer = [1, 2, 3, 4, 5], 4
    test(prices, answer)

    prices, answer = [7, 6, 4, 3, 1], 0
    test(prices, answer)


if __name__ == '__main__':
    main()
