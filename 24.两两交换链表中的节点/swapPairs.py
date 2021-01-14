# -*- encoding: utf-8 -*-
"""
@file: swapPairs.py
@time: 2020/8/13 下午6:40
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 24.两两交换链表中的节点

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

example： 1->2->3->4, 返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china
"""


class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next


def swap_pairs1(head):
    """
    :param head: (Node) 链表头节点
    :return: (Node) 链表对象
    """
    if not isinstance(head, Node):
        return False
    if head.next is None:
        return head

    head_next = head.next
    prev, prev.next = Node(None, None), head
    while prev.next and prev.next.next:
        temp1 = prev.next
        temp2 = temp1.next

        prev.next, temp1.next, temp2.next = temp2, temp2.next, temp1
        prev = temp1

    return head_next


def swap_pairs(head):
    """
    迭代
    :param head: (Node)
    :return: (Node)
    """
    dumpy = Node(None, None)
    dumpy.next = head

    curl, prev = head, dumpy
    while curl and curl.next:
        start = curl
        end = curl.next

        prev.next = end
        start.next = end.next
        end.next = start

        curl = start.next
        prev = start

    return dumpy.next


def create_one_way_linked(value):
    """
    创建单向无环链表。
    :param value: (list, mandatory) 列表元素
    :return: (Node) 头节点对象
    """
    linked = [Node(v, None) for v in value]
    head = linked[0]
    shifting = linked[0]
    for node in linked[1:]:
        shifting.next = node
        shifting = node
    return head


def test(inputs, answer):
    head = create_one_way_linked(inputs)
    root = swap_pairs(head)
    outputs = []
    while root:
        outputs.append(root.val)
        root = root.next

    print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test([1, 2, 3, 4, 7, 8], [2, 1, 4, 3, 8, 7])
    test([1, 2, 3, 4, 7], [2, 1, 4, 3, 7])


if __name__ == '__main__':
    main()
