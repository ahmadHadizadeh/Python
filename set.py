# define
# set is Not Repeat ..!  or majmoeha
# add update remove delete
my_set = {"Banana", "Apple", "Limonad", "orang"}
print(my_set)
# add
my_set.add("milk")
print(my_set)
# not Add similar element into set
my_set.add("milk")
my_set.add("milk")
my_set.add("milk")
my_set.add("milk")
my_set.add("milk")
print(my_set)
# update set
my_set.update([1, 3, 4, 5, 7, 8])
print(my_set)
# my_set.remove("apple")  # KeyError: 'apple'
my_set.remove("Apple")  # correct: ' Apple '
print(my_set)
print(len(my_set))
