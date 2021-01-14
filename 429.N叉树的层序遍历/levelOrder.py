# -*- encoding: utf-8 -*-
"""
@file: levelOrder.py
@time: 2020/9/4 上午11:43
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 429.N 叉树的层序遍历

给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

返回其层序遍历:
[
     [1],
     [3,2,4],
     [5,6]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
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
    def level_order(self, root):
        """
        使用广度优先搜索. 时间复杂度 O(N), 空间复杂度 O(N)
        :param root: (Node)
        :return: (list)
        """
        if not root:
            return []

        queue = [root]
        res = []
        while queue:
            children_val = []
            layer = []
            for node in queue:
                children_val.append(node.val)
                layer.extend(node.children)
            queue = layer
            res.append(children_val)
        return res


class Solution(object):
    def level_order(self, root):
        """
        使用递归的方法
        :param root: (Node)
        :return: (list)
        """
        if not root:
            return []

        self.res = []
        self.helper(root, level=0)
        return self.res

    def helper(self, root, level):
        if len(self.res) == level:
            self.res.append([])
        self.res[level].append(root.val)
        for children in root.children:
            self.helper(children, level + 1)


def main():
    root = create_tree(1, [3, 2, 4])
    add_children(root.children[0], [5, 6])

    sol1 = Solution()
    outputs = sol1.level_order(root)
    answer = [[1], [3, 2, 4], [5, 6]]
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format([3, 2, 4, 5, 6], outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
