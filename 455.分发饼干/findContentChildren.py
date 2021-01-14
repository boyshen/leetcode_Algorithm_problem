# -*- encoding: utf-8 -*-
"""
@file: findContentChildren.py
@time: 2020/9/20 下午6:20
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 455.分发饼干

假设你是一位很棒的家长，想要给你的孩子们一些小饼干。
但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。
如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

注意：
你可以假设胃口值为正。∂
一个小朋友最多只能拥有一块饼干。

示例 1:
输入: [1,2,3], [1,1]
输出: 1
解释:
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。

示例 2:
输入: [1,2], [1,2,3]
输出: 2
解释:
你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/assign-cookies
"""


def find_content_children(g, s):
    """
    贪心。时间复杂度 O(nlogn) nlogn 为排序需要的时间复杂度
         空间复杂度为 O(g + s) g + s 为排序之后需要对 g 和 s排序的结果进行保存
    :param g: (list[int])
    :param s: (list[int])
    :return: (int)
    """
    g = sorted(g)
    s = sorted(s)

    count = 0
    i, j = 0, 0
    while i < len(s) and j < len(g):
        if s[i] >= g[j]:
            count += 1
            i += 1
            j += 1
        else:
            i += 1

    return count


def test(g, s, answer):
    outputs = find_content_children(g, s)
    print("Inputs:g={},s={}, Outputs:{}, Except:{}".format(g, s, outputs, answer))
    assert outputs == answer, print("Inputs:g={},s={}, Outputs:{}, Except:{}".format(g, s, outputs, answer))


def main():
    g, s, answer = [1, 2, 3], [1, 1], 1
    test(g, s, answer)

    g, s, answer = [1, 2], [1, 2, 3], 2
    test(g, s, answer)


if __name__ == '__main__':
    main()
