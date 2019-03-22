def bubble_sort(items):
    length = len(items)
    for i in range(0,length):
        swapped = False
        for element in range(0,length-i-1):
            if items[element]> items[element + 1]:
                hold= items[element + 1]
                items[element + 1]=items[element]
                items[element]= hold
                swapped= True
        if not swapped:break
    return items

def merge_sort(items):
  """ Return array of items, sorted in ascending order """
  if len(items) >1:
      mid = len(items)//2 #Finding the mid of the array
      L = items[:mid] # Dividing the array elements
      R = items[mid:] # into 2 halves
      merge_sort(L) # Sorting the first half
      merge_sort(R) # Sorting the second half
      i = j = k = 0
      # Copy data to temp arrays L[] and R[]
      while i < len(L) and j < len(R):
          if L[i] < R[j]:
              items[k] = L[i]
              i+=1
          else:
              items[k] = R[j]
              j+=1
          k+=1
      # Checking if any element was left
      while i < len(L):
          items[k] = L[i]
          i+=1
          k+=1
      while j < len(R):
          items[k] = R[j]
          j+=1
          k+=1
  return items



def quick_sort(items,index=-1):
    '''Return array of items, sorted in ascending order'''

    len_i = len(items)

    if len_i <= 1:
        # Logic Error
        # identified with test run [1,5,4,3, 2, 6, 5, 4, 3, 8, 6, 5, 3, 1]
        # len <= 1
        return items

    pivot = items[index]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
    i2 = merge_sort(items[mid_point:])

    return merge(i1, i2)
