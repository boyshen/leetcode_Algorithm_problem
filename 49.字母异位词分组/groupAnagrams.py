# -*- encoding: utf-8 -*-
"""
@file: groupAnagrams.py
@time: 2020/8/31 下午4:07
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 49.字母异位词分组

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

example:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
"""
from collections import defaultdict


def group_anagrams1(s):
    """
    哈希 + 排序的方法。 时间复杂度 O(n * klogk), 空间复杂度 O(n)
    :param s: (list[str])
    :return: (list[list[str]])
    """
    s_dict = {}
    for x in s:
        x_key = tuple(sorted(x))
        s_dict[x_key] = s_dict.get(x_key, []) + [x]
    return s_dict.values()


def group_anagrams2(strs):
    """
    哈希 + 列表。
    时间复杂度 O(M * N), 空间复杂度 O(M * N)
    M 为 strs 的长度，N 为字符串的长度
    :param strs: (list[str])
    :return: (list[list[str]])
    """

    def decoding(string):
        k = [0] * 26
        for char in string:
            index = ord(char) - ord('a')
            k[index] += 1
        return tuple(k)

    str_dict = {}
    for s in strs:
        key = decoding(s)
        if key in str_dict:
            str_dict[key].append(s)
        else:
            str_dict[key] = [s]
    return list(str_dict.values())


def group_anagrams(strs):
    """
    哈希 + 列表。简化版
    :param strs: (list[str])
    :return: (list[list[str]])
    """
    dict_str = defaultdict(list)
    for s in strs:
        key = [0] * 26
        for char in s:
            key[ord(char) - ord('a')] += 1
        dict_str[tuple(key)].append(s)
    return list(dict_str.values())


def main():
    inputs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    answer = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
    outputs = group_anagrams(inputs)
    print(outputs)
    print(answer)
    for out in outputs:
        assert sorted(out) in answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))


if __name__ == '__main__':
    main()
