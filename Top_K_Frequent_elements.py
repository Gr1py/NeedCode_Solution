# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

nums = [1,1,1,2,2,3]
k = 2

# output: [1,2]
seznam= {}
for num in nums:
    if num in seznam:
        seznam[num] += 1
    else:
        seznam[num] = 1
serazeno = sorted(seznam.items(), key=lambda x: x[1], reverse=True)
top = [item[0] for item in serazeno[:k]]
print (top)