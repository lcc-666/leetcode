"""
给你一个数组，将数组中的元素向右轮转 k个位置，其中k是非负数。

示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
"""

class Solution:
    def __init__(self):
        self.nums=[1,2]
        self.k=3
    def rotate(self) :
        nums=self.nums
        k=self.k
        #算法部分
        k = k % len(nums)
        for i in range(k):
            a=nums.pop()
            nums.insert(0,a)
        print(nums)


if __name__ == '__main__':
    t=Solution()
    t.rotate()