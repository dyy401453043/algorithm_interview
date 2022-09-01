# leetcode 212, 用Trie来给dfs的单词搜索减枝，达到加速
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        from collections import defaultdict
        class Trie():
            def __init__(self):
                self.is_end = False
                self.next = defaultdict(Trie)
                self.result = None
            def insert(self, word):
                node = self
                for ch in word:
                    node = node.next[ch]
                node.is_end = True
                node.result = word

        M, N = len(board), len(board[0])
        visited = [[False] * N for i in range(M)]
        result = []
        def dfs(i, j, node):
            if node.is_end:
                result.append(node.result)
            for i,j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=i<M and 0<=j<N and not visited[i][j]:
                    ch=board[i][j]
                    if ch in node.next:
                        visited[i][j] = True
                        dfs(i,j,node.next[ch])
                        visited[i][j] =False
        
        root = Trie()
        for word in words:
            root.insert(word)
        for i in range(M):
            for j in range(N):
                ch = board[i][j]
                if ch in root.next:
                    visited[i][j] = True
                    dfs(i,j,root.next[ch])
                    visited[i][j] =False
        return list(set(result))
