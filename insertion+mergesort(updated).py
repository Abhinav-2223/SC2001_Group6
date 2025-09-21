import matplotlib.pyplot as plt # for plotting graphs
import random # for generating random test cases
import time # for measuring execution time

# ---------- Counting helper Class ----------
class ComparisonsCounter:
    def __init__(self): 
        self.count = 0

    def increment(self, k=1): 
        self.count += k

    def returnKeyComparisons(self): 
        return self.count




def insertion_sort(arr, c = None):
    """Sorts an array using the insertion sort algorithm."""
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if c: 
                c.increment() # count 'key < arr[j]'

            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
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
        if A1[i] < A2[j]: # compare elements from both arrays and append the smaller one to the sorted list
            sorted.append(A1[i])
            i += 1
        else:
            sorted.append(A2[j])
            j += 1
    sorted.extend(A1[i:])
    sorted.extend(A2[j:])
    return sorted



def insertion_merge_hybird_sort(arr, S=16): # use S=16 as default threshold
    """Sorts an array using mergesort splitting until subarrays are size S, then use Insertion sort for those small subarrays, then merge back up."""
    if len(arr) <= S:
        sorted_arr, comparisons = insertion_sort(arr) # use the insertion sort for the broken up arrays that are <= S size
        return sorted_arr, comparisons
    else:
        mid = len(arr) // 2 # find the middle index

        # split and sort the two halves recursively, then merge and return total comparisons
        # also count comparisons made in the insertion sorts
        left, comp_left = insertion_merge_hybird_sort(arr[:mid], S)
        right, comp_right = insertion_merge_hybird_sort(arr[mid:], S)
        merged = merge(left, right)

        return merged, comp_left + comp_right # returns the merged sorted array and total comparisons made in the hybrid sort


def sorted_check(arr):
    """Helper function to check if an array is sorted."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# S = 16 # threshold for switching to insertion sort

#arr = [-10, -5, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr_size = list(range(1000, 10_000_001, (10_000_000 - 1000) // 9))

# arr_size: 1000 to 10_000 (interval 1000), 10_000 to 100_000 (interval 10_000),
# 100_000 to 1_000_000 (interval 100_000), 1_000_000 to 10_000_000 (interval 1_000_000)

arr_size = list(range(1000, 10_001, 1000)) \
         + list(range(20_000, 100_001, 10_000)) \
         + list(range(200_000, 1_000_001, 100_000)) \
         + list(range(2_000_000, 10_000_001, 1_000_000))

# 1000 to 10,000 - 10 sizes
# 20,000 to 100,000 - 9 sizes
# 200,000 to 1,000,000 - 9 sizes
# 2,000,000 to 10,000,000 - 9 sizes
# total of 37 different sizes of arrays to test


list_of_arrays = []

for i in arr_size:
    arr = [random.randint(1, i) for _ in range(i)]
    list_of_arrays.append(arr)


if __name__ == "__main__":
    sizes = []
    comparisons_list = []
    times_list = []

    for arr in list_of_arrays:
        # print('-------------------------------')
        # print("Array size:", len(arr))

        start = time.perf_counter()
        sorted_arr, comparisons = insertion_merge_hybird_sort(arr)
        end = time.perf_counter()
        sizes.append(len(arr))
        comparisons_list.append(comparisons)
        times_list.append(end - start)

    # Plot array size vs time
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, times_list, marker='o')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Array Size vs Time (S=16)')
    plt.grid(True)
    plt.show()

    # Plot array size vs key comparisons
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, comparisons_list, marker='o', color='orange')
    plt.xlabel('Array Size')
    plt.ylabel('Key Comparisons')
    plt.title('Array Size vs Key Comparisons (S=16)')
    plt.grid(True)
    plt.show()















'''When it runs: 

Array size: 1000
Sorted check: True
Array size: 1112000
Sorted check: True
Array size: 2223000
Sorted check: True
Array size: 3334000
Sorted check: True
Array size: 4445000
Sorted check: True
Array size: 5556000
Sorted check: True
Array size: 6667000
Sorted check: True
Array size: 7778000
Sorted check: True
Array size: 8889000
Sorted check: True
Array size: 10000000
Sorted check: True

'''
'''
Array size: 1000
Key comparisons: 4470
Sorted check: True
Array size: 2000
Key comparisons: 8748
Sorted check: True
Array size: 3000
Key comparisons: 10472
Sorted check: True
Array size: 4000
Key comparisons: 17499
Sorted check: True
Array size: 5000
Key comparisons: 14337
Sorted check: True
Array size: 6000
Key comparisons: 20488
Sorted check: True
Array size: 7000
Key comparisons: 27341
Sorted check: True
Array size: 8000
Key comparisons: 35134
Sorted check: True
Array size: 9000
Key comparisons: 23603
Sorted check: True
Array size: 10000
Key comparisons: 28785
Sorted check: True
Array size: 20000
Key comparisons: 58462
Sorted check: True
Array size: 30000
Key comparisons: 126644
Sorted check: True
Array size: 40000
Key comparisons: 115968
Sorted check: True
Array size: 50000
Key comparisons: 178132
Sorted check: True
Array size: 60000
Key comparisons: 251374
Sorted check: True
Array size: 70000
Key comparisons: 179926
Sorted check: True
Array size: 80000
Key comparisons: 231375
Sorted check: True
Array size: 90000
Key comparisons: 289095
Sorted check: True
Array size: 100000
Key comparisons: 354821
Sorted check: True
Array size: 200000
Key comparisons: 708557
Sorted check: True
Array size: 300000
Key comparisons: 818614
Sorted check: True
Array size: 400000
Key comparisons: 1419704
Sorted check: True
Array size: 500000
Array size: 200000
Key comparisons: 708557
Sorted check: True
Array size: 300000
Key comparisons: 818614
Sorted check: True
Array size: 400000
Key comparisons: 1419704
Sorted check: True
Array size: 500000
Key comparisons: 708557
Sorted check: True
Array size: 300000
Key comparisons: 818614
Sorted check: True
Array size: 400000
Key comparisons: 1419704
Sorted check: True
Array size: 500000
Sorted check: True
Array size: 300000
Key comparisons: 818614
Sorted check: True
Array size: 400000
Key comparisons: 1419704
Sorted check: True
Array size: 500000
Array size: 300000
Key comparisons: 818614
Sorted check: True
Array size: 400000
Key comparisons: 1419704
Sorted check: True
Array size: 500000
Key comparisons: 818614
Sorted check: True
Array size: 400000
Key comparisons: 1419704
Sorted check: True
Array size: 500000
Sorted check: True
Array size: 400000
Key comparisons: 1419704
Sorted check: True
Array size: 500000
Array size: 400000
Key comparisons: 1419704
Sorted check: True
Array size: 500000
Key comparisons: 2174374
Sorted check: True
Key comparisons: 1419704
Sorted check: True
Array size: 500000
Key comparisons: 2174374
Sorted check: True
Array size: 600000
Key comparisons: 1638491
Array size: 500000
Key comparisons: 2174374
Sorted check: True
Array size: 600000
Key comparisons: 1638491
Sorted check: True
Array size: 700000
Key comparisons: 2174374
Sorted check: True
Array size: 600000
Key comparisons: 1638491
Sorted check: True
Array size: 700000
Array size: 600000
Key comparisons: 1638491
Sorted check: True
Array size: 700000
Key comparisons: 2200983
Sorted check: True
Array size: 800000
Sorted check: True
Array size: 700000
Key comparisons: 2200983
Sorted check: True
Array size: 800000
Key comparisons: 2200983
Sorted check: True
Array size: 800000
Key comparisons: 2841224
Sorted check: True
Sorted check: True
Array size: 800000
Key comparisons: 2841224
Sorted check: True
Key comparisons: 2841224
Sorted check: True
Sorted check: True
Array size: 900000
Key comparisons: 3554914
Key comparisons: 3554914
Sorted check: True
Array size: 1000000
Sorted check: True
Array size: 1000000
Array size: 1000000
Key comparisons: 4352030
Key comparisons: 4352030
Sorted check: True
Array size: 2000000
Key comparisons: 8695029
Sorted check: True
Array size: 3000000
Key comparisons: 10050604
Sorted check: True
Array size: 4000000
Key comparisons: 17398388
Sorted check: True
Array size: 5000000
Key comparisons: 14195174
Sorted check: True
Array size: 6000000
Key comparisons: 20096781
Sorted check: True
Array size: 7000000
Key comparisons: 26962133
Sorted check: True
Array size: 8000000
Key comparisons: 34790646
Sorted check: True
Array size: 9000000
Key comparisons: 23206462
Sorted check: True
Array size: 10000000
Key comparisons: 28389376
Sorted check: True




'''



