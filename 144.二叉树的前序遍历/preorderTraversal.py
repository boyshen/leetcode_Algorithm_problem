# -*- encoding: utf-8 -*-
"""
@file: preorderTraversal.py
@time: 2020/9/2 下午5:46
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 144.二叉树的前序遍历

给定一个二叉树，返回它的 前序 遍历。

example:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
"""
from tree.treeNode import create_binary_search_tree, add_tree_node


def preorder_traversal1(root):
    """
    递归
    :param root: (TreeNode, mandatory)
    :return: (list)
    """
    if root is None:
        return []
    return [root.val] + preorder_traversal1(root.left) + preorder_traversal1(root.right)


def preorder_traversal(root):
    """
    栈实现。时间复杂度 O(n), 空间复杂度 O(n)
    :param root: (TreeNode)
    :return: (list[int])
    """
    stack = []
    res = []
    curl = root

    while curl is not None or len(stack) != 0:
        while curl:
            res.append(curl.val)
            stack.append(curl)
            curl = curl.left

        node = stack.pop()
        curl = node.right
    return res


def main():
    inputs = create_binary_search_tree(1, None, 2)
    add_tree_node(inputs.right, 3)
    outputs = preorder_traversal(inputs)
    answer = [1, 2, 3]
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format([1, None, 2, 3], outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
