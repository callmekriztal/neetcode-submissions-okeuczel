class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        tp = 0 
        isSub = False
        if len(s) == 0:
            return True
        
        while tp < len(t) and sp < len(s):
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
            else:
                tp += 1
        
        if sp != len(s):
            return False
        else :
            return True
            