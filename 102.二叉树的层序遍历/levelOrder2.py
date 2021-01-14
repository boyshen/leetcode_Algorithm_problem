# -*- encoding: utf-8 -*-
"""
@file: levelOrder2.py
@time: 2020/9/15 下午5:01
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 102.二叉树的层序遍历

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order(root):
    """
    广度优先搜索实现(BFS). 时间复杂度 O(n), 空间复杂度 O(2n)
    :param root: (TreeNode)
    :return: (list)
    """
    if not root:
        return []

    res = []
    queue = [root]

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
        res.append(layer)
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
    root = create_tree(3, 9, 20)
    add_node(root.right, 15, 7)
    outputs = level_order(root)
    answer = [[3], [9, 20], [15, 7]]
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(root, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
