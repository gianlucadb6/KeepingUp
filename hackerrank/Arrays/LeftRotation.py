def rotLeft(a, d):
    # Write your code here
    n = []
    for i in range(len(a)):
        x = i + d
        if x > len(a)-1:
            x-=len(a)
        n.append(a[x])
    return n
