# -*- encoding: utf-8 -*-
"""
@file: generateParenthesis.py
@time: 2020/9/7 下午5:36
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 22.括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
"""


def generate_parenthesis(n):
    """
    回溯。时间复杂度 O(2^2n / sqrt(n))。 空间复杂度为 O(n)
    :param n: (int)
    :return: (list)
    """
    res = []

    def _generator(left, right, max, parenthesis):
        if left == max and right == max:
            res.append(parenthesis)
            return

        if left < max:
            _generator(left + 1, right, max, parenthesis + '(')
        # 只有当有左括号存在的时候才能执行
        if left > right:
            _generator(left, right + 1, max, parenthesis + ')')

    _generator(0, 0, n, '')
    return res


def main():
    inputs = 3
    outputs = generate_parenthesis(inputs)
    print(outputs)
    answer = ['((()))', '(()())', '(())()', '()(())', '()()()']
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
