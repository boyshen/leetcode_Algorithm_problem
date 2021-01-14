# -*- encoding: utf-8 -*-
"""
@file: searchMatrix.py
@time: 2020/9/20 下午11:20
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  74. 搜索二维矩阵

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

示例 1:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true

示例 2:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
"""


def search_matrix1(matrix, target):
    """
    二分法
    :param matrix: (list[list[int]])
    :param target: (int)
    :return: (int)
    """
    if not matrix or not matrix[0]:
        return False

    low, height = 0, len(matrix) - 1
    while low <= height:
        mid = int(low + (height - low) / 2)
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            return search(matrix[mid], target)
        elif matrix[mid][0] > target:
            height = mid - 1
        elif matrix[mid][-1] < target:
            low = mid + 1
    return False


def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def search_matrix(matrix, target):
    """
    二分法查找。输入的 m x n 矩阵可以视为长度为 m x n的有序数组
    row = mid // n, column = mid % n
    :param matrix: (list[list[int]])
    :param target: (int)
    :return: (bool)
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // n][mid % n]
        if value == target:
            return True
        elif target < value:
            right = mid - 1
        else:
            left = mid + 1

    return False


def test(matrix, target, answer):
    outputs = search_matrix(matrix, target)
    print("Inputs:nums={},target={}, Outputs:{}, Except:{}".format(matrix, target, outputs, answer))
    assert outputs == answer, print("Answer failed")


def main():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target, answer = 3, True
    test(matrix, target, answer)

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target, answer = 13, False
    test(matrix, target, answer)

    matrix = [
        [1, 3]
    ]
    target, answer = 3, True
    test(matrix, target, answer)


if __name__ == '__main__':
    main()
