Num1 = input("enter the first number:")
Num2 = input("enter the second number:")

num1 = float(Num1)
num2 = float(Num2)

list_add = []
list_subtract = []
list_multiply = []
list_divide = []

print("1. Addition:")
print("2. subtraction:")
print("3. multiply:")
print("4. division:")

Choice =input("enter your choice 1/2/3/4:")
choice = int(Choice)

if choice == 1:
    result= num1 + num2
    list_add.append(result)
    print("sum result added to the list",list_add)
    if len(list_add)>1:
        print("previous result:",list_add[-2])
    else:
        print("no previous result")

elif choice == 2:
    result = num1 - num2
    list_subtract.append(result)
    print("subtract made added to the list:",list_subtract[-1])
    if(len(list_subtract)>1):
        print("previous result:",list_subtract[-2])
    else:
        print("no previous list")
elif choice == 3:
    result=num1 * num2
    print(result)
elif choice == 4:
    if (num2 !=0):
        result=num1/num2
        print(result)
        list_divide(result)
    else:
        print("cannot divide by zero")
else:
    print("invalid")
