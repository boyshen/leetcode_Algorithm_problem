# -*- encoding: utf-8 -*-
"""
@file: reverseWords.py
@time: 2020/11/5 下午6:20
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  557.反转字符串中的单词 III

给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：
输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

提示：
在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
"""
import unittest


def reverse_words1(s):
    """
    暴力法。时间复杂度 O(N), 空间复杂度为 O(N)
    :param s: (str)
    :return: (str)
    """

    words_list = s.split()
    for i, word in enumerate(words_list):
        words_list[i] = word[::-1]
    return ' '.join(words_list)


def reverse_words2(s):
    """
    暴力法。 时间复杂度 O(N), 空间复杂度为 O(N)
    先对字符串 s 进行反转，然后再 split，最后再反转, 最后 join
    例如：s = "Let's take LeetCode contest"

    1. 反转: s[::-1] = "tsetnoc edoCteeL ekat s'teL"
    2. split: s[::-1].split() = ['tsetnoc', 'edoCteeL', 'ekat', "s'teL"]
    3. 再反转：s[::-1].split()[::-1] = ["s'teL", 'ekat', 'edoCteeL', 'tsetnoc']
    4。 最后 join：' '.join(s[::-1].split()[::-1]) = "s'teL ekat edoCteeL tsetnoc"

    :param s: (str)
    :return: (str)
    """
    return ' '.join(s[::-1].split()[::-1])


def reverse_words(s):
    """
    双指针。 时间复杂度 O(N), 空间复杂度 O(N)
    python 中字符串不可变，所以需要进行切片。
    :param s: (str)
    :return: (str)
    """
    s = list(s)
    left, right = 0, 0
    while right < len(s):
        while right < len(s) and s[right] != ' ':
            right += 1
        swap(s, left, right - 1)
        left = right + 1
        right = right + 1
    return ''.join(s)


def swap(s, left, right):
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def work(s, answer):
    outputs = reverse_words(s)
    print("Inputs:{}, Outputs:{}, Except:{}".format(s, outputs, answer))
    return outputs


class TestReverseWords(unittest.TestCase):
    def test_reverse_words(self):
        s = "Let's take LeetCode contest"
        answer = "s'teL ekat edoCteeL tsetnoc"
        self.assertEqual(work(s, answer), answer)

    def test_swap(self):
        s = list("hello world leetcode")
        answer = list("hello dlrow leetcode")
        swap(s, 6, 10)
        self.assertEqual(s, answer)


if __name__ == '__main__':
    unittest.main()
