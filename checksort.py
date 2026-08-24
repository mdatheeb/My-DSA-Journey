def check_sort(arr):
    if len(arr) == 0:
        return False
    for i in range(len(arr) - 2):
        if arr[i] > arr[i+1]:
            return False
    return True


def check_sort2(arr):
    return False if len(arr) < 1 else for i in range(len(arr)-1) return False if arr[i] > arr[i+1] else True


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    arr2 = [100, 20, 30, 50, 90]
    print("Yes" if check_sort(arr) else "No")
    print("Yes" if check_sort(arr2) else "No")
