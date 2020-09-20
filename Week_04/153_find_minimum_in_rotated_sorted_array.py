class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None: return None
        if len(nums) == 1: return nums[0]

        left, right = 0, len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
