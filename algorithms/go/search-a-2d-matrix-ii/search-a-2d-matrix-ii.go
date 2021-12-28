func searchMatrix(matrix [][]int, target int) bool {
	return recSearchMatrix(matrix, target, 0, len(matrix), 0, len(matrix[0]))
}

func recSearchMatrix(matrix [][]int, target int, rowStart, rowEnd, colStart, colEnd int) bool {
	if rowStart >= rowEnd || colStart >= colEnd {
		return false
	}
	rowPivot, colPivot := rowStart, (colStart+colEnd)/2
	for rowPivot < rowEnd {
		if matrix[rowPivot][colPivot] == target {
			return true
		} else if matrix[rowPivot][colPivot] > target {
			return recSearchMatrix(matrix, target, rowStart, rowEnd, colStart, colPivot)
		} else if rowPivot+1 < rowEnd && matrix[rowPivot+1][colPivot] > target && matrix[rowPivot][colPivot] < target {
			return recSearchMatrix(matrix, target, rowStart, rowPivot+1, colPivot+1, colEnd) || recSearchMatrix(matrix, target, rowPivot+1, rowEnd, colStart, colPivot)
		}
		rowPivot++
	}
	return recSearchMatrix(matrix, target, rowStart, rowEnd, colPivot+1, colEnd)
}