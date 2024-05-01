arr = [17,18,5,4,6,1]   
# Correct output[18,6,6,6,1,-1]

max_right = -1
for i in range(len(arr) - 1, -1, -1):
    temp = arr[i]
    arr[i] = max_right
    max_right = max(max_right, temp) 
print (arr)