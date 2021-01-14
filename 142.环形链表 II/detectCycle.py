# -*- encoding: utf-8 -*-
"""
@file: detectCycle.py
@time: 2020/8/17 下午2:47
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 142.环形链表 II

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

example：
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
"""


class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next


def detect_cycle1(head):
    """
    哈希表。时间复杂度: O(N), 空间复杂度：O(N)
    :param head: (Node)
    :return: (Node)
    """
    if not isinstance(head, Node):
        return None

    curl, linked_list = head, []
    while curl.next:
        if curl in linked_list:
            return curl
        linked_list.append(curl)
        curl = curl.next

    return None


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


def main():
    head = create_one_way_cycle_linked([1, 2, 3, 4, 5], 1)
    result = detect_cycle1(head)
    print("tail connects to node index : ", result)


if __name__ == '__main__':
    main()
