# -*- encoding: utf-8 -*-
"""
@file: validPalindrome.py
@time: 2020/11/18 下午2:24
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 680. 验证回文字符串 Ⅱ

给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:
输入: "aba"
输出: True

示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。

注意:
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-ii
"""
import unittest


def valid_palindrome1(s):
    """
    贪心算法。 时间复杂度为 O(n), 空间复杂度为O(1)
    1. 枚举左右指针。如果左右字符相等，则进入下一个。如果不相等，则进行删除左字符或右字符。
    :param s: (str)
    :return: (bool)
    """

    def check_palindrome(low, height):
        i, j = low, height
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return check_palindrome(left + 1, right) or check_palindrome(left, right - 1)
    return True


def valid_palindrome(s):
    def valid(low, height):
        while low < height:
            if s[low] != s[height]:
                return False
            low += 1
            height -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return valid(left + 1, right) or valid(left, right - 1)
    


def work(s, answer):
    outputs = valid_palindrome(s)
    print("Inputs:{}, Outputs:{}, Except:{}".format(s, answer, outputs))
    return outputs


class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        s, answer = "aba", True
        self.assertTrue(work(s, answer))

        s, answer = "abca", True
        self.assertTrue(work(s, answer))

        s, answer = "abcaadba", False
        self.assertFalse(work(s, answer))


if __name__ == '__main__':
    unittest.main()
