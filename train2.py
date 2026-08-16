def naming(n):
    match n:
        case 1:
            return "One "
        case 2:
            return "Two "
        case 3:
            return "Three "
        case 4:
            return "Four "
        case 5:
            return "Five "
        case 6:
            return "Six "
        case 7:
            return "Seven "
        case 8:
            return "Eight "
        case 9:
            return "Nine "
        case 0:
            return "Zero "


def printing(arr):
    n = len(arr)
    output = ""
    for i in range(n):
        output += naming(arr[i])
    return output


if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    print(printing(arr))
