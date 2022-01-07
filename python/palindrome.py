class Solution():
    def isParindrome(self, x:int):
        if x < 0:
            return False
        x = str(x)
        last = len(x) - 1
        half = int(len(x)/2)

        for i in range(half):
            if x[i] != x[last]:
                return False
            
            last -= 1

        return True
    def recur(self, x:int):
        if x < 0:
            return False
        
        x = str(x)
        if len(x) <= 1:
            return True
        else:
            if x[0] != x[-1]:
                return False
            else:
                return self.recur(int(x[1:-1]))
    def easyBuff(self, x:int):
        x = str(x)
        return x == x[::-1]

if __name__ == '__main__':
    sol = Solution()
    test = 11
    ans = sol.easyBuff(test)
    print('Is Palindrome:', ans)