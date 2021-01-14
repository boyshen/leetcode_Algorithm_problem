# -*- encoding: utf-8 -*-
"""
@file: threeSum.py
@time: 2020/8/20 上午11:20
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 15.三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

example:
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
"""


def three_sum1(nums):
    """
    排序 + hash。时间复杂度: O(N^2), 空间复杂度: O(logN)
    :param nums: (list, mandatory)
    :return: (list)
    """
    res = set()
    nums.sort()
    for i in range(len(nums) - 2):
        save_dict = {}
        for j in range(i + 1, len(nums)):
            if 0 - (nums[i] + nums[j]) in save_dict:
                res.add((nums[i], -(nums[i] + nums[j]), nums[j]))
            else:
                save_dict[nums[j]] = 1

    return list(res)


def three_sum2(nums):
    """
    排序 + 双指针。时间复杂度: O(N^2), 空间复杂度：O(logN)
    :param nums: (list, mandatory)
    :return: (list)
    """
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s > 0:
                right -= 1
            elif s < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res


def three_sum(nums):
    """
    排序 + 双指针。时间复杂度: O(N^2), 空间复杂度：O(logN)
    :param nums: (list)
    :return: (list)
    """
    res = []
    nums.sort()

    i, size = 0, len(nums)
    for i in range(size - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, size - 1
        while left < right:
            val = nums[left] + nums[right] + nums[i]
            if val == 0:
                res.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

            elif val > 0:
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                right -= 1

            else:
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                left += 1
    return res


def test(nums, answer):
    outputs = three_sum(nums)
    print("Inputs:{}, Output:{}, Answer:{}".format(nums, outputs, answer))
    assert len(outputs) == len(answer), print("Answer Failed")
    for output in outputs:
        assert list(output) in answer, print("Answer Failed")


def main():
    inputs = [0, 0]
    answer = []
    test(inputs, answer)

    inputs = [0, 0, 0]
    answer = [[0, 0, 0]]
    test(inputs, answer)

    inputs = [1, -1, -1, 0]
    answer = [[-1, 0, 1]]
    test(inputs, answer)

    inputs = [-1, 0, 1, 2, -1, -4]
    answer = [[-1, -1, 2], [-1, 0, 1]]
    test(inputs, answer)

    inputs = [-2, 0, 1, 1, 2]
    answer = [[-2, 0, 2], [-2, 1, 1]]
    test(inputs, answer)

    inputs = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    answer = [[-4, -2, 6], [-2, 0, 2], [-4, 1, 3], [-4, 2, 2], [-4, 0, 4], [-2, -2, 4]]
    test(inputs, answer)


if __name__ == '__main__':
    main()
