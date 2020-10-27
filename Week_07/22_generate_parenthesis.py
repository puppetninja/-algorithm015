class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, S = [], ''
        self.dfs(res, n, S, 0, 0)
        return res
    
    def dfs(self, res, n, S, left, right):
        if len(S) == 2 * n:
            res.append(S)
            return
        
        if left < n:
            S += '('
            self.dfs(res, n, S, left+1, right)
            S = S[:-1]

        if left > right:
            S += ')'
            self.dfs(res, n, S, left, right+1)
            S = S[:-1]
