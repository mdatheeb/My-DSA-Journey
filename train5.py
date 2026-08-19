def palindrome(st: str) -> bool:
    return str(abs(int(st))) == str(abs(int(st)))[::-1]


n = 121
n1 = -121
n2 = "121"
n3 = "-121"

print("Yes" if palindrome(n2) else "NO")
