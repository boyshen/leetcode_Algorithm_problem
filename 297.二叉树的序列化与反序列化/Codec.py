# -*- encoding: utf-8 -*-
"""
@file: Codec.py
@time: 2020/9/8 下午5:52
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 297. 二叉树的序列化与反序列化

序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，
采取相反方式重构得到原数据。
请设计一个算法来实现二叉树的序列化与反序列化。
这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 
你可以将以下二叉树：
    1
   / \
  2   3
     / \
    4   5
序列化为 "[1,2,3,null,null,4,5]"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec1(object):
    """
    递归实现
    """

    @staticmethod
    def serialize(root):
        """
        前序遍历.将树转换成序列字符输出
        :param root:
        :return:
        """
        if not root:
            return ''

        def recursion(node, string):
            if not node:
                return string + 'None,'
            else:
                string += str(node.val) + ','
                string = recursion(node.left, string)
                string = recursion(node.right, string)
            return string

        return recursion(root, '')

    @staticmethod
    def deserialize(data):
        """
        将字符序列转换成树
        :param data: (str)
        :return: (TreeNode)
        """
        if data == '' or len(data) == 0:
            return

        def recursion():
            val = next(values)
            if val == 'None':
                return None
            # "1,2,None,None,3,4,None,None,5,None,None,"
            node = TreeNode(int(val))
            node.left = recursion()
            node.right = recursion()
            return node

        values = iter(data.split(','))
        root = recursion()
        return root


class Codec2(object):
    """
    广度优先收缩BFS实现
    """

    @staticmethod
    def serialize(root):
        """
        序列化
        :param root: (TreeNode)
        :return: (str)
        """
        if not root:
            return ''
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                res.append(str(node.val) if node else str(node))

                if node is None:
                    continue
                queue.append(node.left)
                queue.append(node.right)

        return ','.join(res)

    @staticmethod
    def deserialize(data):
        """
        反序列化
        :param data: (str)
        :return: (TreeNode)
        """
        if data == '' or len(data) == 0:
            return
        values = data.split(',')
        root = TreeNode(int(values[0]))
        queue = [root]
        for i in range(1, len(values), 2):
            parent = queue.pop(0)
            if values[i] != 'None':
                left = TreeNode(int(values[i]))
                parent.left = left
                queue.append(left)
            if values[i + 1] != 'None':
                right = TreeNode(int(values[i + 1]))
                parent.right = right
                queue.append(right)
        return root


class Codec(object):
    @staticmethod
    def serialize(root):
        """
        前序遍历。将树转换成序列字符串输出
        """
        if root is None:
            return ''

        def recursion(node):
            if node is None:
                return 'None'
            return str(node.val) + ',' + recursion(node.left) + ',' + recursion(node.right)

        return recursion(root)

    @staticmethod
    def deserialize(data):
        """
        将字符串转换成树
        """
        if data == '' or len(data) == 0:
            return

        def recursion():
            value = next(values)
            if value == 'None':
                return None

            node = TreeNode(int(value))
            node.left = recursion()
            node.right = recursion()
            return node

        values = iter(data.split(','))
        return recursion()


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


def main():
    # root = create_tree(1, 2, 3)
    # add_node(root.right, 4, 5)
    # output = Codec.serialize(root)
    # print(output)

    # 递归测试
    inputs = "1,2,None,None,3,4,None,None,5,None,None"
    root = Codec.deserialize(inputs)
    outputs = Codec.serialize(root)
    assert outputs == inputs, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, inputs))

    # BFS(广度优先搜索测试)
    # inputs = "1,2,3,None,None,4,5,None,None,None,None"
    # root = Codec.deserialize(inputs)
    # outputs = Codec.serialize(root)
    # assert outputs == inputs, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, inputs))

    print("The test passed")


if __name__ == '__main__':
    main()
