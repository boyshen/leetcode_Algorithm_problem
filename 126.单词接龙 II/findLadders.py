# -*- encoding: utf-8 -*-
"""
@file: findLadders.py
@time: 2020/9/16 下午4:45
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 126.单词接龙 II
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
1. 每次转换只能改变一个字母。
2. 转换后得到的单词必须是字典中的单词。

说明:
如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
输出: []
解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder-ii
"""

from collections import defaultdict


def find_ladders(begin_word, end_word, word_list):
    """
    BFS. 时间复杂度为 O(N^2 * C) C 为 word_list 大小。 N 为 单词的大小
    :param begin_word: (str)
    :param end_word: (str)
    :param word_list: (list)
    :return: (list)
    """
    word_list = set(word_list)
    words = []
    for w in word_list:
        words.extend(list(w))
    words = set(words)

    res = []
    layer = {begin_word: [[begin_word]]}
    size = len(begin_word)

    while layer:
        new_layer = defaultdict(list)
        for word, sequence in layer.items():
            if word == end_word:
                res.extend(val for val in sequence)
            else:
                for i in range(size):
                    for s in words:
                        temp = word[:i] + s + word[i + 1:]
                        if temp in word_list:
                            new_layer[temp] += [val + [temp] for val in sequence]

        word_list -= set(new_layer.keys())
        layer = new_layer

    return res


def main():
    begin_word, end_word, word_list = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    outputs = find_ladders(begin_word, end_word, word_list)
    answer = [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]
    print("begin:{}, end:{}, word_list:{}, Output:{}".format(begin_word, end_word, word_list, outputs))
    assert outputs == answer, print(
        "Inputs: begin={}, end={}, word_list:{}, Outputs:{}, Except:{}".format(begin_word, end_word, word_list, outputs,
                                                                               answer))

    begin_word, end_word, word_list = "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
    outputs = find_ladders(begin_word, end_word, word_list)
    answer = []
    print("begin:{}, end:{}, word_list:{}, Output:{}".format(begin_word, end_word, word_list, outputs))
    assert outputs == answer, print(
        "Inputs: begin={}, end={}, word_list:{}, Outputs:{}, Except:{}".format(begin_word, end_word, word_list, outputs,
                                                                               answer))

    begin_word, end_word, word_list = "red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
    outputs = find_ladders(begin_word, end_word, word_list)
    answer = [['red', 'ted', 'tad', 'tax'], ['red', 'ted', 'tex', 'tax'], ['red', 'rex', 'tex', 'tax']]
    print("begin:{}, end:{}, word_list:{}, Output:{}".format(begin_word, end_word, word_list, outputs))
    assert outputs == answer, print(
        "Inputs: begin={}, end={}, word_list:{}, Outputs:{}, Except:{}".format(begin_word, end_word, word_list, outputs,
                                                                               answer))


if __name__ == '__main__':
    main()
