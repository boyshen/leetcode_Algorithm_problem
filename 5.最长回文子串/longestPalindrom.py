# -*- encoding: utf-8 -*-
"""
@file: longestPalindrom.py
@time: 2020/11/6 下午5:42
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 5.最长回文子串

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
对于一个子串而言，如果它是回文串，并且长度大于 2，那么将它首尾的两个字母去除之后，它仍然是个回文串。
例如对于字符串 ababa，去掉首尾的 a 之后，剩下的 'bab' 仍然是回文串。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "aacabdkacaa"
输出: "aca"
注意: "aacabdkacaa" 不是回文串，去掉首尾的 "acaa" 之后，剩下的 bdk 不是回文串

示例 3：
输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
"""
import unittest


def longest_palindromic_substring1(s):
    """
    中心扩散法, 选择一个中心点，由中心点向 left 和 right 两个方向进行扩散。
    当扩散点满足 s[left] == s[right] 时候则找到一个回文串。

    中心点的选择需要考虑奇数和偶数，
    例如: bab 情况下，中心点是 a 开始,
         cbbd 情况下，中心点在 bb 中间, 同时 bb 也属于回文串，为了防止遗漏，则从两个字符的中间开始

    时间复杂度 O(N^2), 空间复杂度 O(1)
    :param s: (str)
    :return: (str)
    """

    def search_palindromic_substring(l, r):
        # 由中心向两边进行扩散。找出回文字串
        while l >= 0 and r < length and s[l] == s[r]:
            l -= 1
            r += 1
        # l - 1  和 r - 1 表示在 while 循环中，l -= 1 和 r += 1 进入到下一个查询，
        # 如果下一个不满足条件，退出循环，并恢复为找到回文子串索引
        return l + 1, r - 1

    length = len(s)
    if length < 2:
        return s

    start, end = 0, 0
    for i in range(length):
        # 奇数情况
        left1, right1 = search_palindromic_substring(i, i)
        # 偶数情况
        left2, right2 = search_palindromic_substring(i, i + 1)

        # 对比找到的子串大小。保留最大的子串
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    return s[start:end + 1]


def longest_palindromic_substring(s):
    """
    DP. 时间复杂度 O(N^2), 空间复杂度 O(N)
    DP 方程。 dp[i][j]  ==> bool 类型。 dp(i,j) 表示字符串 s 的第 i 到 j 个字母组成的串。如果是回文串则表示 True，否则为 False

    # i 和 j 可以看作是从左和从右进行检索的结果。
    # dp[i+1][j-1] 即上一个比较是不是回文串。
    # j - i < 2 则说明目前只有一个字符，单个字符也是回文串。
    if s[i] == s[j] and (dp[i+1][j-1] == True or j - i < 2):
        dp[i][j] = True
    else:
        dp[i][j] = False

    动态转移表，输入："babad" 由下往上递推（由下往上递推可以减少条件判断），i = 4, j = i
                    b   a   b   a   d
                j = 0   1   2   3   4
       i = 0   b    T   F   T   F   F
           1   a        T   F   T   F
           2   b            T   F   F
           3   a                T   F
           4   d                    T

    :param s: (str)
    :return: (str)
    """
    length = len(s)
    if length < 2:
        return s

    res = ""
    dp = [[False] * length for _ in range(length)]

    for i in range(length - 1, -1, -1):
        for j in range(i, length):
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1] is True):
                dp[i][j] = True

            if dp[i][j] is True and (j - i + 1 > len(res)):
                res = s[i:j + 1]
    return res


def work(s, answer):
    outputs = longest_palindromic_substring(s)
    print("Inputs:{}, Outputs:{}, Except:{}".format(s, outputs, answer))
    return outputs


class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_longest_palindromic_substring(self):
        s = "babad"
        answer = ["bab", "aba"]
        self.assertIn(work(s, answer), answer)

        s = "cbbd"
        answer = "bb"
        self.assertEqual(work(s, answer), answer)

        s = "aaaaaa"
        answer = "aaaaaa"
        self.assertEqual(work(s, answer), answer)


if __name__ == '__main__':
    unittest.main()
