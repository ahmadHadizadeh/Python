# def fun-nam():
# ...
# ...
# ... ...
# return ...
# def carName(car):
#     print("hello %s" % car)


# carName("B M W")

# default value into function
# def userInfo(homeCode, name, last_name, age, Phone, city="tehran"):
#     print("HomeCode :", homeCode)
#     print("name :", name)
#     print("last_name:", last_name)
#     print("age:", age)
#     print("Phone:", Phone)
#     print("city:", city)


# userInfo(120, "Arsalan", "shahani", 28, 9197020019, "Shiraz")


# args

# def order(*args):
#     print(type(args), args)
#     print(args[2])


# order("1", "250$", "Mobile", "nike")
# order("5", "9000$", "T-Shert", "adidas")
# order("8", "400$", "wallet")

# return


# def plus(a, b):
#     c = a+b
#     return c


# result = plus(300, 30)
# print(result)


# def mines(a, b):
#     c = a-b
#     return c


# res = mines(100, 50)
# print(res)

# base condition
# fibonachi

# def fibo(num):
#     if num == 0 or num == 1:
#         return num
#     else:
#         return fibo(num - 1) + fibo(num - 2)


# num = int(input("please inter number : "))
# for i in range(0, num):
#     print(fibo(i))
