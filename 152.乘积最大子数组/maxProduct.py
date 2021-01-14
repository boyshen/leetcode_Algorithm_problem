# -*- encoding: utf-8 -*-
"""
@file: maxProduct.py
@time: 2020/10/9 下午2:53
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  152.乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
"""


def max_product1(nums):
    """
    暴力法。时间复杂度 O(N^2), 空间复杂度 O(N^2)
    Time Limit Exceeded
    :param nums: (list[int])
    :return: (int)
    """
    value = []
    n = len(nums)
    for i in range(n):
        res = nums[i]
        value.append(res)
        for j in range(i + 1, n):
            res = res * nums[j]
            value.append(res)
    return max(value)


def max_product(nums):
    """
    DP. 时间复杂度 O(N), 空间复杂度 O(1)

    imax 保存上一个最大值。imin 保存上一步的最小值。
    如果遇到 nums[i] < 0 的时候，则需要对 imax 和 imin 进行交换（由于存在负数，则最小的可能变成最大的，最大的可能变成最小的）。
    imax = max(imax * nums[i], nums[i])
    imin = min(imin * nums[i], nums[i])
    f[i] = max(max, imax)

    :param nums: (list[int])
    :return: (int)
    """
    i_max, i_min, max_val = 1, 1, nums[0]
    for val in nums:
        if val < 0:
            i_max, i_min = i_min, i_max
        i_max = max(i_max * val, val)
        i_min = min(i_min * val, val)
        max_val = max(i_max, max_val)

    return max_val


def test(nums, answer):
    outputs = max_product(nums)
    print("Inputs:{}, Outputs:{}, Except:{}".format(nums, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test([2, 3, -2, 4], 6)
    test([-2, 0, -1], 0)
    test([-2], -2)
    test([0, 2], 2)


if __name__ == '__main__':
    main()
