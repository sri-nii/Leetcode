class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        track=0
        for i in range(len(nums)):
            if nums[i] != val:
                track += 1
            else:
                nums[i] = "_"
        nums.sort(key=lambda x:(not isinstance(x,int),x) )
        return track
obj = Solution()
ansq = obj.removeElement(nums = [3,2,2,3], val = 3)

print(ansq)