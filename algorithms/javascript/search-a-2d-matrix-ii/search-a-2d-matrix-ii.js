/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    const rowLength = matrix.length;
    const columnLength = matrix[0].length;

    const recSearchMatrix = (rowStart, rowEnd, columnStart, columnEnd) => {
        if (rowStart >= rowEnd || columnStart >= columnEnd) {
            return false;
        }
        let rowPivot = rowStart;
        const columnPivot = Math.floor((columnStart + columnEnd) / 2);
        while (rowPivot < rowEnd) {
            if (matrix[rowPivot][columnPivot] === target) {
                return true;
            } else if (matrix[rowPivot][columnPivot] > target) {
                return recSearchMatrix(rowStart, rowEnd, columnStart, columnPivot); 
            } else if (rowPivot + 1 < rowEnd && matrix[rowPivot][columnPivot] < target && matrix[rowPivot + 1][columnPivot] > target) {
                return recSearchMatrix(rowStart, rowPivot + 1, columnPivot + 1, columnEnd) || recSearchMatrix(rowPivot, rowEnd, columnStart, columnPivot);
            }
            rowPivot++;
        }
        return recSearchMatrix(rowStart, rowEnd, columnPivot + 1, columnEnd);
    }

    return recSearchMatrix(0, rowLength, 0, columnLength);
};