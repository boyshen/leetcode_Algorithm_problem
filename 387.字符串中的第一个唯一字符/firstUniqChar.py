# -*- encoding: utf-8 -*-
"""
@file: firstUniqChar.py
@time: 2020/11/1 下午5:36
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 387.字符串中的第一个唯一字符

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：
s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

提示：你可以假定该字符串只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string/
"""


def first_uniq_char(s):
    """
    哈希法。时间复杂度 O(N), 空间复杂度 O(N)
    :param s: (str)
    :return: (int)
    """
    char_map = {}
    for char in s:
        char_map[char] = char_map.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_map[char] == 1:
            return i

    return -1


def test(s, answer):
    outputs = first_uniq_char(s)
    print("Inputs:{}, Outputs:{}, Except:{}".format(s, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test("leetcode", 0)
    test("loveleetcode", 2)


if __name__ == '__main__':
    main()
