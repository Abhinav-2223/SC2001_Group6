'''
(a) Suppose the input graph G = (V, E) is stored in an array of adjacency lists and 
    we  use  a  minimizing  heap  for  the  priority  queue.  

    Implement  the  Dijkstra’s algorithm using this setting and analyze its time complexity 
    with respect to |V| and |E| both theoretically and empirically. 
'''

# implementation: 

# import heap 
import heapq

# adjacency list = adjacency list of the graph

V = {'1', '2', '3', '4', '5'}

E = {
    '1': [('2', 4), ('3', 2), ('4', 6), ('5', 8)],
    '2': [('4', 4), ('5', 3)],
    '3': [('4', 1)],
    '4': [('2', 1), ('5', 3)],
    '5': []
}

start = '1'  # starting from vertex '1'

def dijkstras(V, E, start):
    d = {node: float('inf') for node in V}      # distance from start to node
    pi = {node: None for node in V}             # predecessor of node in the shortest path
    d[start] = 0
 
    # Min-heap priority queue: stores (distance, vertex) tuples 
    # heapq maintains min-heap property based on the first element of the tuple (distance)

    pq = [(0, start)]  # priority queue as a min-heap of (distance, vertex)

    visited = set()  # set of visited nodes
    iteration = 0 # to keep track of iterations for printing

    while pq: # iterate through all vertices
        current_dist, u = heapq.heappop(pq) # get the vertex with the smallest distance

        # Add this check:
        if current_dist > d[u]:
            continue  # Skip stale/outdated entry

        if u in visited:
            continue  # skip if already visited

        visited.add(u) # mark vertex 'u' as visited


        for v, w in E[u]:
            if v not in visited:
                new_dist = d[u] + w

                if new_dist < d[v]:
                    d[v] = new_dist
                    pi[v] = u
                    # insert/decrease key operation in the priority queue
                    heapq.heappush(pq, (new_dist, v))

        iteration += 1
        print_d_and_pi(d, pi, iteration)
        
    return d, pi


def print_d_and_pi(d, pi, iteration):
        print(f"Iteration {iteration}:")
        print("d:", d)
        print("pi:", pi)
        print()





if __name__ == "__main__":
    print("Testing Dijkstra's Algorithm with Min-Heap Priority Queue and Adjacency List")
    print("Graph vertices:", V)
    print("Graph edges:", E)
    print("Starting node:", start)
    print("adjecency list:", E)
    print()

    d, pi = dijkstras(V, E, start)
    print("Shortest distances from start node:", d)
    print("Predecessors in shortest path tree:", pi)


