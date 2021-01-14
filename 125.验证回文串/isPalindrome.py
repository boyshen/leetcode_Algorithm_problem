# -*- encoding: utf-8 -*-
"""
@file: isPalindrome.py
@time: 2020/11/18 上午11:02
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 125.验证回文串

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
"""
import unittest


def is_palindrome1(s):
    """
    双指针。 时间复杂度 O(s), 空间复杂度 O(1)
    :param s: (str)
    :return: (bool)
    """
    s_len = len(s)
    if s_len == 0:
        return True

    left, right = 0, s_len - 1
    while left < right:
        if s[left] == ' ' or (not s[left].isalpha() and not s[left].isdigit()):
            left += 1
            continue
        if s[right] == ' ' or (not s[right].isalpha() and not s[right].isdigit()):
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


def is_palindrome(s):
    """
    筛选 + 正反字符串对比。时间复杂度 O(n), 空间复杂度 O(n)
    筛选：提取出数字、字母
    对比：正序和逆序对比。如果相等则是回文串，如果不相等则不是。
    :param s: (str)
    :return: (bool)
    """

    res = []
    for char in s:
        if char.isalpha():
            res.append(char.lower())
        elif char.isalnum():
            res.append(char)
    return res[::1] == res[::-1]


def work(s, answer):
    outputs = is_palindrome(s)
    print("Inputs:{}, Outputs:{}, Except:{}".format(s, outputs, answer))
    return outputs


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        s = "A man, a plan, a canal: Panama"
        answer = True
        self.assertTrue(work(s, answer))

        s = "race a car"
        answer = False
        self.assertFalse(work(s, answer))

        s = "rac 123321 car"
        answer = True
        self.assertTrue(work(s, answer))

        s = "rac 1235321 car"
        answer = True
        self.assertTrue(work(s, answer))


if __name__ == '__main__':
    unittest.main()
    # s = "race a car"
    # is_palindrome(s)
