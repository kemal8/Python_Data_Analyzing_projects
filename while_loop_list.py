# ***This is the while loop list feature*****************

list = []

num = 1
while num<=100:
    list.append(num)
    num = num+1

print(list)


# ************************************************************


# list2 = []

# for num in range(100):
#     list2.append(num)

# print(list2)


# ************************************************************


list3 = [num for num in range(100)]
evennumbers = [num*2 for num in range(100)]

print(list3)

print(evennumbers)

