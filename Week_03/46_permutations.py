# 原始思路
# 傻递归，不断地recursion创建list的拷贝，没get到backtracking的点
# 对于 permutations ii 这样的题没法做
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 or nums is None:
            return []

        if len(nums) == 1:
            return [nums]

        last_digit = nums[-1]
        perms = self.permute(nums[:-1])
        res = []

        for perm in perms:
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, last_digit)
                res.append(perm_copy)
        return res

# 采用backtracking
# 内存减少，但是时间显著增加，应该是用了backtracking复杂度升高
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list()
        path = list()
        self.dfs(nums, path, res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
