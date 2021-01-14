# -*- encoding: utf-8 -*-
"""
@file: getLeastNumbers.py
@time: 2020/9/4 下午6:00
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 剑指 Offer 40. 最小的k个数

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

example:
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof

"""

from queue import PriorityQueue


def get_least_numbers(arr, k):
    """
    使用优先队列
    :param arr: (list)
    :param k: (int)
    :return: (list)
    """
    priority_queue = PriorityQueue()
    for x in arr:
        priority_queue.put(x)

    res = [priority_queue.get() for _ in range(k)]
    return res


def main():
    inputs, k = [3, 2, 1], 2
    answer = [1, 2]
    outputs = get_least_numbers(inputs, k)
    assert sorted(outputs) == answer, print("Inputs:{},{}, Outputs:{}, Except:{}".format(inputs, k, outputs, answer))

    inputs, k = [2, 1], 2
    answer = [1, 2]
    outputs = get_least_numbers(inputs, k)
    assert sorted(outputs) == answer, print("Inputs:{},{}, Outputs:{}, Except:{}".format(inputs, k, outputs, answer))

    inputs, k = [1, 6], 1
    answer = [1]
    outputs = get_least_numbers(inputs, k)
    assert sorted(outputs) == answer, print("Inputs:{},{}, Outputs:{}, Except:{}".format(inputs, k, outputs, answer))

    inputs, k = [0, 1, 2, 1], 1
    answer = [0]
    outputs = get_least_numbers(inputs, k)
    assert sorted(outputs) == answer, print("Inputs:{},{}, Outputs:{}, Except:{}".format(inputs, k, outputs, answer))

    inputs, k = [4, 5, 1, 6, 2, 7, 3], 4
    answer = [1, 2, 3, 4]
    outputs = get_least_numbers(inputs, k)
    assert sorted(outputs) == answer, print("Inputs:{},{}, Outputs:{}, Except:{}".format(inputs, k, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
