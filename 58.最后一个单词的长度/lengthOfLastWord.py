# -*- encoding: utf-8 -*-
"""
@file: lengthOfLastWord.py
@time: 2020/11/1 下午4:40
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 58.最后一个单词的长度

给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

示例:
输入: "Hello World"
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-last-word/
"""


def length_of_last_word1(s):
    """
    :param s: (str)
    :return: (int)
    """
    s = s.strip()
    if len(s) == 0:
        return 0

    count = 0
    for i in range(1, len(s) + 1):
        if 'A' <= s[-i] <= 'z':
            count += 1
        else:
            break

    return count


def length_of_last_word(s):
    """
    :param s: (str)
    :return: (int)
    """
    if not s:
        return 0

    count = 0
    for char in s[::-1]:
        if char == ' ' and count == 0:
            continue
        elif char != ' ':
            count += 1
        else:
            break

    return count



def test(s, answer):
    outputs = length_of_last_word(s)
    print("Inputs:{}, Outputs:{}, Except:{}".format(s, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test("Hello World", 5)


if __name__ == '__main__':
    main()
