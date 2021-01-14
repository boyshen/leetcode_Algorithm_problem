# -*- encoding: utf-8 -*-
"""
@file: topKFrequent.py
@time: 2020/9/6 下午9:58
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  347.前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
"""
import heapq
from queue import PriorityQueue


class Solution1(object):
    def top_k_frequent(self, nums, k):
        """
        使用堆的方法
        :param nums: (list)
        :param k: (int)
        :return:
        """
        # 统计频率
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        num, counts = [], []
        for x, count in freq.items():
            num.append(x)
            counts.append(count)

        # 创建最小堆
        num_heap, count_heap = self.build_heap(num[:k], counts[:k], k)

        # 使用剩余的count与堆的最小count对比。
        # 如果剩余的count小于堆的count，则忽略。否则更新堆顶，并进行堆化
        for i in range(len(num) - k):
            if count_heap[0] >= counts[i + k]:
                continue
            num_heap[0], count_heap[0] = num[i + k], counts[i + k]
            self.heapify(num_heap, count_heap, k, 0)

        return num_heap

    def build_heap(self, num, counts, n):
        """
        构建最小堆
        :param num: (list)
        :param counts: (list)
        :param n: (int)
        :return: (list, list)
        """
        i = int(n / 2) - 1
        while i >= 0:
            self.heapify(num, counts, n, i)
            i -= 1
        return num, counts

    def heapify(self, num, counts, n, i):
        """
        堆化
        :param num: (list)
        :param counts: (list)
        :param n: (int)
        :param i: (int)
        :return:
        """
        while True:
            min_pos = i
            if i * 2 + 1 < n and counts[i * 2 + 1] < counts[min_pos]:
                min_pos = i * 2 + 1
            if i * 2 + 2 < n and counts[i * 2 + 2] < counts[min_pos]:
                min_pos = i * 2 + 2
            if min_pos == i:
                break
            self.swap(num, counts, i, min_pos)
            i = min_pos

    def swap(self, num, counts, i, j):
        """
        交换元素位置
        :param num: (list)
        :param counts: (list)
        :param i: (int)
        :param j: (int)
        :return:
        """
        temp1, temp2 = num[i], counts[i]
        num[i], counts[i] = num[j], counts[j]
        num[j], counts[j] = temp1, temp2


class Solution2(object):
    def top_k_frequent(self, nums, k):
        """
        使用 PriorityQueue 实现。PriorityQueue 是基于最小堆的优先队列。
        时间复杂度 O(nlogk), 空间复杂度 O(n)
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 1) + 1

        priority_queue = PriorityQueue()
        for num, count in freq.items():
            # 由于这里需要使用的是最大堆，所以将整数转换为负数进行。
            priority_queue.put((-count, num))

        res = [priority_queue.get()[1] for _ in range(k)]
        return res


class Solution(object):
    def top_k_frequent(self, nums, k):
        """
        使用 python 提供的 heapq 堆实现。
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 1) + 1

        heap = []
        # 创建迭代器
        freq = iter(freq.items())
        for i, (num, count) in enumerate(freq):
            heapq.heappush(heap, (count, num))
            if i + 1 == k:
                break

        # 最小堆。使用当前元素count与最小堆元素count进行比较
        # 如果当前元素count比堆顶元素的count大， 则进行更新堆化
        # 否则不处理
        for (num, count) in freq:
            if count > heap[0][0]:
                # 移除堆顶元素
                heapq.heappop(heap)
                # 将新元素加入堆
                heapq.heappush(heap, (count, num))

        return [num for _, num in heap]


def main():
    inputs = [1, 1, 1, 2, 2, 3]
    k = 2
    solution = Solution()
    outputs = solution.top_k_frequent(inputs, k)
    answer = [1, 2]
    assert sorted(outputs) == answer, print(
        "Inputs:nums={}/k={}, Outputs:{}, Except:{}".format(inputs, k, outputs, answer))

    inputs = [1]
    k = 1
    solution = Solution()
    outputs = solution.top_k_frequent(inputs, k)
    answer = [1]
    assert sorted(outputs) == answer, print(
        "Inputs:nums={}/k={}, Outputs:{}, Except:{}".format(inputs, k, outputs, answer))


if __name__ == '__main__':
    main()
