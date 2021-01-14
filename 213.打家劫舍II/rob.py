# -*- encoding: utf-8 -*-
"""
@file: rob.py
@time: 2020/10/10 下午2:18
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  213.打家劫舍II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2:
输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-ii
"""


def rob1(nums):
    """
    DP. 时间复杂度 O(N), 空间复杂度 O(N)
    将环状的数据分割成两个单排。要么偷第一个不偷最后一个nums[:-1], 要么偷最后一个不偷第一个 nums[1:], 最后比较两个大小。

    dp1[i] = Max(dp[i-2] + nums[i], dp[i-1]) . nums[:-1]
    dp2[i] = Max(dp[i-2] + nums[i], dp[i-1]) . nums[1:]
    max = Max(dp1[-1], dp2[-1])
    边界：{
        max = Max(nums), if len(nums) <= 3.
    }
    :param nums: (list[int])
    :return: (int)
    """

    def simple(num):
        n = len(num)
        dp = [num[0]] + [max(num[0], num[1])] + [0] * (n - 2)
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + num[i], dp[i - 1])
        return dp[-1]

    if not nums:
        return 0
    elif len(nums) <= 3:
        return max(nums)
    else:
        return max(simple(nums[:-1]), simple(nums[1:]))


def rob(nums):
    """
    DP.(优化) 时间复杂度 O(N), 空间复杂度 O(1)
    :param nums: (list[int])
    :return: (int)
    """

    def sample(i, j):
        prev, now = nums[i], max(nums[i], nums[i + 1])
        for idx in range(i + 2, j):
            prev, now = now, max(prev + nums[idx], now)
        return now

    if not nums:
        return 0
    elif len(nums) <= 3:
        return max(nums)
    else:
        n = len(nums)
        return max(sample(0, n - 1), sample(1, n))


def test(nums, answer):
    outputs = rob(nums)
    print("Inputs:{}, Outputs:{}, Except:{}".format(nums, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test([2, 3, 2], 3)
    test([1, 2, 3, 1], 4)
    test([2, 1, 1, 2], 3)
    test([1, 3, 1, 3, 100], 103)
    test([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 16)


if __name__ == '__main__':
    main()
