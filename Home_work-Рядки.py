from email.mime import text

arrey = [1,2,'e',True]
string = 'Hello'
for ch in string:
    print(ch)
print(string[-1])
print('a' in string)
print('h' in string)
print('hello' in string)
print(len(string))
print(string[1:3])
arrey[3] = False
print(arrey)
str = 'b'
print(string)

print(string.find('b'))
print(string.replace('l','*'))
name = "Ron"
grade = 7.4
print(f'Student {name.upper():<10}' + 'grade' + f'{grade:.2f}')

point = (1,2)
print(point)
x,y =  point
point = (f'x: {x}, Y:{y}')
print(point)
