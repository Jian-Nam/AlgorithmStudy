class Solution:
    def letterCombinations(self, digits):
        self.letterMap = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z'],
        }
        self.discovered = []
        self.digits = digits
        self.dfs('', 0)

        return self.discovered


    def dfs(self, combination, index):
        if len(combination) == len(self.digits):
            if(combination != ''):
                self.discovered.append(combination)
            return

        for letter in self.letterMap[self.digits[index]]:
            newCombination = combination + letter
            self.dfs(newCombination, index + 1)


s = Solution()
print(s.letterCombinations("23"))