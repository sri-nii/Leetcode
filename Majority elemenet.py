class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for num in count:
            if count[num] > len(nums) // 2:
                return num

obj = Solution()
ans = obj.majorityElement(nums = [3,2,3])
print(ans)