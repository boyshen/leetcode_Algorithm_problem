# -*- encoding: utf-8 -*-
"""
@file: toLowerCase.py
@time: 2020/11/1 下午4:26
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  709.709.转换成小写字母

实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

示例 1：

输入: "Hello"
输出: "hello"
示例 2：

输入: "here"
输出: "here"
示例 3：

输入: "LOVELY"
输出: "lovely"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/to-lower-case/
"""


def to_lower_case(str):
    """
    :param str: (str)
    :return: (str)
    """

    res = []
    for s in str:
        if 'A' <= s <= 'Z':
            res.append(chr(ord(s) + 32))
        else:
            res.append(s)

    return ''.join(res)


def test(str, answer):
    outputs = to_lower_case(str)
    print("Inputs:{}, Outputs:{}, Except:{}".format(str, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test("Hello", "hello")
    test("here", "here")
    test("LOVELY", "lovely")


if __name__ == '__main__':
    main()
