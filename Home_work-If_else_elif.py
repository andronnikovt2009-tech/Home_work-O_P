a = int(input("Введи 1 ч"))
if a>=0:
    print("Додатнє")
elif a<0:
    print("Відємне")
elif a==0:
    print("Дорівнює 0")
if a%2==0:
    print("Ціле")
else:
    print("Дробове")
b = int(input("Введи 2 ч"))
if a > b:
    print("Більше", a)
elif a < b:
    print("Більше", b)
else:
    print("Числа рівні")
c = int(input("Введи 3 ч"))
if a >= b and a >= c:
    print("a")
elif b >= a and b >= c:
    print("b")
elif c >= a and c >= b:
    print("c")
if a % b ==0:
    print("Діл без ост")
else:
    print("Діл з ост")
if a % 10 % 2 == 0:
    print("Ост. парна")
else:
    print("Ост. непарна")
abs(a)
if 10 <= abs(a) <=99:
    print("2 значне")
else:
    print("Не 2 значне")
if 10 <= abs(a) ==99:
    print("Потрапляє")
else:
    print("Не потрапляє")
if 1<=a ==12:
    print("Дитина")
elif 12<=a==17:
    print("Підліток")
elif 18<=a == 59:
    print("Дорослий")
elif a<=60:
    print("Поважний вік")
if 1<= a ==3:
    print("Bed")
elif 3<=a==6:
    print("Not bad")
elif 6<=a==9:
    print("Good")
elif 9<=a==12:
  print("Weri good")
if 0<=a ==100:
    print("Not0")
elif a <=90:
    print("A")
elif a <=80:
    print("B")
elif a <=70:
    print("C")
elif a <=60:
    print("D")
else:
    print("F")
d = int(input("Ваш вік"))
if 1<=d<=18:
    print("Високий")
water = int(input("C"))
if water >= 0:
    print("Ice")
elif water < 0:
    print("water")
else:
    print("par")
