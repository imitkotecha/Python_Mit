num= int(input("Enter a Number"))
factorial = 1
if num<0:
    print("Factorial doesnt exist for negative number")
elif num==0:
    print("The factorial of 0 is 1")
else :
    for i in range(1,num+1):
        factorial = factorial*i
        print("the factorial of",num,"is",factorial)