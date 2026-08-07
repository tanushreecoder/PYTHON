def match_words(words):
    ctr = 0
    list = []
    for i in words:
        if len(i)>1 and i[0] == i[-1]:
            ctr += 1
            list.append(i)
    print("List of words with first and last letter same\n", list)
    return ctr
count = match_words(["abc", "cfc", "xyz", "aba", "1221", "lily"])
print("Number of words having first and last charecter same: ", count)