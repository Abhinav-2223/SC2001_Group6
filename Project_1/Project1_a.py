import random, sys, time
from dataclasses import dataclass
from typing import List

# Increase recursion limit for big n
sys.setrecursionlimit(20_000_000)

# ---------------- Counter ----------------
@dataclass
class Counter:
    comps: int = 0
    def add(self, k: int = 1):
        self.comps += k

# ---------------- Insertion Sort ----------------
def insertion_sort_count(a: List[int], left: int, right: int, c: Counter):
    for i in range(left + 1, right + 1):
        key = a[i]
        j = i - 1
        while j >= left:
            c.add(1)                # compare a[j] > key
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key

# ---------------- Merge ----------------
def merge_count(a: List[int], left: int, mid: int, right: int, c: Counter):
    L = a[left:mid + 1]
    R = a[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        c.add(1)
        if L[i] <= R[j]:
            a[k] = L[i]; i += 1
        else:
            a[k] = R[j]; j += 1
        k += 1
    while i < len(L):
        a[k] = L[i]; i += 1; k += 1
    while j < len(R):
        a[k] = R[j]; j += 1; k += 1

# ---------------- Hybrid MergeSort ----------------
def hybrid_sort_count(a: List[int], left: int, right: int, S: int, c: Counter):
    if right - left + 1 <= S:
        insertion_sort_count(a, left, right, c)
        return
    mid = (left + right) // 2
    hybrid_sort_count(a, left, mid, S, c)
    hybrid_sort_count(a, mid + 1, right, S, c)
    merge_count(a, left, mid, right, c)

def hybrid_sort(a: List[int], S: int = 32):
    """Sorts list a in-place using hybrid MergeSort+Insertion Sort with cutoff S."""
    c = Counter(0)
    hybrid_sort_count(a, 0, len(a) - 1, S, c)
    return c.comps

# ---------------- Test Harness ----------------
if __name__ == "__main__":
    sizes = [1_000, 10_000, 100_000, 1_000_000, 10_000_000]  # extend up to 10_000_000 if your machine can handle
    S_values = [8, 16, 24, 32, 48, 64]

    for S in S_values:
        print(f"\n=== Testing Hybrid Sort with S={S} ===")
        for n in sizes:
            arr = [random.randint(1, 10**9) for _ in range(n)]
            t0 = time.perf_counter()
            comps = hybrid_sort(arr, S)
            t1 = time.perf_counter()
            print(f"n={n:,} | comps={comps:,} | time={t1 - t0:.3f}s")
