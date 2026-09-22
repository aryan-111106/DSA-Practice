class Solution:
    def sumOfDigits(self, n):
        temp=n
        sum=0
        while n!= 0:
            remainder= n % 10
            sum+=remainder
            n //= 10
        return int(sum)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna