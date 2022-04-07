"""
给定两个字符串, s和goal。如果在若干次旋转操作之后，s能变成goal，那么返回true。

s的 旋转操作 就是将s 最左边的字符移动到最右边。

例如, 若s = 'abcde'，在旋转一次之后结果就是'bcdea'。

示例 1:

输入: s = "abcde", goal = "cdeab"
输出: true
示例 2:

输入: s = "abcde", goal = "abced"
输出: false
"""


class Solution:
    def __init__(self):
        self.s = "abcde"
        self.goal = "abced"

    def rotateString(self):
        s = self.s
        goal = self.goal
        # 算法部分
        if len(s) != len(goal):
            return False
        for i in range(len(goal)):
            if goal[i] == s[0]:
                if (goal[i:]+goal[0:i])==s:
                    return True
        return False



if __name__ == '__main__':
    s = Solution()
    print(s.rotateString())
