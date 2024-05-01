# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

strs = ["flower","flow","flight"]
# output: fl

ans=""
strs=sorted(strs)
first=strs[0]
last=strs[-1]
for i in range(min(len(first),len(last))):
    if(first[i]!=last[i]):
        print( ans)
    ans+=first[i]
    print (ans) 