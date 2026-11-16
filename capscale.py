from collections import deque

def run():
    ln1 = input().split()  #graph size
    n = int(ln1[0])  #num of nodes
    m = int(ln1[1])  #num of edges

    ln2 = input().split()  #source and sink
    s = int(ln2[0])  #source node
    t = int(ln2[1])  #sink node

    #edge arrays,, edge i goes to to[i] and has cap[i] left
    # edge i and edge i^1 are pair (forward and reverse)
    to = []
    cap = []
    graph = [[] for _ in range(n)]  #list of edge ids leaving u

    def add_edge(u, v, c):
        graph[u].append(len(to))  #forward edge
        to.append(v)
        cap.append(c)
        graph[v].append(len(to))  #reverse edge, starts with 0 cap
        to.append(u)
        cap.append(0)

    max_cap = 0  #biggest cap in graph
    for _ in range(m):
        e = input().split()
        add_edge(int(e[0]), int(e[1]), int(e[2]))
        max_cap = max(max_cap, int(e[2]))

    def find_path(delta):  #bfs that only uses edges with cap >= delta
        prev = [-1] * n  #edge used to reach each node
        seen = [False] * n
        seen[s] = True
        q = deque([s])
        while q:
            u = q.popleft()
            for i in graph[u]:
                v = to[i]
                if not seen[v] and cap[i] >= delta:
                    seen[v] = True
                    prev[v] = i
                    if v == t:  #reached sink, stop searching
                        return prev
                    q.append(v)
        return None  #no path with this delta

    #starting delta = biggest power of 2 that is <= max capacity
    delta = 1
    while delta * 2 <= max_cap:
        delta *= 2

    flow = 0  #total flow so far
    while delta >= 1:
        while True:
            prev = find_path(delta)
            if prev is None:  #no more paths for this delta
                break

            #find bottleneck by walking back from sink to source
            push = float("inf")
            v = t
            while v != s:
                i = prev[v]
                push = min(push, cap[i])
                v = to[i ^ 1]  # i^1 is the reverse edge,, points back to tail

            #push flow along path,, update forward and reverse edges
            v = t
            while v != s:
                i = prev[v]
                cap[i] -= push
                cap[i ^ 1] += push
                v = to[i ^ 1]

            flow += push
        delta //= 2  #halve delta, last round is delta = 1

    print("max flow:", flow)


run()