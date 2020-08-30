class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2: return 0
        
        left_pointer = 0
        right_pointer = len(height) - 1
        left_max = height[left_pointer]
        right_max = height[right_pointer]
        trapped_water = 0

        while left_pointer < right_pointer:
            if height[left_pointer] < height[right_pointer]:
                if height[left_pointer] < left_max:
                    trapped_water += left_max - height[left_pointer]
                else:
                    left_max = height[left_pointer]
                left_pointer += 1
            else:
                if height[right_pointer] < right_max:
                    trapped_water += right_max - height[right_pointer]
                else:
                    right_max = height[right_pointer]
                right_pointer -= 1

        return trapped_water
