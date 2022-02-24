"""
给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1：
输入：s = "Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

示例 2:
输入： s = "God Ding"
输出："doG gniD"
"""


def reverseString(s):
    s=list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left = left + 1
        right = right - 1
    s="".join(s)
    return s

class Solution:
    def __init__(self):
        self.s = "Let's take LeetCode contest"

    def reverseWords(self):
        s = self.s
        # 算法部分
        ls=s.split()
        reult=[]
        for i in ls:
            item=reverseString(i)
            reult.append(item)
        s=" ".join(reult)
        print(s)




if __name__ == '__main__':
    t=Solution()
    t.reverseWords()