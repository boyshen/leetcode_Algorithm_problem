# -*- encoding: utf-8 -*-
"""
@file: longestCommonPrefix.py
@time: 2020/11/1 下午9:30
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  14.最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
"""


def longest_common_prefix(strs):
    """
    纵向扫描。时间复杂度：O(mn)，其中 m 是字符串数组中的字符串的平均长度，n 是字符串的数量。空间复杂度 O(1)
    :param strs: (list[str])
    :return: (str)
    """
    if not strs:
        return ""

    length, count = len(strs[0]), len(strs)
    for i in range(length):
        char = strs[0][i]
        if not all((True if i < len(strs[j]) and char == strs[j][i] else False for j in range(1, count))):
            return strs[0][:i]
    return strs[0]


def test(strs, answer):
    outputs = longest_common_prefix(strs)
    print("Inputs:{}, Outputs:{}, Except:{}".format(strs, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test(["flower", "flow", "flight"], 'fl')
    test(["dog", "racecar", "car"], '')


if __name__ == '__main__':
    main()
