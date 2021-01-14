# -*- encoding: utf-8 -*-
"""
@file: invertTree.py
@time: 2020/9/8 上午10:09
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  226.翻转二叉树
翻转一棵二叉树。

示例：
输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
"""
from queue import Queue


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def invert_tree1(root):
    """
    递归。时间复杂度 O(n), 空间复杂度 O(n)
    :param root: (TreeNode)
    :return: (TreeNode)
    """
    if root:
        root.left, root.right = root.right, root.left
        invert_tree1(root.left)
        invert_tree1(root.right)

    return root


def invert_tree(root):
    """
    队列实现。时间复杂度为 O(n), 空间复杂度 O(n)
    :param root: (TreeNode)
    :return: (TreeNode)
    """
    if not root:
        return root

    queue = [root]
    while queue:
        node = queue.pop(0)
        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root


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


def inorder_traversal(root):
    """
    中序遍历
    :param root: (TreeNode)
    :return: (list)
    """
    if not root:
        return []

    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def main():
    inputs_root = create_tree(4, 2, 7)
    add_node(inputs_root.left, 1, 3)
    add_node(inputs_root.right, 6, 9)
    inputs = inorder_traversal(inputs_root)
    outputs_root = invert_tree(inputs_root)
    outputs = inorder_traversal(outputs_root)
    answer = [9, 7, 6, 4, 3, 2, 1]
    assert answer == outputs, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs_root = create_tree(1, 2, None)
    inputs = inorder_traversal(inputs_root)
    outputs_root = invert_tree(inputs_root)
    outputs = inorder_traversal(outputs_root)
    answer = [1, 2]
    assert answer == outputs, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs_root = create_tree(None, None, None)
    inputs = inorder_traversal(inputs_root)
    outputs_root = invert_tree(inputs_root)
    outputs = inorder_traversal(outputs_root)
    answer = [None]
    assert answer == outputs, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
