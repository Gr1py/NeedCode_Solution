# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
nums = [1,2,3,1]
#Output: true

#Update from GitHub
# update of comments
# one more time to make sure everything works fine
n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] == nums[j]:
            #return True
            print(True)
#return False
print (False)
