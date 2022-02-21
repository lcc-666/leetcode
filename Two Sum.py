'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
'''

class Solution:
    def __init__(self):
        self.nums=[3,2,4]
        self.target=6
    def twoSum(self):
        nums=self.nums
        target=self.target
        #算法部分
        num=len(nums)
        for i in range(num):
            for j in range(i+1,num):
                two_sum=nums[i]+nums[j]
                if two_sum==target:
                    return [i,j]



if __name__ == '__main__':
    t=Solution()
    print(t.twoSum())