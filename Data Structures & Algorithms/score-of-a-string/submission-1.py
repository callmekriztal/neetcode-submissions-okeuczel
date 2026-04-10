class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_value = 0
        for i in range(1,len(s)):
            ascii_value +=abs(ord(s[i-1])-ord(s[i]))
        
        return ascii_value