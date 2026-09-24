class Solution:
    def countOfElements(self, x, arr):
        count=0
        for i in range(len(arr)):
            if arr[i]<=x:
                count+=1
        return count



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna