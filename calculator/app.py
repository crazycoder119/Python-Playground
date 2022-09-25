# define the functions needed

def add(a, b):
    answer = a+b
    print(str(a) + "+" +str(b) + "=" + str(answer))
    return answer


def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))
    return answer

def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))
    return answer

def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer))
    return answer


loopOrder = True
answer = None

while loopOrder:
    # User instructions
    print("A. addition \nB. subtraction \nC. division \nD. multiplication \nE. exit")
    choice = input("input your command : ")
    if answer:
        if choice == "a" or choice == "A":
            print("You have choosen addition functionality \n")
            variable2 = int(input("input your value : "))
            answer = add(answer, variable2)
        elif choice == "b" or choice == "B":
            print("You have choosen substraction functionality \n")
            variable2 = int(input("input your value : "))
            answer = sub(answer, variable2)
        elif choice == "c" or choice == "C":
            print("You have choosen division functionality \n")
            variable2 = int(input("input your value : "))
            answer = div(answer, variable2)
        elif choice == "d" or choice == "D":
            print("You have choosen multiplication functionality \n")
            variable2 = int(input("input your value : "))
            answer = mul(answer, variable2)
        elif choice == "e" or choice == "E":
            print("shutting down")
            loopOrder = False
    else:
        if choice == "a" or choice == "A":
            print("You have choosen addition functionality \n")
            variable1 = int(input("input your first value : "))
            variable2 = int(input("input your second value : "))
            answer = add(variable1, variable2)
        elif choice == "b" or choice == "B":
            print("You have choosen substraction functionality \n")
            variable1 = int(input("input your first value : "))
            variable2 = int(input("input your second value : "))
            answer = sub(variable1, variable2)
        elif choice == "c" or choice == "C":
            print("You have choosen division functionality \n")
            variable1 = int(input("input your first value : "))
            variable2 = int(input("input your second value : "))
            answer = div(variable1, variable2)
        elif choice == "d" or choice == "D":
            print("You have choosen multiplication functionality \n")
            variable1 = int(input("input your first value : "))
            variable2 = int(input("input your second value : "))
            answer = mul(variable1, variable2)
        elif choice == "e" or choice == "E":
            print("shutting down")
            loopOrder = False
