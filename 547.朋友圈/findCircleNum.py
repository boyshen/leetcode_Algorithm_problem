# -*- encoding: utf-8 -*-
"""
@file: findCircleNum.py
@time: 2020/10/14 下午2:24
@author: shenpinggang
@contact: 1285456152@qq.com
@desc:  547.朋友圈

班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。
如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。
如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

示例 1：
输入：
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出：2
解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回 2 。

示例 2：
输入：
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出：1
解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，所以他们三个在一个朋友圈，返回 1 。


提示：
1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]
"""


class Solution1(object):
    """
    DFS 实现。 时间复杂度 O(n^2). 空间复杂度为 O(n)
    """

    def find_circle_num(self, m):
        nums, count = len(m), 0
        visit = [False] * nums
        for i in range(nums):
            if not visit[i]:
                self.dfs(i, m, visit)
                count += 1
        return count

    def dfs(self, i, m, visit):
        for j in range(len(m)):
            if m[i][j] == 1 and not visit[j]:
                visit[j] = True
                self.dfs(j, m, visit)


class Solution2(object):
    """
    并查集。时间复杂度为 O(n^3). 空间复杂度为 O(n)
    """

    def find_circle_num(self, m):
        size = len(m)
        parent = [i for i in range(size)]

        for i in range(size):
            for j in range(size):
                if m[i][j] == 1:
                    self.union(parent, i, j)
        return len(set([self.find(parent, i) for i in range(size)]))

    def union(self, parent, i, j):
        p1 = self.find(parent, i)
        p2 = self.find(parent, j)
        parent[p1] = p2

    def find(self, parent, i):
        root = i
        while root != parent[root]:
            root = parent[root]
        while parent[i] != i:
            x = i
            i = parent[i]
            parent[x] = root
        return root


class Solution(object):
    """
    BFS 实现。 时间复杂度 O(n^2). 空间复杂度为 O(n)
    """

    def find_circle_num(self, m):
        size = len(m)
        visit = [False] * size
        queue, count = [], 0
        for i in range(size):
            if not visit[i]:
                queue.append(i)
                while queue:
                    s = queue.pop(0)
                    visit[s] = True
                    for j in range(size):
                        if m[s][j] == 1 and not visit[j]:
                            queue.append(j)
                count += 1
        return count


def test(m, answer):
    outputs = Solution().find_circle_num(m)
    print("Inputs:{}, Outputs:{}, Except:{}".format(m, outputs, answer))
    # assert outputs == answer, print("Answer Failed")


def main():
    m = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    test(m, 2)

    m = [[1, 1, 0],
         [1, 1, 1],
         [0, 1, 1]]
    test(m, 1)


if __name__ == '__main__':
    main()
