n = int(input("Enter number to check prime or not : "))
temp=1
for i in range (2,n):
    if n%i==0 :
        temp=0

if temp==1 :
    print("Number is prime")
else :
    print("Number is not prime")