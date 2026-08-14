dictionary = {"Codingal": 2, "Is": 2, "The": 1, "Best": 2, "For": 1, "Coding": 2}
print("The original dictionary:" + str(dictionary))
K = 2
res = 0
for key in dictionary:
    if dictionary[key] == K:
        res+=1
print(f"Frequency of K is: {str(res)}")