i=1
while i==1 :
    operation = input("Enter arithmatic operation from +,-,*,/ and enter 0 to exit : ")
    if operation == '0' :
        i=0
        break

    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    
    if operation == '+' : 
        print("Sum of given number is : ",(num1+num2))
    elif operation == '-' :
        print("Subtraction of given number is : ",(num1-num2))
    elif operation == '*' :
        print("Multiplication of given number is : ",(num1*num2))
    elif operation == '/' :
        print("Division of given number is : ",(num1/num2))
    else : 
        print("Invalid operation choice !!")
    print("\n")
    