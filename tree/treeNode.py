# -*- encoding: utf-8 -*-
"""
@file: treeNode.py
@time: 2020/8/21 下午2:11
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_binary_search_tree(root, left=None, right=None):
    root = TreeNode(root)
    if left:
        root.left = TreeNode(left)
    if right:
        root.right = TreeNode(right)
    return root


def add_tree_node(root, left=None, right=None):
    if not isinstance(root, TreeNode):
        return False

    if left:
        root.left = TreeNode(left)
    if right:
        root.right = TreeNode(right)
    return root


def ergodic_tree(root, root_val, tree_dict):
    if root is None:
        return None
    else:
        if root_val:
            tree_dict[root_val] = tree_dict.get(root_val, []) + [root.val]

        # print(root.val)
        ergodic_tree(root.left, root.val, tree_dict)
        ergodic_tree(root.right, root.val, tree_dict)


def main():
    root = create_binary_search_tree(2, 1, 3)
    print("root: ", root.val)
    print("left val: ", root.left.val)
    print("right val: ", root.right.val)

    add_tree_node(root.left, 0.5, 1.5)
    add_tree_node(root.left.left, 0.2, 1.2)
    add_tree_node(root.left.right, 0.9, 0.99)
    add_tree_node(root.right, 2.5, 3.5)

    tree_dict = {}
    ergodic_tree(root, None, tree_dict=tree_dict)
    print(tree_dict)


if __name__ == '__main__':
    main()
