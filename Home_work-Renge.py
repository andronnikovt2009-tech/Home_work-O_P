numbers = []
for i in range(5):
 n = int(input())
 numbers.append(n)
minimum = numbers[0]
for n in numbers[1:]:
 if n < minimum:
        minimum = n
print(minimum)

aa = [1,True, "str"]
print(aa)
print(aa[-3])