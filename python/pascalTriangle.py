class Solution():
    def getRow(self, rowIndex):
        return self.pascalSolve(end=rowIndex)
    
    def pascalSolve(self, start=0, end=0, l=[1]):
        if start == end:
            return l

        tmpL = l.copy()
        tmpL.insert(0, 0)
        l.append(0)
        n = [ tmpL[i] + l[i] for i in range(len(l)) ]

        return self.pascalSolve(start + 1, end, n)

if __name__ == '__main__':
    test = int(input('row index:'))
    sol = Solution()
    print(sol.getRow(test))
