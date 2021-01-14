# -*- encoding: utf-8 -*-
"""
@file: lemonadeChange.py
@time: 2020/9/19 下午8:03
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 860.柠檬水找零

在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：
输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

示例 2：
输入：[5,5,10]
输出：true

示例 3：
输入：[10,10]
输出：false

示例 4：
输入：[5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。

提示：
0 <= bills.length <= 10000
bills[i] 不是 5 就是 10 或是 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lemonade-change
"""


def lemonade_change(bills):
    """
    模拟情景。 时间复杂度为 O(n), 空间复杂度为 O(1)
    :param bills: (list)
    :return: (bool)
    """
    money = {5: 0, 10: 0, 20: 0}
    for bill in bills:
        if bill == 5:
            money[bill] = money[bill] + 1
            continue

        elif bill - 5 == 5:
            if money[5] == 0:
                return False
            money[bill] = money[bill] + 1
            money[5] = money[5] - 1
            continue

        elif bill - 5 == 15:
            money[bill] = money[bill] + 1
            if money[10] >= 1 and money[5] >= 1:
                money[10] = money[10] - 1
                money[5] = money[5] - 1
            elif money[5] >= 3:
                money[5] = money[5] - 3
            else:
                return False
    return True


def test(inputs, answer):
    outputs = lemonade_change(inputs)
    print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))
    assert outputs == answer, print("Inputs:{}, Outputs:{}, Except:{}".format(inputs, outputs, answer))


def main():
    bills, answer = [5, 5, 5, 10, 20], True
    test(bills, answer)

    bills, answer = [5, 5, 10], True
    test(bills, answer)

    bills, answer = [10, 10], False
    test(bills, answer)

    bills, answer = [5, 5, 10, 10, 20], False
    test(bills, answer)


if __name__ == '__main__':
    main()
