try:
    n=int(input("Enter the Year :"))
    if n>0:
        if(n%4==0):
            print(n,"Is a Leap Year")
        else:
            print(n,"Is not a Leap Year")
            print("Leap year is :",(n//4)*4)
    else:
        print("Invalid")
except:
    print("Invalid")
