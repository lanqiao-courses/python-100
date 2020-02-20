from graph import Graph, State
from collections import deque


class GraphBfs(Graph):

    def bfs(self, root, visit_func):
        if root is None:
            return
        queue = deque()
        queue.append(root)
        root.visit_state = State.visited
        while queue:
            node = queue.popleft()
            visit_func(node)
            for adjacent_node in node.adj_nodes.values():
                if adjacent_node.visit_state == State.unvisited:
                    queue.append(adjacent_node)
                    adjacent_node.visit_state = State.visited