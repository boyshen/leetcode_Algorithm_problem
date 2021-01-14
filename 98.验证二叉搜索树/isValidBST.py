# -*- encoding: utf-8 -*-
"""
@file: isValidBST.py
@time: 2020/8/21 下午2:08
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 98.验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：
    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。

example:
输入:
    2
   / \
  1   3
输出: true

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
"""


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def is_valid_binary_search_tree1(root):
    """
    采用中序遍历的方法。将 tree 数据从左往右升序排列。
    :param root: (TreeNode)
    :return: (bool)
    """

    def in_order(node):
        if not node:
            return []
        return in_order(node.left) + [node.val] + in_order(node.right)

    order_value = in_order(root)
    return order_value == list(sorted(set(order_value)))


def is_valid_binary_search_tree(root):
    """
    递归。时间复杂度 O(n), 空间复杂度 O(n)
    """
    def in_order(node, lower, upper):
        if node is None:
            return True

        if node.val <= lower or node.val >= upper:
            return False
        if not in_order(node.left, lower, node.val):
            return False
        if not in_order(node.right, node.val, upper):
            return False
        return True
    return in_order(root, float('-inf'), float('inf'))


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
    inputs_root = create_tree(2, 1, 3)
    inputs = preorder_traversal(inputs_root)
    answer = True
    outputs = is_valid_binary_search_tree(inputs_root)
    assert answer == outputs, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs_root = create_tree(5, 1, 4)
    add_node(inputs_root.right, 3, 6)
    inputs = preorder_traversal(inputs_root)
    answer = False
    outputs = is_valid_binary_search_tree(inputs_root)
    assert answer == outputs, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs_root = create_tree(1, 1, None)
    inputs = preorder_traversal(inputs_root)
    answer = False
    outputs = is_valid_binary_search_tree(inputs_root)
    assert answer == outputs, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs_root = create_tree(0, None, None)
    inputs = preorder_traversal(inputs_root)
    answer = True
    outputs = is_valid_binary_search_tree(inputs_root)
    assert answer == outputs, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs_root = create_tree(1, None, 1)
    inputs = preorder_traversal(inputs_root)
    answer = False
    outputs = is_valid_binary_search_tree(inputs_root)
    assert answer == outputs, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    root = create_tree(3, 1, 5)
    add_node(root.left, 0, 2)
    add_node(root.right, 4, 6)
    add_node(root.left.right, None, 3)
    inputs = preorder_traversal(inputs_root)
    answer = False
    outputs = is_valid_binary_search_tree(inputs_root)
    assert answer == outputs, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    root = create_tree(3, None, 30)
    add_node(root.right, 10, None)
    add_node(root.right.left, None, 15)
    add_node(root.right.left.right, None, 45)
    inputs = preorder_traversal(inputs_root)
    answer = False
    outputs = is_valid_binary_search_tree(inputs_root)
    assert answer == outputs, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
