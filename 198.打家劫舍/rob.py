# -*- encoding: utf-8 -*-
"""
@file: rob.py
@time: 2020/10/10 上午10:26
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 198.打家劫舍

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

提示：
0 <= nums.length <= 100
0 <= nums[i] <= 400

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
"""


def rob1(nums):
    """
    DP. 时间复杂度 O(N), 空间复杂度 O(N)
    dp[i] = Max(dp[i-2] + nums[i], dp[i-1])
    边界：{
            dp[0] = nums[0], len(nums) < 2
            dp[1] = Max(nums[0], nums[1]), len(nums) == 2
          }
    :param nums: (list[int])
    :return: (int)
    """
    if not nums:
        return 0

    n = len(nums)
    if n < 2:
        return nums[0]

    dp = [nums[0]] + [max(nums[0], nums[1])] + [0] * (n - 2)
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[-1]


def rob(nums):
    """
    DP.(优化) 时间复杂度 O(N), 空间复杂度 O(1)
    :param nums: (list[int])
    :return: (int)
    """
    if not nums:
        return 0

    n = len(nums)
    if n < 2:
        return nums[0]

    f1, f2 = nums[0], max(nums[0], nums[1])
    for i in range(2, n):
        f1, f2 = f2, max(f1 + nums[i], f2)
    return f2


def test(nums, answer):
    outputs = rob(nums)
    print("Inputs:{}, Outputs:{}, Except:{}".format(nums, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test([1, 2, 3, 1], 4)
    test([2, 7, 9, 3, 1], 12)
    test([4, 4, 5, 17, 8], 21)
    test([2, 1, 1, 2], 4)


if __name__ == '__main__':
    main()
