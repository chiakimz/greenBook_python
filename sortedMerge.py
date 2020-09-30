
def sortedMerge(A: list, B: list) -> list:
    if A == []:
        return B
    if B == []:
        return A

    for i in B:
        low = 0
        high = len(A) - 1
        mid = 0
        while low <= high:
            if i == 12:
                print("HI")
            if low == high:
                if A[high] >= i:
                    A.insert(high, i)
                else:
                    A.insert(high + 1, i)    
                break
            mid = int((low + high) / 2)
            if i > A[mid]:
                low = mid + 1
            elif i < A[mid]:
                high = mid - 1
            else:
                A.insert(mid, i)
                break
    return A

a = [1, 2, 6, 9, 13, 14, 20]
b = [3, 6, 7, 12, 21, 30]
a = [1, 1, 1, 1]
b = [2]
sorted = sortedMerge(a, b)
print("hello")