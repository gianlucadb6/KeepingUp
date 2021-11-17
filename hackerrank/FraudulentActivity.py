"""
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to  2x the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
"""

def activityNotifications(expenditure, d):
    # Write your code here
    notifications = 0
    for i in range(d-1, len(expenditure)):
        if i+1 > d:
            med = statistics.median(expenditure[i-d:i])
            if expenditure[i] >= 2*med:
                notifications+=1
    return notifications

#have to fix time complexity



def activityNotifications(expenditure, d):
    # Write your code here
    notifications = 0
    for i in range(d-1, len(expenditure)):
        if i+1 > d:
            l = sorted(expenditure[i-d:i])
            if len(expenditure) % 2 == 0:
                med = l[(len(expenditure)-1)/2]
            else:
                med = (l[(len(expenditure)-1)//2]+l[(len(expenditure))//2])/2
            if expenditure[i] >= 2*med:
                notifications+=1
    return notifications

#i think median() function is taking too long. on the order of O(n), on top of iterating the list, looking at n^2 so i need a faster way to find the median. this does not work for all cases, but does for 2 of them
