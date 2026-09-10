x=int(input())
print("Number is odd:",x%2!=0)

age=int(input("Enter age:"))
print(age," years = ",age*365," days")

min = int(input("Enter minutes:"))
print(min//60," hours ",min%60," minutes")

num=int(input())
print(num," last digit:",abs(num%10))

#inputs: role(student/teacher),age.   eligible if role==student and age<=21
role=input("Enter role(Teacher/Student):")
age=int(input("Enter age:"))
if(age<=21 and role=="Student"):
    print("eligible")
else:
    print("not elgible")
