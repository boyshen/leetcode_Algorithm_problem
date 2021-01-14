# -*- encoding: utf-8 -*-
"""
@file: minDepth.py
@time: 2020/9/8 下午3:53
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:111.二叉树的最小深度

给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。

示例:
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
"""


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


# def min_depth(root):
#     """
#     参考：https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36060/3-lines-in-Every-Language
#     :param root: (TreeNode)
#     :return: (int)
#     """
#     if not root:
#         return 0
#     d = map(min_depth, [root.left, root.right])
#     return 1 + (min(d, default=0) or max(d, default=0))


def min_depth1(root):
    """
    递归实现
    :param root: (TreeNode)
    :return: (int)
    """
    if not root:
        return 0

    def helper(node, depth):
        if not node.left and not node.right:
            return 1
        if node.left:
            depth = min(helper(node.left, depth), depth)
        if node.right:
            depth = min(helper(node.right, depth), depth)
        return depth + 1

    return helper(root, 10 ** 9)


def min_depth(root):
    """
    广度优先搜索
    :param root: (TreeNode)
    :return: (int)
    """
    if not root:
        return 0

    queue = [root]
    res = 1
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.pop(0)
            if not node.left and not node.right:
                return res
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
    outputs = min_depth(inputs_root)
    answer = 2
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs_root = create_tree(3, 9, 20)
    add_node(inputs_root.left, 3, 4)
    add_node(inputs_root.left.right, 5, 6)
    inputs = preorder_traversal(inputs_root)
    outputs = min_depth(inputs_root)
    answer = 2
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs_root = create_tree(3, 9, None)
    inputs = preorder_traversal(inputs_root)
    outputs = min_depth(inputs_root)
    answer = 2
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    inputs_root = TreeNode(None)
    inputs = []
    outputs = min_depth(inputs_root)
    answer = 1
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
