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


def dijkstras(adj_matrix, start, verbose=True):
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
                if d[u] + adj_matrix[u][v] < d[v]: # relax edge , meaning found a shorter path to v through u
                    d[v] = d[u] + adj_matrix[u][v]
                    pi[v] = u


        iteration += 1
        if verbose:  # Only print if verbose mode is on
            print_d_and_pi(d, pi, iteration)
        
    return d, pi


def print_d_and_pi(d, pi, iteration):
        print(f"Iteration {iteration}:")
        print("d:", d)
        print("pi:", pi)
        print()






# function to check if dijkstra's algorithm works correctly

def verify_with_floyd_warshall(adj_matrix, start, computed_distances):
    """
    Use Floyd-Warshall algorithm to compute all-pairs shortest paths
    and compare distances from start vertex
    """
    n = len(adj_matrix)
    
    # Initialize distance matrix for Floyd-Warshall
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Copy adjacency matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif adj_matrix[i][j] != float('inf'):
                dist[i][j] = adj_matrix[i][j]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Compare distances from start vertex
    floyd_distances = dist[start]
    
    for i in range(n):
        if computed_distances[i] != floyd_distances[i]:
            print(f"ERROR: Vertex {i} - Floyd-Warshall: {floyd_distances[i]}, Dijkstra: {computed_distances[i]}")
            return False
    
    print("✓ Dijkstra matches Floyd-Warshall results!")
    return True




# function to make a random adjacency matrix
def make_random_adj_matrix(num_vertices, max_weight=10, density=0.5):
    """
    Generate a random adjacency matrix for a directed graph.
    
    Parameters:
    -----------
    num_vertices : int
        Number of vertices in the graph (|V|)
    max_weight : int
        Maximum weight for edges (default: 10)
    density : float
        Graph density between 0.0 and 1.0 (default: 0.5)
        - density = 0.0: No edges (empty graph)
        - density = 0.5: Half of possible edges exist (moderate)
        - density = 1.0: All possible edges exist (complete graph)
        
    Graph Density Definition:
    -------------------------
    Density = |E| / |E_max|
    
    For a DIRECTED graph:
        |E_max| = V × (V - 1)  [maximum possible edges, excluding self-loops]
        Density = |E| / [V × (V - 1)]
    
    For an UNDIRECTED graph:
        |E_max| = V × (V - 1) / 2
        Density = |E| / [V × (V - 1) / 2]
    
    Examples:
    ---------
    - Sparse graph: density ≈ 0.1 to 0.3 (few edges)
    - Medium graph: density ≈ 0.4 to 0.6 (moderate edges)
    - Dense graph: density ≈ 0.7 to 1.0 (many edges)
    
    Returns:
    --------
    adj_matrix : list of lists
        Adjacency matrix where adj_matrix[i][j] is the weight of edge from i to j
        - 0 indicates no self-loop (i == j)
        - float('inf') indicates no edge exists
        - positive value indicates edge weight
    """
    import random

    adj_matrix = []  # adjacency matrix: row <-> from vertex, column ^ to vertex

    for i in range(num_vertices):
        row = []
        for j in range(num_vertices):
            if i == j:
                row.append(0)  # distance to self is 0 (no self-loops)
            else:
                # Use density as the probability of edge existing
                rand_prob = random.random()
                if rand_prob < density:  # edge exists with probability = density
                    row.append(random.randint(1, max_weight))
                else:
                    row.append(float('inf'))  # no edge

        adj_matrix.append(row)

    return adj_matrix


def calculate_graph_density(adj_matrix):
    """
    Calculate the actual density of a graph from its adjacency matrix.
    
    Returns:
    --------
    density : float
        Actual density of the graph = |E| / |E_max|
    edge_count : int
        Number of edges in the graph (|E|)
    max_edges : int
        Maximum possible edges (|E_max|)
    """
    n = len(adj_matrix)
    edge_count = 0
    
    # Count edges (excluding self-loops)
    for i in range(n):
        for j in range(n):
            if i != j and adj_matrix[i][j] != float('inf') and adj_matrix[i][j] > 0:
                edge_count += 1
    
    max_edges = n * (n - 1)  # maximum edges in directed graph (no self-loops)
    density = edge_count / max_edges if max_edges > 0 else 0
    
    return density, edge_count, max_edges

# adj_matrix = make_random_adj_matrix(5)
# print (adj_matrix)


"""
=============================================================================
THEORETICAL TIME COMPLEXITY ANALYSIS
=============================================================================

Dijkstra's Algorithm with Adjacency Matrix + Array-based Priority Queue

Operations:
-----------
1. Initialization:
   - Create arrays d, pi, S: O(V)
   
2. Main Loop (runs V times):
   For each of V iterations:
   
   a) Extract-Min (find unvisited vertex with minimum distance):
      - Scan through all V vertices: O(V)
   
   b) Mark vertex as visited: O(1)
   
   c) Edge Relaxation (check all adjacent vertices):
      - Check all V entries in adjacency matrix row: O(V)
      - For each edge that exists, update distance: O(1)

Time Complexity Breakdown:
-------------------------
- Initialization: O(V)
- Main Loop: V iterations × [O(V) extract-min + O(V) relaxation]
            = V × O(V)
            = O(V²)

Total Time Complexity: O(V) + O(V²) = O(V²)

Relationship with |E|:
---------------------
- The algorithm checks all V² possible edges in the adjacency matrix
- Actual edge relaxations: O(E), but we check O(V²) matrix entries
- Final complexity: O(V²) regardless of |E|
- This is optimal when E ≈ V² (dense graphs)

Space Complexity: O(V²) for adjacency matrix + O(V) for arrays = O(V²)

=============================================================================
"""

# Empirical analysis function
def empirical_time_analysis():
    """
    Empirically measure running time vs |V| and |E| to verify O(V²) complexity
    """
    import time
    import matplotlib.pyplot as plt
    
    print("\n" + "="*80)
    print("EMPIRICAL TIME COMPLEXITY ANALYSIS")
    print("="*80)
    
    # Test 1: Vary |V| with different densities
    print("\nTest 1: Time Complexity vs |V| for Different Graph Densities")
    print("-" * 80)
    
    vertex_sizes = [10, 20, 50, 100, 200, 300, 400, 500]
    densities = [0.2, 0.5, 0.8]  # sparse, medium, dense
    
    results = {density: {'V': [], 'E': [], 'time': []} for density in densities}
    
    for density in densities:
        print(f"\nDensity = {density} ({'SPARSE' if density < 0.3 else 'MEDIUM' if density < 0.7 else 'DENSE'}):")
        print(f"{'|V|':<8} {'|E|':<10} {'Time (s)':<12} {'Time/V²':<12}")
        print("-" * 50)
        
        for n in vertex_sizes:
            adj_matrix = make_random_adj_matrix(n, density=density)
            actual_density, edge_count, _ = calculate_graph_density(adj_matrix)
            
            start_time = time.time()
            dijkstras(adj_matrix, 0, verbose=False)
            end_time = time.time()
            
            elapsed = end_time - start_time
            normalized = elapsed / (n * n) if n > 0 else 0
            
            results[density]['V'].append(n)
            results[density]['E'].append(edge_count)
            results[density]['time'].append(elapsed)
            
            print(f"{n:<8} {edge_count:<10} {elapsed:<12.6f} {normalized:<12.9f}")
    
    # Test 2: Verify O(V²) relationship
    print("\n\nTest 2: Verifying O(V²) Time Complexity")
    print("-" * 80)
    print("If algorithm is O(V²), then Time ≈ c × V² for some constant c")
    print()
    
    density = 0.5
    print(f"Using density = {density}")
    print(f"{'|V|':<8} {'V²':<12} {'Time (s)':<12} {'Ratio (Time/V²)':<15}")
    print("-" * 60)
    
    for n in vertex_sizes:
        adj_matrix = make_random_adj_matrix(n, density=density)
        
        start_time = time.time()
        dijkstras(adj_matrix, 0, verbose=False)
        end_time = time.time()
        
        elapsed = end_time - start_time
        v_squared = n * n
        ratio = elapsed / v_squared if v_squared > 0 else 0
        
        print(f"{n:<8} {v_squared:<12} {elapsed:<12.6f} {ratio:<15.9f}")
    
    print("\nNote: The ratio Time/V² should be roughly constant, confirming O(V²) complexity")
    
    # Test 3: Effect of |E| (edge count)
    print("\n\nTest 3: Time vs |E| (with fixed |V|)")
    print("-" * 80)
    print("For adjacency matrix implementation, time should be O(V²) regardless of |E|")
    print()
    
    fixed_v = 200
    test_densities = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    
    print(f"Fixed |V| = {fixed_v}")
    print(f"{'Density':<10} {'|E|':<10} {'Time (s)':<12} {'Time/V²':<12}")
    print("-" * 50)
    
    for density in test_densities:
        adj_matrix = make_random_adj_matrix(fixed_v, density=density)
        _, edge_count, _ = calculate_graph_density(adj_matrix)
        
        start_time = time.time()
        dijkstras(adj_matrix, 0, verbose=False)
        end_time = time.time()
        
        elapsed = end_time - start_time
        normalized = elapsed / (fixed_v * fixed_v)
        
        print(f"{density:<10.1f} {edge_count:<10} {elapsed:<12.6f} {normalized:<12.9f}")
    
    print("\nObservation: Time remains O(V²) regardless of edge count |E|")
    print("This confirms the algorithm checks all V² matrix entries, not just |E| edges")
    
    # Plotting results
    try:
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Plot 1: Time vs |V| for different densities
        for density in densities:
            axes[0].plot(results[density]['V'], results[density]['time'], 
                        marker='o', label=f'Density {density}')
        axes[0].set_xlabel('Number of Vertices (|V|)')
        axes[0].set_ylabel('Time (seconds)')
        axes[0].set_title('Time Complexity vs |V| (Different Densities)')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Plot 2: Time vs |E| (should show independence)
        axes[1].scatter([results[d]['E'][i] for d in densities for i in range(len(results[d]['E']))],
                       [results[d]['time'][i] for d in densities for i in range(len(results[d]['time']))],
                       alpha=0.6)
        axes[1].set_xlabel('Number of Edges (|E|)')
        axes[1].set_ylabel('Time (seconds)')
        axes[1].set_title('Time vs |E| (Adjacency Matrix Implementation)')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('dijkstra_complexity_analysis_part_a.png', dpi=300)
        print("\n✓ Plots saved as 'dijkstra_complexity_analysis_part_a.png'")
        plt.show()
    except ImportError:
        print("\n(matplotlib not available for plotting)")
    
    print("\n" + "="*80)
    print("CONCLUSION:")
    print("="*80)
    print("✓ Empirical results confirm O(V²) time complexity")
    print("✓ Time is independent of |E| (edge count)")
    print("✓ Algorithm is optimal for dense graphs where |E| ≈ V²")
    print("="*80 + "\n")


# Test the algorithm
if __name__ == "__main__":
    # Simple test
    print("="*80)
    print("SIMPLE TEST EXAMPLE")
    print("="*80)
    
    test_density = 0.5
    adj_matr = make_random_adj_matrix(5, density=test_density)
    
    print("Testing Dijkstra's Algorithm with Array-based Priority Queue")
    print(f"Target Density: {test_density}")
    print("Adjacency Matrix:", adj_matr)
    
    # Calculate actual density
    actual_density, edge_count, max_edges = calculate_graph_density(adj_matr)
    print(f"\nGraph Statistics:")
    print(f"  Vertices (|V|): {len(adj_matr)}")
    print(f"  Edges (|E|): {edge_count}")
    print(f"  Max Possible Edges: {max_edges}")
    print(f"  Actual Density: {actual_density:.2f} ({edge_count}/{max_edges})")
    
    if actual_density < 0.3:
        print(f"  Graph Type: SPARSE")
    elif actual_density < 0.7:
        print(f"  Graph Type: MEDIUM")
    else:
        print(f"  Graph Type: DENSE")
    
    print(f"\nStarting vertex: {start}")
    print()
    
    distances, predecessors = dijkstras(adj_matr, start)
    
    print("Final Results:")
    print("Shortest distances:", distances)
    print("Predecessors:", predecessors)

    print("\nVerification:")
    verify_with_floyd_warshall(adj_matr, start, distances)
    
    # Run empirical analysis
    print("\n" + "="*80)
    run_analysis = input("Run empirical time complexity analysis? (y/n): ")
    if run_analysis.lower() == 'y':
        empirical_time_analysis()