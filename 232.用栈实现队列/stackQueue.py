# -*- encoding: utf-8 -*-
"""
@file: stackQueue.py
@time: 2020/8/18 上午11:33
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 232. 用栈实现队列

使用栈实现队列的下列操作：
push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。

example:
MyQueue 703.数据流中的第 K 大元素 = new MyQueue();
703.数据流中的第 K 大元素.push(1);
703.数据流中的第 K 大元素.push(2);
703.数据流中的第 K 大元素.peek();  // 返回 1
703.数据流中的第 K 大元素.pop();   // 返回 1
703.数据流中的第 K 大元素.empty(); // 返回 false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
"""


class StackQueue(object):
    """
    使用栈实现队列。基本思想：设计两个 stack 。
    """

    def __init__(self):
        self.stack_input = list()
        self.stack_output = list()

    def push(self, x):
        """
        添加一个元素到队列。
        :param x: (int, mandatory) 入栈
        :return: None
        """
        self.stack_input.append(x)
        return None

    def pop(self):
        """
        从队列首部移除元素。
        :return: (int) 元素 或 None
        """
        # 如果 stack_output 非空，则直接取出栈顶元素
        if self.stack_output:
            return self.stack_output.pop()
        elif self.stack_input:
            # 将 stack_input 里的数据 pop 取出放到 stack_output 栈中。并返回栈顶元素
            while self.stack_input:
                self.stack_output.append(self.stack_input.pop())
            return self.stack_output.pop()
        return None

    def peek(self):
        """
        返回队列首部元素
        :return: (int)
        """
        if self.stack_output:
            return self.stack_output[-1]
        elif self.stack_input:
            while self.stack_input:
                self.stack_output.append(self.stack_input.pop())
            return self.stack_output[-1]

    def empty(self):
        """
        判断是否为空队列
        :return: (bool). 空队列返回 True，非空队列返回 False
        """
        if self.stack_input or self.stack_output:
            return False
        else:
            return True


def main():
    queue = StackQueue()
    queue.push(1)
    queue.push(2)
    print("703.数据流中的第 K 大元素 peek: ", queue.peek())
    print("703.数据流中的第 K 大元素 pop: ", queue.pop())
    print("empty: ", queue.empty())


if __name__ == '__main__':
    main()
