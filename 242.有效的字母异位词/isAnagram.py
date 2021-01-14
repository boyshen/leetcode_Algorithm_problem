# -*- encoding: utf-8 -*-
"""
@file: isAnagram.py
@time: 2020/8/20 上午10:05
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 242. 242.有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

example:
输入: s = "anagram", t = "nagaram"
输出: true

输入: s = "rat", t = "car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram/description/
"""


def is_anagram1(s, t):
    """
    使用排序的方法。将字符 s 和字符 t 进行排序，排序比较两个字符是否相同。
    排序使用快排，时间复杂度为 O(NlogN), 空间复杂度 O(1)
    :param s: (str, mandatory)
    :param t: (str, mandatory)
    :return: (bool)
    """
    return sorted(s) == sorted(t)


def is_anagram2(s, t):
    """
    使用 dict (hash) 的方式。将s和t两个字符串的元素分别存入 dict 中。key = 字符、 value = 字符数量。
    最后比较两个 dict 是否相同。时间复杂度为 O(n), 空间复杂度 O(n + m). n 和 m 分别为字符串s 和 t 的长度
    :param s: (str, mandatory)
    :param t: (str, mandatory)
    :return: (bool)
    """
    dict1, dict2 = {}, {}
    for x in s:
        dict1[x] = dict1.get(x, 0) + 1
    for x in t:
        dict2[x] = dict2.get(x, 0) + 1
    return dict1 == dict2


def is_anagram(s, t):
    """
    使用 list 的方式。 初始化两个列表: list1 = [0] * 26， list2 = [0] * 26 。
    将字符元素转换成 ASCII 编码 - 97 即可得到 0 ～ 25 的范围。
    时间复杂度为 O(n), 空间复杂度 O(n + m). n 和 m 分别为字符串s 和 t 的长度
    :param s: (str, mandatory)
    :param t: (str, mandatory)
    :return: (bool)
    """
    dict1, dict2 = [0] * 26, [0] * 26
    for x in s:
        dict1[ord(x) - 97] += 1
    for x in t:
        dict2[ord(x) - 97] += 1
    return dict1 == dict2


def main():
    inputs_s = "anagram"
    inputs_t = "nagaram"
    answer = True
    outputs = is_anagram(inputs_s, inputs_t)
    assert outputs is answer, print("Inputs:{},{}, Outputs:{}, Except:{}".format(inputs_s, inputs_t, outputs, answer))
    # print("input s:{}, t:{}, output:{}".format(s, t, is_anagram1(s, t)))
    # print("input s:{}, t:{}, output:{}".format(s, t, is_anagram2(s, t)))
    # print("input s:{}, t:{}, output:{}".format(s, t, is_anagram3(s, t)))

    inputs_s = "car"
    inputs_t = "tar"
    answer = False
    outputs = is_anagram(inputs_s, inputs_t)
    assert outputs is answer, print("Inputs:{},{}, Outputs:{}, Except:{}".format(inputs_s, inputs_t, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
