
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False

        if len(matrix) == 1:
            target_row = 0
        else:
            top, bottom = 0, len(matrix)-1
            while top <= bottom:
                print(f'top is {top} bottom is {bottom}')
                mid = (top + bottom) // 2
                if matrix[mid][0] >= target:
                    bottom = mid - 1
                else:
                    top = mid + 1

            target_row = mid

        start, end = 0, len(matrix[target_row])
        while start <= end:
            mid = (start + end) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False
