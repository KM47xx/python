h=int(input())
if h>18:
    print("eligible to drive")
else:
    print("Not elgible")    
print("Thank you")

n=int(input())
print("Number is even?:",n%2==0)

d=int(input("Enter day no:"))
if d==1:
    print("mon")
elif d==2:
    print("tue")
elif d==3:
    print("wed")
elif d==4:
    print("thur")
elif d==5:
    print("fri")
elif d==6:
    print("sat")
elif d==7:
    print("sun")
else:
    print("No such day")

match d:
    case 1:
        print("a")
    case 2:
        print("b")
    case 3:
        print("c")