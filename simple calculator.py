try:
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    op=input("Enter Operation(+,-,*,/): ")
    
    if op=="+":
        print("Result:",num1+num2)
    elif op=="-":
        print("Result:",num1-num2)
    elif op=="*":
        print("Result:",num1*num2)
    elif op=="/":
        print("Result:",num1/num2)
    else:
        print("Invalid operator")

except ValueError:
    print("Enter numbers only!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    
    
