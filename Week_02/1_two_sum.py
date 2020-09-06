class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp not in num_dict:
                num_dict[nums[i]] = i
            else:
                return [num_dict[comp], i]
