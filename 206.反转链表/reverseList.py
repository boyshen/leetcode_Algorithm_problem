# -*- encoding: utf-8 -*-
"""
@file: reverseList.py
@time: 2020/8/13 下午4:14
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 206.反转链表

输入：1->2->3->4->5->NULL
输出：5->4->3->2->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
"""


class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next


def reverse_linked1(head):
    """
    输入：1->2->3->4->5->NULL
    输出：5->4->3->2->1->NULL

    解题思路：
        将 1->2->3->4->5->NULL 的指针改为： NULL<-1<-2<-3<-4<-5 时间复杂度 O(n)
        返回节点值为5的Node对象地址
    :param head: (Node, mandatory)
    :return: (Node)
    """
    curl, prev = head, None
    while curl:
        curl.next, prev, curl = prev, curl, curl.next
    return prev


def reverse_linked(head):
    """
    :param head: (Node)
    :return: (Node)
    """
    curl, prev = head, None
    while curl:
        # 保存当前节点的指针
        temp = curl.next
        # 修改当前指针指向上一个节点
        curl.next = prev
        # 更新上一个节点为当前节点
        prev = curl
        # 循环
        curl = temp
    return prev


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
    head = create_one_way_linked([1, 2, 3, 4, 5, 7])
    tail = reverse_linked(head)
    outputs = []
    while tail:
        outputs.append(tail.val)
        tail = tail.next

    print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test([1, 2, 3, 4, 5, 7], [7, 5, 4, 3, 2, 1])


if __name__ == "__main__":
    main()
