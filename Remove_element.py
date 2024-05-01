# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Input: 
nums = [0,1,2,2,3,0,4,2]
val = 2
# Output: 2, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

k = 0
for cislo in range(len(nums)):
            
    if nums[cislo] != val:
                
        nums[k] = nums[cislo]
        k+=1
            
print (k,nums) #Works, in nums list I just do not remove values