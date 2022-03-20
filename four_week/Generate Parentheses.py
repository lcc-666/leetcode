"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
"""


class Solution:
    def __init__(self):
        self.n = 3

    def generateParenthesis(self):
        n = self.n
        # 算法部分
        result = []
        if n <= 0:
            return []

        def getParenthesis(path, left, right):
            if left == 0 and right == 0:
                result.append(path[:])
                return result

            if left == right:
                getParenthesis(path + "(", left - 1, right)
            elif left < right:
                if left > 0:
                    getParenthesis(path + "(", left - 1, right)
                getParenthesis(path + ")", left, right - 1)

        getParenthesis("", n, n)
        return result


if __name__ == '__main__':
    s = Solution()
    t = s.generateParenthesis()
    print(t)
