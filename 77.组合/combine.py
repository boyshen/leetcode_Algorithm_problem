# -*- encoding: utf-8 -*-
"""
@file: combine.py
@time: 2020/9/11 下午2:12
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 77.组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
"""


def combine(n, k):
    """
    递归。时间复杂度 O((n,k) * k), 空间复杂度 O(n + k)
    :param n: (int)
    :param k: (int)
    :return:
    """
    res = []

    def helper(idx, comb):
        if len(comb) == k:
            # 拷贝保存
            res.append(comb.copy())
            return
        for i in range(idx, n + 1):
            comb.append(i)
            helper(i + 1, comb)
            # 移除最后一个元素
            comb.pop()

    helper(1, [])
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
    n, k = 4, 2
    outputs = removal(combine(n, k))
    answer = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert len(outputs) == len(answer), print("Inputs:{}/{}, Outputs:{}, Except:{}".format(n, k, outputs, answer))
    for output in outputs:
        assert output in answer, print("Inputs:{}/{}, Outputs:{}, Except:{}".format(n, k, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
