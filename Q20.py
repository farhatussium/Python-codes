num=int(input("Enter your number:"))
if num>=80 and num<=100:
    print("A+")
elif num>=70:
    print("A")
elif num>=60:
    print("A-")
elif num>=50:
    print("B")
elif num>=40:
    print("C")
elif  num>= 1 and num<=30:
    print("F")
else: 
    print("Invalid Input")