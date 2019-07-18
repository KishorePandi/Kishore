a=int(input('Enter any number: '))
number = a%2
if number == 0:
    print(a, "is an even number")
elif number ==1:
    print(a,"is an odd number")
else:
    print("Error, Invalid input")
