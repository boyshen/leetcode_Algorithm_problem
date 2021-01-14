# -*- encoding: utf-8 -*-
"""
@file: buildTree.py
@time: 2020/9/10 下午12:07
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  105.从前序与中序遍历序列构造二叉树

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
"""


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution1(object):
    """
    分治。时间复杂度 O(n), 空间复杂度 O(n)
    """

    @staticmethod
    def build_tree(preorder, inorder):
        def recursion(pre, inord):
            if not pre or not inord:
                return None

            val = pre[0]
            root = TreeNode(val)
            size = inord.index(val)

            # 划分左子树和右子树节点。
            p_left = pre[pre.index(val) + 1: size + 1]
            p_right = pre[size + 1:]

            i_left = inord[:size]
            i_right = inord[size + 1:]

            root.left = recursion(p_left, i_left)
            root.right = recursion(p_right, i_right)

            return root

        return recursion(preorder, inorder)


class Solution2(object):
    """
    递归实现。(改进)。 时间复杂度 O(n), 空间复杂度 O(n)
    """

    @staticmethod
    def build_tree(preorder, inorder):
        index = {val: i for i, val in enumerate(inorder)}

        def recursion(p_left, p_right, i_left, i_right):
            if p_left > p_right or i_left > i_right:
                return None
            if p_left == p_right:
                return TreeNode(preorder[p_left])

            val = preorder[p_left]
            root = TreeNode(val)
            size = index[val]

            count = size - i_left
            root.left = recursion(p_left + 1, p_left + count, i_left, size - 1)
            root.right = recursion(p_left + count + 1, p_right, size + 1, i_right)

            return root

        return recursion(0, len(preorder) - 1, 0, len(inorder) - 1)


class Solution(object):
    """
    迭代实现。时间复杂度 O(n), 空间复杂度 O(n)
    """

    @staticmethod
    def build_tree(preorder, inorder):
        if not preorder or not inorder:
            return

        val_to_index = {val: i for i, val in enumerate(inorder)}
        root = TreeNode(preorder[0])
        index = val_to_index[preorder[0]]
        stack = [(root, index)]

        for p_index in range(1, len(preorder)):
            i_index = val_to_index[preorder[p_index]]
            if i_index > stack[-1][1]:
                # 右子树
                node = None
                while stack and i_index > stack[-1][1]:
                    node = stack[-1][0]
                    stack.pop()
                node.right = TreeNode(preorder[p_index])
                stack.append((node.right, i_index))
            else:
                # 左子树
                node = stack[-1][0]
                node.left = TreeNode(preorder[p_index])
                stack.append((node.left, i_index))
        return root


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


def inorder_traversal(root):
    """
    中序遍历
    :param root: (TreeNode)
    :return: (list)
    """
    if not root:
        return []

    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


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
    inorder = [4, 2, 8, 5, 9, 1, 6, 3, 7]
    preorder = [1, 2, 4, 5, 8, 9, 3, 6, 7]
    outputs_root = Solution.build_tree(preorder, inorder)
    outputs = inorder_traversal(outputs_root)
    assert outputs == inorder, print("Inputs:{}/{}, Outputs:{}, Except:{}".format(inorder, preorder, outputs, inorder))

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    outputs_root = Solution.build_tree(preorder, inorder)
    outputs = inorder_traversal(outputs_root)
    assert outputs == inorder, print("Inputs:{}/{}, Outputs:{}, Except:{}".format(inorder, preorder, outputs, inorder))

    print("The test passed")


if __name__ == '__main__':
    main()
