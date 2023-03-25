# define
# Felexibility changable
# key & value Data Strutcher ==> use into  Api
# similar set type  & jason

my_dic = {
    "name": "Usdt",
    "price": "1$",
    "volume": 300,
    "changePrice": 2.1,
    "Country": "Usa"
}
print(my_dic)
print(my_dic.keys())  # key
print(my_dic.values())  # values
# get value
val = my_dic.get("price")
print(val)  # output key 1$

# len
print(len(my_dic))  # 5
#  chang value in dictionry
my_dic['name'] = "bTC"
print(my_dic)  # 'name': 'bTC'
my_dic['Country'] = "iran"  # 'Country': 'iran'
print(my_dic)

first_dict = {
    "Education": "python",
    "framework": "flask",
    "timing": "28H",
    "website": "Asancode.com",
    "teacher": "Amir Sale"
}
tow_dic = {
    "Education": "python",
    "framework": "django",
    "teacher": "Ahmad hadizadeh",
}
print(first_dict)
first_dict.update(tow_dic)
print(first_dict)
