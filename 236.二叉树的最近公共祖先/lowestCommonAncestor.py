# -*- encoding: utf-8 -*-
"""
@file: lowestCommonAncestor.py
@time: 2020/9/9 下午4:15
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 236.二叉树的最近公共祖先

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
"""


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def lowest_common_ancestor1(root, p, q):
    """
    递归实现. (后序遍历)。 时间复杂度 O(N), 空间复杂度 O(N)
    :param root: (TreeNode)
    :param p: (TreeNode)
    :param q: (TreeNode)
    :return: (TreeNode)
    """
    if root in (None, p, q):
        return root

    left = lowest_common_ancestor1(root.left, p, q)
    right = lowest_common_ancestor1(root.right, p, q)
    return root if left and right else left or right


def lowest_common_ancestor(root, p, q):
    """
    迭代 + 记录访问路径。时间复杂度 O(N), 空间复杂度 O(N*2)
    :param root: (TreeNode)
    :param p: (TreeNode)
    :param q: (TreeNode)
    :return: (TreeNode)
    """
    parent = {root: None}
    stack = [root]
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
            parent[node.left] = node
        if node.right:
            stack.append(node.right)
            parent[node.right] = node

    path = set()
    while p:
        path.add(p)
        p = parent[p]
    while q not in path:
        q = parent[q]
    return q


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


def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def main():
    root = create_tree(3, 5, 1)
    add_node(root.left, 6, 2)
    add_node(root.right, 0, 8)
    add_node(root.left.right, 7, 4)
    inputs = preorder(root)
    p = root.left
    q = root.left.right.right
    outputs = lowest_common_ancestor(root, p, q)
    answer = 5
    assert outputs.val == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs.val, answer))

    root = create_tree(3, 5, 1)
    add_node(root.left, 6, 2)
    add_node(root.right, 0, 8)
    add_node(root.left.right, 7, 4)
    inputs = preorder(root)
    p = root.left
    q = root.right
    outputs = lowest_common_ancestor(root, p, q)
    answer = 3
    assert outputs.val == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs.val, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
