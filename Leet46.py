list =[1, 2, 3]

class MySolution:
    def permute(self, nums):
        self.nums = nums
        self.prev_elements = []
        self.result = []
        self.dfs()
        return self.result

    def dfs(self):
        if len(self.prev_elements) == len(self.nums) :
            self.result.append(self.prev_elements[:])
            return
        
        for i in self.nums:
            if i not in self.prev_elements:
                self.prev_elements.append(i)
                self.dfs()
                self.prev_elements.pop()

class Solution:
    def permute(self, nums):
        self.nums = nums
        self.prev_elements = []
        self.result = []
        self.dfs(nums[:])
        return self.result

    def dfs(self, remain:[]):
        if len(remain) == 0 :
            self.result.append(self.prev_elements[:])
            return
        
        for i in remain:
            next_remain = remain[:]
            next_remain.remove(i)
            self.prev_elements.append(i)
            self.dfs(next_remain)
            self.prev_elements.pop()


s = Solution()
print(s.permute(list))
