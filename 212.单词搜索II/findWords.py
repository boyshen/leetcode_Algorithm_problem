# -*- encoding: utf-8 -*-
"""
@file: findWords.py
@time: 2020/10/12 下午4:46
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  212.单词搜索 II

给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母在一个单词中不允许被重复使用。

示例:
输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:
你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？
散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
"""


class TrieNode1(object):
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie1(object):
    def __init__(self):
        self.root = TrieNode1()

    def insert(self, words):
        node = self.root
        for char in words:
            node = node.children.setdefault(char, TrieNode1())
        node.is_word = True


class Solution1(object):
    """
    Trie + DFS 实现。
    时间复杂度 O(M * (4 * 3^L)) 。
        M 为表格的字符大小 m * n。
        在表格中找到单词的第一个字符有 4 种选择，即上下左右，最糟糕的情况下4个方向都需要进行搜索。
        在表格中找到单词的第二个字符、第三个字符等都有 3 种选择，原因是同一个单元格内的字母在一个单词中不允许被重复使用。
        L 为单词长度
    空间复杂度为 O(N). N 为Trie中的字符数量
    """

    def find_words(self, board, words):
        """
        :param board: (list[list[str]])
        :param words: (list[str])
        :return: (int)
        """
        trie = Trie1()
        node = trie.root
        for word in words:
            trie.insert(word)

        res = list()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in node.children:
                    self.dfs(board, node, i, j, res, '')
        return res

    def dfs(self, board, node, i, j, res, w):
        if node.is_word:
            res.append(w)
            node.is_word = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        char = board[i][j]
        if char == '#':
            return
        if char not in node.children:
            return
        node = node.children[char]

        board[i][j] = '#'
        self.dfs(board, node, i, j + 1, res, w + char)
        self.dfs(board, node, i + 1, j, res, w + char)
        self.dfs(board, node, i - 1, j, res, w + char)
        self.dfs(board, node, i, j - 1, res, w + char)
        board[i][j] = char


class Solution(object):
    """
    Trie + DFS 的另一种实现方式
    """

    def find_words(self, board, words):
        """
        :param board: (list[list[str]])
        :param words: (list[str])
        :return: (list)
        """

        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        m, n = len(board), len(board[0])
        res = set()

        def dfs(i, j, node, w, visit):
            if '#' in node:
                res.add(w)

            for (x, y) in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                dx, dy = x + i, y + j
                if 0 <= dx < m and 0 <= dy < n and board[dx][dy] in node and (dx, dy) not in visit:
                    dfs(dx, dy, node[board[dx][dy]], w + board[dx][dy], visit | {(dx, dy)})

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        return list(res)


def test(board, words, answer):
    solution = Solution()
    outputs = solution.find_words(board, words)
    print("Inputs:board={}, words={}, Outputs:{}, Except:{}".format(board, words, outputs, answer))


def main():
    board = [['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']]
    words = ["oath", "pea", "eat", "rain"]
    test(board, words, ["eat", "oath"])


if __name__ == '__main__':
    main()
