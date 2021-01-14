# -*- encoding: utf-8 -*-
"""
@file: maxSlidingWindow.py
@time: 2020/8/19 下午12:02
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 239.滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

example:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
"""


def max_sliding_window(nums, k):
    """
    队列。 时间复杂度 O(N), 空间复杂度 O(N)
    :param nums: (list[int])
    :param k: (int)
    :return: (list[int])
    """
    size = len(nums)
    if size * k == 0:
        return []

    if size < k:
        return []

    window, result = [], []
    for i, x in enumerate(nums):
        # 从队列中移除第一个元素
        if i >= k and window[0] == i - k:
            window.pop(0)

        # 利用队列中的元素和新元素比较，如果小于新元素，则将队列中元素出队，将新元素加入队列。
        while window and nums[window[-1]] < x:
            window.pop()
        window.append(i)

        # 保存最大的元素
        if i + 1 >= k:
            result.append(nums[window[0]])

    return result


def main():
    inputs = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    answer = [3, 3, 5, 5, 6, 7]
    outputs = max_sliding_window(inputs, k)
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
