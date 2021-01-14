# -*- encoding: utf-8 -*-
"""
@file: myCircularDeque.py
@time: 2020/8/31 上午9:41
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 641.设计实现双端队列。
你的实现需要支持以下操作：

MyCircularDeque(k)：构造函数,双端队列的大小为k。

insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
isEmpty()：检查双端队列是否为空。
isFull()：检查双端队列是否满了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-circular-deque/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china
"""


class MyCircularDeque(object):
    """
    使用数组 + 双指针的方式。为避免数据搬移操作，设计为循环队列。规定队空和队满条件
    # 队空条件：head == tail
    # 队满条件：(tail + 1) % k == head
    """

    def __init__(self, k):
        # 循环队列会浪费一个单位的存储空间。所以 K + 1
        self.k = k + 1
        self.queue = [None] * self.k
        self.head, self.tail = 0, 0

    def insert_front(self, value):
        """
        先更新 head， 后插入值。
        :param value: (int, mandatory)
        :return: (bool)
        """
        if self.is_full():
            return False
        self.head = (self.head - 1) % self.k
        self.queue[self.head] = value
        return True

    def insert_last(self, value):
        """
        先插入值，后更新 tail。
        :param value: (int, mandatory)
        :return: (bool)
        """
        if self.is_full():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        return True

    def delete_front(self):
        """
        :return: (bool)
        """
        if self.is_empty():
            return False
        self.head = (self.head + 1) % self.k
        return True

    def delete_last(self):
        """
        :return: (bool)
        """
        if self.is_empty():
            return False
        self.tail = (self.tail - 1) % self.k
        return True

    def get_front(self):
        """
        :return: (int)
        """
        if self.is_empty():
            return -1
        return self.queue[self.head]

    def get_rear(self):
        """
        :return: (int)
        """
        if self.is_empty():
            return -1
        return self.queue[(self.tail - 1) % self.k]

    def is_empty(self):
        """
        :return: (bool)
        """
        return self.head == self.tail

    def is_full(self):
        """
        :return: (bool)
        """
        return (self.tail + 1) % self.k == self.head


def main():
    queue = MyCircularDeque(5)

    assert queue.insert_front(1) is True
    assert queue.insert_front(2) is True
    assert queue.insert_last(3) is True
    assert queue.insert_last(4) is True
    assert queue.insert_last(5) is True
    assert queue.insert_last(6) is False

    assert queue.get_front() == 2
    assert queue.get_rear() == 5
    assert queue.delete_last() is True
    assert queue.delete_front() is True
    assert queue.get_front() == 1
    assert queue.get_rear() == 4

    assert queue.delete_front() is True
    assert queue.get_front() == 3

    assert queue.delete_last() is True
    assert queue.get_rear() == 3

    assert queue.insert_front(7) is True
    assert queue.get_rear() == 3
    assert queue.get_front() == 7

    print("The test passed")


if __name__ == '__main__':
    main()
