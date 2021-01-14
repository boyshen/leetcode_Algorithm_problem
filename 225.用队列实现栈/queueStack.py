# -*- encoding: utf-8 -*-
"""
@file: queueStack.py
@time: 2020/8/18 下午2:18
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 225. 用队列实现栈
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-stack-using-queues
"""


class QueueStack(object):
    def __init__(self):
        self.queue = list()

    def push(self, x):
        self.queue.append(x)
        return None

    def pop(self):
        if self.queue:
            return self.queue.pop()
        return None

    def top(self):
        if self.queue:
            return self.queue[-1]
        return None

    def empty(self):
        """
        返回栈是否为空。 空栈返回 True， 非空返回 False
        :return: (bool)
        """
        if self.queue:
            return False
        return True


def main():
    stack = QueueStack()
    stack.push(1)
    stack.push(2)
    print("stack pop: ", stack.pop())
    print("stack top: ", stack.top())
    print("stack empty: ", stack.empty())


if __name__ == '__main__':
    main()
