# Лаба - 1
for a in range(5):
    print(a + 1, "0")


# Лаба - 2
x=1
y=0
while x<101:
    y=y+x
    x=x+1
print(y)


# Лаба - 3
list = []
for b in range(53, 3946):
    if b % 5 == 0:
        list.append(b)
print(list)


# Лаба - 4
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
winter = [1, 2, 12]
c = int(input("Введите номер месяца: "))
if c in spring:
    print("Весна")
elif c in summer:
    print("Лето")
elif c in autumn:
    print("Осень")
elif c in winter:
    print("Зима")
else:
    print("Проверьте номер месяца")