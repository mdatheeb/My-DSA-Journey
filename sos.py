def sum_of_squares(n):
    ans = 0
    for i in range(1, n+1):
        ans += i*i
    return ans


if __name__ == "__main__":
    print(sum_of_squares(3))
