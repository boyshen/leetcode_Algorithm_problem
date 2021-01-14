# -*- encoding: utf-8 -*-
"""
@file: reverseString.py
@time: 2020/11/5 下午4:09
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 344.反转字符串

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

示例 2：
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
"""
import unittest


def reverse_string1(s):
    """
    双指针进行首尾交换。 时间复杂 O(N), 空间复杂度 O(1)

    输入：["h","e","l","l","o"]
    i = 0, j = 4, ["o","e","l","l","h"]
    i = 1, j = 3, ["o","l","l","e","h"]
    i = 2, j = 2. break

    输入： ["H","a","n","n","a","h"]
    i = 0, j = 5, ["h","a","n","n","a","H"]
    i = 1, j = 4, ["h","a","n","n","a","h"]
    i = 2, j = 3, ["h","a","n","n","a","h"]
    i = 3, j = 2, break

    :param s: (list[str])
    :return: (list[str])
    """
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


def reverse_string(s):
    """
    python 库函数。
    s[::-1] 表示反转列表元素
    :param s: (list[str])
    :return:  (list[str])
    """
    s[:] = s[::-1]


def work(s, answer):
    print("Inputs: {}, ".format(s), end='')
    reverse_string(s)
    print("Outputs: {}, Except:{}".format(s, answer))


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        s = ["h", "e", "l", "l", "o"]
        answer = ["o", "l", "l", "e", "h"]
        work(s, answer)
        self.assertEqual(s, answer)

        s = ["H", "a", "n", "n", "a", "h"]
        answer = ["h", "a", "n", "n", "a", "H"]
        work(s, answer)
        self.assertEqual(s, answer)


if __name__ == '__main__':
    unittest.main()
