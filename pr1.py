num1 = float(input("Введите первое число: "))
op = input("Введите оператор (+, -, *, /, //, %, **, ==, !=, >, <, >=, <=): ")
num2 = float(input("Введите второе число: "))

if op == '+':
    sum = num1 + num2
    print(f"сумма чисел {sum}")
elif op == '-':
    min = num1 - num2
    print(f"разность чисел {min}")
elif op == '*':
    pr = num1 * num2
    print(f"произведение чисел {pr}")
elif op == '/':
    if num2 == 0:
        print("Ошибка: деление на ноль")
    else:
        print(f"часное чисел {num1 / num2}")
elif op == '//':
    if num2 == 0:
        print("Ошибка: деление на ноль")
    else:
        print(f"часное чисел без остатка {num1 // num2}")
elif op == '%':
    if num2 == 0:
        print("Ошибка: деление на ноль")
    else:
        print(f"часное чисел  остатком {num1 % num2}")
elif op == '**':
    print(f"{num1} в степени {num2} - {num1 ** num2}")

elif op == '==':
    print(f"{num1} == {num2} -> {num1 == num2}")
elif op == '!=':
    print(f"{num1} != {num2} -> {num1 != num2}")
elif op == '>':
    print(f"{num1} > {num2} -> {num1 > num2}")
elif op == '<':
    print(f"{num1} < {num2} -> {num1 < num2}")
elif op == '>=':
    print(f"{num1} >= {num2} -> {num1 >= num2}")
elif op == '<=':
    print(f"{num1} <= {num2} -> {num1 <= num2}")

else:
    print(f"Неизвестный оператор: {op}")