"""
LC 1480: 一维数组的动态和
思路: nums[i] += nums[i-1]，原地累加
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            # nums[i] = nums[i] + nums[i-1]
            nums[i] += nums[i-1]  #上面的等价写法
        return nums


# ===== 本地测试 =====
if __name__ == "__main__":
    s = Solution()
    print(s.runningSum([1, 2, 3, 4]))      # 预期: [1, 3, 6, 10]
    print(s.runningSum([1, 1, 1, 1, 1]))   # 预期: [1, 2, 3, 4, 5]
    print(s.runningSum([3, 1, 2, 10, 1]))  # 预期: [3, 4, 6, 16, 17]
