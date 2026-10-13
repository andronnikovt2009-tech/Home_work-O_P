import re

text = input("Введіть текст: ")

words = re.findall(r'\w+', text.lower())

palindromes = [w for w in words if len(w) > 1 and w == w[::-1]]

if palindromes:
    print("Паліндроми:", palindromes)
else:
    print("Паліндромів не знайдено")