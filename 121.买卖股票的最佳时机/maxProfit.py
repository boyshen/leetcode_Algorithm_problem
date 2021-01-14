# -*- encoding: utf-8 -*-
"""
@file: maxProfit.py
@time: 2020/10/10 下午3:53
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  121.买卖股票的最佳时机

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""


def max_profit(prices):
    """
    DP. 时间复杂度 O(N), 空间复杂度 O(1)

    初始化： dp[0] = 0,  purchase = prices[0].  purchase 为买入的股票价格。dp 为最大获利
    DP 方程：
        dp[i] = max(dp[i-1], prices[i] - purchase).
        purchase = min(purchase, prices[i]).

    :param prices: (list[int])
    :return: (int)
    """
    if not prices:
        return 0

    profit, purchase = 0, prices[0]
    n = len(prices)
    for i in range(1, n):
        profit = max(profit, prices[i] - purchase)
        purchase = min(purchase, prices[i])
    return profit


def test(prices, answer):
    outputs = max_profit(prices)
    print("Inputs:{}, Outputs:{}, Answer:{}".format(prices, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test([7, 1, 5, 3, 6, 4], 5)
    test([7, 6, 4, 3, 1], 0)


if __name__ == '__main__':
    main()
