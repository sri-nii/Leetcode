class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum = prices[0]
        diff = 0

        for price in prices:
            if price < minimum:
                minimum = price

            difference = price - minimum

            if difference > diff:
                diff = difference

        return diff


obj = Solution()
ans = obj.maxProfit(prices = [7,1,5,3,6,4])
print(ans)