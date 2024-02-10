class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        prevList = self.generate(numRows - 1)
        prev = prevList[numRows - 2]
        ret = [0] * (numRows)
        ret[0] = 1
        ret[numRows-1] = 1
        for i in range(1, numRows - 1):
            ret[i] = prev[i-1] + prev[i]
        prevList.append(ret)
        
        return prevList
