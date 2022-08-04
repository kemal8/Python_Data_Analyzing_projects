# Mini-project #2 - Multiplication Table

num = int(input("What Multiplication Table doyou want ? "))

MultiplicationTableList0 = [x * num for x in range(20)]
MultiplicationTableList = [(x+1) * num for x in range(20)]
MultiplicationTableListNew = [str(x+1)+" x "+str(num)+" = "+str((x+1)*num) for x in range(20)]
MultiplicationTableListF = [f"{x+1} x {num} = {(x+1)*num}" for x in range(20)]

print("This is your Multiplication Table " ,MultiplicationTableList0)
print("This is your Multiplication Table without Zero " ,MultiplicationTableList)
print("This is your New Multiplication Table " ,MultiplicationTableListNew)
print("This is your Multiplication Table F " ,MultiplicationTableListF)

# f Expressions in Python
