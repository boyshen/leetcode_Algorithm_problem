# -*- encoding: utf-8 -*-
"""
@file: reverseWord.py
@time: 2020/11/5 下午5:01
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  151.翻转字符串里的单词

给定一个字符串，逐个翻转字符串中的每个单词。

说明：
无空格字符构成一个 单词 。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

示例 1：
输入："the sky is blue"
输出："blue is sky the"

示例 2：
输入："  hello world!  "
输出："world! hello"
解释：输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
输入："a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

示例 4：
输入：s = "  Bob    Loves  Alice   "
输出："Alice Loves Bob"

示例 5：
输入：s = "Alice does not even like bob"
输出："bob like even not does Alice" 

提示：
1 <= s.length <= 104
s 包含英文大小写字母、数字和空格 ' '
s 中 至少存在一个 单词

进阶：
请尝试使用 O(1) 额外空间复杂度的原地解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
"""
import unittest


def reverse_words(s):
    """
    暴力法。时间复杂度 O(N), 空间复杂度 O(N). N 为字符串中单词加空格的数量。
    :param s: (str)
    :return: (str)
    """
    words_list = s.split()
    # words_list = list(filter(None, words_list))
    i, j = 0, len(words_list) - 1
    while i < j:
        words_list[i], words_list[j] = words_list[j], words_list[i]
        i += 1
        j -= 1
    return ' '.join(words_list)


def work(s, answer):
    outputs = reverse_words(s)
    print("Inputs:{}, Outputs:{}, Except:{}".format(s, outputs, answer))
    return outputs


class TestReverseWords(unittest.TestCase):
    def test_reverse_words(self):
        s = "the sky is blue"
        answer = "blue is sky the"
        self.assertEqual(work(s, answer), answer)

        s = "  hello world!  "
        answer = "world! hello"
        self.assertEqual(work(s, answer), answer)

        s = "a good   example"
        answer = "example good a"
        self.assertEqual(work(s, answer), answer)

        s = "  Bob    Loves  Alice   "
        answer = "Alice Loves Bob"
        self.assertEqual(work(s, answer), answer)

        s = "Alice does not even like bob"
        answer = "bob like even not does Alice"
        self.assertEqual(work(s, answer), answer)


if __name__ == '__main__':
    unittest.main()
