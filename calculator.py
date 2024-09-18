while(1): 
    num1=int(input("Enter the Number 1: "))
    op=input("Enter operation: ")
    num2=int(input("Enter the Number 2: "))
    print(op)
    if(op=="+"):
         print(f"addition of {num1} & {num2} is",num1+num2)
    elif(op == "-"):
         print(f"Substraction of {num1} & {num2} is",num1-num2)
    elif(op=="*"):
         print(f"Multiplication of {num1} & {num2} is",num1*num2)
    elif(op=="/"):
         print(f"Division of {num1} & {num2} is",num1/num2)
    else:
         print("Enter valid input")  