n=4
k=2

class Solution(object):
    def combine(self, n, k):
        self.k = k
        self.n=n
        self.nums = []
        self.prev = []
        self.result = []
        for i in range(1,n+1):
            self.nums.append(i)
        self.dfs(0)
        return self.result
        
    def dfs(self, start):
        if len(self.prev) == self.k:
            self.result.append(self.prev[:])
            return
        
        for i in range(start, self.n):
            self.prev.append(self.nums[i])
            self.dfs(i+1)
            self.prev.pop()


s = Solution()
print(s.combine(n, k))