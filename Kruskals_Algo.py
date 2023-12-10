class WeightedUndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        # Add an edge to the graph
        self._add_edge(u, v, weight)
        self._add_edge(v, u, weight)

    def _add_edge(self, u, v, weight):
        if u in self.graph:
            self.graph[u][v] = weight
        else:
            self.graph[u] = {v: weight}

    def update_weight(self, u, v, new_weight):
        # Update the weight of an existing edge
        if u in self.graph and v in self.graph[u]:
            self.graph[u][v] = new_weight
            if v in self.graph and u in self.graph[v]:
                self.graph[v][u] = new_weight
            else:
                print(f"Edge {v}-{u} not found.")
        else:
            print(f"Edge {u}-{v} not found.")

    def display_graph(self):
        # Display the graph
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def minimum_spanning_tree(self):
        # Kruskal's Algorithm to find the Minimum Spanning Tree
        parent = {}
        rank = {}

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                else:
                    parent[root1] = root2
                    if rank[root1] == rank[root2]:
                        rank[root2] += 1

        # Initialize parent and rank for each vertex
        for vertex in self.graph:
            parent[vertex] = vertex
            rank[vertex] = 0

        edges = []
        for u in self.graph:
            for v, weight in self.graph[u].items():
                edges.append((u, v, weight))

        # Sort edges based on their weights
        edges.sort(key=lambda x: x[2])

        minimum_spanning_tree = WeightedUndirectedGraph()

        for edge in edges:
            u, v, weight = edge
            if find(u) != find(v):
                minimum_spanning_tree.add_edge(u, v, weight)
                union(u, v)

        return minimum_spanning_tree


# Example Usage:
if __name__ == "__main__":
    weighted_graph = WeightedUndirectedGraph()

    weighted_graph.add_edge("A", "B", 5)
    weighted_graph.add_edge("B", "C", 7)
    weighted_graph.add_edge("C", "D", 3)
    weighted_graph.add_edge("A", "D", 1)

    print("Initial Graph:")
    weighted_graph.display_graph()

    weighted_graph.update_weight("B", "C", 10)

    print("\nGraph after updating weight:")
    weighted_graph.display_graph()

    mst = weighted_graph.minimum_spanning_tree()
    print("Minimum Spanning Tree:")
    mst.display_graph()
