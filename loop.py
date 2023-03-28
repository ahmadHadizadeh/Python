# syntax for i in element(step)
# start loop i
# incresment 2
# decreysment 2


# for i in range(0, 50):
#     print(i)
# for i in range(0, 50, 2):
#     print(i)
# for i in range(0, 50, 10):
#     print(i)


# alert = "Error : Please set calon in Bitwin Code:"

# for x in alert:
#     print(x)

# Ls_UserName = ["shima", "Ramin", "Ahmad", "Asancode.com"]
# for i in Ls_UserName:
#     print(i)

# while
# num = 0
# while num <= 80:
#     print(num)
#     num += 5
# while num <= 80:
#     print(num)
#     num += 5
# while num <= 80:
#     num += 5
#     print(num)
#     if num == 30:
#         print("number is : 30")
#     elif num == 50:
#         print("number is : 50")
#     elif num == 80:
#         print("number is : 80")
#     else:
#         print("****")
i = 0
Ls_UserName = ["shima", "Ramin", "Ahmad", "Asancode.com"]
while i < len(Ls_UserName):
    print(Ls_UserName[i])
    i += 1


# break continue
x = 0
while x < 28:
    x += 1
    if x == 16:  # ==> 16 not print
        continue  # skip 16
    elif x == 23:  # ==>  print 1 from 22 out code
        break

    print("X =", x)
