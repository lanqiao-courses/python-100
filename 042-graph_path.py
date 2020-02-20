from graph import Graph, State
from collections import deque


class GraphPathExists(Graph):

    def path_exists(self, start, end):
        if start is None or end is None:
            return False
        if start is end:
            return True
        queue = deque()
        queue.append(start)
        start.visit_state = State.visited
        while queue:
            node = queue.popleft()
            if node is end:
                return True
            for adj_node in node.adj_nodes.values():
                if adj_node.visit_state == State.unvisited:
                    queue.append(adj_node)
                    adj_node.visit_state = State.visited
        return False