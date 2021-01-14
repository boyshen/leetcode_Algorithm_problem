# -*- encoding: utf-8 -*-
"""
@file: isMatch.py
@time: 2020/11/12 下午5:43
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 44.通配符匹配

给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。

示例 3:
输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

示例 4:
输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

示例 5:
输入:
s = "acdcb"
p = "a*c?b"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
"""
import unittest


def is_match(s, p):
    """
    DP. 时间复杂度 O(mn), 空间复杂度 O(mn). m 为 s 字符串的长度，n 为 p 字符串的长度
    DP 方程。dp[i][j] ==> 表示字符串s从开始到 i 位置与字符串p从开始到 j 的位置是否匹配。

    # 当 s[i] 与 p[j] 相等或 p[j] == '?' 时
    if s[i] == p[j] or p[j] == '?'
        dp[i][j] = dp[i-1][j-1]
    elif p[j] == '*':
        # dp[i-1][j] 表示当 p[j] == '*' 时，可以匹配一个或多个
        # dp[i][j-1] 表示当 p[j] == '*' 时，可以匹配零个
        dp[i][j] = dp[i-1][j] or dp[i][j-1]
    else
        # 其他情况为 False

    初始化： m + 1 和 n + 1 是在考虑空字符的情况下
        dp = [[False] * n+1 for _ in range(m+1)]
        dp[0][0] = True

        # 特殊情况处理，如果 p 是以若干个 '*' 开头。'*' 是可以匹配空格的将多个 '*'匹配成空格
        for i in range(1, n):
            if p[i-1] == '*'
                dp[0][i] = True
            else:
                break

    DP 动态转移表
        #   *   a   *   b
    #   T   T   F   F   F
    a   F   T   T   T   F
    d   F   T   F   T   F
    c   F   T   F   T   F
    e   F   T   F   T   F
    b   F   T   F   T   T

    :param s: (str)
    :param p: (str)
    :return: (bool)
    """

    p_size = len(p)
    s_size = len(s)

    dp = [[False] * (p_size + 1) for _ in range(s_size + 1)]
    dp[0][0] = True
    for i in range(1, p_size + 1):
        if p[i - 1] != '*':
            break
        dp[0][i] = True

    for i in range(1, s_size + 1):
        for j in range(1, p_size + 1):
            if p[j - 1] in {s[i - 1], '?'}:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[-1][-1]


def work(s, p, answer):
    outputs = is_match(s, p)
    print("Inputs:s={}, p={}, Outputs:{}, Except:{}".format(s, p, outputs, answer))
    return outputs


class TestIsMatch(unittest.TestCase):
    def test_is_match(self):
        s, p = "aa", "a"
        self.assertFalse(work(s, p, False))

        s, p = "aa", "*"
        self.assertTrue(work(s, p, True))

        s, p = "cb", "?a"
        self.assertFalse(work(s, p, False))

        s, p = "adceb", "*a*b"
        self.assertTrue(work(s, p, True))

        s, p = "acdcb", "a*c?b"
        self.assertFalse(work(s, p, False))


if __name__ == '__main__':
    unittest.main()
