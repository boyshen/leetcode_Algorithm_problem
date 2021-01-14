# -*- encoding: utf-8 -*-
"""
@file: numDecodings.py
@time: 2020/10/11 下午10:22
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  91.解码方法

一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。
题目数据保证答案肯定是一个 32 位的整数。

示例 1：
输入："12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2：
输入："226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

示例 3：
输入：s = "0"
输出：0

示例 4：
输入：s = "1"
输出：1

示例 5：
输入：s = "2"
输出：1
 
提示：
1 <= s.length <= 100
s 只包含数字，并且可以包含前导零。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
"""


def num_decoding_s(s):
    """
    DP. 时间复杂度 O(N), 空间复杂度 O(N+1)
    DP 方程。 dp[i]  ==> 从nums[0] 到 nums[i] 的解码数量

    初始化： dp = [0] * (len(s) + 1)
            dp[0] = 1
            dp[1] = 0 if s[0] == '0' else 1
    计算：
        if 10 <= int(s[i-2] + s[i-1]) <= 26: dp[i] = dp[i-2] + dp[i]
        if 1 <= int(s[i-1] <= 9): dp[i] = dp[i-1] + dp[i]

    递推：输入"1201234"
        1   2   0   1   2   3   4
    i = 0   1   2   3   4   5   6   7
    dp= 1   1   2   1   1   2   3   3

    :param s: (list[int])
    :return: (int)
    """
    n = len(s)
    if n == 0 or s == ' ':
        return 0

    state = [0] * (n + 1)
    state[0] = 1
    state[1] = 1 if s[0] != '0' else 0

    for i in range(2, n + 1):
        first = int(s[i - 1])
        second = int(s[i - 2] + s[i - 1])

        if 1 <= first <= 9:
            state[i] += state[i - 1]
        if 10 <= second <= 26:
            state[i] += state[i - 2]
    return state[-1]


def test(s, answer):
    outputs = num_decoding_s(s)
    print("Inputs:{}, Outputs:{}, Except:{}".format(s, outputs, answer))
    assert outputs == answer, "Answer Failed"


def main():
    test("12", 2)
    test("226", 3)
    test("0", 0)
    test("1", 1)
    test("10", 1)
    test("1201234", 3)


if __name__ == '__main__':
    main()
