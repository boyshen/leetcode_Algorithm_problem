# -*- encoding: utf-8 -*-
"""
@file: reverseOnlyLetters.py
@time: 2020/11/6 下午2:17
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  917.仅仅反转字母

给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：
输入："ab-cd"
输出："dc-ba"

示例 2：
输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

示例 3：
输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
 

提示：
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S 中不包含 \ or "

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-only-letters
"""
import unittest


def reverse_only_letters1(s):
    """
    双指针。时间复杂度 O(N), 空间复杂度 O(N)
    :param s: (str)
    :return: (str)
    """

    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z':
            if 'A' <= s[j] <= 'Z' or 'a' <= s[j] <= 'z':
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            i += 1

    return ''.join(s)


def reverse_only_letters(s):
    """
    字母栈，利用 stack 先入后出的思想进行反转。 时间复杂度 O(N), 空间复杂度 O(N
    设计：
        1. 维护一个栈 stack. 将 s 中的字母依次加人到 stack 中
        2. 创建 res 空字符， 遍历 s。
            如果 s[i] 是字母，则从stack中取出字符加入到 res 中
            否则就添加 s[i] 字符
        3. 返回

    输入：s = 'ab-cd'
    stack = ['a', 'b', 'c', 'd']
    遍历 s：
    s = 'd'
    s = 'dc'
    s = 'dc-'
    s = 'dc-b'
    s = 'dc-ba'

    :param s: (str)
    :return: (str)
    """

    stack = [char for char in s if char.isalpha()]
    res = []
    for char in s:
        if char.isalpha():
            res.append(stack.pop())
        else:
            res.append(char)
    return ''.join(res)


def work(s, answer):
    outputs = reverse_only_letters(s)
    print("Inputs:{}, Outputs:{}, Except:{}".format(s, outputs, answer))
    return outputs


class TestReverseOnlyLetters(unittest.TestCase):
    def test_reverse_only_letters(self):
        s = "ab-cd"
        answer = "dc-ba"
        self.assertEqual(work(s, answer), answer)

        s = "a-bC-dEf-ghIj"
        answer = "j-Ih-gfE-dCba"
        self.assertEqual(work(s, answer), answer)

        s = "Test1ng-Leet=code-Q!"
        answer = "Qedo1ct-eeLg=ntse-T!"
        self.assertEqual(work(s, answer), answer)


if __name__ == '__main__':
    unittest.main()
