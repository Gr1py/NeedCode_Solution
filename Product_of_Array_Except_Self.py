# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: 
nums = [1,2,3,4]
# Output: [24,12,8,6]

celkem = []

for j in range(len(nums)):
    # print(f"jecko {j}")
    vysledek = 1
    for i in range(j+1,len(nums)):
        # print(f"icko {i}")
        vysledek = vysledek * nums[i]
    for k in range(j):
        # print(f"kacko {k}")
        vysledek = vysledek * nums[k]   
    celkem.append(vysledek)
print (celkem) #Problem with runtime, otherwise bulletproof solution