# print("Hello world")
# print(2+2)
#
# print("Hello world")
#     #print(2+2)
#
# if 1<2:
#     print("Привет")
# else:
#     print("Пока")
#
# #регистро зависимость
# print("Привет")
# # Print("Привет") неправильно
#
# # коментарии
#
# # строчные
# # print("Привет") вывод инфы на консоль
#
# # блочные
#
# # нельза назыв переменые
# '''  False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield '''
#
# name = "Анастосия"
# print(type(name)) #для понятия что за тип переменое
# # два типа наименования переменых
# # camel case
# userName="Fil"
#
# # underscore notation
#
# users_name="Fil"
#
# age = 23
# Age = 23
# age = 34
# print(age)
#
# #Числовые типы данных
# '''
# int- Целые числа x=5
# float - вещественный тип данных(число с плавающей точкой) y=5.6
#
# '''
#
# #Текстовые типы данных
# '''
# str - Строка, состоящие из символов, заключенных в одинарные или двойные кавычки
# name="Фил"
# '''
# #Логические типы данных
# '''
# bool - Логические значения (True-истина,False-ложь)
#
# is_activate=True
# '''
#
# #Cписки и коллекции
#
# #None
# '''
# NoneType- особый тип данных, который представляет отсутствие значения
# z=None
# '''
# x = 5
# y = 5.6
# is_activate=False
# r = None
# name = "Fil"
# name1 = "Fil"
#
# print(x,y,is_activate,r,name1,name)
#
# # print("значениеб end=конечный символ")
# # print("привет мир",end=" ")
# # print("привет мир", end=" и пока")
#
# # name = input("Введите имя" )
# # print(name)
# #
# # age = int(input("введите возрвст "))
# # print(age)
#
# 2-10
# a =0b11
# b = 0b1011
#
# print(a,b)
# 8 ричная
# a1 = 0o7
# b1 = 0o11
# print(a1,b1)
# # 16-10
# s = 0x0A
# print(s)
#
# name2 = (input("введите имя: "))
# print(f'Привет' ,name2, '!')
#
# a = float(input("Введите длину: "))
# b = float(input("Введите ширену: "))
#
# print(f'площядь:{a*b} периметор:{a+b}')
# from os.path import split

# явное преобразование
# x = 10
# y = str(x)
# z = float(x)
# print(type(y))
# print(type(z))

# неявное преобразование
# y = 6
# x = y+8.9
# print(type(x))

# ccomplexNumber = 2+3j
# print(ccomplexNumber)

# ''' Управляющие последовательности в строке
#
# Строка может содержать ряд специальных символов - управляющих последовательностей.
#
# Некоторые из них:
#
# \: позволяет добавить внутрь строки слеш
#
# ': позволяет добавить внутрь строки одинарную кавычку
#
# ": позволяет добавить внутрь строки двойную кавычку
#
# \n: осуществляет переход на новую строку
#
# \t: добавляет табуляцию (4 отступа)
#
# '''


# text = "Сщщбщение: \n\"Привет друзья!\""
# print(text)
#
# text1 = "Привет\t друзья!"
# print(text1)

# print(значение, end=онечные символы)
# print("привет", end= " ")
# print("Привет", end= " друзтя ")

# арифметические операции
# + - / *
# // - целочисленое диление
# % - остаток от деления
# ** - степень

# print(5+5)
# print(10-5)
# print(3*4)
# print(8/2)
# print(25//4)
# print(50%26)
# print(2**2)

# ** - справо направо
# * // / % слева направо
# + - слева на право

# number = 3+4*5**2+7
# print(number)
# # 5**2=25
# 25*4=100
# 100+3=103
# 103+7=110



# s = 5
# s += 5 #s=s+5
# s -= 5
# s *= 5
# s /= 5
# s //= 5
# s %= 5
# s**=5
# print(s)

# округление чисел

# num_1 = 2.0001
# num_2 = 5
# num_3 = num_1+num_2
# print(num_3)
# print(round(num_3,2))


# операторы сравнения
# res = (5>3)
# print(res)
# res = (5<3)
# print(res)
# res = (5==3)
# print(res)
# res = (5!=3)
# print(res)
# res = (5<=3)
# print(res)
# res = (5>=3)
# print(res)

# будет правда если оба истина
# num = (5>3) and (6==6)
# print(num)
#
# # будет правда если хоть 1 истина
# num_1 = (5>3) or (6==9)
# print(num_1)
#
# # bydthcbz ,skj kj; cnfytn ghfdlf
# num_2 = not(5==7)
# print(num_2)



# ператоры членства
# r = [1,2,3,4]
# resl = 1 in r
# resl1 = 5 not in r
# print(resl)
# print(resl1)

# print( 'операторы тождевствености')
# r = [1,2,3,4]
# u = r
# print(u is r)
#
# i = [1,2,3]
# o = [1,2,3]
# print(i is not o) # несылается ли


# пользователь вводит 2 числа погрома выводит сумму разность вычисления всех арифмитических опер

# a = float(input('введите первое число: '))
# b = float(input('введите второе число: '))
# print(f' сумма: {a+b}, разность:{a-b},произведени:{a*b}, частное:{a/b}, степень:{a**b},остаток:{a//b},делениебез остатка:{a%b} ')

# пользователь вводит радиус круга прога вычисляет площядь круга
# из цельсия в фарингейта
# радиус шара вычис объём
# 3 числа вычисляет средне арифмитическое

# a = float(input("первое число: "))
# b = float(input("первое число: "))
# c = float(input("первое число: "))
# s = a+b+c
# print(f" среднее арифметическое: {s/3})

# a = float(input("Введите радиус: "))
# d = 3.14 * a**2
# print(d)


# i = [1,2,3]
# o = [1,2,3]
# print(i is not o)

#условные операторы/конструкции
# if условие:
#    блок кода который выполняется если условие истено или = True
# ледующий блок кода
# x = 4
# if x>5:
#     print("х больше 5")

# water = 45
# money = float(input("Введите количество денежных средств: "))
#
# if money>=water:
#     print("Вы можете приобрести воду")
# else:
#     print("Недостаточно средств")
#     kol = water-money
#     print(f'вам не хвотает {kol}')
#
# x = 4
# if x>5:
#     print(f"х больше 5")
# else:
#     print("х меньше 5")


# x = 23
# if x>10:
#     print("х больше 10")
#     if x>20:
#         print("х больше 20")
#     else:
#         print("х больше 10 , но меньше или равно 20")
# else:
#     print("х меньше или равно 10")
# тернарный оператор
# x = 10
# if x>5:
#     print("х больше 5")
# result="ч больше 5" if x>5 else "ч не больше 5"
# print(result)
#
# if - роверяет перве условие
# elif - проверяет следующие условя, если предыдущее условие было ложно
# else - выполняет блок, если все предыдушие были ложные

# if условие1:
#      блок кода1
# elif условие 2:
#     блок кода2
# elif условие 3:
#     блок кода3
# else:
#     блок кода 4

# x = 7
# if x>10:
#     print("х больше 10")
# elif x>5:
#     print("х больше 5,но меньше или равен 10")
# elif x>0:
#     print("х больше 0,но меньше или равен 5")
# else:
#     print("х меньше или равен 5")

#
# age=int(input("Введите возраст: "))
# if age>=18:
#     print( "Воход разрешон")
# else:
#     print("Вход запрещён")

# пользователь водит первую и последнию букву алфавита если да верно если нет неверно
#
# a = input("Введите первую букву: ")
# z = input("Введите последнию букву ")
# if (a == "а" or a == "А") and (z == "я" or z == "Я"):
#     print("всё верно")
# else:
#     print("неверно")


# сокращёная запись
# if x>=0 and x<100
# if x 0<=x<100

#
# a = float(input("Введите первую сторону: "))
# b = float(input("Введите вторую сторону: "))
# c = float(input("Введите третью сторону: "))
# if a+b>c and a+c>b and c+b>a:
#     print("Треугольник существует")
# else:
#     print("Треугольник не существует")

# a = float(input("Введите балл: "))
#
# if a >= 90:
#     print("отлично")
# elif a >= 75:
#     print("хорошо")
# elif a >= 60:
#     print("удовлетворительно")
# elif a > 0:
#     print("неудовлетворительно")
# else:
#     print("некорректный балл")


# Строки в Python — это последовательности символов, заключённые в одинарные
# ( '...' ), двойные ( "..." ), тройные одинарные ( '''...''' ) или тройные двойные
# ( """...""" ) кавычки. Они представляют собой неизменяемые (immutable) типы данных,
# что означает, что после создания строки её содержимое нельзя изменить.

# str = "gg"
# str1 = 'gg'
# str2 = '''gg'''
# str3 = """gg"""


#
# s = "hello"
# # h e l l o
# # 0 1 2 3 4
# s[0] = "H" TypeError: 'str' object does not




# синтаксис среза
# оследовательность[start:stop:stet]


# start - индекс начала (включительно), по умолчанию
#stop - идекс конца (не включительно), По умолчанию идёт до длины последовательности
#step - шаг(через сколько элементов брать).По умолчанию 1

# p y t h o n
# 0 1 2 3 4 5
#  -5-4-3-2-1
# s = "python"
# print(s[0])
# print(s[-1])
#
# print(s[0:3])
# print(s[3:])
# print(s[2:5])
# print(s[4:])
# print(s[0:])
# print(s[:])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::])
# print(s[:])
#
#
# s1 = "hello"
# str1 = "H" + s1[1:]
# print(str1)

# конкотенация
# f = "gh"
# f1 = "fg"
# print(f +" "+ f1)
#
# #повтор
# print(f*7)
#
# # форматирование
# print(f"переменная 1 {f}, переменная 2 {f1}")



# методы работы над значениями
# l = "привет мИР.привет"
# print(l.capitalize())
# print(l.swapcase())
# print(l.lower())
# print(l.upper())
# print(l.title())
#
# print(l.find("мир"))
# print(l.startswith("с"))
# print(l.endswith("т"))
# print(l.count("П"))
#
# l = "     привет    мир привет    "
# print(l.strip())
# print(l.lstrip())
# print(l.rsplit())
# print(l.replace("мир", "оаоаао"))
#
#
#
# s = "apple,banana,cherry"
# fruts = s.split(",")
# fruts1 =s.split(" ")
#
# print(fruts)
# print(fruts1)
#
# joind = "-".join(fruts)
# print(joind)


#равнение строк
# print("apple">"banana")
# print("apple">="banana")
# print("apple"<="banana")
# print("apple"=="banana")
# print("apple"!="banana")


# s = "hello"
# for i in s:
#     print(i)
#
#
# a = "apple"
# b = "apple"
# print(a is b)


# print("嗨")

# print(len("kfjshfksl"))
# a = "dlmfldfl"
# print(len(a))

# Списки в Python — это изменяемые последовательности элементов,
# # которые могут содержать данные любого типа: числа, строки,
# # другие списки и даже объекты. Списки позволяют хранить упорядоченные
# # коллекции элементов, доступ к которым можно получить по индексу.
#
# my_list = [1,2,3,"b",6.7,True,False,None]
# print(my_list)
#
# print(my_list[2])
# print(my_list[-1])
#
# my_list.append(4)#добовляет в конец
# print(my_list)
# my_list.insert(4,7)#двигает
# print(my_list)
# my_list.extend([4,5,6])#обавляет список в конец
# print(my_list)
# my_list.remove(2)#удоляет 1 найденый такой элемент
# print(my_list)
# my_list.remove(4)
# print(my_list)
#
# caunt = my_list.count(5)
# print(caunt)
#
# indexs = my_list.index(6.7)#выводит индекс
# print(indexs)
#
# my_list = [9,2,3,7,5]
# my_list.sort()#сортирует список
# print(my_list)
#
#
# list1 = [1,2,3,4]
# sortd = sorted(list1)
# print(sortd)
# print(list1)
#
# my_list1 = [9,2,3,7,5,4,1]
# my_list1.sort(reverse=True)
# print(my_list1)
#
# my_list2 = [1,2,3]
# my_list2.reverse()
# print(my_list2)
#
# print(len(my_list2))
#
# list = list(range(6))
# print(list)
#
# s = [1,2,3,[1,2,3]]
# print(s[3][0])
#
# list5 = [10,20,30,40,50,60]
# print(list5.copy())
# print(list5[::])
#
# print(list5[::2])#чётные
# print(list5[1::2])#нечётные
# print(list5[-2:-5:-1])
#
#
# list6 = [ x**2 for x in range(5) ]
# print(list6)
#
#
# print(max(list6))
# print(min(list6))
# print(sum(list6))
#
# list7 = [1,2,3]
# list8 = [4,5,6]
# print(list7+list8)
#
# print(list7*4)
#
# listP = [1,2,3,4,5,6,7]#простая распоковка будет 1 2 3
# a,b,c = listP
# print(a,b,c)
#
# # a,*b,c = listP #сложная распоковка
# # print(a,b,c)
#
# a,_,*v,c = listP
# print(listP)

# Кортедж - последовательность элементов неизменяемого типа
# t = ("str",4,5)
# print(t)
#
# t1 = "str",4,5
# print(t1)
# data = (1,2,3,4,5)
# print(tuple(data))# теперь список картедж
#
# print(len(t1))
#
# print(t1[0])
# print(t1[-1])
# print(t1[1])
#
#
# # t1[0] = "?"
# # print(t1)
#
# name,age,company,position,role = ("fillip",34,"gogl","web","programist")
# print(name)
# print(age)
# print(company)
# print(position)
# print(role)
#
# s = (("fillip",34,"gogl","web","programist"))
# print(s[:2])
# print(s[2:])
# print(s[::-1])
#
#
#
# #множества(set) - это набор уникальных элементов неупорядоченоя коллекция элементов
#
# # selt1 = {} - это путой словарь
#
# set2 = set()
# print(set2)
#
# set1 = {1,1,1,1,2,3,4,5}
# print(set1)
#
# date = [1]
#
# set1 = {1,}
# date = [1,2,3,4,"ghgh"]
# print(set(date))
# print(len(set(date)))

# # fruits = set()- пустое
# fruits = {1,2,3,4}
# fruits.add(5) #- добовляет в конец как append
# print(fruits)
# fruit = 5
#
# # if fruit in fruits:
# #     fruits.remove(5) - удоление
# #     print(fruits)
#
# fruits.discard(6) - удоляет если есть
# print(fruits)
# fruits.clear()
# print(fruits)

#
# user = {"fill","artem"}
# user = user.copy()
# print(user)
#
# user1 = {"fill","ivan"}
# user2 = {"germann","artem","fill"}
# user3 = user1.union(user2)
# print(user3)
#
# print(user1 | user2)
# user3 = user1.intersection(user2)
#
# # пересечение
# print(user3)
# print(user1 & user2)
#
# #разность множеств
# user1 = {"fill","ivan"}
# user2 = {"germann","artem","fill"}
# print(user1.difference(user2))
# print(user2.difference(user1))
# print(user1 - user2)
# print(user2 - user1)
#
# # симетрическая разность
#
# user1 = {"fill","ivan"}
# user2 = {"germann","artem","fill"}
# print(user1.symmetric_difference(user2))
# print(user2.symmetric_difference(user1))
# print(user1 ^ user2)

# user1 = {"fill","ivan"}
# user2 = {"germann","artem","fill","ivan"}
#
# # является частью
# print(user1.issubset(user2))
# print(user2.issubset(user1))
#
# print(user1.issuperset(user2))
# print(user2.issuperset(user1))
#
# s = frozenset(user1)
# print(s)