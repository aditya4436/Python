def EvenNumber(num):
    if(num%2==1):
        print(num, " is an Odd Number.")
    else:
        print(num, " is not an Odd Number.")

number=int(input("Enter a numnber: "))
EvenNumber(number)