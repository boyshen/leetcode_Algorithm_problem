# -*- encoding: utf-8 -*-
"""
@file: hasCycle.py
@time: 2020/8/14 上午11:29
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 141.环形链表

给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
"""


class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next


def has_cycle1(head):
    """
    快慢指针实现, 通过快慢指针判断是否有环。时间复杂度 O(n)，空间复杂度：O(1)
    :param head: (Node)
    :return: (bool)
    """
    if head is None or head.next is None:
        return False

    fast = head.next
    slow = head

    while fast != slow:
        if fast is None or fast.next is None:
            return False
        fast = fast.next.next
        slow = slow.next
    return True


def has_cycle(head):
    """
    通过哈希实现。时间复杂度 O(n), 空间复杂度 O(n)
    :param head: (Node)
    :return: (bool)
    """

    table = set()
    curl = head
    while curl:
        if curl in table:
            return True

        table.add(curl)
        curl = curl.next
    return False


def create_one_way_cycle_linked(value, pos=-1):
    """
    创建单向有环链表
    :param value: (list, mandatory) 列表元素
    :param pos: (int) 使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环
    :return: (Node) 头节点对象
    """
    if pos > len(value) - 1:
        print("Pos value greater than linked list index value")
        return False

    cycle_linked = [Node(v, None) for v in value]
    head = cycle_linked[0]
    shifting = cycle_linked[0]
    for node in cycle_linked[1:]:
        shifting.next = node
        shifting = node

    temp = head
    index = 0
    while temp:
        if index == pos:
            shifting.next = temp
            break
        temp = temp.next
        index = index + 1

    return head


def test(inputs, pos, answer):
    head = create_one_way_cycle_linked(inputs, pos)
    outputs = has_cycle(head)
    print("Inputs:nums={}, pos={}, Outputs:{}, Except:{}".format(inputs, pos, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test([1, 2, 3, 4, 5], 3, True)


if __name__ == '__main__':
    main()
