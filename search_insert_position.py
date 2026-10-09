class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for idx, num in enumerate(nums):
            if num == target:
                return idx
            elif num > target:
                return idx
        return len(nums)
            
obj = Solution()
resp = obj.searchInsert(nums = [1,3,5,6], target = 7)
print(resp)