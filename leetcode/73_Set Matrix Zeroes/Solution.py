class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowList = []
        colList = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rowList.append(i)
                    colList.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rowList or j in colList:
                    matrix[i][j] = 0
