"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.
"""

def arrayManipulation(n, queries):
    # Write your code here
    arr = []
    for i in range(n):
        arr.append(0)
    for q in queries:
        for i in range(q[0]-1, q[1]):
            arr[i]+=q[2]
    return max(arr)

#fails on time restriction. cases with huge inputs dont pass (7-13)
