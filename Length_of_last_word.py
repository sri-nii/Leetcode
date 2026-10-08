class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(" ")
        print(len(s[-1]))


obj = Solution()
obj.lengthOfLastWord(s = "   fly me   to   the moon  ")