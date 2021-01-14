# -*- encoding: utf-8 -*-
"""
@file: numJewelsInStones.py
@time: 2020/11/1 下午5:05
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  771.771.宝石与石头

给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

示例 1:
输入: J = "aA", S = "aAAbbbb"
输出: 3

示例 2:
输入: J = "z", S = "ZZ"
输出: 0

注意:
S 和 J 最多含有50个字母。
 J 中的字符不重复。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jewels-and-stones
"""


def num_jewels_in_stones1(j, s):
    """
    暴力法。时间复杂度 O(mn), 空间复杂度 O(1)
    :param j: (str)
    :param s: (str)
    :return: (int)
    """

    count = 0
    for char in s:
        if char in j:
            count += 1
    return count


def num_jewels_in_stones(j, s):
    """
    哈希。时间复杂度 O(m+n), 空间复杂度 O(m)
    :param j: (str)
    :param s: (str)
    :return: (int)
    """

    j_set = set(j)
    count = 0
    for x in s:
        if x in j_set:
            count += 1

    return count


def test(j, s, answer):
    outputs = num_jewels_in_stones(j, s)
    print("Inputs:J = {}, S={}, Outputs:{}, Except:{}".format(j, s, outputs, answer))


def main():
    test("aA", "aAAbbbb", 3)
    test("z", "ZZ", 0)


if __name__ == '__main__':
    main()
