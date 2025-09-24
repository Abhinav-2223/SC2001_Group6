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


'''
Final o/p 

Finding optimal S for each array size...
============================================================
Testing array size: 1,000 (array 1/37)
  → Optimal S = 3, Comparisons = 8,704, Time = 0.0022s
Testing array size: 2,000 (array 2/37)
  → Optimal S = 3, Comparisons = 19,383, Time = 0.0036s
Testing array size: 3,000 (array 3/37)
  → Optimal S = 3, Comparisons = 19,383, Time = 0.0036s
Testing array size: 3,000 (array 3/37)
  → Optimal S = 4, Comparisons = 30,895, Time = 0.0045s
Testing array size: 4,000 (array 4/37)
  → Optimal S = 4, Comparisons = 30,895, Time = 0.0045s
Testing array size: 4,000 (array 4/37)
  → Optimal S = 2, Comparisons = 42,840, Time = 0.0067s
Testing array size: 5,000 (array 5/37)
  → Optimal S = 2, Comparisons = 42,840, Time = 0.0067s
Testing array size: 5,000 (array 5/37)
  → Optimal S = 3, Comparisons = 55,168, Time = 0.0082s
Testing array size: 6,000 (array 6/37)
  → Optimal S = 3, Comparisons = 55,168, Time = 0.0082s
Testing array size: 6,000 (array 6/37)
  → Optimal S = 4, Comparisons = 67,874, Time = 0.0095s
Testing array size: 7,000 (array 7/37)
  → Optimal S = 4, Comparisons = 67,874, Time = 0.0095s
Testing array size: 7,000 (array 7/37)
  → Optimal S = 2, Comparisons = 80,647, Time = 0.0128s
Testing array size: 8,000 (array 8/37)
  → Optimal S = 2, Comparisons = 80,647, Time = 0.0128s
Testing array size: 8,000 (array 8/37)
  → Optimal S = 3, Comparisons = 93,640, Time = 0.0147s
Testing array size: 9,000 (array 9/37)
  → Optimal S = 3, Comparisons = 93,640, Time = 0.0147s
Testing array size: 9,000 (array 9/37)
  → Optimal S = 3, Comparisons = 106,924, Time = 0.0156s
Testing array size: 10,000 (array 10/37)
  → Optimal S = 3, Comparisons = 106,924, Time = 0.0156s
Testing array size: 10,000 (array 10/37)
  → Optimal S = 2, Comparisons = 120,358, Time = 0.0196s
Testing array size: 20,000 (array 11/37)
  → Optimal S = 2, Comparisons = 120,358, Time = 0.0196s
Testing array size: 20,000 (array 11/37)
  → Optimal S = 2, Comparisons = 260,920, Time = 0.0443s
Testing array size: 30,000 (array 12/37)
  → Optimal S = 2, Comparisons = 260,920, Time = 0.0443s
Testing array size: 30,000 (array 12/37)
  → Optimal S = 3, Comparisons = 408,614, Time = 0.0596s
Testing array size: 40,000 (array 13/37)
  → Optimal S = 3, Comparisons = 408,614, Time = 0.0596s
Testing array size: 40,000 (array 13/37)
  → Optimal S = 2, Comparisons = 561,848, Time = 0.0857s
Testing array size: 50,000 (array 14/37)
  → Optimal S = 2, Comparisons = 561,848, Time = 0.0857s
Testing array size: 50,000 (array 14/37)
  → Optimal S = 2, Comparisons = 718,033, Time = 0.1148s
Testing array size: 60,000 (array 15/37)
  → Optimal S = 2, Comparisons = 718,033, Time = 0.1148s
Testing array size: 60,000 (array 15/37)
  → Optimal S = 3, Comparisons = 877,105, Time = 0.1323s
Testing array size: 70,000 (array 16/37)
  → Optimal S = 3, Comparisons = 877,105, Time = 0.1323s
Testing array size: 70,000 (array 16/37)
  → Optimal S = 2, Comparisons = 1,039,111, Time = 0.1709s
Testing array size: 80,000 (array 17/37)
  → Optimal S = 2, Comparisons = 1,039,111, Time = 0.1709s
Testing array size: 80,000 (array 17/37)
  → Optimal S = 2, Comparisons = 1,203,730, Time = 0.1834s
Testing array size: 90,000 (array 18/37)
  → Optimal S = 2, Comparisons = 1,203,730, Time = 0.1834s
Testing array size: 90,000 (array 18/37)
  → Optimal S = 2, Comparisons = 1,369,322, Time = 0.2190s
Testing array size: 100,000 (array 19/37)
  → Optimal S = 2, Comparisons = 1,369,322, Time = 0.2190s
Testing array size: 100,000 (array 19/37)
  → Optimal S = 3, Comparisons = 1,536,205, Time = 0.2168s
Testing array size: 200,000 (array 20/37)
  → Optimal S = 3, Comparisons = 1,536,205, Time = 0.2168s
Testing array size: 200,000 (array 20/37)
  → Optimal S = 2, Comparisons = 3,272,811, Time = 0.5088s
Testing array size: 300,000 (array 21/37)
  → Optimal S = 2, Comparisons = 3,272,811, Time = 0.5088s
Testing array size: 300,000 (array 21/37)
  → Optimal S = 2, Comparisons = 5,084,054, Time = 0.8724s
Testing array size: 400,000 (array 22/37)
  → Optimal S = 2, Comparisons = 5,084,054, Time = 0.8724s
Testing array size: 400,000 (array 22/37)
  → Optimal S = 2, Comparisons = 6,945,223, Time = 1.1486s
Testing array size: 500,000 (array 23/37)
  → Optimal S = 2, Comparisons = 6,945,223, Time = 1.1486s
Testing array size: 500,000 (array 23/37)
  → Optimal S = 3, Comparisons = 8,837,205, Time = 1.3767s
Testing array size: 600,000 (array 24/37)
  → Optimal S = 3, Comparisons = 8,837,205, Time = 1.3767s
Testing array size: 600,000 (array 24/37)
  → Optimal S = 3, Comparisons = 10,769,337, Time = 6.4757s
Testing array size: 700,000 (array 25/37)
  → Optimal S = 3, Comparisons = 10,769,337, Time = 6.4757s
Testing array size: 700,000 (array 25/37)
  → Optimal S = 3, Comparisons = 12,722,184, Time = 2.1696s
Testing array size: 800,000 (array 26/37)
  → Optimal S = 3, Comparisons = 12,722,184, Time = 2.1696s
Testing array size: 800,000 (array 26/37)
  → Optimal S = 3, Comparisons = 14,690,844, Time = 2.3442s
Testing array size: 900,000 (array 27/37)
  → Optimal S = 3, Comparisons = 14,690,844, Time = 2.3442s
Testing array size: 900,000 (array 27/37)
  → Optimal S = 2, Comparisons = 16,678,125, Time = 10.8804s
Testing array size: 1,000,000 (array 28/37)
  → Optimal S = 2, Comparisons = 16,678,125, Time = 10.8804s
Testing array size: 1,000,000 (array 28/37)
  → Optimal S = 3, Comparisons = 18,673,372, Time = 8.7582s
Testing array size: 2,000,000 (array 29/37)
  → Optimal S = 3, Comparisons = 18,673,372, Time = 8.7582s
Testing array size: 2,000,000 (array 29/37)
  → Optimal S = 3, Comparisons = 39,348,254, Time = 18.7097s
Testing array size: 3,000,000 (array 30/37)
  → Optimal S = 3, Comparisons = 39,348,254, Time = 18.7097s
Testing array size: 3,000,000 (array 30/37)
  → Optimal S = 2, Comparisons = 60,820,023, Time = 11.0167s
Testing array size: 4,000,000 (array 31/37)
  → Optimal S = 2, Comparisons = 60,820,023, Time = 11.0167s
Testing array size: 4,000,000 (array 31/37)
  → Optimal S = 3, Comparisons = 82,696,377, Time = 14.1362s
Testing array size: 5,000,000 (array 32/37)
  → Optimal S = 3, Comparisons = 82,696,377, Time = 14.1362s
Testing array size: 5,000,000 (array 32/37)
  → Optimal S = 2, Comparisons = 105,051,125, Time = 19.7445s
Testing array size: 6,000,000 (array 33/37)
  → Optimal S = 2, Comparisons = 105,051,125, Time = 19.7445s
Testing array size: 6,000,000 (array 33/37)
  → Optimal S = 3, Comparisons = 127,641,665, Time = 21.2833s
Testing array size: 7,000,000 (array 34/37)
  → Optimal S = 3, Comparisons = 127,641,665, Time = 21.2833s
Testing array size: 7,000,000 (array 34/37)
  → Optimal S = 3, Comparisons = 150,447,064, Time = 64.4618s
Testing array size: 8,000,000 (array 35/37)
  → Optimal S = 3, Comparisons = 150,447,064, Time = 64.4618s
Testing array size: 8,000,000 (array 35/37)
  → Optimal S = 2, Comparisons = 173,391,457, Time = 31.3063s
Testing array size: 9,000,000 (array 36/37)
  → Optimal S = 2, Comparisons = 173,391,457, Time = 31.3063s
Testing array size: 9,000,000 (array 36/37)
  → Optimal S = 2, Comparisons = 196,642,442, Time = 1062.4486s
Testing array size: 10,000,000 (array 37/37)
  → Optimal S = 2, Comparisons = 196,642,442, Time = 1062.4486s
Testing array size: 10,000,000 (array 37/37)
  → Optimal S = 3, Comparisons = 220,101,178, Time = 159.0308s

============================================================
SUMMARY OF OPTIMAL S VALUES:
============================================================
Array size:      1,000 | Optimal S:   3 | Comparisons:        8,704 | Time:   0.0022s
Array size:      2,000 | Optimal S:   3 | Comparisons:       19,383 | Time:   0.0036s
Array size:      3,000 | Optimal S:   4 | Comparisons:       30,895 | Time:   0.0045s
Array size:      4,000 | Optimal S:   2 | Comparisons:       42,840 | Time:   0.0067s
Array size:      5,000 | Optimal S:   3 | Comparisons:       55,168 | Time:   0.0082s
Array size:      6,000 | Optimal S:   4 | Comparisons:       67,874 | Time:   0.0095s
Array size:      7,000 | Optimal S:   2 | Comparisons:       80,647 | Time:   0.0128s
Array size:      8,000 | Optimal S:   3 | Comparisons:       93,640 | Time:   0.0147s
Array size:      9,000 | Optimal S:   3 | Comparisons:      106,924 | Time:   0.0156s
Array size:     10,000 | Optimal S:   2 | Comparisons:      120,358 | Time:   0.0196s
Array size:     20,000 | Optimal S:   2 | Comparisons:      260,920 | Time:   0.0443s
Array size:     30,000 | Optimal S:   3 | Comparisons:      408,614 | Time:   0.0596s
Array size:     40,000 | Optimal S:   2 | Comparisons:      561,848 | Time:   0.0857s
Array size:     50,000 | Optimal S:   2 | Comparisons:      718,033 | Time:   0.1148s
Array size:     60,000 | Optimal S:   3 | Comparisons:      877,105 | Time:   0.1323s
Array size:     70,000 | Optimal S:   2 | Comparisons:    1,039,111 | Time:   0.1709s
Array size:     80,000 | Optimal S:   2 | Comparisons:    1,203,730 | Time:   0.1834s
Array size:     90,000 | Optimal S:   2 | Comparisons:    1,369,322 | Time:   0.2190s
Array size:    100,000 | Optimal S:   3 | Comparisons:    1,536,205 | Time:   0.2168s
Array size:    200,000 | Optimal S:   2 | Comparisons:    3,272,811 | Time:   0.5088s
Array size:    300,000 | Optimal S:   2 | Comparisons:    5,084,054 | Time:   0.8724s
Array size:    400,000 | Optimal S:   2 | Comparisons:    6,945,223 | Time:   1.1486s
Array size:    500,000 | Optimal S:   3 | Comparisons:    8,837,205 | Time:   1.3767s
Array size:    600,000 | Optimal S:   3 | Comparisons:   10,769,337 | Time:   6.4757s
Array size:    700,000 | Optimal S:   3 | Comparisons:   12,722,184 | Time:   2.1696s
Array size:    800,000 | Optimal S:   3 | Comparisons:   14,690,844 | Time:   2.3442s
Array size:    900,000 | Optimal S:   2 | Comparisons:   16,678,125 | Time:  10.8804s
Array size:  1,000,000 | Optimal S:   3 | Comparisons:   18,673,372 | Time:   8.7582s
Array size:  2,000,000 | Optimal S:   3 | Comparisons:   39,348,254 | Time:  18.7097s
Array size:  3,000,000 | Optimal S:   2 | Comparisons:   60,820,023 | Time:  11.0167s
Array size:  4,000,000 | Optimal S:   3 | Comparisons:   82,696,377 | Time:  14.1362s
Array size:  5,000,000 | Optimal S:   2 | Comparisons:  105,051,125 | Time:  19.7445s
Array size:  6,000,000 | Optimal S:   3 | Comparisons:  127,641,665 | Time:  21.2833s
Array size:  7,000,000 | Optimal S:   3 | Comparisons:  150,447,064 | Time:  64.4618s
Array size:  8,000,000 | Optimal S:   2 | Comparisons:  173,391,457 | Time:  31.3063s
Array size:  9,000,000 | Optimal S:   2 | Comparisons:  196,642,442 | Time: 1062.4486s
Array size: 10,000,000 | Optimal S:   3 | Comparisons:  220,101,178 | Time: 159.0308s

============================================================
FREQUENCY ANALYSIS OF OPTIMAL S VALUES:
============================================================
S =   2: appears 17 times ( 45.9%)
S =   3: appears 18 times ( 48.6%)
S =   4: appears  2 times (  5.4%)

============================================================
RECOMMENDATION:
============================================================
Most frequently optimal S = 3
This S value is optimal for 18 out of 37 array sizes
Recommendation: Use S = 3 as the general-purpose threshold
Average optimal S = 2.6
  → Optimal S = 3, Comparisons = 220,101,178, Time = 159.0308s

============================================================
SUMMARY OF OPTIMAL S VALUES:
============================================================
Array size:      1,000 | Optimal S:   3 | Comparisons:        8,704 | Time:   0.0022s
Array size:      2,000 | Optimal S:   3 | Comparisons:       19,383 | Time:   0.0036s
Array size:      3,000 | Optimal S:   4 | Comparisons:       30,895 | Time:   0.0045s
Array size:      4,000 | Optimal S:   2 | Comparisons:       42,840 | Time:   0.0067s
Array size:      5,000 | Optimal S:   3 | Comparisons:       55,168 | Time:   0.0082s
Array size:      6,000 | Optimal S:   4 | Comparisons:       67,874 | Time:   0.0095s
Array size:      7,000 | Optimal S:   2 | Comparisons:       80,647 | Time:   0.0128s
Array size:      8,000 | Optimal S:   3 | Comparisons:       93,640 | Time:   0.0147s
Array size:      9,000 | Optimal S:   3 | Comparisons:      106,924 | Time:   0.0156s
Array size:     10,000 | Optimal S:   2 | Comparisons:      120,358 | Time:   0.0196s
Array size:     20,000 | Optimal S:   2 | Comparisons:      260,920 | Time:   0.0443s
Array size:     30,000 | Optimal S:   3 | Comparisons:      408,614 | Time:   0.0596s
Array size:     40,000 | Optimal S:   2 | Comparisons:      561,848 | Time:   0.0857s
Array size:     50,000 | Optimal S:   2 | Comparisons:      718,033 | Time:   0.1148s
Array size:     60,000 | Optimal S:   3 | Comparisons:      877,105 | Time:   0.1323s
Array size:     70,000 | Optimal S:   2 | Comparisons:    1,039,111 | Time:   0.1709s
Array size:     80,000 | Optimal S:   2 | Comparisons:    1,203,730 | Time:   0.1834s
Array size:     90,000 | Optimal S:   2 | Comparisons:    1,369,322 | Time:   0.2190s
Array size:    100,000 | Optimal S:   3 | Comparisons:    1,536,205 | Time:   0.2168s
Array size:    200,000 | Optimal S:   2 | Comparisons:    3,272,811 | Time:   0.5088s
Array size:    300,000 | Optimal S:   2 | Comparisons:    5,084,054 | Time:   0.8724s
Array size:    400,000 | Optimal S:   2 | Comparisons:    6,945,223 | Time:   1.1486s
Array size:    500,000 | Optimal S:   3 | Comparisons:    8,837,205 | Time:   1.3767s
Array size:    600,000 | Optimal S:   3 | Comparisons:   10,769,337 | Time:   6.4757s
Array size:    700,000 | Optimal S:   3 | Comparisons:   12,722,184 | Time:   2.1696s
Array size:    800,000 | Optimal S:   3 | Comparisons:   14,690,844 | Time:   2.3442s
Array size:    900,000 | Optimal S:   2 | Comparisons:   16,678,125 | Time:  10.8804s
Array size:  1,000,000 | Optimal S:   3 | Comparisons:   18,673,372 | Time:   8.7582s
Array size:  2,000,000 | Optimal S:   3 | Comparisons:   39,348,254 | Time:  18.7097s
Array size:  3,000,000 | Optimal S:   2 | Comparisons:   60,820,023 | Time:  11.0167s
Array size:  4,000,000 | Optimal S:   3 | Comparisons:   82,696,377 | Time:  14.1362s
Array size:  5,000,000 | Optimal S:   2 | Comparisons:  105,051,125 | Time:  19.7445s
Array size:  6,000,000 | Optimal S:   3 | Comparisons:  127,641,665 | Time:  21.2833s
Array size:  7,000,000 | Optimal S:   3 | Comparisons:  150,447,064 | Time:  64.4618s
Array size:  8,000,000 | Optimal S:   2 | Comparisons:  173,391,457 | Time:  31.3063s
Array size:  9,000,000 | Optimal S:   2 | Comparisons:  196,642,442 | Time: 1062.4486s
Array size: 10,000,000 | Optimal S:   3 | Comparisons:  220,101,178 | Time: 159.0308s

============================================================
FREQUENCY ANALYSIS OF OPTIMAL S VALUES:
============================================================
S =   2: appears 17 times ( 45.9%)
S =   3: appears 18 times ( 48.6%)
S =   4: appears  2 times (  5.4%)

============================================================
RECOMMENDATION:
============================================================
Most frequently optimal S = 3
This S value is optimal for 18 out of 37 array sizes
Recommendation: Use S = 3 as the general-purpose threshold
Average optimal S = 2.6




'''
