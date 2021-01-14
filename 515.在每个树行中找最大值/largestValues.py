# -*- encoding: utf-8 -*-
"""
@file: largestValues.py
@time: 2020/9/15 下午6:58
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 515.在每个树行中找最大值

您需要在二叉树的每一行中找到最大的值。

示例：
输入:

          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row
"""


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def largest_values1(root):
    """
    BFS. 时间复杂度为 O(n*k), 空间复杂度 O(2*n)
    :param root: (TreeNode)
    :return: (list)
    """
    if not root:
        return []

    queue = [root]
    res = []

    while queue:
        size = len(queue)
        layer = []
        for _ in range(size):
            node = queue.pop(0)
            layer.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(max(layer))

    return res


def largest_values(root):
    """
    DFS. 时间复杂度为 O(n), 空间复杂度为 O(2n)
    :param root: (TreeNode)
    :return: (list)
    """
    if not root:
        return []

    layer = {}

    def helper(node, level):
        if node is None:
            return

        layer[level] = layer.get(level, []) + [node.val]
        helper(node.left, level + 1)
        helper(node.right, level + 1)

    helper(root, 0)
    res = [max(v) for i, v in layer.items()]

    return res


def create_tree(x, left, right):
    """
    创建树
    :param x: (int)
    :param left:  (int)
    :param right:  (int)
    :return:
    """
    root = TreeNode(x)
    if left:
        root.left = TreeNode(left)
    if right:
        root.right = TreeNode(right)
    return root


def add_node(root, left, right):
    """
    添加叶子节点
    :param root: (int)
    :param left: (int)
    :param right: (int)
    :return:
    """
    if left:
        root.left = TreeNode(left)
    if right:
        root.right = TreeNode(right)


def main():
    root = create_tree(1, 3, 2)
    add_node(root.left, 5, 3)
    add_node(root.right, None, 9)

    outputs = largest_values(root)
    print(outputs)


if __name__ == '__main__':
    main()
