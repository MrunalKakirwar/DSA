class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sHashMap = {}
        tHashMap = {}

        if len(s) == len(t):
            for n in range(len(s)):
                if s[n] in sHashMap:
                    if sHashMap[s[n]] != t[n]:
                        return False
                else:
                    sHashMap[s[n]] = t[n]
                if t[n] in tHashMap:
                    if tHashMap[t[n]] != s[n]:
                        return False
                else:
                    tHashMap[t[n]] = s[n]
            return True                
        return False
        