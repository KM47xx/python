while True:
    print("1Add 2Sub 3Mul 4Div 5Fact")
    choice=int(input("Enter choice"))
    match choice:
        case 1:
            a=int(input("a:"))
            b=int(input("b:"))
            print(a+b)
        case 2:
            a=int(input("a:"))
            b=int(input("b:"))
            print(a-b)
        case 3:
            a=int(input("a:"))
            b=int(input("b:"))
            print(a*b)
        case 4:
            a=int(input("a:"))
            b=int(input("b:"))
            print(a/b)
        case 5:
            a=int(input("a:"))
            while a>0:
                a*=a-1
                a-=1
            print(a)