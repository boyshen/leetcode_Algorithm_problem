# -*- encoding: utf-8 -*-
"""
@file: reversePairs.py
@time: 2020/10/28 下午5:49
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 493.翻转对

给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
你需要返回给定数组中的重要翻转对的数量。

示例 1:
输入: [1,3,2,3,1]
输出: 2

示例 2:
输入: [2,4,3,5,1]
输出: 3

注意:
给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-pairs
"""


class Solution(object):
    """
    归并排序。时间复杂度 O(nlogn). 空间复杂度 O(N)
    """

    def reverse_pairs(self, nums):
        return self.merger(nums, 0, len(nums) - 1)

    def merger(self, nums, left, right):
        if left >= right:
            return 0
        mid = (left + right) >> 1
        count = self.merger(nums, left, mid) + self.merger(nums, mid + 1, right)

        s, e = left, mid + 1
        while s <= mid and e <= right:
            if nums[s] > 2 * nums[e]:
                e += 1
                # (mid + 1) - s 是表示在满足条件后，因为序列经过排序，当前的元素以及当前元素到mid+1的元素都满足条件。
                # 例如： left ==> [2,3,4], right ==> [1,5]
                #       当left = 0, mid = 2, right = 4
                #       当 left ==> 3 满足大于 right ==> 1 的条件时候，则同样的 left ==> 4 也满足。所以不需要重复查看，直接
                #          (mid + 1）- s 表示当前元素到剩余的元素数量
                count += (mid + 1) - s
            else:
                s += 1

        nums[left:right + 1] = sorted(nums[left:right + 1])
        return count


def test(nums, answer):
    print("Inputs:{}".format(nums), end="")
    outputs = Solution().reverse_pairs(nums)
    print("Outputs:{}, Except:{}".format(outputs, answer))


def main():
    test([1, 3, 2, 3, 1], 2)
    test([2, 4, 3, 5, 1], 3)


if __name__ == '__main__':
    main()
