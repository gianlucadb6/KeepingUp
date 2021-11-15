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
        queue = []
        visited = []
        dict = {}
        queue.append(node)
        def bfs(queue):
            while queue:
                cur = queue.pop()
                if cur not in visited:
                    visited.append(cur)
                    dict[cur.val] = Node(cur.val, None)
                    tempNeighbors = []
                    for n in cur.neighbors:
                        if not dict.get(n):
                            queue.append(n)
                            bfs(queue)
                    dict[cur.val].neighbors = tempNeighbors
        bfs(queue)
        return dict.get(1) 

#coming together. using bfs but i need to make sure this is doing what i think its doing. interesting to see that in one way i created a dictionary somewhere in memory but when referenced differently its just a list of nodes.
