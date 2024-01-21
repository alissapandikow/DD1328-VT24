k = 6
x = [0, 2, 3, 4, 6, 8, 9]
n = 7
low = 0
high = n - 1

while low <= high:
    mid = (low+high)//2
    if k < x[mid]:
        high = mid - 1
    elif k > x[mid]:
        low = mid + 1
    else:
        print(f"{k}\n{x}\n{n}\n{mid}\n")
        break
