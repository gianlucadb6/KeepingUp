"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = []
        newList = []
        cur = node
        while cur not in visited:
            visited.append(cur)
            newList.append(Node(cur.val, cur.neighbors))
            for n in cur.neighbors:
                if n not in visited:
                    cur = n
        return newList
            

#doesn't work. getting some ideas together
