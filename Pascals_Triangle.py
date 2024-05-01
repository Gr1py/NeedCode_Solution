# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


numRows = 10
# output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

triangel = []
for i in range(numRows):
    row = [1] * (i + 1)
    for j in range(1,i):
        row[j] = triangel[i-1][j-1] + triangel[i-1][j]
    triangel.append(row)
print (triangel) 
