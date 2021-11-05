"""

"""

def hourglassSum(arr):
    # Write your code here
    sum = []
    
    for r in range(len(arr)-2):
        for c in range(len(arr[0])-2):
            sum.append(arr[r][c]+arr[r][c+1]+arr[r][c+2]+arr[r+1][c+1]+arr[r+2][c]+
                arr[r+2][c+1]+arr[r+2][c+2])
    
    return max(sum)

#passes everything
