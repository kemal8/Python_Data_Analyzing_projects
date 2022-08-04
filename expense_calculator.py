#i = 1
#while i<=10:
#    print (i)
#    i = i + 1

# exp = [12,18,10,19,23,10]
# print("befor",exp)
# print("Total items in exp list", len(exp))
# print(len("python"))
# exp.append(10)
# print("after",exp)

exp = []
stopped = False
while not stopped:
    e = int(input("(What is the expences (type to 0 for stop): "))
    if e!=0:
        exp.append(e)
    else:
        stopped = True
print(exp)
print("total Expences : ",sum(exp))