name =input("What is your name? ")
age = int(input("How old are you? "))

yearsto30 = 30 - age

if yearsto30>0:
    print("Hello " +name+" You will be 30 in "+str(yearsto30)+" years")
else:
    print("Hello " +name+" You were 30 "+str(-yearsto30)+" years ago")

print("Than have a gret day "+name.title()+" ")