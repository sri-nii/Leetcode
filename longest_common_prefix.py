class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i in range(len(strs)):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
    
obj = Solution()
resp = obj.longestCommonPrefix(strs = ["flower","flow","flight"])
print(resp)