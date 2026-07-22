"""
LC 1512: 好数对的数目
思路: 字典统计出现次数，每遇到一个数字，它之前出现过几次就加几对
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}      # 字典：记录每个数字出现了几次
        pairs = 0       # 好数对总数

        for num in nums:
            # 这个数字之前出现过几次，就能和它组成几对
            pairs += count.get(num, 0)
            # 这个数字出现次数 +1
            count[num] = count.get(num, 0) + 1

        return pairs


# ===== 本地测试 =====
if __name__ == "__main__":
    s = Solution()
    print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # 预期: 4
    print(s.numIdenticalPairs([1, 1, 1, 1]))        # 预期: 6
    print(s.numIdenticalPairs([1, 2, 3]))            # 预期: 0
