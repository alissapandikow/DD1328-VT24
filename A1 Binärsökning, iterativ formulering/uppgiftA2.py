k = 6
x = [0, 2, 3, 4, 6, 8, 9]
n = 7
lo = 0
hi = n - 1


def binary_search(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return f"{target}\n{arr}\n{n}\n{mid + 1}\n"

        elif target < arr[mid]:
            return binary_search(arr, low, mid - 1, target)

        elif target > arr[mid]:
            return binary_search(arr, mid + 1, high, target)


result = binary_search(x, lo, hi - 1, k)
print(result)