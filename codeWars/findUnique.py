
# def find_uniq(arr):
#     arr = sorted(arr)
#     if max(arr) > arr[1]:
#         return arr[1]
#     else:
#         return max(arr)


# set cannot have duplicates which splits it into different ones
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

find_uniq([1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1])
