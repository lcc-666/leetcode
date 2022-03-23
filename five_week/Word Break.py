"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
注意，你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""


class Solution:
    def __init__(self):
        self.s = "leetcode"
        self.wordDict = {"leet", "code"}

    def wordBreak(self):
        s = self.s
        wordDict = self.wordDict
        # 算法部分
        wordDictlist = list(wordDict)
        db = [False] * (len(s) + 1)
        db[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if db[j] and s[j:i] in wordDictlist:
                    db[i] = True
                    break
        return db[len(s)]


if __name__ == '__main__':
    s = Solution()
    t = s.wordBreak()
    print(t)
