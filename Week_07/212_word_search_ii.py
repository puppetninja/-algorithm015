class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        end_of_word = '$'
        chars = {}
        for word in words:
            node = chars
            for c in word:
                node = node.setdefault(c, {})
            node[end_of_word] = word
        
        row_num = len(board)
        col_num = len(board[0])
        res = []
        
        def dfs(row, col, parent):
            if row < 0 or row >= row_num or col < 0 or col >= col_num:
                return

            char = board[row][col]
            if not char in parent:
                return

            next_nodes = parent[char]
            if end_of_word in parent[char] and next_nodes[end_of_word] not in res:
                res.append(next_nodes[end_of_word])

            board[row][col] = '#'

            dfs(row+1, col, next_nodes)
            dfs(row-1, col, next_nodes)
            dfs(row, col-1, next_nodes)
            dfs(row, col+1, next_nodes)

            board[row][col] = char


        for i in range(row_num):
            for j in range(col_num):
                if board[i][j] in chars:
                    dfs(i, j, chars)
                    
        return res
