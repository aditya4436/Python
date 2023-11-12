def PrimeNumber(num):
    flag=False
    if num==1:
        print(num, " is not a Prime Number.")
    elif num>1:
        for i in range(2, num):
            if(num%i)==0:
                flag=True
                break
        if flag==True:
            print(num, " is not a Prime Number.")
        else:
            print(num, " is a Prime Number.")

number=int(input("Enter the number to check if it is a Prime Number or not."))
PrimeNumber(number)