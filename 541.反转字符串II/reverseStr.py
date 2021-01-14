# -*- encoding: utf-8 -*-
"""
@file: reverseStr.py
@time: 2020/11/1 下午10:12
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 541.反转字符串 II

给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:
输入: s = "abcdefg", k = 2
输出: "bacdfeg"

提示：
该字符串只包含小写英文字母。
给定字符串的长度和 k 在 [1, 10000] 范围内。
"""


def reverse_str1(s, k):
    """
    暴力法。
    :param s: (str)
    :param k: (int)
    :return: (str)
    """
    res = list(s)
    for i in range(0, len(s), 2 * k):
        res[i:i + k] = reversed(res[i:i + k])
    return ''.join(res)


def reverse_str(s, k):
    """
    暴力法。替换切片操作
    :param s: (str)
    :param k: (int)
    :return: (int)
    """
    s_list = list(s)
    for i in range(0, len(s), 2 * k):
        # right = min(i+k-1, tail_index)。 当 i+k-1 > len(s) -1 时候，则选择到字符的最后.
        # 符合剩余字符少于 k 个，则将剩余字符全部反转
        left, right = i, min(i + k - 1, len(s) - 1)
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    return ''.join(s_list)


def test(s, k, answer):
    outputs = reverse_str(s, k)
    print("Inputs:s={},k={}, Outputs:{}, Except:{}".format(s, k, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test("abcdefg", 5, "edcbafg")
    test("abcdefg", 2, "bacdfeg")
    test("abcdefg", 1, "abcdefg")


if __name__ == '__main__':
    main()
