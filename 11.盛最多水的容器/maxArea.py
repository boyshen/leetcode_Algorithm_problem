# -*- encoding: utf-8 -*-
"""
@file: maxArea.py
@time: 2020/8/27 下午4:28
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 11.盛最多水的容器

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

example:
输入：[1,8,6,2,5,4,8,3,7]
输出：49

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
"""


def max_area1(height):
    """
    暴力法。时间复杂度 O(n^2), 空间复杂度 O(1)
    :param height: (list, mandatory)
    :return: (int)
    """
    max_val = 0
    for i in range(1, len(height)):
        for j in range(i):
            area = min(height[j], height[i]) * (i - j)
            max_val = max(area, max_val)
    return max_val


def max_area(height):
    """
    双指针。时间复杂度 O(n), 空间复杂度 O(1)
    两步夹逼的方法。由左右两步的元素依次向中间逼近
    :param height: (list, mandatory)
    :return: (int)
    """
    max_val = 0
    i, j = 0, len(height) - 1
    while i < j:
        area = min(height[i], height[j]) * (j - i)
        max_val = max(area, max_val)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_val


def test(height, answer):
    outputs = max_area(height)
    print("Inputs:{}, Outputs:{}, Except:{}".format(height, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    output = 49
    test(height, output)

    height = [1, 2]
    output = 1
    test(height, output)


if __name__ == '__main__':
    main()
