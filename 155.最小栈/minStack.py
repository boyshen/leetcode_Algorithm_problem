# -*- encoding: utf-8 -*-
"""
@file: minStack.py
@time: 2020/8/30 下午5:01
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 155.最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

example:
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack
"""


class MinStack(object):
    """
    建立两个栈。一个常数栈，一个最小栈。常数栈：保存添加的数据。155.最小栈：跟随常数栈保存最小的元素。
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if self.min_stack:
            self.min_stack.append(min(x, self.min_stack[-1]))
        else:
            self.min_stack.append(x)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


def main():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    outputs = min_stack.get_min()
    assert outputs == -3, print("Output:{}, Except:{}".format(outputs, -3))

    min_stack.pop()
    outputs = min_stack.top()
    assert outputs == 0, print("Output:{}, Except:{}".format(outputs, 0))

    outputs = min_stack.get_min()
    assert outputs == -2, print("Output:{}, Except:{}".format(outputs, -2))

    print("The test passed")


if __name__ == '__main__':
    main()
