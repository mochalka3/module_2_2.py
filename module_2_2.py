first = int(input("Введите_первое_число: "))
second = int(input("Введите_второе_число: "))
third = int(input("Введите_третье_число: "))
if "first" == "second" == "third":
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)