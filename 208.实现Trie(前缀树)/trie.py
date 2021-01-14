# -*- encoding: utf-8 -*-
"""
@file: trie.py
@time: 2020/10/12 下午3:41
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  208.实现 Trie (前缀树)

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true

说明:
你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree/
"""


class Trie(object):

    def __init__(self):
        self.root = {}
        self.end = '#'

    def insert(self, word):
        """
        :param word: (str)
        :return:
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end] = self.end

    def search(self, word):
        """
        :param word: (str)
        :return: (bool)
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end in node

    def starts_with(self, prefix):
        """
        :param prefix: (str)
        :return: (bool)
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


def main():
    trie = Trie()
    trie.insert("apple")
    outputs = trie.search("apple")
    assert outputs is True, print("Answer Failed")

    outputs = trie.search("app")
    assert outputs is False, print("Answer Failed")

    outputs = trie.starts_with("app")
    assert outputs is True, print("Answer Failed")

    trie.insert("app")
    outputs = trie.search("app")
    assert outputs is True, print("Answer Failed")

    print("test over")


if __name__ == '__main__':
    main()
