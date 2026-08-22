class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n == 1:
            return False
        temp = n
        sum = 0
        prod = 1
        while n != 0:
            dig = n % 10
            sum += dig
            prod *= dig
            n //= 10
        return temp % (sum + prod) == 0

        
        