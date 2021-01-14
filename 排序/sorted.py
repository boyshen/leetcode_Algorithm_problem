# -*- encoding: utf-8 -*-
"""
@file: sorted.py
@time: 2020/10/25 下午7:09
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  相关排序算法实现
"""
import copy
import heapq
from queue import PriorityQueue


def selection_sorted(arr):
    """
    选择排序. 时间复杂度 O(n^2), 空间复杂度 O(1), 不稳定
    :param arr: (list[int])
    :return: (list[int])
    """
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sorted(arr):
    """
    插入排序。时间复杂度 O(n^2), 空间复杂度 O(1),
    :param arr: (list[int])
    :return: (list[int])
    """
    length = len(arr)
    for i in range(1, length):
        pre_index = i - 1
        temp = arr[i]
        while pre_index >= 0 and arr[pre_index] > temp:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = temp
    return arr


def bubble_sorted(arr):
    """
    冒泡排序. 时间复杂度 O(n^2), 空间复杂度 O(1), 稳定排序
    :param arr: (list[int])
    :return: (list[int])
    """
    length = len(arr)
    for i in range(length):
        for j in range(length):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def quick_sorted(arr, begin, end):
    """
    快速排序。时间复杂度 O(nlogn), 空间复杂度 O(nlogn), 不稳定
    :param arr: (list[int])
    :param begin: (int)
    :param end: (int)
    :return:
    """
    if begin >= end:
        return

    pivot = partition(arr, begin, end)
    quick_sorted(arr, begin, pivot - 1)
    quick_sorted(arr, pivot + 1, end)


def partition(arr, begin, end):
    pivot = arr[begin]
    mask = begin
    # begin + 1 ==> 从下一个元素和 pivot 进行比较。
    # end + 1 ==> 需要比较到 end 整个元素
    for i in range(begin + 1, end + 1):
        if arr[i] < pivot:
            mask += 1
            # 小于标杆的元素都移动到左边
            arr[i], arr[mask] = arr[mask], arr[i]
    arr[mask], arr[begin] = arr[begin], arr[mask]

    return mask


def heap_sorted1(arr):
    """
    堆排序。时间复杂度 O(nlogn), 空间复杂度 O(n), 不稳定
    :param arr: (list[int])
    :return: (list[int])
    """
    p_queue = PriorityQueue()
    length = len(arr)
    for i in range(length):
        p_queue.put(arr[i])

    for i in range(length):
        arr[i] = p_queue.get()


def heap_sorted2(arr):
    """
    堆排序。时间复杂度 O(nlogn), 空间复杂度 O(n), 不稳定
    :param arr: (list[int])
    :return: (list[int])
    """
    heap = []
    length = len(arr)
    for i in range(length):
        heapq.heappush(heap, arr[i])
    return [heapq.heappop(heap) for _ in range(length)]


def merge_sorted(arr, left, right):
    """
    归并排序。时间复杂度 O(nlogn), 空间复杂度 O(n), 稳定
    :param arr: (list[int])
    :param left: (int)
    :param right: (int)
    :return:
    """
    if left >= right:
        return
    mid = (left + right) >> 1
    merge_sorted(arr, left, mid)
    merge_sorted(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    i, j = left, mid + 1
    temp = []
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= right:
        temp.append(arr[j])
        j += 1

    arr[left:right + 1] = temp


def count_sort(arr):
    """
    计数排序。时间复杂度 O(n + k), 空间复杂度 O(n + k), 稳定排序
    :param arr: (list[int])
    :return: (list[int])
    """
    # 查找数据范围，找到最大的值
    max_val = max(arr)

    # 申请计数数组。
    k = max_val + 1
    count = [0] * k

    # 添加数据到数组中
    length = len(arr)
    for i in range(length):
        count[arr[i]] += 1

    # 将排序的数组放到 arr 中
    index = 0
    for i in range(k):
        while count[i] > 0:
            arr[index] = i
            count[i] -= 1
            index += 1
    return arr


def bucket_sort(arr, bucket_size=2):
    """
    桶排序。时间复杂度 O(n), 空间复杂度 O(n+k), 稳定
    :param arr: (list[int])
    :param bucket_size: (int)
    :return: (list[int])
    """
    # 找到数据的最大值和最小值。
    min_val = min(arr)
    max_val = max(arr)

    # 初始化桶数量
    bucket_count = (max_val - min_val) // bucket_size + 1
    bucket = [[] for _ in range(bucket_count)]

    # 将数据加入桶
    length = len(arr)
    for i in range(length):
        bucket[(arr[i] - min_val) // bucket_size].append(arr[i])

    arr = []
    for i in range(bucket_count):
        # 先对每个桶内数据进行排序
        sort_bucket = sorted(bucket[i])
        for x in sort_bucket:
            arr.append(x)
    return arr


def test(operation):
    arr = [1, 3, 2, 4, 6, 7, 5, 8, 9, 0]
    outputs = None

    if operation == selection_sorted.__name__:
        outputs = selection_sorted(copy.deepcopy(arr))
    elif operation == insertion_sorted.__name__:
        outputs = insertion_sorted(copy.deepcopy(arr))
    elif operation == bubble_sorted.__name__:
        outputs = bubble_sorted(copy.deepcopy(arr))
    elif operation == quick_sorted.__name__:
        outputs = copy.deepcopy(arr)
        quick_sorted(outputs, 0, len(outputs) - 1)
    elif operation == merge_sorted.__name__:
        outputs = copy.deepcopy(arr)
        merge_sorted(outputs, 0, len(outputs) - 1)
    elif operation == heap_sorted1.__name__:
        outputs = copy.deepcopy(arr)
        heap_sorted1(outputs)
    elif operation == heap_sorted2.__name__:
        outputs = copy.deepcopy(arr)
        outputs = heap_sorted2(outputs)
    elif operation == count_sort.__name__:
        arr = [1, 3, 2, 4, 6, 7, 5, 8, 9, 0, 2, 3, 4, 4, 5, 6, 3, 8, 9, 0]
        outputs = count_sort(arr)
    elif operation == bucket_sort.__name__:
        arr = [1, 3, 2, 4, 6, 7, 5, 8, 9, 0, 2, 3, 4, 4, 5, 6, 3, 8, 9, 0]
        outputs = bucket_sort(arr)

    print(outputs)


def main():
    # test(selection_sorted.__name__)
    # test(insertion_sorted.__name__)
    # test(bubble_sorted.__name__)
    # test(quick_sorted.__name__)
    # test(merge_sorted.__name__)
    # test(heap_sorted1.__name__)
    # test(heap_sorted2.__name__)
    # test(count_sort.__name__)
    test(bucket_sort.__name__)


if __name__ == '__main__':
    main()
