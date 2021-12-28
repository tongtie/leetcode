"""
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = 
[
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
], target = 5

Output: true
Example 2:


Input: matrix = 
[
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
], target = 20

Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9
"""

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        return self.recSearchMatrix(matrix, target, 0, 0, len(matrix), len(matrix[0]))

    def recSearchMatrix(self, matrix, target, row_start, column_start, row_end, column_end):
        """
        参考：https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2869/
        在一个矩阵里，寻找这样一个分割点V(i,j)，使得target > V(i,j) 并且 target < V(i+1,j), 这样我们就可以只求解原始矩阵的右上部分和左下部分两个子矩阵。
        时间复杂度应该是O(mlog(m*n))。每次将矩阵2分，并比对分割点当前列的值和target的大小。
        """
        if row_start >= row_end or column_start >= column_end:
            return False
        row_pivot, column_pivot = row_start, int((column_start + column_end) / 2)
        if matrix[row_pivot][column_pivot] == target:
            return True
        # 输入只有一个元素，并且不相等
        if column_end - column_start == 1 and row_end - row_start == 1:
            return False
        while row_pivot < row_end:
            if matrix[row_pivot][column_pivot] == target:
                return True
            # 如果当前矩阵的第一行，column_pivot列大于target
            elif matrix[row_pivot][column_pivot] > target:
                return self.recSearchMatrix(matrix, target, row_start, column_start, row_end, column_pivot)
            # 如果当前矩阵的第row_pivot行， column_pivot列小于target，并且row_pivot+1行，column_pivot列大于target
            elif row_pivot + 1 < row_end and matrix[row_pivot][column_pivot] < target and matrix[row_pivot + 1][column_pivot] > target:
                return self.recSearchMatrix(matrix, target, row_start, column_pivot + 1, row_pivot + 1, column_end) \
                    or self.recSearchMatrix(matrix, target, row_pivot + 1, column_start, row_end, column_pivot)
            row_pivot += 1
        # 当前列都小于target
        return self.recSearchMatrix(matrix, target, row_start, column_pivot + 1, row_end, column_end)
    
    def searchMatrix2(self, matrix, target: int) -> bool:
        """
        参考：https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66140/My-concise-O(m%2Bn)-Java-solution
        从矩阵的右上角开始求解，如果当前元素大于target，则向左移动一列，如果当前元素小于target，则向下移动一行。
        时间复杂度为：O(m+n)
        """
        row, column = len(matrix), len(matrix[0])
        i, j = 0, column - 1
        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    # matrix = [
    #     [1,4,7,11,15],
    #     [2,5,8,12,19],
    #     [3,6,9,16,22],
    #     [10,13,14,17,24],
    #     [18,21,23,26,30]
    # ]
    # wrong answer
    # matrix = [
    #     [5],
    #     [6]
    # ]
    # index out of range
    matrix = [
        [1, 1]
    ]
    print(Solution().searchMatrix(matrix, 6))