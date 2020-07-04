# Unsorted Array
ua = [1, 7, 34, 9, 18, 11, 2, 89, 4]
#p = [0, 1,  2, 3,  4,  5, 6,  7, 8] <- positions (indexes)

"""
Understanding the calculation for half in merge sort

left = 0, right = 8
half + left = 8 - 0 / 2 = 4 + 0 = 4
half + 1 = 5

0-4

5-8
left = 5, right = 8
half + left = 8 - 5 / 2 = 2 + 5 = 7
half + 1 = 8

5-7 y 8-8

5-7
left = 5, right = 7
half + left = 7 - 5 / 2 = 1 + 5 = 6
half + 1 = 7

5-6 y 7-7
...



107, 110        4, 89
4,89,

"""
