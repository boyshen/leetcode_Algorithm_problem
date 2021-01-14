# -*- encoding: utf-8 -*-
"""
@file: longestValidParentheses.py
@time: 2020/11/4 下午3:42
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  32. 最长有效括号

给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses/
"""
import unittest


def longest_valid_parentheses1(s):
    """
    DP . 时间复杂度 O(N),  空间复杂度 O(N)
    DP 方程。 dp[i] ==> 第 s[i] 个字符的括号长度。

    # 如果 s[i] == ')', 且 s[i-1] == '(' 时候，说明找到一对，则在前一对括号长度上 + 2
    if s[i] == ')' and s[i-1] == '(': dp[i] = dp[i - 2] + 2

    # 如果 s[i] == ')', 当s[i-1] = ')' 时，则需要跳过 i-1 找与之配对的 '(' 。
    # 例如 '(())' 中。计算 s[3] = ')' 时候，则需要判断 s[0] == '('
        0   1   2   3
        (   (   )   )
    if s[i] == ')' and s[i - dp[i-1] - 1] == '(': dp[i] = dp[i-1] + dp[i - dp[i-1] -2] + 2

    DP 转移表
            (   )   )   (   (   )   )
    dp[i]   0   2   0   0   0   2   4

    :param s: (str)
    :return: (int)
    """
    length = len(s)
    if length == 0:
        return 0

    dp = [0] * length
    for i in range(1, length):
        if s[i] == ')' and s[i - 1] == '(':
            dp[i] = dp[i - 2] + 2
        elif s[i] == ')' and (i - dp[i - 1] - 1) >= 0 and s[i - dp[i - 1] - 1] == '(':
            dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
    return max(dp)


def longest_valid_parentheses2(s):
    """
    栈实现。 时间复杂度 O(N), 空间复杂度 O(N).

    设计思想：
        1. 维护一个 stack 栈，使用left 保存无法配对的字符索引，res 保存最大值。
        2. 遍历 s 。
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        # 例如：(()) 情况。当i = 2时候。索引 1 出栈。 当前 i - stack[-1] = 2.
                        res = max(res, i - stack[-1])
                    else:
                        # 如果当前出栈之后，栈元素为空，则说明当前配对的前存在一个无法配对的元素。
                        # 例如 "())()" 。 left 保存了 2 索引。 i = 4 时候。 当前长度 i - left = 2
                        res = max(res, i - left)
                else:
                    # 如果 stack 为空，则说明没有与之找到配对的 '('。 保存。
                    # 例如：')()'
                    left = i
        3. 返回 res
    :param s: (str)
    :return: (int)
    """
    stack = []
    left, res = -1, 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    res = max(res, i - left)
            else:
                left = i
    return res


def longest_valid_parentheses(s):
    """
    栈。 时间复杂度 O(N), 空间复杂度 O(N).
    参考：https://leetcode.com/problems/longest-valid-parentheses/discuss/14167/Simple-JAVA-solution-O(n)-time-one-stack

    设计思想：
        1. 维护一个 stack 栈。res 保存最大值。
        2. 遍历 s 。
            # 当找到一对括号的时候就出栈
            if s[i] == ')' and len(stack) > 0 and s[stack[-1]] == '('
                stack.pop()
                res = max(res, i - stack[-1])
            else:
                stack.append(i)
        3. 返回 res
    :param s: (str)
    :return: (int)
    """
    # 添加一个元素。因为 len(stack) > 1 .即需要 stack 中两个数据，但是每次只出栈一个，所以添加一个数据做铺垫
    # 例如出现 (()) 情况时候，需要依次出栈 0，1 索引。
    stack = [-1]
    res = 0
    for i, char in enumerate(s):
        if char == ')' and len(stack) > 1 and s[stack[-1]] == '(':
            stack.pop()
            res = max(res, i - stack[-1])
        else:
            stack.append(i)
    return res


def work(s, answer):
    outputs = longest_valid_parentheses(s)
    print("Inputs:{}, Outputs:{}, Except:{}".format(s, outputs, answer))
    return outputs


class Test(unittest.TestCase):
    def test_longest_valid_parentheses(self):
        self.assertEqual(work("(()", 2), 2)
        self.assertEqual(work(")()())", 4), 4)
        self.assertEqual(work("())(())", 4), 4)
        self.assertEqual(work("", 0), 0)
        self.assertEqual(work("(()))())(", 4), 4)


if __name__ == '__main__':
    unittest.main()
