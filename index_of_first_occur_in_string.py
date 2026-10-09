class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1    
obj = Solution()
resp = obj.strStr(haystack = "sadbutsad", needle = "sad")
print(resp)