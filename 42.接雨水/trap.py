# -*- encoding: utf-8 -*-
"""
@file: trap.py
@time: 2020/9/1 上午9:29
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 42.接雨水

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）.

example:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
"""


def trap1(height):
    """
    双指针。使用左右累积的方式实现(1)。时间复杂度 O(n), 空间复杂度 O(1)
    :param height: (list)
    :return: (int)
    """
    n = len(height)
    max_left, max_right = 0, 0
    left, right = 0, n - 1
    result = 0

    # 终止条件
    while left < right:
        # 如果左边的高度小于右边的高度，则更新左边
        if height[left] < height[right]:
            # 如果当前的高度大于最大值，则说明是递增趋势，更新最大值
            if height[left] >= max_left:
                max_left = height[left]
            else:
                result += max_left - height[left]
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                result += max_right - height[right]
            right -= 1

    return result


def trap2(height):
    """
    双指针。使用左右累积的方式实现(2)。时间复杂度 O(n), 空间复杂度 O(1)
    :param height: (list)
    :return: (int)
    """
    n = len(height)
    left, right = 0, n - 1
    max_left, max_right = 0, 0
    result = 0

    while left <= right:
        max_left = max(max_left, height[left])
        max_right = max(max_right, height[right])
        if max_left < max_right:
            result += max_left - height[left]
            left += 1
        else:
            result += max_right - height[right]
            right -= 1
    return result


def trap(height):
    """
    使用单调栈的方法。时间复杂度为 O(N)
    解题方法与 84.柱状图中的最大面积。相似。
    :param height: (list[int])
    :return: (int)
    """
    size = len(height)
    stack = []
    answer = 0
    for i in range(size):
        while stack and height[stack[-1]] < height[i]:
            top = stack[-1]
            stack.pop()
            if not stack or len(stack) == 0:
                break

            # 左边界 和 右边界
            left = stack[-1]
            right = i

            # 计算宽度和高度。
            width = min(height[left], height[right]) - height[top]
            answer += (right - left - 1) * width
        stack.append(i)
    return answer


def main():
    inputs = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    outputs = trap(inputs)
    answer = 6
    assert outputs == answer, print("Inputs:{}, Output:{}, Except:{}".format(inputs, outputs, answer))

    inputs = [4, 2, 3]
    outputs = trap(inputs)
    answer = 1
    assert outputs == answer, print("Inputs:{}, Output:{}, Except:{}".format(inputs, outputs, answer))
    print("The test passed")


if __name__ == '__main__':
    main()
