# def f():
#     count = 0
#     def g():
#         nonlocal count
#         count+=1
#         # print(a)
#         return count
#     return g
#
# b = f()
# print(b())
# print(b())
# print(b())

from collections import namedtuple
Human = namedtuple("Human",['ism','familiya','phone'])
ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
tel_raqam = input("Telefon raqamingizni kiriting: ")
human1 = Human(ism,familiya,tel_raqam)
print(human1.ism)
print(human1.familiya)
print(human1.phone)

import json
data = {
    "name": "Ali",
    "age": 25,
    "skills": ["Python", "JavaScript"],
    "details": {
        "hobby": "Chess",
        "city": "Tashkent"
    }
}
def dict_to_namedtuple():
    pass