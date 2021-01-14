# -*- encoding: utf-8 -*-
"""
@file: preorder.py
@time: 2020/9/3 下午3:23
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 589.N叉树的前序遍历

给定一个 N 叉树，返回其节点值的前序遍历。

example:
给定一个 3叉树 :
返回其后序遍历: [1,3,5,6,2,4].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
"""


class Node(object):
    def __init__(self, val, children=None):
        self.val = val
        self.children = children if children is not None else []


def create_tree(val, children):
    """
    创建树
    :param val: (int)
    :param children: (list[int])
    :return: (Node)
    """
    root = Node(val)
    children = [Node(i) for i in children]
    root.children = children
    return root


def add_children(root, children):
    """
    添加子节点
    :param root: (Node)
    :param children: (list[int])
    :return:
    """
    children = [Node(i) for i in children]
    root.children = children


class Solution1(object):
    def preorder(self, root):
        """
        使用递归方法
        :param root: (Node)
        :return: (list)
        """
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return None

        self.res.append(root.val)
        for children in root.children:
            self.helper(children)


class Solution(object):
    def preorder(self, root):
        """
        使用栈方法
        :param root: (Node)
        :return: (list)
        """
        if not root:
            return None
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for i in range(1, len(node.children) + 1):
                stack.append(node.children[-i])
        return res


def main():
    root = create_tree(1, [3, 2, 4])
    add_children(root.children[0], [5, 6])

    sol1 = Solution()
    outputs = sol1.preorder(root)
    answer = [1, 3, 5, 6, 2, 4]
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format([3, 2, 4, 5, 6], outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
