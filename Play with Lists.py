import random
import string
#Vowels from words
words = ["apple", "banana", "orange"]
vowels = [ch
          for i in words
          for ch in i
          if ch in "aeiou"]
print(vowels)
#Password generator
'''letters = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbol = ["@", "!", "#", "$", "%", "^", "&", "*", "(", ")"]
password2 = [f"{i}{numbers}{symbol}{letters}" for i in letters for n in numbers]
print(password2)
'''
length = 12
password = "".join(random.choice(string.ascii_letters+string.digits)
                   for _ in range(length))
print(password)
#Matrix
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C=[A[i][j] + B[i][j] for j in range(2)  for i in range(2)]
print(C)