
print('''1.find if any 5 numbers are positive or negative. and write addition of positive numbers.
         2.find whether a year is leap year.
         3.display multiplication table of a number.
         4.find factorial of a number.
         5.display list of five numbers
         0.exit the program
         
''')

    
while True:
    choice=int(input("enter the your choice's number:"))
    
    if choice==1:
        pos=0
        for i in range (5):
            number =int(input(f"enter the {i+1} number"))
            if number>0:
                pos=pos+number
                print(number,"is positive")
            elif number<0:
                print(number,"is negative")
                continue
            elif number==0:
                print("zero is neither negative nor zero.")
        print("addition of positive numbers is: ",pos)
        
    elif choice==2:
        year=int(input("enter the year:"))
        if(year%4==0 and year%100!=0)or\
        (year%100==0 and year%400==0):
            print(year,"is a leap year")
                
        else:
            print(year,"is not a leap year")
            
    elif choice==3:
        num=int(input("enter the number"))
        for i in range(1,11):
            print(f"{num} * {i:2} = {num*i:2}")
            
    elif choice==4:
        number=int(input("enter the number:"))
        fact=1
        i=1
        while i<=number:
            fact=fact*i
            i=i+1
        print(f"factorial of {number} is {fact}.")

    elif choice==5:
        list=[]
        for num in range(5):
            num=int(input("enter the number:"))
            list.append(num)
        print(list)
                
    elif choice==0:
        print("thank you!")
        break
        
    else:
        print("enter choice from give menu")
        
        
    
