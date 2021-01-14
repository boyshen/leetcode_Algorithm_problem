# -*- encoding: utf-8 -*-
"""
@file: ladderLength.py
@time: 2020/9/16 上午11:37
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 127.单词接龙

给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
1. 每次转换只能改变一个字母。
2. 转换过程中的中间单词必须是字典中的单词。

说明:
如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出: 5
解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。

示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
输出: 0
解释: endWord "cog" 不在字典中，所以无法进行转换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder
"""


def ladder_length1(begin_word, end_word, word_list):
    """
    BFS。时间复杂度：O(M*N)，其中 M 是单词的长度 N 是单词表中单词的总数。
    空间复杂度 O(M*N). 需要记录每个单词的通用状态。
    :param begin_word: (str)
    :param end_word: (str)
    :param word_list: (list)
    :return: (int)
    """
    if end_word not in word_list:
        return 0

    words_dict = {}
    n = len(begin_word)
    for word in word_list:
        for i in range(n):
            key = word[:i] + '*' + word[i + 1:]
            words_dict[key] = words_dict.get(key, []) + [word]

    queue = [(begin_word, 1)]
    while queue:
        word, step = queue.pop(0)
        for i in range(n):
            temp = word[:i] + '*' + word[i + 1:]
            for w in words_dict.get(temp, []):
                if w == end_word:
                    return step + 1
                queue.append((w, step + 1))
            if temp in words_dict:
                words_dict[temp] = []

    return 0


def ladder_length2(begin_word, end_word, word_list):
    """
    双向 BFS。 时间复杂度：O(M*N)，其中 M 是单词的长度 N 是单词表中单词的总数。
    空间复杂度 O(M*N). 需要记录每个单词的通用状态。
    :param begin_word: (str)
    :param end_word: (str)
    :param word_list: (list)
    :return: (int)
    """
    if end_word not in word_list:
        return 0

    # 构建字典树
    words_dict = {}
    size = len(begin_word)
    for word in word_list:
        for i in range(size):
            key = word[:i] + '*' + word[i + 1:]
            words_dict[key] = words_dict.get(key, []) + [word]

    start_queue = [(begin_word, 1)]
    end_queue = [(end_word, 1)]
    start_visit = {begin_word: 1}
    end_visit = {end_word: 1}
    while start_queue and end_queue:
        # start 和 end 两步双向同时查找
        res = visit_word(start_queue, words_dict, start_visit, end_visit)
        if res:
            return res

        res = visit_word(end_queue, words_dict, end_visit, start_visit)
        if res:
            return res
    return 0


def ladder_length3(begin_word, end_word, word_list):
    """
    双向 BFS。另一种实现方式。
    :param begin_word: (str)
    :param end_word: (str)
    :param word_list: (list[str])
    :return: (int)
    """
    if end_word not in word_list:
        return 0

    if begin_word in word_list:
        word_list.remove(begin_word)

    begin_visit = {begin_word}
    end_visit = {end_word}
    visit = {begin_word, end_word}
    step = 1

    while begin_visit and end_visit:
        # beginVisited 和 endVisited 交替使用. 每次从单词数量小的集合开始扩散
        if len(begin_visit) > len(end_visit):
            begin_visit, end_visit = end_visit, begin_visit

        next_layer_visit = set()
        for word in begin_visit:
            w_list = list(word)
            for i in range(len(w_list)):
                origin_char = w_list[i]
                for c in range(26):
                    w_list[i] = chr(ord('a') + c)
                    next_word = ''.join(w_list)
                    if next_word in word_list:
                        if next_word in end_visit:
                            return step + 1
                        if next_word not in visit:
                            visit.add(next_word)
                            next_layer_visit.add(next_word)
                w_list[i] = origin_char
        step += 1
        begin_visit = next_layer_visit
    return 0


def visit_word(queue, words_dict, visit, other_visit):
    """
    :param queue: (list)
    :param words_dict: (dict)
    :param visit: (dict)
    :param other_visit: (dict)
    :return: (int)
    """
    word, step = queue.pop(0)
    for i in range(len(word)):
        temp = word[:i] + '*' + word[i + 1:]
        for w in words_dict.get(temp, []):
            # 如果开始和结束都有共同的词，则返回
            if w in other_visit:
                return step + other_visit[w]
            if w not in visit:
                queue.append((w, step + 1))
                visit[w] = step + 1

    return None


def ladder_length(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0

    word_dict = {}
    for word in word_list:
        for i in range(len(word)):
            key = word[:i] + '*' + word[i + 1:]
            word_dict[key] = word_dict.get(key, []) + [word]

    start_queue = [(begin_word, 1)]
    end_queue = [(end_word, 1)]
    start_visit = {begin_word: 1}
    end_visit = {end_word: 1}
    while start_queue and end_queue:
        res = visit_word(start_queue, word_dict, start_visit, end_visit)
        if res is not None:
            return res

        res = visit_word(end_queue, word_dict, end_visit, start_visit)
        if res is not None:
            return res
    return 0


def visit_word1(queue, word_dict, visit, other_visit):
    word, step = queue.pop(0)
    for i in range(len(word)):
        key = word[:i] + '*' + word[i + 1:]
        for w in word_dict.get(key, []):
            if w in other_visit:
                return step + other_visit[w]
            visit[w] = step + 1
            queue.append((w, step + 1))
    return None


def test(begin_word, end_word, word_list, answer):
    outputs = ladder_length(begin_word, end_word, word_list)
    print("Inputs:begin_word={}, end_word={}, word_list={}, Outputs:{}, Except:{}".format(begin_word, end_word,
                                                                                          word_list, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    begin_word, end_word, word_list = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    test(begin_word, end_word, word_list, 5)

    begin_word, end_word, word_list = "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
    test(begin_word, end_word, word_list, 0)

    begin_word, end_word, word_list = "red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
    test(begin_word, end_word, word_list, 4)


if __name__ == '__main__':
    main()
