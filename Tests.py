import random

global_count = 0

def recursive_function(r):
    # Recursive function to show scope of a variable
    global global_count
    global_count = global_count + 1
    print(r)
    if (r < 1):
        return r
    recursive_function(r-1)


print("global_count", global_count)
rf = recursive_function(random.randrange(1, 10))
print("global_count", global_count)



