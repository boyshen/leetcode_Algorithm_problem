# -*- encoding: utf-8 -*-
"""
@file: inorderTraversal.py
@time: 2020/9/2 下午5:05
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 94.二叉树的中序遍历

给定一个二叉树，返回它的中序 遍历。

example:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
"""
from tree.treeNode import create_binary_search_tree
from tree.treeNode import add_tree_node


def inorder_traversal1(root):
    """
    递归方法实现
    :param root: (TreeNode)
    :return:
    """
    if root is None:
        return []
    return inorder_traversal1(root.left) + [root.val] + inorder_traversal1(root.right)


def inorder_traversal(root):
    """
    使用栈的方式实现
    :param root: (TreeNode, mandatory)
    :return: (list)
    """
    res = []
    stack = []
    curl = root

    while curl is not None or len(stack) != 0:
        while curl:
            stack.append(curl)
            curl = curl.left

        curl = stack.pop()
        res.append(curl.val)
        curl = curl.right

    return res


def main():
    inputs = create_binary_search_tree(1, None, 2)
    add_tree_node(inputs.right, 3)
    outputs = inorder_traversal(inputs)
    answer = [1, 3, 2]
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format([1, None, 2, 3], outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
