# -*- encoding: utf-8 -*-
"""
@file: moveZeros.py
@time: 2020/8/27 下午2:41
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  283.移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

example:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes/
"""


def move_zeroes1(nums):
    """
    指针法
    时间复杂度 O(n), 空间复杂度 O(1)
    :param nums: (list, mandatory)
    :return: (list or None)
    """
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1
    return nums


def move_zeroes(nums):
    """
    指针法
    时间复杂度O(n), 空间复杂度 O(1)
    :param nums: (list[int])
    :return: (list[int])
    """
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1

    while pos < len(nums):
        nums[pos] = 0
        pos += 1

    return nums


def test(inputs, answer):
    print("Inputs:{}, ".format(inputs), end='')
    outputs = move_zeroes(inputs)
    print("Outputs:{}, Except:{}".format(inputs, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    nums = [0, 1, 0, 3, 12]
    output = [1, 3, 12, 0, 0]
    test(nums, output)

    nums = [0, 0, 0, 1]
    output = [1, 0, 0, 0]
    test(nums, output)

    nums = [1, 1, 13, 5, 7, 0]
    output = [1, 1, 13, 5, 7, 0]
    test(nums, output)

    nums = [1, 1, 1, 3, 4]
    output = [1, 1, 1, 3, 4]
    test(nums, output)

    nums = [0, 0, 0, 0]
    output = [0, 0, 0, 0]
    test(nums, output)


if __name__ == '__main__':
    main()
