# -*- encoding: utf-8 -*-
"""
@file: largestRectangleArea.py
@time: 2020/8/30 下午10:10
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 84.柱状图中最大的矩形

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

example：
输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
"""


def largest_rectangle_area1(heights):
    """
    单调栈 + 最小常数优化. 时间复杂度：O(N), 空间复杂度：O(N)
    解题思路：
        首先枚举某一根柱子 i 作为高 h = heights[i]；
        随后需要进行向左右两边扩展，使得扩展到的柱子的高度均小于 h。
        即找到左右两侧最近的高度小于 h 的柱子，这样这两根柱子之间的所有柱子高度均小于 h，并且就是 i 能够扩展到的最远范围。

    :param heights:  (list, mandatory)
    :return: (int)
    """
    size = len(heights)
    left, right = [0] * size, [size] * size

    stack = []
    for i in range(size):
        while stack and heights[stack[-1]] > heights[i]:
            right[stack[-1]] = i
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    area = 0
    for i in range(size):
        area = max((right[i] - left[i] - 1) * heights[i], area)

    return area


def largest_rectangle_area(heights):
    """
    单调栈. 时间复杂度：O(N), 空间复杂度：O(N)
    :param heights: (list)
    :return: (int)
    """
    n = len(heights)
    left, right = [0] * n, [0] * n

    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    area = max([(right[i] - left[i] - 1) * heights[i] for i in range(n)]) if n > 0 else 0
    return area


def test(inputs, answer):
    outputs = largest_rectangle_area(inputs)
    print("Inputs:{}, Outputs:{}, Answer:{}".format(inputs, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    inputs = [6, 7, 5, 2, 4, 5, 9, 3, 1]
    answer = 16
    test(inputs, answer)


if __name__ == '__main__':
    main()
