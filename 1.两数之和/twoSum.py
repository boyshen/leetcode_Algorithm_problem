# -*- encoding: utf-8 -*-
"""
@file: twoSum.py
@time: 2020/8/20 上午10:34
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 1.两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

example:
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
"""


def two_sum(nums, target):
    """
    一遍哈希表. 时间复杂度 O(n), 空间复杂度 O(n)
    :param nums: (list, mandatory)
    :param target: (int, mandatory)
    :return: (list)
    """
    word_dict = {}
    for i, x in enumerate(nums):
        if target - x in word_dict:
            return [word_dict[target - x], i]
        word_dict[x] = i
    return []


def test(nums, targets, answer):
    outputs = two_sum(nums, targets)
    print("Inputs:nums={},targets={}, Outputs:{}, Except:{}".format(nums, targets, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    inputs = [2, 7, 11, 15]
    target = 9
    answer = [0, 1]
    test(inputs, target, answer)


if __name__ == '__main__':
    main()
