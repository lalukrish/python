def addition(num1,num2):
    print("addition=",num1+num2)

def subtraction(num1,num2):
    print("subtraction=",num1-num2)

def multiplication(num1,num2):
    print("multiplication=",num1*num2)

def division(num1,num2):
    print("division=",num1/num2)

while True:
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")    
    print("5. exit")
    choice=int(input("Enter your choice(1-5):"))

    if choice==1:
        num1=int(input("first  no:"))
        num2=int(input("second no:"))
        addition(num1,num2)


    elif choice==2:
        num1=int(input("first  no:"))
        num2=int(input("second no:"))
        subtraction(num1,num2)
    
    elif choice==3:
        num1=int(input("first  no:"))
        num2=int(input("second no:"))
        multiplication(num1,num2)
    
    elif choice==4:
        num1=int(input("first  no:"))
        num2=int(input("second no:"))
        if num2 == 0:
            print('Infinity')
        else:
            division(num1,num2)
                
    elif choice==5:
        break
    else:
        print("invalid Choice")
