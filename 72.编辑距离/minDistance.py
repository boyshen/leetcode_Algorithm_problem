# -*- encoding: utf-8 -*-
"""
@file: minDistance.py
@time: 2020/10/31 下午7:38
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  72.编辑距离

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
"""


def min_distance(word1, word2):
    """
    DP, 时间复杂度 O(m * n), 空间复杂度((m+1) * (n*1)) . m 和 n 分别为word1和word2的单词长度

    DP 方程： dp[m+1][n+1].
        其中 dp[i-1][j-1] 表示word1和word2都插入／删除／替换一个字符
            dp[i-1][j]   表示word1插入／替换／删除一个字符，word2不操作
            dp[i][j-1]   表示word2插入／替换／删除一个字符，word1不操作

        dp[i][j] = dp[i-1][j-1]                                   ==> if word1[i] == word2[j]
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1  ==> if word1[i] != word2[j]

    DP 转移表。 '#' 代表空格的情况下， 当 word == '' 时候的编辑距离
            #   r   o   s
        #   0   1   2   3
        h   1   1   2   3
        o   2   2   1   2
        r   3   2   2   2
        s   4   3   3   2
        e   5   4   4   3

    :param word1: (str)
    :param word2: (str)
    :return: (int)
    """

    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化 '#' 的情况
    for i in range(1, m + 1):
        dp[i][0] = i

    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[-1][-1]


def test(word1, word2, answer):
    outputs = min_distance(word1, word2)
    print("Inputs:word1={}, word2={}, Outputs:{}, Except:{}".format(word1, word2, outputs, answer))


def main():
    test("horse", "ros", 3)
    test("intention", "execution", 5)


if __name__ == '__main__':
    main()
