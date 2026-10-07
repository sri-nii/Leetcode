class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1
        for i in range(len(nums)):
            if nums[i] != nums[j-1]:
                nums[j] = nums[i]
                j+=1
        return j

obj = Solution()
ansq = obj.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])
