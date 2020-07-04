import variables

ua = variables.ua

def mergesort(array, left, right):
    if left < right:
        half = left + int((right - left) / 2)
        
        mergesort(array, left, half)
        mergesort(array, half + 1, right)

        merge(array, left, half, right)
    else:
        return

def merge(array, left, half, right):
    l = left
    r = half + 1
    newarray = []
    while l <= half and r <= right:
        if array[l] < array[r]:
            newarray.append(array[l])
            l += 1
        else:
            newarray.append(array[r])
            r += 1

    while l <= half:
        newarray.append(array[l])
        l += 1

    while r <= right:
        newarray.append(array[r])
        r += 1

    i = 0
    for n in newarray:
        array[left + i] = n
        i += 1


algorithm = "* * * MERGESORT ALGORITHM * * *"
print(algorithm)
print("Unsorted Array", ua)
mergesort(ua, 0, len(ua) - 1)
print("Sorted Array", ua)


