# -*- encoding: utf-8 -*-
"""
@file: merge.py
@time: 2020/10/28 下午3:09
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  56.合并区间

给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

提示：
intervals[i][0] <= intervals[i][1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals/
"""


def merge(intervals):
    """
    排序。 在排完序的列表中，可以合并的区间一定是连续的。

    集合 a 和 集合 b。在排序完之后， a[1] 集合a的第二个元素，b[0] 集合b的第一个元素
    如果：
        a[1] < b[0] 则两个集合不能合并
        a[1] >= b[0] 则两个集合可以合并

    时间复杂度 O(NlogN) 排序需要 NlogN 开销，除去排序开销还需要一次线性遍历
    空间复杂度 O(logN)
    :param intervals: (list[list[int]])
    :return: (list[list[int]])
    """
    intervals.sort(key=lambda x: x[0])

    res = []
    for val in intervals:
        # 如果 res 为空 或 如果 a[1] < b[0] 则两个集合不能合并
        if len(res) == 0 or res[-1][1] < val[0]:
            res.append(val)
        else:
            # 合并集合
            res[-1][1] = max(res[-1][1], val[1])

    return res


def test(intervals, answer):
    outputs = merge(intervals)
    print("Inputs:{}, Outputs:{}, Except:{}".format(intervals, outputs, answer))


def main():
    test([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]])
    test([[1, 4], [4, 5]], [[1, 5]])


if __name__ == '__main__':
    main()
