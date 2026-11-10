class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max = 0
        for row in accounts:
            total = 0
            for money in row:
                total += money
                if total > max:
                    max = total
        return max