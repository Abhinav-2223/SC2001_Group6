'''
(a) Suppose the input graph G = (V, E) is stored in an adjacency matrix and we 
    use an array for the priority queue. 
    
    Implement the Dijkstra’s algorithm using this setting  and  analyze  its  time  complexity  
    with  respect  to |V| and  |E| both theoretically and empirically.
'''

# implementation:


# adj_matrix = adjacency matrix of the graph
# start = starting vertex

adj_matrix_test = [
    [0, 4, 2, 6, 8],
    [float('inf'), 0, float('inf'), 4, 3],
    [float('inf'), float('inf'), 0, 1, float('inf')],
    [float('inf'), 1, float('inf'), 0, 3],
    [float('inf'), float('inf'), float('inf'), float('inf'), 0]
]

start = 0  # starting from vertex '1' which is index 0


def dijkstras(adj_matrix, start):
    n = len(adj_matrix)         # num of vertices
    d = [ float('inf')] * n     # list of shortest distances from start
    pi = [ None ] * n           # list of predecessors in the shortest path
    d[start] = 0
    S = [False ] * n            # visited set as a list of booleans

    iteration = 0
    

    while iteration < n:
        # array based priority queue: find the unvisited vertex with the smallest distance
        min_dist = float('inf')
        u = -1

        for vertex in range(n):
            if not S[vertex] and d[vertex] < min_dist:
                min_dist = d[vertex]
                u = vertex
        if u == -1:  # all remaining vertices are inaccessible from start
            break

        S[u] = True

        # relax all adjacent vertices of u
        for v in range(n):
            if adj_matrix[u][v] != float('inf'):  # there is an edge from u to v
                if d[u] + adj_matrix[u][v] < d[v]: # relax edge
                    d[v] = d[u] + adj_matrix[u][v]
                    pi[v] = u


        iteration += 1
        print_d_and_pi(d, pi, iteration)
        
    return d, pi


def print_d_and_pi(d, pi, iteration):
        print(f"Iteration {iteration}:")
        print("d:", d)
        print("pi:", pi)
        print()






# function to check if dijkstra's algorithm works correctly

# function to make a random adjacency matrix
def make_random_adj_matrix(num_vertices, max_weight=10, edge_prob=0.3):
    import random

    adj_matrix = [] # with row <-> and column ^

    for i in range(num_vertices):
        row = []
        for j in range(num_vertices):
            if i == j:
                row.append(0) # distance to self is 0, eg. B to B is 0
            else:
                if random.random() < edge_prob: # probability of edge existing
                    row.append(random.randint(1, max_weight))
                else:
                    row.append(float('inf'))

        adj_matrix.append(row)

    return adj_matrix

# adj_matrix = make_random_adj_matrix(5)
# print (adj_matrix)


# Test the algorithm
if __name__ == "__main__":
    print("Testing Dijkstra's Algorithm with Array-based Priority Queue")
    print("Adjacency Matrix:", adj_matrix_test)
    print("Starting vertex:", start)
    print()
    
    distances, predecessors = dijkstras(adj_matrix_test, start)
    
    print("Final Results:")
    print("Shortest distances:", distances)
    print("Predecessors:", predecessors)
