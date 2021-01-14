# -*- encoding: utf-8 -*-
"""
@file: search2.py
@time: 2020/9/23 下午3:36
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  二分法查找进阶。

查找有序数据中存在重复的数据。
1. 查找等于给定值元素的第一个值下标。
    例如：
    输入：arr = [1,2,3,4,5,6,7,8,8,8,9]，value = 8
    输出： 7
    解释：数组中第一个等于 8 的元素下标是 7

2. 查找等于给定值的最后一个值下标。
    例如：
    输入：arr = [1,2,3,4,5,6,7,8,8,8,9]，value = 8
    输出： 9
    解释：数组中最后一个等于 8 的元素下标是 9

3. 查找第一个大于给定值的元素
    例如：
    输入：arr = [3,4,6,7,10]，value = 5
    输出： 6
    解释：数组中第一个大于给定值元素是 6

4. 查找最后一个小于给定值的元素
    例如：
    输入：arr = [3,5,6,8,9,10]，value = 7
    输出： 6
    解释：数组中最后一个小于给定值的元素是 6
"""


def search1(arr, value):
    """
    查找等于给定值元素的第一个值下标。
    :param arr: (list[int])
    :param value: (int)
    :return: (int)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if arr[mid] < value:
            left = mid + 1
        elif arr[mid] > value:
            right = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != value:
                return mid
            else:
                right = mid - 1
    return -1


def search2(arr, value):
    """
    查找等于给定值元素的最后一个值下标。
    :param arr: (list[int])
    :param value: (int)
    :return: (int)
    """
    left, right = 0, len(arr) - 1
    size = len(arr)
    while left <= right:
        mid = int(left + (right - left) / 2)
        if arr[mid] < value:
            left = mid + 1
        elif arr[mid] > value:
            right = mid - 1
        else:
            if mid == size - 1 or arr[mid + 1] != value:
                return mid
            else:
                left = mid + 1
    return -1


def search3(arr, value):
    """
    查找第一个大于给定值的元素
    :param arr: (list[int])
    :param value: (int)
    :return: (int)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if arr[mid] >= value:
            if mid == 0 or arr[mid - 1] < value:
                return arr[mid]
            else:
                right = mid - 1
        else:
            left = mid + 1
    return -1


def search4(arr, value):
    """
    查找最后一个小于给定值的元素
    :param arr: (list[int])
    :param value: (int)
    :return: (int)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if arr[mid] <= value:
            if mid == len(arr) - 1 or arr[mid + 1] > value:
                return arr[mid]
            else:
                left = mid + 1
        else:
            right = mid - 1
    return -1


def test(arr, value, answer, search):
    outputs = None
    if search == search1.__name__:
        outputs = search1(arr, value)
    if search == search2.__name__:
        outputs = search2(arr, value)
    if search == search3.__name__:
        outputs = search3(arr, value)
    if search == search4.__name__:
        outputs = search4(arr, value)

    print("Search:{}, Inputs:arr={},value={}, Outputs:{}, Except:{}".format(search, arr, value, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test([1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9], value=8, answer=7, search=search1.__name__)
    test([1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9], value=8, answer=9, search=search2.__name__)
    test([3, 4, 6, 7, 10], value=5, answer=6, search=search3.__name__)
    test([3, 5, 6, 8, 9, 10], value=7, answer=6, search=search4.__name__)


if __name__ == '__main__':
    main()
