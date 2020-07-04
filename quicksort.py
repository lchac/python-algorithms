import variables

ua = variables.ua

def partition(a, left, right, pivot):
    while left <= right:
        while a[left] < a[pivot]:
            left = left + 1
            #print("left: ", left)

        while a[right] > a[pivot]:
            right = right - 1
            #print("right: ", right)

        if left <= right:
            aux = a[left]
            a[left] = a[right]
            a[right] = aux
            right = right - 1
            left = left + 1

    return left

def quicksort(a, left, right):
    "Quicksort Recursive Function"
    if (left >= right):
        return
    pivot = int((left + right) / 2)
    index = partition(a, left, right, pivot)
    quicksort(a, left, index - 1)
    quicksort(a, index, right)


print("* * * QUICKSORT ALGORITHM IMPLEMENTATION * * *")


print("UNSORTED: ", ua)
quicksort(ua, 0, len(ua) - 1)
print("SORTED: ", ua)






