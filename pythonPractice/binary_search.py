# binary search

def binarySearch():
    a = [1,2,3,4,5,6,7,8,9,10]
    b = int(input("Enter the number you want to search: "))
    start = 0
    end = len(a)-1
    while start <= end:
        mid = (start+end)//2
        if a[mid] == b:
            print("Found at index: ", mid)
            break
        elif a[mid] > b:
            end = mid-1
        else:
            start = mid+1
    else:
        print("Not found")