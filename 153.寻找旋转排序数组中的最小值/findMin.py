# -*- encoding: utf-8 -*-
"""
@file: findMin.py
@time: 2020/9/21 下午2:13
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  153.寻找旋转排序数组中的最小值

假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
你可以假设数组中不存在重复元素。

示例 1:
输入: [3,4,5,1,2]
输出: 1

示例 2:
输入: [4,5,6,7,0,1,2]
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
"""


def find_min1(nums):
    """
    二分法
    :param nums: (list[int])
    :return: (int)
    """
    #
    if len(nums) < 2:
        return nums[0]

    # 满足 nums[0] < nums[-1]. 说明是有序序列。
    if nums[0] < nums[-1]:
        return nums[0]

    left, right = 0, len(nums) - 1
    n = len(nums)
    while left <= right:
        mid = int(left + (right - left) / 2)
        if mid + 1 < n and nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        elif mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
            return nums[mid]
        elif nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1


def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


def test(inputs, answer):
    outputs = find_min(inputs)
    print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    nums, answer = [3, 4, 5, 1, 2], 1
    test(nums, answer)

    nums, answer = [4, 5, 6, 7, 0, 1, 2], 0
    test(nums, answer)

    nums, answer = [1], 1
    test(nums, answer)

    nums, answer = [1, 2, 3], 1
    test(nums, answer)


if __name__ == '__main__':
    main()
