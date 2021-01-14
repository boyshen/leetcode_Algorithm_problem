# -*- encoding: utf-8 -*-
"""
@file: kthLargest.py
@time: 2020/8/18 下午3:46
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 703.数据流中的第 K 大元素

设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。
KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。
每次调用 KthLargest.add，返回当前数据流中第K大的元素。

example:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream

解题：
    1. 使用排序sorted方法。对输入序列进行从大到小的排序。 取排序后 k 对应的值返回。时间复杂度为 O(KlogK)
    2. 使用优先队列 min 347.前K个高频元素 的方法。维护 k 个数据。其中优先级最高的元素为值最小的元素。 也就是需要的提取的 K 值。使用 add 时候，有两种情况：
        a. 当 add(n) n 小于优先队列中优先级最高的元素时候。队列不变，返回原来的 k。时间复杂度为 O(1)
        b. 当 add(n) n 大于优先队列中优先级最高的元素时候。则移处队列中优先级最高的元素。将 n 加入队列，重新获取高优先级元素。时间复杂度 O(k)
"""

import queue


class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums

        # 使用优先队列实现。
        self.priority_queue = queue.PriorityQueue(self.k)
        for x in self.nums:
            if self.priority_queue.qsize() == self.k:
                value = self.priority_queue.get()
                if value < x:
                    self.priority_queue.put(x)
                else:
                    self.priority_queue.put(value)
            else:
                self.priority_queue.put(x)

    def add(self, n):
        # 如果队列大小 小于 k， 则向队列添加元素
        if self.priority_queue.qsize() < self.k:
            self.priority_queue.put(n)
            final_value = self.priority_queue.get()
            self.priority_queue.put(final_value)

        else:
            value = self.priority_queue.get()
            if value < n:
                self.priority_queue.put(n)
            else:
                self.priority_queue.put(value)
            final_value = self.priority_queue.get()
            self.priority_queue.put(final_value)

        return final_value


def main():
    k = 3
    nums = [4, 5, 8, 2]
    kth_largest = KthLargest(k, nums)

    test = [3, 5, 10, 9, 4]
    for x in test:
        value = kth_largest.add(x)
        print("k={}, nums={}, n={}, value={}".format(k, nums, x, value))

    k = 1
    nums = []
    kth_largest = KthLargest(k, nums)

    test = [-3, -2, -4, 0, 4]
    for x in test:
        value = kth_largest.add(x)
        print("k={}, nums={}, n={}, value={}".format(k, nums, x, value))

    k = 3
    nums = [5, -1]
    kth_largest = KthLargest(k, nums)

    test = [2, 1, -1, 3, 4]
    for x in test:
        value = kth_largest.add(x)
        print("k={}, nums={}, n={}, value={}".format(k, nums, x, value))


if __name__ == '__main__':
    main()
