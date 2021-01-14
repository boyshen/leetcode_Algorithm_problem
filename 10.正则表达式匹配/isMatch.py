# -*- encoding: utf-8 -*-
"""
@file: isMatch.py
@time: 2020/11/11 下午6:42
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  10.10.正则表达式匹配

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
 
示例 1：
输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

示例 2:
输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3：
输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4：
输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5：
输入：s = "mississippi" p = "mis*is*p*."
输出：false
 

提示：
0 <= s.length <= 20
0 <= p.length <= 30
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
保证每次出现字符 * 时，前面都匹配到有效的字符

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
"""
import unittest


def is_match1(s, p):
    """
    递归。 时间复杂度 O((S + P) * 2^(S+P/2)), 空间复杂度 O((S + P) * 2^(S+P/2))

    递归终结条件：如果 p 等于空，则判断 s 是否等于空。s 等于空返回 True，否则返回 False
    递归处理：
        1. 判断当前字符s与表达式p的第一个字符是否相等。
            即： s[0] in [p[0] or '.'].  ==> '.' 表示任意字符。
            state = p[0] in [s[0] or '.']

        2. 如果表示式的第二个字符是 "*" 。这里第二个字符'*' 是因为根据条件 '*' 前面必须有一个字符。
            if len(p) >= 2 and p[1] == '*':
                如果是 '*' 则有两种处理结果。
                a. 不匹配(匹配 0 次)，则跳过 p[j+1] 进入下一层判断。 is_match(s, p[2:]).
                b. 匹配 1 次或多次。前提在 state 为 True 的情况。
                即 '*' 的前一个字符与s[0] 相匹配条件下, 进行下一层 is_match(s[1:], p)
            else：
                返回 state and is_match(s[1:], p[1:])

    :param s: (str)
    :param p: (str)
    :return: (bool)
    """
    if not p:
        return not s

    state = bool(s) and p[0] in {s[0], '.'}
    if len(p) >= 2 and p[1] == '*':
        return is_match(s, p[2:]) or (state and is_match(s[1:], p))
    else:
        return state and is_match(s[1:], p[1:])


def is_match(s, p):
    """
    递归 + 记忆化。 在递归的基础上添加记忆化搜索。
    时间复杂度 O(S * P). 空间复杂度 O(S * P) S 和 P 分别为字符串s和p的长度
    :param s: (str)
    :param p: (str)
    :return: (bool)
    """
    s_size = len(s)
    p_size = len(p)
    memory = {}

    def dfs(i, j):
        if (i, j) in memory:
            return memory[(i, j)]
        if j >= p_size:
            return i == s_size

        state = True if (i < s_size and p[j] in {s[i], '.'}) else False
        if j <= p_size - 2 and p[j + 1] == '*':
            temp = dfs(i, j + 2) or (state and dfs(i + 1, j))
        else:
            temp = (state and dfs(i + 1, j + 1))

        memory[(i, j)] = temp
        return temp

    return dfs(0, 0)


def work(s, p, answer):
    outputs = is_match(s, p)
    print("Inputs:s={},p={}, Outputs:{}, Except:{}".format(s, p, outputs, answer))
    return outputs


class TestIsMatch(unittest.TestCase):
    def test_is_match(self):
        s, p = "aa", "a"
        self.assertFalse(work(s, p, False))

        s, p = "ab", "a*"
        self.assertFalse(work(s, p, False))

        s, p = "ab", ".*"
        self.assertTrue(work(s, p, True))

        s, p = "abcdefg", ".*"
        self.assertTrue(work(s, p, True))

        s, p = "aab", "c*a*b"
        self.assertTrue(work(s, p, True))

        s, p = "mississippi", "mis*is*p*."
        self.assertFalse(work(s, p, False))


if __name__ == '__main__':
    unittest.main()
