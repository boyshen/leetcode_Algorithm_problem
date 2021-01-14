# -*- encoding: utf-8 -*-
"""
@file: minMutation.py
@time: 2020/9/15 下午6:32
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  433. 最小基因变化

一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。

现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，
请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

注意:
起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
所有的目标基因序列必须是合法的。
假定起始基因序列与目标基因序列是不一样的。

示例 1:
start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]
返回值: 1

示例 2:
start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
返回值: 2

示例 3:
start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
返回值: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-genetic-mutation
"""


def min_mutation1(start, end, bank):
    """
    广度优先搜索。时间复杂度 O(M * N). M 为基因序列的长度，N 为bank的长度。 空间复杂度 O(M * N)
    :param start: (str)
    :param end: (str)
    :param bank: (list)
    :return: (int)
    """
    if end not in bank:
        return -1

    sequence = ['A', 'C', 'G', 'T']
    queue = [(start, 0)]
    while queue:
        word, step = queue.pop(0)

        if word == end:
            return step

        for i in range(len(word)):
            for pos in sequence:
                if pos == word[i]:
                    continue
                temp = word[:i] + pos + word[i + 1:]
                if temp in bank:
                    bank.remove(temp)
                    queue.append((temp, step + 1))
    return -1


def min_mutation(start, end, bank):
    """
    双向 BFS
    :param start: (str)
    :param end: (str)
    :param bank: (list[str])
    :return: (int)
    """
    if end not in bank:
        return -1

    sequence = ['A', 'C', 'G', 'T']
    start_visit = {start}
    end_visit = {end}
    visit = {start, end}
    step = 0

    while start_visit and end_visit:
        if len(start_visit) > len(end_visit):
            start_visit, end_visit = end_visit, start_visit

        next_layer_visit = set()
        for word in start_visit:
            w_list = list(word)
            for i in range(len(w_list)):
                origin_char = w_list[i]
                for c in sequence:
                    if origin_char == c:
                        continue
                    w_list[i] = c
                    next_word = ''.join(w_list)
                    if next_word in bank:
                        if next_word in end_visit:
                            return step + 1
                        if next_word not in visit:
                            next_layer_visit.add(next_word)
                            visit.add(next_word)

                w_list[i] = origin_char
        step += 1
        start_visit = next_layer_visit
    return -1


def test(start, end, bank, answer):
    print("Inputs:start={},end={},back={}, ".format(start, end, bank), end='')
    outputs = min_mutation(start, end, bank)
    print("Outputs:{}, Except:{}".format(outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    start, end, bank = "AACCGGTT", "AACCGGTA", ["AACCGGTA"]
    test(start, end, bank, 1)

    start, end, bank = "AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    test(start, end, bank, 2)

    start, end, bank = "AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    test(start, end, bank, 3)

    start, end, bank = "AACCTTGG", "AATTCCGG", ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"]
    test(start, end, bank, -1)

    start, end, bank = "AAAACCCC", "CCCCCCCC", ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC", "ACCCCCCC", "CCCCCCCC",
                                                "AAACCCCC", "AACCCCCC"]
    test(start, end, bank, 4)


if __name__ == '__main__':
    main()
