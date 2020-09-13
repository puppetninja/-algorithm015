class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list()
        path = list()
        nums.sort()
        self.dfs(nums, path, res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
