class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(n):
            temp = [0] * (i+1)
            if i == 0:
                res.append([1])   
            elif i == 1:
                res.append([1, 1])
            else:
                prevList = res[i-1]
                for j in range(len(prevList)):
                    if j == 0:
                        temp[j] = 1
                    else:
                        temp[j] = prevList[j-1] + prevList[j]
                temp[len(temp)-1] = 1          
                res.append(temp)
        return res