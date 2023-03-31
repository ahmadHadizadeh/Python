# python string

# text = "hello user well com may class room"
# a = "hello"
# a = """ hello user well com
# my class room are
# you ok class room
# .if have buy t-shert
# you must be
# have enof mony.
# """

# b = ''' hello user well com
# my class room are
# you ok class room
# .if have buy t-shert
# you must be
# have enof mony.
# '''
# print(b)

# for x in "apple banana orang":
#     print(x)
# fruits = "apple banana orang"

# if "ahmad" in c:
# print("Yes, 'ahmad', is Exist to c ")
# if "oraneg" not in fruits:
# print("Sorry ,Not exist orang in  c ")

# slice string

fruits = "apple banana orang"
# print(fruits[0:5])  # char 0 from 5 ==>apple
# print(fruits[6:13])
# print(fruits[13:18])
# print(fruits[3:])  # ==>from end
# print(fruits[-12:-7])

# define cancat string
# a = "apple"
# b = "banana"
# c = a+"-"+b
# print(c)

# not coorect format
# age = 35
# txt = "i am user  my name Jak . age is "+age
# print(txt)
# using format( ) method ==>use {}
# age = 35
# txt = "i am user  my name Jak . age is {}"
# print(txt.format(age))

# wallet = 200

# description = "there is compony amazon, doposit mony is: {}"
# print(description.format(wallet))

# withdraw = -200
# diposit = +300
# asset = 100
# plus = 600

# way one
# textmony = "my wallet is withdraw: {}, diposit: {},asset: {}, plus: {} "
# print(textmony.format(withdraw, diposit, asset, plus))

# textmony = "my wallet is withdraw: {0}, diposit: {1},asset: {2}, plus: {3} "
# print(textmony.format(withdraw, diposit, asset, plus))


# 5- Scope character
txt = "the best fotbalist is \"leo messi \" very Good ... ! "
print(txt)

dialog = "thi is a best  \"Dialog \" in The \n \" The Best In life Is Free\" . "

print(dialog)

# define \n==>new lin \t ==>tab  \\ ==>\
# \'name\'==>'name'


description = "The film  \"viking\" rang IMDB is : \n: \n*\n*\n*\n*\n*\n🧡\t🧡\t🧡 and slim : \'😇\' "

print(description)
# string-Method
print("\n")

# capitalize()
# txt = "hello, welcome my world."
# x = txt.capitalize() #first character uppercase
txt = "HELLO , WELCOME MY WORLD"
# x = txt.capitalize()
x = txt.casefold()  # convert string to  lowercase


print(x)
