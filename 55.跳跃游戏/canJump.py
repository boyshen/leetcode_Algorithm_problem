# -*- encoding: utf-8 -*-
"""
@file: canJump.py
@time: 2020/9/20 下午7:28
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  55.跳跃游戏

给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
"""


def can_jump1(nums):
    """
    贪心 (从左往右贪心)
    :param nums: (list[int])
    :return: (int)
    """
    if not nums:
        return False

    max_position = 0
    size = len(nums)
    for i in range(size):
        if i <= max_position:
            max_position = max(max_position, i + nums[i])
            if max_position >= size - 1:
                return True
    return False


def can_jump(nums):
    """
    贪心 (从右往左贪心)
    :param nums: (list[int])
    :return: (int)
    """
    right_position = len(nums) - 1
    j = len(nums) - 1
    while j >= 0:
        if nums[j] + j >= right_position:
            right_position = j
        j -= 1

    return right_position == 0


def test(inputs, answer):
    outputs = can_jump(inputs)
    print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    nums, answer = [2, 3, 1, 1, 4], True
    test(nums, answer)

    nums, answer = [3, 2, 1, 0, 4], False
    test(nums, answer)


if __name__ == '__main__':
    main()
