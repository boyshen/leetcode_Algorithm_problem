# -*- encoding: utf-8 -*-
"""
@file: maxDepth.py
@time: 2020/9/8 下午12:01
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 104.二叉树的最大深度

给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
"""
from queue import Queue


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def max_depth1(root):
    """
    递归实现
    :param root: (TreeNode)
    :return: (int)
    """
    if not root:
        return 0
    return 1 + max(max_depth1(root.left), max_depth1(root.right))


def max_depth(root):
    """
    广度优先搜索. 时间复杂度 O(n), 空间复杂度 O(n)
    :param root: (TreeNode)
    :return: (int)
    """
    if not root:
        return 0

    queue = [root]
    res = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res += 1
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


def preorder_traversal(root):
    """
    前序遍历
    :param root: (TreeNode)
    :return: (list)
    """
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def main():
    inputs_root = create_tree(3, 9, 20)
    add_node(inputs_root.right, 15, 7)
    inputs = preorder_traversal(inputs_root)
    outputs = max_depth(inputs_root)
    answer = 3
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs_root = create_tree(3, 9, 20)
    add_node(inputs_root.left, 3, 4)
    add_node(inputs_root.left.right, 5, 6)
    inputs = preorder_traversal(inputs_root)
    outputs = max_depth(inputs_root)
    answer = 4
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs_root = TreeNode(None)
    inputs = []
    outputs = max_depth(inputs_root)
    answer = 1
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
