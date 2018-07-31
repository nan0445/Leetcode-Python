class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix:
            self.__s = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
            for i in range(1, len(matrix)+1):
                for j in range(1, len(matrix[0])+1):
                    self.__s[i][j] = self.__s[i-1][j] + self.__s[i][j-1] - self.__s[i-1][j-1] + matrix[i-1][j-1]
        else: self.__s = []
        #print(self.__s)
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.__s:
            return self.__s[row2+1][col2+1] - self.__s[row2+1][col1] - self.__s[row1][col2+1] + self.__s[row1][col1]
        else: return


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
