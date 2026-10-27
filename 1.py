# множества
# 1)
# list = [1,2,3,4,4,4,2,3]
# print(set(list))
# print(len(set(list)))

#2)
# user = {1,2,3}
# user.add(4)
# user.discard(2)
# print(user)

#3)
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1 | set2)

#4)
# user1 = {"fill","vi"}
# user2 = {"gnom","art","fill"}
# print(user1 & user2)

#5)
# set1 = {1, 2, 3, 4, "ru"}
# set2 = {3, 4, 5, 6}
# result = set1.symmetric_difference(set2)
# print(result)

# 6)
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# result = set1.symmetric_difference(set2)
# print(set1 ^ set2)

# 7)
# my_set = {10, 20, 30, 40, 50}
# x = 30
# if x in my_set:
#     print("Есть")
# else:
#     print("Нет")
#
# # 8)
# set1 = {2, 3}
# set2 = {1, 2, 3, 4, 5}
# result = set1.issubset(set2)
# print(result)
#
# # 9)
# text = "программирование"
# unique_chars = set(text)
# print(unique_chars)
# print(len(unique_chars))
#
# # 10)
# list1 = [5, 2, 8, 2, 1, 9]
# list2 = [2, 8, 3, 8, 7, 5]
# common = set(list1) & set(list2)
# result = sorted(list(common))
# print(result)

# кортеджи
# # 1)
# t1 = (10, 20, 30, 40, 50)
# print(t1[0])
# print(t1[-1])
# print(t1[2])
#
# # 2)
# t2 = (1, 2, 3, 4, 5, 6, 7, 8)
# print(t2[:2])
# print(t2[-2:])
# print(t2[::-1])
#
# # 3)
# t3 = (5, 2, 9, 1, 5, 6)
# print(len(t3))
# print(sum(t3))
# print(min(t3))
# print(max(t3))
#
# # 4)
# t4 = (1, 2, 3, 2, 4, 2, 5)
# x = 2
# print(x in t4)
# print(t4.count(x))
# print(t4.index(x))
#
# # 5)
# t5_a = (1, 2, 3)
# t5_b = (4, 5, 6)
# result = t5_a + t5_b
# print(result)
#
# # 6)
# t6 = (99,)
# print(type(t6))
#
# # 7)
# person = ("Иван", 25, "Москва")
# name, age, city = person
# print(name)
# print(age)
# print(city)
#
# # 8)
# a = 10
# b = 20
# a, b = b, a
# print(a, b)
#
# # 9)
# t9 = (10, 20, 30, 40)
# new_t9 = t9[:1] + (99,) + t9[2:]
# print(new_t9)
#
# # 10)
# t10 = (5, 1, 3, 5, 2, 1, 4)
# result = tuple(sorted(set(t10)))
# print(result)