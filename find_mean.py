def findmean(arr):
    avg = 0
    for i in range(len(arr)):
        avg = avg + ((arr[i]-avg) / (i+1))
    return int(avg)


if __name__ == "__main__":
    arr = [4, 4, 2, 2]
    print(findmean(arr))
