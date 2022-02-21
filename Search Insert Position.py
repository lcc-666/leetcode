'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
'''

class Solution:
    def __init__(self):
        self.nums = [1,3,5,6]
        self.target = 7

    def searchInsert(self):
        nums = self.nums
        target = self.target
        #算法部分
        low = 0
        height = len(nums) - 1
        mid = (height + low) // 2
        while low != height:
            #print(low, mid, height)

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                height = mid
            mid = int((low + height) / 2)
        if nums[low] == target:
            return low
        if nums[0]>target:
            return 0
        if nums[-1]<target:
            return len(nums)
        return low

if __name__ == '__main__':
    t=Solution()
    s=t.searchInsert()
    print(s)


