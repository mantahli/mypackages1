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
    if len(items)>1:
        mid=len(items)//2
        myL=items[:mid]
        myR=items[mid:]
        merge_sort(myL)
        merge_sort(myR)

        i=j=k=0

        while i < len(myL) and j < len(myR):
            if myL[i] < myR[j]:
                items[k] = myL[i]
                i+=1
            else:
                items[k] = myR[j]
                j+=1
            k+=1
        while i < len(myL):
            items[k] = myL[i]
            i+=1
            k+=1
        while j < len(myR):
            items[k] = myR
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
