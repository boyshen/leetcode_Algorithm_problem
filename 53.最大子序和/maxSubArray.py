# -*- encoding: utf-8 -*-
"""
@file: maxSubArray.py
@time: 2020/10/8 下午7:47
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  53.最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray/
"""


def max_sub_array(nums):
    """
    DP. 时间复杂度 O(N), 空间复杂度 O(1)
    f[i] = max(f[i-1] + a[i], a[i])

    :param nums: (list[int])
    :return: (int)
    """

    max_value = nums[0]
    prev = nums[0]
    for i in range(1, len(nums)):
        prev = max(nums[i] + prev, nums[i])
        max_value = max(prev, max_value)
    return max_value


def test(nums, answer):
    outputs = max_sub_array(nums)
    print("Inputs:{}, Outputs:{}, Except:{}".format(nums, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    test([1, 2], 3)


if __name__ == '__main__':
    main()
