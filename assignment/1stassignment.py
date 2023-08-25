print("create a table using for loop and while loop")
num=int(input('for loop table'))
for i in range (1,11):
    print(num , 'x' ,i ,'=' ,num*i)
    print()


number=int(input('while loop table'))
count=1
while count<=10:
    print(number,'x' , count, '=' ,number*count)
    count+=1

print()

print("creating a logic using conditional statment")
list =[3,76,65,32,87]
for num in list :
    if num ==3:
        print("number is" , num)

    elif num ==76:
        print("number is" ,num)

    elif num==65:
        print("number is " , num)

    else:
        print("number not found")

 
print()


print("create a logic using relational and logical operator")
z=[30,90,99,85,92,50,35]
for num in z:
    if((num==99) or (num==99)):
        print("state topper" ,num)

    elif(num>90):
        print("college topper" ,num)

    elif(num>=40 & num<90):
        print("passed" ,num)

    else:
        print("failed" ,num)
