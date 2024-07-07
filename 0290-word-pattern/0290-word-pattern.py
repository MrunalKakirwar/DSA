class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        phash = {}
        shash = {}
        s = s.split()
        if (len(pattern) != len(s)):
            return False
        else:
            for n in range (len(pattern)):
                if pattern[n] not in phash:
                    phash[pattern[n]] = s[n]
                else:
                    if phash[pattern[n]] != s[n]:
                        return False
                if s[n] not in shash:
                    shash[s[n]] = pattern[n]
                else:
                    if shash[s[n]] != pattern[n]:
                        return False
            return True

