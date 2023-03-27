# tuple is 1 stractcher not chang & unchangeable
# define:

TupleName = ("Car", "Mobile", "Animal", "human", "ocean")
### tuple is unchangeble
print(TupleName)

# if want chang tuple
# first chang in type list
x = list(TupleName)
# chang Andis
x[4] = "Sea"
TupleName = x
print(TupleName)

# join tuple
num1 = (1, 2, 3)
num2 = (4, 5, 6)
plus = num1+num2
print(type(plus), plus)
