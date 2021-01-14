# -*- encoding: utf-8 -*-
"""
@file: postorder.py
@time: 2020/9/2 下午6:25
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 590.N叉树的后序遍历
给定一个 N 叉树，返回其节点值的后序遍历。

example:
给定一个 3叉树 :
返回其后序遍历: [5,6,3,2,4,1].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
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
    def postorder(self, root):
        """
        递归
        :param root: (Node)
        :return: (list)
        """
        self.res = []
        self.order(root)
        return self.res

    def order(self, root):
        if root is None:
            return None
        for children in root.children:
            self.order(children)
        self.res.append(root.val)


class Solution(object):
    def postorder(self, root):
        """
        栈实现
        :param root: (Node)
        :return: (list)
        """
        if root is None:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            for children in node.children:
                stack.append(children)

        res.reverse()
        return res


def main():
    root = create_tree(1, [3, 2, 4])
    add_children(root.children[0], [5, 6])

    sol1 = Solution()
    outputs = sol1.postorder(root)
    answer = [5, 6, 3, 2, 4, 1]
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format([3, 2, 4, 5, 6], outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
