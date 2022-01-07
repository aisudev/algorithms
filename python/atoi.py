class Solution:
    def Atoi(self, s:str):
        s = s.lstrip()
        isNeg = False
        n = ''
        numerical = [str(i) for i in range(10)]
        if len(s) == 0:
            return 0

        # Find negative number or positive number
        if s[0] == '-':
            isNeg = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        for i in range(len(s)):
            if s[i] in numerical:
                n += s[i]
            else:
                break
        
        if len(n) == 0:
            return 0

        ans = -int(n) if isNeg else int(n)
        if ans > 2**31-1:
            return 2**31-1
        elif ans < -2**31:
            return -2**31
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.Atoi('  -+123 abcd')) 
