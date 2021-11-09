"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dict = {}
        prev = None
        ptr = head
        while ptr != None:
            if ptr not in dict:
                dict[ptr] = Node(ptr.val, ptr.next, ptr.random)
            if prev != None:
                prev.next = dict[ptr]
            else:
                head = dict[ptr]
            if ptr.random != None:
                if ptr.random not in dict:
                    dict[ptr.random] = Node(ptr.random.val, ptr.random.next, ptr.random.random)
                dict[ptr].random = dict[ptr.random]
            prev = dict[ptr] 
            ptr = ptr.next
        return head
                    
#complteted     
