class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        mySet = set()
        count = 0
        for n in range(len(s)):
            if s[n] not in mySet:
                mySet.add(s[n])
                
            else:
                count +=2
                mySet.remove(s[n])
        if mySet:
            count +=1
        return count
