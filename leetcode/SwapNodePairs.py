"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        prev = None
        if ptr.next:
            prev = ptr
            ptr = ptr.next
        else:
            return
        head = prev
        while ptr and prev:
            #temp = ptr
            prev.next = ptr.next
            ptr.next = prev
            prev = prev.next
            if prev:
                ptr = prev.next
            else:
                break
        return head
            
        
#some initial ideas
