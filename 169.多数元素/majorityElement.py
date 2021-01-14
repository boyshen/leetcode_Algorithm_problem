# -*- encoding: utf-8 -*-
"""
@file: majorityElement.py
@time: 2020/12/22 下午7:13
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  169. 多数元素

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
"""
from collections import Counter


def majority_element(nums):
    """
    哈希
    """
    count = Counter(nums)
    return max(count.keys(), key=count.get)


def main():
    outputs = majority_element([3, 2, 3])
    answer = 3
    assert outputs == answer

    outputs = majority_element([2, 2, 1, 1, 1, 2, 2])
    answer = 2
    assert outputs == answer


if __name__ == '__main__':
    main()
