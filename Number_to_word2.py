def toDigit(n, arr):
    if n == 0:
        return
    digit = n % 10
    n //= 10
    toDigit(n, arr)
    print(arr[digit], end=" ")


arr = ["zero", "one", "two", "three", "four",
       "five", "six", "seven", "eight", "nine"]
n = 2026
toDigit(n, arr)
