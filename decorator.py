# # def my_decorator(func):
# #     def wrapper():
# #         print("Akbarni funksiyasi funksiyadan oldin ishlayapti")
# #         func()
# #         print("Akbarni funksiyasi funksiyadan oldin ishlayapti")
# #     return wrapper()
# # @my_decorator
# # def say_hello():
# #     print("salom,Dunyo")
#
#
# def qoshish(func):
#     def wrapper(*args,**kwargs):
#         print(f"funksiyadan oldin ishlayapti: {func.__name__}")
#         result = func(*args,**kwargs)
#         print(f"Natija: {result}")
#     return wrapper
# @qoshish
# def add(*args):
#     return sum(args)
#
# add(2,3,4,232,452,4124,341,4622,873145,9,4325,2345,1254,13453534656)

