"""
LC 2235: 两整数相加
思路: 直接 return num1 + num2
"""


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


# ===== 本地测试 =====
if __name__ == "__main__":
    s = Solution()
    print(s.sum(12, 5))       # 预期: 17
    print(s.sum(-10, 4))      # 预期: -6
    print(s.sum(0, 0))        # 预期: 0
