class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = {}
        for n in strs:
            char_list = list(n)
            char_list.sort()
            sortedWord = ''.join(char_list)
            if sortedWord not in hashMap:
                hashMap[sortedWord] = [n]
            else:
                hashMap[sortedWord].append(n)
        return list(hashMap.values())

