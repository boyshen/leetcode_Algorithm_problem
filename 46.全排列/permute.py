# -*- encoding: utf-8 -*-
"""
@file: permute.py
@time: 2020/9/13 下午3:16
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 46.全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
"""


def permute(nums):
    """
    搜索回溯。时间复杂为 (n * n!), 空间复杂度 O(n)
    :param nums: (list)
    :return: (list)
    """
    if not nums:
        return
    if len(nums) == 1:
        return [nums]

    res = []

    def helper(num, perm):
        if len(num) == 2:
            res.append(perm + [num[0]] + [num[1]])
            res.append(perm + [num[1]] + [num[0]])
            return

        for i in range(len(num)):
            perm.append(num[i])
            helper(num[:i] + num[i + 1:], perm)
            perm.pop()

    helper(nums, [])
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
    outputs = removal(permute(inputs))
    answer = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert len(outputs) == len(answer), print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    for output in outputs:
        assert output in answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs = [1]
    outputs = removal(permute(inputs))
    answer = [[1]]
    assert len(outputs) == len(answer), print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    for output in outputs:
        assert output in answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
