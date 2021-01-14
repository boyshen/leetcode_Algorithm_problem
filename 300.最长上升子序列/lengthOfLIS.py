# -*- encoding: utf-8 -*-
"""
@file: lengthOfLIS.py
@time: 2020/11/3 下午3:25
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  300. 300.最长上升子序列

给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。

进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/
"""


def length_of_lis1(nums):
    """
    DP. 时间复杂度 O(N^2), 空间复杂度 O(N)
    DP. 方程
    dp[i]  ==> 表示从nums[0] 到 nums[i] 的上升序列长度。

    初始化：
        dp = [1] * len(nums)  == > 表示每个元素都有一个上升序列长度

    计算
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                # dp[j] 表示 i 之前元素的上升序列。 当 nums[i] > nums[j] 则说明在j元素到i元素之间存在上升序列。
                dp[i] = max (dp[i], dp[j] + 1)  # DP 方程

    :param nums: (list[int])
    :return: (int)
    """
    if not nums:
        return 0

    length = len(nums)
    dp = [1] * length

    for i in range(length):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def length_of_lis(nums):
    """
    二分法。 时间复杂度 O(NlogN), 空间复杂度 O(N)

    设计思路：
        1. 维护一个有序列表 res。 依次遍历 nums 中的每个元素。
        2. 将每个元素nums[i]进行判断
            if nums[i] > res[-1]：
                res.append(nums[i])
            else:
                进入二分查找。
                查找到当 nums[i] >= res[j] 时候。
                替换 res[j+1] 中的元素为 nums[i]

        3. 统计 res 目录中的元素数量作为返回结果

    输入：[10, 9, 2, 5, 3, 7, 101, 18]
    计算：   1. res = [10]
            2. res = [9]
            3. res = [2]
            4. res = [2, 5]
            5. res = [2, 3]
            6. res = [2, 3, 7]
            7. res = [2, 3, 7, 101]
            8. res = [2, 3, 7, 18]
    返回：len(res)
    :param nums: (list[int])
    :return: (int)
    """

    if not nums:
        return 0

    res = [nums[0]]
    length = len(nums)
    for i in range(1, length):
        if nums[i] > res[-1]:
            res.append(nums[i])
        else:
            left, right = 0, len(res) - 1
            while left < right:
                mid = (left + right) >> 1
                if res[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            res[left] = nums[i]

    return len(res)


def test(nums, answer):
    outputs = length_of_lis(nums)
    print("Inputs:{}, Outputs:{}, Except:{}".format(nums, outputs, answer))
    assert outputs == answer, "Answer Failed"


def main():
    test([10, 9, 2, 5, 3, 7, 101, 18], 4)


if __name__ == '__main__':
    main()
