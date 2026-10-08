class Solution:
    def romanToInt(self, s: str) -> int:
        nmap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    
        value=0
        for i in range(len(s)):
            if i + 1 < len(s) and nmap[s[i]] < nmap[s[i+1]]:
                value -= nmap[s[i]]
            else:
                value += nmap[s[i]]
        return value

obj = Solution()
ans = obj.romanToInt(s = "MCMXCIV")
print(ans)