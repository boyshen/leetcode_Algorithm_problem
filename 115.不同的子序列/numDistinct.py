# -*- encoding: utf-8 -*-
"""
@file: numDistinct.py
@time: 2020/11/13 下午5:04
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 115.不同的子序列

给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
题目数据保证答案符合 32 位带符号整数范围。

示例 1：
输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

示例 2：
输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
(上箭头符号 ^ 表示选取的字母)
babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

提示：
0 <= s.length, t.length <= 1000
s 和 t 由英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences
"""
import unittest


def num_distinct(s, t):
    """
    DP. 时间复杂度 O(s*t), 空间复杂度 O(s*t). s 和 t 分别表示字符串s和t的长度。

    DP 方程。dp[i][j] ==> 表示字符串 t 从开始到 i 与字符串 s 从开始到 j 的序列匹配个数
    if s[i-1] == t[j-1]:
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    else:
        dp[i][j] = dp[i][j-1]

    初始化：
        dp = [[0] * (s+1) for _ in range(t+1)]
        dp[0] = [1] * [s+1]

    dp 转移表。 # 表示空字符。 # 与 # 匹配则为 1。
        #   r   a   b   b   b   i   t
    #   1   1   1   1   1   1   1   1   ==> dp[i][j] = dp[i][j-1] .dp[0][0] 等于1，则后面的也等于 1
    r   0   1   1   1   1   1   1   1
    a   0   0   1   1   1   1   1   1
    b   0   0   0   1   2   3   3   3
    b   0   0   0   0   1   3   3   3
    i   0   0   0   0   0   0   3   3
    t   0   0   0   0   0   0   0   3

    :param s: (str)
    :param t: (str)
    :return: (int)
    """

    s_size = len(s)
    t_size = len(t)
    dp = [[0] * (s_size + 1) for _ in range(t_size + 1)]
    dp[0] = [1] * (s_size + 1)

    for i in range(1, t_size + 1):
        for j in range(1, s_size + 1):
            if s[j - 1] == t[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]

    return dp[-1][-1]


def work(s, t, answer):
    outputs = num_distinct(s, t)
    print("Inputs:s={}, t={}, Outputs:{}, Except:{}".format(s, t, outputs, answer))
    return outputs


class TestNumDistinct(unittest.TestCase):
    def test_num_distinct(self):
        s, t = "rabbbit", "rabbit"
        answer = 3
        self.assertEqual(work(s, t, answer), answer)

        s, t = "babgbag", "bag"
        answer = 5
        self.assertEqual(work(s, t, answer), answer)


if __name__ == '__main__':
    unittest.main()
