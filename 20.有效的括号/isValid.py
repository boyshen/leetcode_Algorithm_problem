# -*- encoding: utf-8 -*-
"""
@file: isValid.py
@time: 2020/8/17 下午5:56
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  20.有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

example:
    输入: "()"
    输出: true

    输入: "()[]{}"
    输出: true

    输入: "(]"
    输出: false

    输入: "([)]"
    输出: false

解题：
    1. 使用栈方法实现。如果匹配到 '(',  '[',  '{' 则入栈，没有匹配到，则根据结果取栈顶元素进行匹配。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses/
"""


def is_valid(s):
    """
    栈实现。时间复杂度: O(N), 空间复杂度: O(N + M) M 为字符集个数
    :param s: (str)
    :return: (bool)
    """
    stack = []
    matching_str = {'(': ')', '{': '}', '[': ']'}

    for string in list(s):
        # 匹配元素是不是 '(',  '[',  '{'
        if string in matching_str.keys():
            stack.append(string)
        # 如果栈为空，且有输入元素，则返回False
        elif not stack:
            return False
        # 如果栈不为空，则取与栈顶元素相匹配的元素 与 字符元素进行比较。如果不等则返回 False
        elif stack and string != matching_str[stack.pop()]:
            return False

    return not stack


def main():
    inputs = ["()", "()[]{}", "(]", "([)]", "]"]
    answer = [True, True, False, False, False]
    for i, string in enumerate(inputs):
        outputs = is_valid(string)
        print("Input:{}, Output:{}, Except:{}".format(string, outputs, answer[i]))
        assert outputs == answer[i], print("Answer Failed")


if __name__ == '__main__':
    main()
