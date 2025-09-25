import random, time
import matplotlib.pyplot as plt

# ---------- Counting helper ----------
class ComparisonsCounter:
    def __init__(self): self.count = 0
    def increment(self, k=1): self.count += k
    def returnKeyComparisons(self): return self.count

# ---------- Insertion sort (counts comparisons in inner while) ----------
def insertion_sort(a, c=None):
    n = len(a)
    for i in range(1, n):
        key = a[i]; j = i - 1
        while j >= 0:
            if c: c.increment()            # count 'key < a[j]'
            if key < a[j]:
                a[j+1] = a[j]; j -= 1
            else:
                break
        a[j+1] = key
    return a

# ---------- Merge (counts comparisons during merge) ----------
def merge(a, b, c=None):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if c: c.increment()                # count 'a[i] < b[j]'
        if a[i] < b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out

# ---------- Traditional Hybrid sort: mergesort recursion with insertion sort at leaves ----------
def hybrid_sort(a, S, c=None):
    # If array size <= S, use insertion sort (base case)
    if len(a) <= S:
        return insertion_sort(a, c)
    
    # Otherwise, use mergesort approach: split, recurse, merge
    mid = len(a) // 2
    left = hybrid_sort(a[:mid], S, c)
    right = hybrid_sort(a[mid:], S, c)
    return merge(left, right, c)

# ---------- Part C experiments ----------
if __name__ == "__main__":
    random.seed(42) # for reproducibility

    # -----------------------------------------------------------
    # (c)(i): S fixed, comparisons vs n
    # -----------------------------------------------------------
    S_FIXED = 16
    sizes = [1_000, 5_000, 10_000, 20_000, 50_000, 100_000]  # expand if your machine can
    comps_n = []
    for n in sizes:
        arr = [random.randint(1, 10**9) for _ in range(n)]
        ctr = ComparisonsCounter()
        hybrid_sort(arr, S_FIXED, ctr)
        comps_n.append(ctr.returnKeyComparisons())

    plt.figure(figsize=(12, 5))
    plt.plot(sizes, comps_n, marker='o')
    plt.title('Graph of number of Key Comparisons against different Input List Sizes N')
    plt.xlabel('Input List Size N')
    plt.ylabel('Number of Key Comparisons')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # -----------------------------------------------------------
    # (c)(ii): n fixed, comparisons vs S
    # -----------------------------------------------------------
    n_FIXED = 20_000
    base = [random.randint(1, 10**9) for _ in range(n_FIXED)]
    S_vals = list(range(2, 191))           # 2..190 for a clean step-like curve
    comps_S = []
    for S in S_vals:
        arr = base[:]
        ctr = ComparisonsCounter()
        hybrid_sort(arr, S, ctr)
        comps_S.append(ctr.returnKeyComparisons())

    plt.figure(figsize=(12, 5))
    plt.plot(S_vals, comps_S, marker='o')
    plt.title('Graph of number of Key Comparisons over different Threshold Values S')
    plt.xlabel('Threshold Values S')
    plt.ylabel('Number of Key Comparisons')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # -----------------------------------------------------------
    # (c)(iii): For each n, find the S that MINIMIZES key comparisons
    # -----------------------------------------------------------
    sizes_c3   = [1_000, 5_000, 10_000, 20_000, 50_000, 100_000]  # reuse / expand as needed
    sweep_S    = list(range(2, 101))                               # you can widen to 190 if you like
    best_S     = []
    best_comps = []
    best_time  = []

    for n in sizes_c3:
        base = [random.randint(1, 10**9) for _ in range(n)]
        bS = None
        bC = None
        bT = None
        for S in sweep_S:
            arr = base[:]
            ctr = ComparisonsCounter()
            t0 = time.perf_counter()
            hybrid_sort(arr, S, ctr)
            t1 = time.perf_counter()
            C = ctr.returnKeyComparisons()
            T = t1 - t0
            # primary: minimize comparisons; tie-breaker: faster time
            if bC is None or C < bC or (C == bC and T < bT):
                bC, bT, bS = C, T, S
        best_S.append(bS)
        best_comps.append(bC)
        best_time.append(bT)

    # Plot 1 for (c)(iii): Optimal S vs n
    plt.figure(figsize=(12, 5))
    plt.plot(sizes_c3, best_S, marker='o')
    plt.title('Optimal Threshold S vs Input List Size N (min key comparisons)')
    plt.xlabel('Input List Size N')
    plt.ylabel('Optimal Threshold S')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot 2 for (c)(iii): Key Comparisons (at optimal S) vs n
    plt.figure(figsize=(12, 5))
    plt.plot(sizes_c3, best_comps, marker='o')
    plt.title('Number of Key Comparisons vs N (using optimal S per N)')
    plt.xlabel('Input List Size N')
    plt.ylabel('Number of Key Comparisons (at optimal S)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # (Optional) If you want to discuss runtime too:
    # plt.figure(figsize=(12,5))
    # plt.plot(sizes_c3, best_time, marker='o')
    # plt.title('Runtime vs N (using optimal S per N)')
    # plt.xlabel('Input List Size N')
    # plt.ylabel('Time (s)')
    # plt.grid(True)
    # plt.tight_layout()
    # plt.show()
