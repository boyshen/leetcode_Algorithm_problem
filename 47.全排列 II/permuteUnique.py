# -*- encoding: utf-8 -*-
"""
@file: permuteUnique.py
@time: 2020/9/13 下午5:28
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 47.全排列 II
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii/
"""


def permute_unique1(nums):
    """
    回溯 + 去重。 时间复杂度 O(n * n!), 空间复杂度 (n * 3)
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
            helper(num[: i] + num[i + 1:], perm)
            perm.pop()

    helper(nums, [])

    values = []
    for r in res:
        if r not in values:
            values.append(r)
    return values


def permute_unique(nums):
    """
    回溯 + 剪枝.  时间复杂度 O(n * n!), 空间复杂度 (n * 2)
    :param nums: (list[int])
    :return: (list[list[int]])
    """
    if not nums:
        return
    if len(nums) == 1:
        return [nums]

    res = []

    def helper(num, perm, used, level):
        if len(num) == 2:
            # 如果两个子元素相等，则保存一份 (剪枝)
            if num[0] == num[1]:
                res.append(perm + [num[0]] + [num[1]])
            else:
                res.append(perm + [num[0]] + [num[1]])
                res.append(perm + [num[1]] + [num[0]])
            return

        for i in range(len(num)):
            # 如果元素被访问过，则跳过 (剪枝)
            if num[i] in used.get(level, []):
                continue
            perm.append(num[i])
            # 记录当前层级访问过的元素
            used[level] = used.get(level, []) + [num[i]]
            helper(num[: i] + num[i + 1:], perm, used, level + 1)
            perm.pop()
        # 删除当前层级的访问的元素
        used.pop(level)

    helper(nums, [], {}, 1)
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
    inputs = [1, 1, 2]
    outputs = removal(permute_unique(inputs))
    answer = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert len(outputs) == len(answer), print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    for output in outputs:
        assert output in answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs = [2, 2, 1, 1]
    outputs = removal(permute_unique(inputs))
    answer = [[2, 2, 1, 1], [2, 1, 2, 1], [2, 1, 1, 2], [1, 2, 2, 1], [1, 2, 1, 2], [1, 1, 2, 2]]
    assert len(outputs) == len(answer), print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    for output in outputs:
        assert output in answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
