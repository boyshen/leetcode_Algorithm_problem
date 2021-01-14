# -*- encoding: utf-8 -*-
"""
@file: totalNQueens.py
@time: 2020/10/26 下午5:08
@author: shenpinggang
@contact: 1285456152@qq.com
@desc: 52.N皇后 II

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

上图为 8 皇后问题的一种解法。
给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:
输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

提示：
皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。
当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或 N-1 步，可进可退。
（引用自 百度百科 - 皇后 ）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens-ii
"""


def total_n_queens(n):
    """
    基于位运算的回溯。 时间复杂度：O(N!)，其中 N 是皇后数量，空间复杂度：O(N)
    参考 https://leetcode-cn.com/problems/n-queens-ii/solution/nhuang-hou-ii-by-leetcode-solution/
    进行理解
    :param n: (int)
    :return: (int)
    """

    def backtrack(row, col, diagonals1, diagonals2):
        if row >= n:
            return 1

        count = 0
        bites = (~(col | diagonals1 | diagonals2)) & ((1 << n) - 1)
        while bites:
            # 放置皇后的位置
            position = bites & (-bites)
            # 将放置皇后的位置设置为 0
            bites = bites & (bites - 1)
            count += backtrack(row + 1,
                               col | position,
                               (diagonals1 | position) << 1,
                               (diagonals2 | position) >> 1)
        return count

    return backtrack(0, 0, 0, 0)


def test(n, answer):
    outputs = total_n_queens(n)
    print("Inputs:{}, Outputs:{}, Except:{}".format(n, outputs, answer))
    assert outputs == answer, print("Answer Failed")


def main():
    test(4, 2)


if __name__ == '__main__':
    main()
