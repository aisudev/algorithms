class Solution:
    def fib(self, n:int) -> int:
        if n < 2:
            return n

        return self.fib(n-1) + self.fib(n-2)

if __name__ == "__main__":
    test = int(input('n fib:'))
    sol = Solution()
    print(sol.fib(test))
