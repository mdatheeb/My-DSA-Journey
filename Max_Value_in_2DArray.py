def FindMax(num):
    if len(num) == 0:
        return False
    elif len(num) > 0:
        max_value = num[0][0]
        for columns in range(len(num[0])):
            for rows in range(len(num)):
                min_value = num[rows][columns]
                if min_value > max_value:
                    max_value = min_value
        return max_value


if __name__ == "__main__":
    mat = [[1, 2, 3, 4],
           [25, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
    print(FindMax(mat))
