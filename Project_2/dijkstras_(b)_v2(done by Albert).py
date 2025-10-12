import heapq
import time
import random



# adjacency list = adjacency list of the graph

def dijkstras(V, E, start):
    d = {node: float('inf') for node in V} #list of nodes
    pi = {node: None for node in V}
    d[start] = 0



    pq = [(0, start)] #contains the distance and vertex

    while pq:
        current_dist, u = heapq.heappop(pq)


        #if the array is outdated, skip~

        if current_dist > d[u]:
            continue

        for v, w in E[u]:
            if w < 0:
                raise ValueError("The graph contains negative edge weights.\n\nThis is not allowed in Dijkstra's Algorithm~")
            new_dist = d[u] + w

            if new_dist < d[v]:
                d[v] = new_dist
                pi[v] = u
                heapq.heappush(pq, (new_dist, v))

    return d, pi


def reconstruct_path(pi, start, target):
    path = []

    while target is not None:
        path.append(target)
        target = pi[target]
    return path[::-1] if path[-1] == start else []
    


def generate_random_graph(n, density=0.3, max_w=10):
    V = {str(i) for i in range(n)}
    E = {str(i): [] for i in range(n)}
    for u in V:
        for v in V:
            if u != v and random.random() < density:
                E[u].append((v, random.randint(1, max_w)))
    return V, E       

#demo
if __name__ == "__main__":
    V = {'1', '2', '3', '4', '5'}
    E = {
        '1': [('2', 4), ('3', 2), ('4', 6), ('5', 8)],
        '2': [('4', 4), ('5', 3)],
        '3': [('4', 1)],
        '4': [('2', 1), ('5', 3)],
        '5': []
    }

    start = '1'
    d, pi = dijkstras(V, E, start)

    print("Shortest distances from start node:", d)
    print("Predecessors in shortest path tree:", pi)
    print("Path 1 → 5:", reconstruct_path(pi, start, '5'))





    #empirical testing

    print("\n\n\n---------- Empirical Testing ----------")

    for n in [100, 500, 1000, 2000, 4000, 8000, 16000, 32000]:
        V, E = generate_random_graph(n, density=0.05)
        start = '0'
        t0 = time.time()
        dijkstras(V, E, start)
        t1 = time.time()
        print(f"n={n}, |E|≈{sum(len(E[v]) for v in E)}, time={t1-t0:.4f}s")
