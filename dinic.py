from collections import deque


class Dinic:
    def __init__(self, n):
        self.n = n
        # graph[u] = list of edges [to, remaining_capacity, index_of_reverse_edge]
        self.graph = [[] for _ in range(n)]
        self.original = []  # (u, position in graph[u], capacity) of each user edge

    def add_edge(self, u, v, cap):
        self.original.append((u, len(self.graph[u]), cap))
        self.graph[u].append([v, cap, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])  # reverse edge

    def _bfs(self, s, t):
        """Build the level graph. Returns True if t is reachable from s."""
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v, cap, _ in self.graph[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] >= 0

    def _dfs(self, u, t, pushed):
        """Send flow along edges that go exactly one level deeper."""
        if u == t:
            return pushed
        while self.it[u] < len(self.graph[u]):
            edge = self.graph[u][self.it[u]]
            v, cap, rev = edge
            if cap > 0 and self.level[v] == self.level[u] + 1:
                d = self._dfs(v, t, min(pushed, cap))
                if d > 0:
                    edge[1] -= d                  # use forward capacity
                    self.graph[v][rev][1] += d    # give it to the reverse edge
                    return d
            self.it[u] += 1                       # dead end: skip this edge from now on
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self._bfs(s, t):
            self.it = [0] * self.n
            while True:
                pushed = self._dfs(s, t, float("inf"))
                if pushed == 0:
                    break
                flow += pushed
        return flow

    def edge_flows(self):
        """Flow used on every edge, in the order the edges were added."""
        result = []
        for u, pos, cap in self.original:
            v, remaining, _ = self.graph[u][pos]
            result.append((u, v, cap, cap - remaining))
        return result


def main():
    # ---------- INPUT (from the user) ----------
    n = int(input("Number of nodes: "))
    m = int(input("Number of edges: "))
    source = int(input("Source node: "))
    sink = int(input("Sink node: "))

    g = Dinic(n)
    print("Enter each edge as: from to capacity")
    for i in range(m):
        u, v, c = map(int, input(f"Edge {i + 1}: ").split())
        g.add_edge(u, v, c)

    # ---------- OUTPUT ----------
    total = g.max_flow(source, sink)
    print("\nFlow on each edge (flow/capacity):")
    for u, v, cap, flow in g.edge_flows():
        print(f"  {u} -> {v}: {flow}/{cap}")
    print(f"\nMaximum flow from {source} to {sink} = {total}")


if __name__ == "__main__":
    main()
