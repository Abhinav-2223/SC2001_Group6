import numpy as np

import time

from playsound import playsound as psnd

import AppKit
        

def MISort(arr, left, right, thresh):
  if(right - left + 1) <= thresh:
    insertion_sort(arr, left, right)
  else:
    mid = (left + right) // 2
    MISort(arr, left, mid, thresh)
    MISort(arr, mid + 1, right, thresh)
    Merge(arr, left, mid, right)



def insertion_sort(arr, left, right):
  for i in range(left + 1, right + 1): 
    key = arr[i]
    j = i - 1
    while(j >= left and arr[j] > key):
      arr[j+1] = arr[j] 
      j -= 1
    arr[j+1] = key 

def Merge(arr, left, mid, right):
  #temp arrays plz

  n1 = mid - left + 1
  n2 = right - mid
  left_array = [0] * n1 
  right_array = [0] * n2 

  #let's copy the data to temp arrays
  for i in range(n1): 
    left_array[i] = arr[left + i]
  for j in range(n2): 
    right_array[j] = arr[mid + j + 1]

  #merge the temp arrays back into the array

  i = 0
  j = 0
  k = left #init index of the merged subarray


  while i < n1 and j < n2:
    if left_array[i] <= right_array[j]:
      arr[k] = left_array[i]
      i += 1
    else:
      arr[k] = right_array[j]
      j += 1
    k += 1

  #copy the remaining elements of the left array if there's any

  while i < n1:
    arr[k] = left_array[i]
    i += 1
    k += 1

  #copy the remaining elements of the right array if there's any
  while j < n2:
    arr[k] = right_array[j]
    j += 1
    k += 1


if __name__ == "__main__":

    #program_completed = "/Users/macbook/Library/CloudStorage/Dropbox/From NTU OneDrive/Personal Notes/Y2S1 Stuff/SC2001 - Algorithms Design & Analysis/Lab 1 Week 6/ding.wav"
    #program_tooktoolong = "/Users/macbook/Library/CloudStorage/Dropbox/From NTU OneDrive/Personal Notes/Y2S1 Stuff/SC2001 - Algorithms Design & Analysis/Lab 1 Week 6/chord.wav"

    # test with an array
    # array = [12, 11, 13, 5, 6, 7]
    # MISort(array, 0, len(array) - 1, 3)
    # print(array)

    # let's use a super large array to evaluate the performance
    max_range = 10000000
    random_integers = np.random.randint(0, max_range, size=max_range)

    # Start timer
    print("Let's start sorting!")
    start_time = time.time()

    MISort(random_integers, 0, len(random_integers) - 1, 128)

    end_time = time.time()
    time_elapsed = end_time - start_time

    if time_elapsed < 5.0:
        print(f"Whew, that was fast bro\n\nTime elapsed: {time_elapsed} seconds")
        #psnd(program_completed)
        
    else:
        
        print(f"No way bro, that's one big array!\n\nTime elapsed: {time_elapsed} seconds")
        #psnd(program_tooktoolong)

