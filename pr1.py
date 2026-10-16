num1 = float(input("Введите первое число: "))
op = input("Введите оператор (+, -, *, /, //, %, **, ==, !=, >, <, >=, <=,and, or, not,in, not, in,is, is, not): ")
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

elif op == 'and':
    res = (num1 != 0) and (num2 != 0)
    print(res)

elif op == 'or':
    res = (num1 != 0) or (num2 != 0)
    print(res)

elif op == 'not':
    res = not (num1 != 0)
    print(res)


elif op == 'in':
    res = num1 in range(0, int(num2) + 1)
    print(res)

elif op == 'not in':
    res = num1 not in range(0, int(num2) + 1)
    print(res)


elif op == 'is':
    res = num1 is num2
    print(res)

elif op == 'is not':
    res = num1 is not num2
    print(res)


else:
    print(f'Ошибка: неизвестный оператор "{op}"')