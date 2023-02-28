n = int(input("Enter number to find factor : "))

print("Factors of given number is :")
for i in range (1,n+1):
    if n%i==0 : 
        print(i)
    