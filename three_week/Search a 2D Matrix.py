"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
"""


class Solution:
    def __init__(self):
        self.matrix = [[1],[3]]
        self.target = 3

    def searchMatrix(self):
        matrix = self.matrix
        target = self.target
        # 算法逻辑
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        def search(target, nums):
            low = 0
            height = len(nums) - 1
            mid = (height + low) // 2
            while low != height:
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    low = mid + 1
                else:
                    height = mid
                mid = int((low + height) / 2)
            if nums[low] == target:
                return low
            return -1

        low = 0
        height = len(matrix) - 1

        while low != height:
            mid = (low + height) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target <= matrix[mid][-1]:
                if search(target, matrix[mid]) == -1:
                    return False
                else:
                    return True
            if matrix[mid-1][-1]>=target:
                height=mid
            else:
                low=mid+1
        if search(target,matrix[-1]) !=-1:
            return True
        return False
if __name__ == '__main__':
    s = Solution()
    t = s.searchMatrix()
    print(t)
