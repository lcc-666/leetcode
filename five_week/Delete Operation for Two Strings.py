"""
给定两个单词word1和word2，返回使得word1和word2相同所需的最小步数。

每步可以删除任意一个字符串中的一个字符。

示例 1：

输入: word1 = "sea", word2 = "eat"
输出: 2
解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
示例  2:

输入：word1 = "leetcode", word2 = "etco"
输出：4
"""

class Solution:
    def __init__(self):
        self.word1="leetcode"
        self.word2="etco"

    def minDistance(self):
        word1=self.word1
        word2=self.word2
        #算法部分
        m,n=len(word1),len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            dp[i][0]=i
        for j in range(1,n+1):
            dp[0][j]=j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1

        return dp[m][n]
