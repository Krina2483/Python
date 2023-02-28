n = int(input("Enter length of fibonacci series : "))

n1=0
n2=1
temp=0

if n<1 :
    print("Enter positive integer !!")    
elif n==1 :
    print("Fibonacci series is ",n1)
elif n==2 :
    print("Fibonacci series is ")
    print(n1,end=" ")
    print(n2)
else :
    print("Fibonacci series is ")
    print(n1,end=" ")
    print(n2,end=" ")

    for i in range(3,n+1) :
        temp=n1+n2
        n1=n2
        n2=temp
        print(temp,end=" ")