# цикл
# 1)
# for i in range(1,11):
#     print(i)

# 2)
# for i in range(2,51,2):
#     print(i)

# 3)
# for i in range(10,0,-1):
#     print(i)

# 4)
# n = int(input("Введите число n: "))
# total_sum = 0
# for i in range(1, n + 1):
#     total_sum += i
# print(total_sum)

# 5)
# n = int(input("Введите число n: "))
# faktorial = 1
# for i in range(1,n+1):
#     faktorial *= i
# print(faktorial)

# 6)
# n = int(input("Введите число n: "))
# for i in range(1,11):
#     result = i * n
#     print(result)

# 7)
# num = [1,-4,5,10,-44]
# plys = 0
# for i in num:
#     if i > 0:
#         plys += 1
# print(plys)

# 8)
# text = "Привет, мир! Как дела?"
# vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
# count_vowels = 0
#
# for char in text:
#     if char in vowels:
#         count_vowels += 1
#
# print(count_vowels)

# 9)
# numbers = [15, 42, 8, 99, 23, 4]
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print(max_num)

# 10)
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i * j:>3}", end="\t")
#     print()


# 1)
# i = 1
# while i <= 10:
#     print(i)
#     i+=1

# 2)
# while True:
#     a = int(input("Введите 1 число: "))
#     b = int(input("Введите 2 число: "))
#     if a == 0 or b == 0:
#         break
#     sum = a+b
#     print(sum)

# 3)
# num = int(input("Введите число: "))
# count = 0
# while num > 0:
#     num = num // 10
#     count += 1
# print(f"Количество цифр: {count}")

# 4)
# num = int(input("Введите число: "))
# sum = 0
# while num > 0:
#     last = num % 10
#     sum += last
#     num = num // 10
# print(f"Сумма цифр: {sum}")

# 5)
# num = int(input("Введите число: "))
# reversed_num = 0
# while num > 0:
#     last_digit = num % 10
#     reversed_num = reversed_num * 10 + last_digit
#     num = num // 10
# print(f"Перевернутое число: {reversed_num}")

# 6)
# n = int(input("Введите число n: "))
# power = 1
#
# while power <= n:
#     print(power, end=" ")
#     power *= 2
# print()

# 7)
# password = input("Введите пароль: ")
#
# while password != "123":
#     print("Неверный пароль!")
#     password = input("Попробуйте еще раз: ")
# print("Пароль верный")

# 8)
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# while b != 0:
#     a, b = b, a % b
# print(f"Наибольший общий делитель: {a}")

# 9)
# n = int(input("Введите число n: "))
# a, b = 0, 1
# while a <= n:
#     print(a, end=" ")
#     a, b = b, a + b
# print()

# 10)
# import random
# secret_number = random.randint(1, 100)
# attempts = 0
# guess = 0
# while guess != secret_number:
#     guess = int(input("Твой вариант: "))
#     attempts += 1
#     if guess < secret_number:
#         print("Загаданное число больше!")
#     elif guess > secret_number:
#         print("Загаданное число меньше!")
# print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток.")


# словари

# 1)
# students = {"Иван": 5, "Мария": 4, "Петр": 3}
# print(students["Мария"])

# 2)
# data = {"a": 1, "b": 2, "c": 3}
# data["d"] = 4  # добавление
# data["a"] = 10 # изменение
# del data["b"]  # удаление
# print(data)

# 3)
# data = {"name": "Дмитрий", "age": 20}
# key = input("Введите ключ: ")
# print(data.get(key, "Нет такого ключа"))

# 4)
# data = {"a": 1, "b": 2, "c": 3}
# print("Ключи:", list(data.keys()))
# print("Значения:", list(data.values()))
# print("Количество пар:", len(data))

# 5)
# products = {"хлеб": 40, "молоко": 80, "сыр": 300}
# for name, price in products.items():
#     print(f"{name}: {price}")

# 6)
# products = {"хлеб": 40, "молоко": 80, "сыр": 300}
# total = 0
# max_price = 0
# max_name = ""
# for name, price in products.items():
#     total += price
#     if price > max_price:
#         max_price = price
#         max_name = name
# print(f"Сумма: {total}, Самый дорогой: {max_name}")

# 7)
# text = "привет"
# char_count = {}
# for char in text:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print(char_count)

# 8)
# text = "яблоко банан яблоко апельсин банан яблоко"
# words = text.split()
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# max_count = 0
# max_word = ""
# for word, count in word_count.items():
#     if count > max_count:
#         max_count = count
#         max_word = word
# print(f"Самое частое слово: {max_word}")

# 9)
# original = {"a": 1, "b": 2}
# inverted = {}
# for key, value in original.items():
#     inverted[value] = key
# print(inverted)

# 10)
# countries = ["Россия", "Франция", "Япония"]
# capitals = ["Москва", "Париж", "Токио"]
# country_dict = {}
# for i in range(len(countries)):
#     country_dict[countries[i]] = capitals[i]
# user_input = input("Введите страну: ")
# print(country_dict.get(user_input, "Нет такой страны"))