# -*- encoding: utf-8 -*-
"""
@file: longestCommonSubsequence.py
@time: 2020/9/30 下午2:49
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  1143.最长公共子序列

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
若这两个字符串没有公共子序列，则返回 0。

示例 1:
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。

示例 2:
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。

示例 3:
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。

提示:
1 <= text1.length <= 1000
1 <= text2.length <= 1000
输入的字符串只含有小写英文字符

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
"""


def longest_common_sub_sequence(text1, text2):
    """
    动态规划。时间复杂度 O(m * n), 空间复杂度 O(m * n)
    DP 方程：dp[i][j]
    dp[i][j]  ==> 从 text1[i] 到 text2[j] 两个字符的最长公共子序列

    if text1[i] == text2[j]:
        dp[i][j] = dp[i-1][j-1] + 1
    else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 删除 text1[i] 或 删除 text2[j]

    状态转移。text1 = "abcde"， text2 = "ace"
            #   a   b   c   d   e
        #   0   0   0   0   0   0
        a   0   1   1   1   1   1
        c   0   1   1   2   2   2
        e   0   1   1   2   2   3

    :param text1: (str)
    :param text2: (str)
    :return: (int)
    """
    m, n = len(text1), len(text2)
    state = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                state[i][j] = state[i - 1][j - 1] + 1
            else:
                state[i][j] = max(state[i][j - 1], state[i - 1][j])
    return state[-1][-1]


def test(text1, text2, answer):
    outputs = longest_common_sub_sequence(text1, text2)
    print("Inputs:text1={}, text2={}, Outputs:{}, Except:{}".format(text1, text2, outputs, answer))


def main():
    test("abcde", "ace", 3)
    test("abc", "abc", 3)
    test("abc", "def", 0)


if __name__ == '__main__':
    main()
