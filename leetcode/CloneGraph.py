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
                if cur:
                    if cur.val not in visited:
                        visited.append(cur.val)
                        dict[cur.val] = Node(cur.val, None)
                        tempNeighbors = []
                        for n in cur.neighbors:
                            if not dict.get(n):
                                queue.append(n)
                                bfs(queue)
                            tempNeighbors.append(dict.get(n.val))
                        dict[cur.val].neighbors = tempNeighbors
        bfs(queue)
        return dict.get(1)

#coming together. using bfs but i need to make sure this is doing what i think its doing. interesting to see that in one way i created a dictionary somewhere in memory but when referenced differently its just a list of nodes.(sub 1)

#passes first case. some simple references i messed up. need to make sure anything in the new graph is pointing to newly created nodes and not anything from the original graph.

#complete: had to add a check before accessing value of something popped from queue. doesn't make sense that anything popped from the queue qould have an empty val attribute... but works now
