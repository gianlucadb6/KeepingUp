def minimumBribes(q):
    # Write your code here
    bribes = 0
    for i in range(len(q)):
        if q[i] - (i+1) > 2: #if person is more than 2 spaces ahead of their og location
            print("Too chaotic")
            return
        temp = q[0:i]
        temp.sort()
        for j in range(len(temp)-1, -1, -1):
            if temp[j] > q[i]:
                bribes+=1
            else:
                break
    print(bribes)

#cant pass test cases 6/7/8/9  
