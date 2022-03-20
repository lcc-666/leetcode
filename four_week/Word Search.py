"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
示例 3：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
"""


class Solution:
    def __init__(self):
        self.board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        self.word = "ABCCED"

    def exist(self):
        board = self.board
        word = self.word
        # 算法设计
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, nwej = i + di, j + dj
                if 0 <= newi < h and 0 <= nwej < w:
                    if (newi, nwej) not in visited:
                        if check(newi, nwej, k + 1):
                            result = True
                            break
            visited.remove((i, j))
            return result

        h = len(board)
        w = len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    s = Solution()
    t = s.exist()
    print(t)
