class nums:
    def __init__(self, vals):
        self.vals = vals
        pass

    def sum(self):
        sum = 0
        for num in self.vals:
            sum += num
        return sum
    
    def sort(self):
        self.vals.sort()
        return self.vals
    
    def max(self):
        return max(self.vals)
    
    def min(self):
        return min(self.vals)
    

nums = nums([100, 20, 30])
print(nums.sum())
print(nums.sort())
print(nums.max())
print(nums.min())
