def check(n):
    num = len(n)
    if int(n[num-1]) % 2 == 0:
        no = 0
        for i in range(num):
            no += int(n[i])
        if no % 3 == 0:
            return "Yes"
        else:
            return "No"
    else:
        return "No"

# A fn. thousand times better than mine


def check_divisible_by_6(st: str) -> bool:
    return False if st[-1] not in "02468" else sum(int(digit) for digit in st) % 3 == 0


if __name__ == "__main__":
    n = "323464625441"
    print(check(n))
    print("Yes" if check_divisible_by_6(n) else "No")
