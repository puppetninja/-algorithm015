class Solution:
    def search(self, nums, target):
        if nums is None: return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1

        # Find the rotation spot
        if nums[0] < nums[len(nums)-1]:
            pivot = 0
        else:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < nums[mid-1]:
                    pivot = mid
                    break
                elif nums[mid] > nums[mid+1] :
                    pivot = mid + 1
                    break
                elif nums[left] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        # Determine which range in the array to search
        if pivot > 0:
            if target >= nums[0]:
                left, right = 0, pivot-1
            else:
                left, right = pivot, len(nums)-1
        else:
            left, right = 0, len(nums)-1

        # Perform binary search
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
