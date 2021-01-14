# -*- encoding: utf-8 -*-
"""
@file: subsets.py
@time: 2020/9/14 下午3:14
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 78.子集

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
"""


def subsets1(nums):
    """
    迭代. 时间复杂度 O(n * n!), 空间复杂度 O(n)
    :param nums: (list)
    :return: (list)
    """
    res = [[]]
    for num in nums:
        res += [val + [num] for val in res]
    return res


def subsets(nums):
    """
    递归。时间复杂度 O(n * n!), 空间复杂度 O(n * 2)
    :param nums: (list)
    :return: (list)
    """
    res = []
    n = len(nums)

    def helper(i, temp):
        res.append(temp)
        for j in range(i, n):
            helper(j + 1, temp + [nums[j]])

    helper(0, [])
    return res


def removal(data):
    """ 去重 """
    res = []
    for val in data:
        if val in res:
            continue
        res.append(val)
    return res


def main():
    inputs = [1, 2, 3]
    outputs = removal(subsets(inputs))
    answer = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    print(outputs)
    assert len(outputs) == len(answer), print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    for output in outputs:
        assert output in answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))


if __name__ == '__main__':
    main()
