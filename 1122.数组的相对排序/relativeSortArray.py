# -*- encoding: utf-8 -*-
"""
@file: relativeSortArray.py
@time: 2020/10/28 下午2:10
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  1122.1122.数组的相对排序

给你两个数组，arr1 和 arr2，
arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

示例：
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]

提示：
arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-sort-array/
"""


def relative_sort_array(arr1, arr2):
    """
    排序
    :param arr1: (list[int])
    :param arr2: (list[int])
    :return: (list[int])
    """

    count = {}
    for val in arr1:
        count[val] = count.get(val, 0) + 1

    res = []
    for val in arr2:
        if val in count:
            res += [val] * count.pop(val)

    for val in sorted(count.keys()):
        res += [val] * count.pop(val)

    return res


def test(arr1, arr2, answer):
    outputs = relative_sort_array(arr1, arr2)
    print("Inputs:arr1={}, arr2={}, Outputs:{}, Except:{}".format(arr1, arr2, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6], [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19])


if __name__ == '__main__':
    main()
