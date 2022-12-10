def add(a,b):
    answer = a+b
    print(str(a)+"+"+str(b)+"="+str(answer)+"\n")
def sub(a,b):
    answer = a-b
    print(str(a)+"-"+str(b)+"="+str(answer)+"\n")
def mul(a,b):
    answer = a*b
    print(str(a)+"*"+str(b)+"="+str(answer)+"\n")
def div(a,b):
    answer = a/b
    print(str(a)+"/"+str(b)+"="+str(answer)+"\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("enter your choice")

    if choice == "A" or choice== "a":
        print("A. Addition")
        a = int(input("enter your first number "))
        b = int(input("enter your second number "))
        add(a,b)
    elif choice == "B" or choice== "b":
        print("B. Subtraction")
        a = int(input("enter your first number "))
        b = int(input("enter your second number "))
        sub(a,b)
    elif choice == "C" or choice== "c":
        print("C. Mutiplication")
        a = int(input("enter your first number "))
        b = int(input("enter your second number "))
        mul(a,b)
    elif choice == "D" or choice== "d":
        print("D. Division")
        a = int(input("enter your first number "))
        b = int(input("enter your second number "))
        div(a,b)
    elif choice == "E" or choice== "e":
        print("Thanks for playing")
        quit()