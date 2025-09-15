import random # for generating random test cases
import time # for measuring execution time
import matplotlib.pyplot as plt # for plotting graphs



def insertion_sort(arr):
    """Sorts an array using the insertion sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def mergesort(A):
    if (len(A) <= 1): 
        return A
    mid = len(A) // 2 # find the middle index
     # recursively sort the two halves
    A1 = mergesort(A[:mid])
    A2 = mergesort(A[mid:])
        # merge the two sorted halves
    return merge(A1, A2)

def merge(A1, A2):
    i, j = 0, 0 # pointers to current index in A1 and A2

    sorted = [] # initialize empty list to store the sorted elements

    while i < len(A1) and j < len(A2):
        if A1[i] < A2[j]:
            sorted.append(A1[i])
            i += 1
        else:
            sorted.append(A2[j])
            j += 1
    sorted.extend(A1[i:])
    sorted.extend(A2[j:])
    return sorted

#S = 8,16,32 or 64  # threshold for switching to insertion sort
# according to empirical testing, the values 16, 32 and 64 are good choices for S, as they give the best time in practice for sorting algorithms, we will use the values in different scenarios to see which works best
# maybe use 64 for > 1,000,000 elements, 32 for > 100,000 elements and 16 for > 10,000 elements 

def insertion_merge_sort(arr):
    """Sorts an array using mergesort splitting until subarrays are size S, then use Insertion sort for those small subarrays, then merge back up."""
    if len(arr) <= 1:
        return arr
    
    if len(arr) > 10_000_000:
        S = 64  # threshold for switching to insertion sort
    elif len(arr) > 100_000:
        S = 32
    elif len(arr) > 10_000:
        S = 16
    else: 
        S = 8
    
           #need to use mergesort first, to breakdown until array sizes are <= S, then use insertion sort on those small arrays, then merge them back up using merge function
    subarrays = collect_subarrays(arr, S) # get list of subarrays of size at most S
    sorted_subarrays = [insertion_sort(subarr) for subarr in subarrays]

    while len(sorted_subarrays) > 1:# merge the sorted subarrays back together
        merged_subarrays = []
        for i in range(0, len(sorted_subarrays), 2):   # step by 2 to merge pairs
            if i + 1 < len(sorted_subarrays):
                merged = merge(sorted_subarrays[i], sorted_subarrays[i + 1])
                merged_subarrays.append(merged) # append the merged result
            else:
                merged_subarrays.append(sorted_subarrays[i])
        sorted_subarrays = merged_subarrays # continue merging until one sorted array remains
    return sorted_subarrays[0] # return that fully sorted array

def collect_subarrays(arr, S): # returns a list of subarrays of arr, each of size at most S
    if len(arr) <= S:
        return [arr]
    mid = len(arr) // 2
    left_subarrays = collect_subarrays(arr[:mid], S)
    right_subarrays = collect_subarrays(arr[mid:], S)
    return left_subarrays + right_subarrays
     

# random test case of random length from 1,000 to 10,000,000 and random integers 
# length = random.randint(1000, 10_000_000)
# test = [random.randint(1, 10**9) for _ in range(length)]

#test = [10, 3, 76, 34, 23, 32, 54, 1, 4, 8]


if __name__ == "__main__":
    # sizes = [1000, 5000, 10000, 20000, 50000,100000, 500000, 1000000, 10000000]  # You can adjust or extend this list
    # S_values = [i for i in range(2,1000)]
    # #[8, 16, 32, 64]
    # times_dict = {S: [] for S in S_values}

    # for S in S_values:
    #     print(f"\nTesting for S = {S}")
    #     for n in sizes:
    #         test = [random.randint(1, 10**9) for _ in range(n)]
    #         # Custom version of insertion_merge_sort with fixed S
    #         def insertion_merge_sort_fixed(arr, S=S):
    #             if len(arr) <= 1:
    #                 return arr
    #             subarrays = collect_subarrays(arr, S)
    #             sorted_subarrays = [insertion_sort(subarr) for subarr in subarrays]
    #             while len(sorted_subarrays) > 1:
    #                 merged_subarrays = []
    #                 for i in range(0, len(sorted_subarrays), 2):
    #                     if i + 1 < len(sorted_subarrays):
    #                         merged = merge(sorted_subarrays[i], sorted_subarrays[i + 1])
    #                         merged_subarrays.append(merged)
    #                     else:
    #                         merged_subarrays.append(sorted_subarrays[i])
    #                 sorted_subarrays = merged_subarrays
    #             return sorted_subarrays[0]

    #         start = time.perf_counter()
    #         insertion_merge_sort_fixed(test, S)
    #         end = time.perf_counter()
    #         times_dict[S].append(end - start)
    #         print(f"S={S}, n={n}: {end - start:.4f} seconds")

    # # Plotting
    # for S in S_values:
    #     plt.plot(sizes, times_dict[S], marker='o', label=f'S={S}')
    # plt.xlabel('Array Length')
    # plt.ylabel('Time (seconds)')
    # plt.title('Sorting Time vs Array Length for Different S')
    # plt.legend()
    # plt.grid(True)
    # plt.show()

    
    sizes = [1000, 5000, 10000, 20000, 50000,100000, 500000, 1000000, 10000000]  # You can adjust or extend this list
    S_values = list(range(2, 1001))
    best_S = []
    best_times = []

    for n in sizes:
        print(f"\nTesting array size n = {n}")
        test = [random.randint(1, 10**9) for _ in range(n)]
        min_time = float('inf')
        min_S = None
        for S in S_values:
            def insertion_merge_sort_fixed(arr, S=S): # Custom version of insertion_merge_sort with fixed S 
                if len(arr) <= 1:
                    return arr
                subarrays = collect_subarrays(arr, S)
                sorted_subarrays = [insertion_sort(subarr) for subarr in subarrays]
                while len(sorted_subarrays) > 1:
                    merged_subarrays = []
                    for i in range(0, len(sorted_subarrays), 2):
                        if i + 1 < len(sorted_subarrays):
                            merged = merge(sorted_subarrays[i], sorted_subarrays[i + 1])
                            merged_subarrays.append(merged)
                        else:
                            merged_subarrays.append(sorted_subarrays[i])
                    sorted_subarrays = merged_subarrays
                return sorted_subarrays[0]

            arr_copy = test.copy()
            start = time.perf_counter()
            insertion_merge_sort_fixed(arr_copy, S)
            end = time.perf_counter()
            elapsed = end - start
            if elapsed < min_time:
                min_time = elapsed
                min_S = S
        best_S.append(min_S)
        best_times.append(min_time)
        print(f"Best S for n={n}: {min_S} (time: {min_time:.4f} seconds)")

    plt.plot(sizes, best_S, marker='o')
    plt.xlabel('Array Length')
    plt.ylabel('Best S')
    plt.title('Best S vs Array Length')
    plt.grid(True)
    plt.show()




