def EvenNumber(num):
    if(num%2==0):
        print(num, " is an Even Number.")
    else:
        print(num, " is not an Even Number.")

number=int(input("Enter a numnber: "))
EvenNumber(number)