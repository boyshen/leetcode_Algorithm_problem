# -*- encoding: utf-8 -*-
"""
@file: letterCombinations.py
@time: 2020/9/14 下午4:48
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  17.电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
"""


def letter_combinations(digits):
    """
    回溯. 时间复杂度 (3^m * 4^n) m 对应输入 3 个字符的数字。n 对应输入 4 个字符的数字
    空间复杂度 (m + n)
    :param digits: (str)
    :return: (list)
    """
    if not digits:
        return []

    letters = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    res = []

    def helper(i, combine):
        if i == len(digits):
            res.append(combine)
            return

        for char in letters[int(digits[i])]:
            helper(i + 1, combine + char)

    helper(0, "")
    return res


def removal(data):
    """ 去重 """
    res = []
    for val in data:
        if val in res:
            continue
        res.append(val)
    return res


def main():
    inputs = "23"
    outputs = removal(letter_combinations(inputs))
    answer = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print(outputs)
    assert len(outputs) == len(answer), print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    for output in outputs:
        assert output in answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))

    print("The test passed")


if __name__ == '__main__':
    main()
