class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        bucket = [0] * 1001
        res = []

        for num in arr1:
            bucket[num] += 1

        for num in arr2:
            if bucket[num] != 0:
                curr_arr = [num] * bucket[num]
                res += curr_arr
                bucket[num] = 0

        for num in range(len(bucket)):
            if bucket[num] != 0:
                curr_arr = [num] * bucket[num]
                res += curr_arr
                bucket[num] = 0

        return res
