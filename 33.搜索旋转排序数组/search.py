# -*- encoding: utf-8 -*-
"""
@file: search.py
@time: 2020/9/20 下午10:45
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  33.搜索旋转排序数组

假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
"""


def search(nums, target):
    """
    二分查找法
    :param nums: (list[int])
    :param target: (int)
    :return: (int)
    """
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            return mid
        elif nums[0] <= nums[mid]:
            if nums[0] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test(nums, target, answer):
    outputs = search(nums, target)
    print("Inputs:nums={},target={}, Outputs:{}, Except:{}".format(nums, target, outputs, answer))
    assert outputs == answer, print("Answer failed")


def main():
    nums, target, answer = [4, 5, 6, 7, 0, 1, 2], 0, 4
    test(nums, target, answer)

    nums, target, answer = [4, 5, 6, 7, 0, 1, 2], 3, -1
    test(nums, target, answer)


if __name__ == '__main__':
    main()
