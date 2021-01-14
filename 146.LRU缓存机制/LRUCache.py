# -*- encoding: utf-8 -*-
"""
@file: LRUCache.py
@time: 2020/8/26 下午3:24
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 146.LRU缓存机制
设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

example：
LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得关键字 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得关键字 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
"""


class DoubleLinkedList(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache1(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.obj_dict = dict()

        # 头尾节点，哨兵
        self.head = DoubleLinkedList(None, None)
        self.tail = DoubleLinkedList(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.obj_dict:
            node = self.obj_dict[key]
            self._move(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.obj_dict:
            node = self.obj_dict[key]
            node.val = value
            self._move(node)

        elif len(self.obj_dict) == self.capacity:
            # 获取最后一个节点, 并在字典中删除该元素
            node = self.tail.prev
            self.obj_dict.pop(node.key)

            # 修改节点值、重新将节点加入到字典中
            node.key, node.val = key, value
            self.obj_dict[key] = node

            # 移动节点到 head
            self._move(node)

        else:
            node = DoubleLinkedList(key, value)
            self.obj_dict[key] = node
            self._add(node)

        return None

    def _move(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node
        temp = self.head.next
        self.head.next, node.prev = node, self.head
        node.next, temp.prev = temp, node

    def _add(self, node):
        head_next = self.head.next
        self.head.next, node.prev = node, self.head
        head_next.prev, node.next = node, head_next


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = {}

        # 哨兵
        self.head = DoubleLinkedList(None, None)
        self.tail = DoubleLinkedList(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.table:
            node = self.table[key]
            self._move(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.table:
            node = self.table[key]
            node.val = value
            self._move(node)

        elif len(self.table) == self.capacity:
            node = self.tail.prev
            # 删除
            self.table.pop(node.key)
            self.tail.prev = node.prev
            node.prev.next = self.tail

            # 更新
            node.key = key
            node.val = value
            self.table[key] = node
            self._add(node)
        else:
            node = DoubleLinkedList(key, value)
            self._add(node)
            self.table[key] = node

    def _move(self, node):
        prev_node, tail_node = node.prev, node.next
        prev_node.next = tail_node
        tail_node.prev = prev_node

        temp = self.head.next
        self.head.next, node.prev = node, self.head
        temp.prev, node.next = node, temp

    def _add(self, node):
        temp = self.head.next
        self.head.next, node.prev = node, self.head
        node.next, temp.prev = temp, node


def main():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache = LRUCache(1)
    assert cache.get(0) == -1
    cache.put(1, 1)
    assert cache.get(1) == 1

    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    assert cache.get(1) == -1
    assert cache.get(2) == 3

    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)

    result = cache.get(4)
    assert result == 4, print("Except: {}, actual: {}".format(4, result))
    result = cache.get(3)
    assert result == 3, print("Except: {}, actual: {}".format(3, result))
    result = cache.get(2)
    assert result == 2, print("Except: {}, actual: {}".format(2, result))
    result = cache.get(1)
    assert result == -1, print("Except: {}, actual: {}".format(-1, result))

    cache.put(5, 5)
    result = cache.get(1)
    assert result == -1, print("Except: {}, actual: {}".format(-1, result))
    result = cache.get(2)
    assert result == 2, print("Except: {}, actual: {}".format(2, result))
    result = cache.get(3)
    assert result == 3, print("Except: {}, actual: {}".format(3, result))
    result = cache.get(4)
    assert result == -1, print("Except: {}, actual: {}".format(-1, result))
    result = cache.get(5)
    assert result == 5, print("Except: {}, actual: {}".format(5, result))

    print("test ok")


if __name__ == '__main__':
    main()
