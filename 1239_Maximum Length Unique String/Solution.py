class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = [0]
        self.dfs("", 0, arr, result)
        return result[0]

    def dfs(self, path, index, arr, result):
        if self.unique(path):
            result[0] = max(result[0], len(path))
        
        if index == len(arr) or not self.unique(path):
            return
        
        for i in range(index, len(arr)):
            self.dfs(path + arr[i], i + 1, arr, result)
    
    def unique(self, s):
        return len(s) == len(set(s))
