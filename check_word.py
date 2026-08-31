def check(word, sentence):
    return word in sentence


if __name__ == "__main__":
    sentence1 = "Geeks for Geeks"
    word1 = "Geeks"
    print("Yes" if check(word1, sentence1) else "No")
