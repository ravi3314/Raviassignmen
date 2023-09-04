#1.write a python program to merge two lists.

L1=eval(input("input 1st list"))
L2=eval(input("input 2nd list")) 
L3=L1+L2
print(L3)

print()


#2.write a python program to find the sum of list element
nums = []
print("Enter 5 elements for the list: ")
for i in range(5):
    val = int(input())
    nums.append(val)

sum = 0
for i in range(5):
    sum = sum + nums[i]

print("\nSum of all elements =", sum)

print()

# 3write a python program to print even and odd numbers seperatly in list.

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)

even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)

# 4.write a python program to delete element of given index in list.

print("Enter 6 Elements: ")
dele = []
for i in range(6):
    dele.append(input())

print("\nEnter the Value to Delete: ")
val = input()

dele.remove(val)

print("\nThe New list is:")
print(dele)

# 6.write a python program to insert an elemet  at given index location.
arr = [1, 2, 3, 4, 5]
num=int(input("Enter a number to insert in array : "))
index=int(input("Enter a index to insert value : "))

arr.insert(index, num)  
print("Array after inserting",num,"=",arr)

# .7.write a python program to check the sizes of given two lists are same.

l1=eval(input("enter 1st list"))
l2=eval(input("enter second list"))
l1.sort()
l2.sort()
if l1 == l2:  
    print("The list1 and list2 are equal")  
else:  
    print("The list1 and list2 are not equal")

print()

#8.Write a Python function that takes two lists and returns True if they have at least one common member
list1=eval(input("enter 1st list"))
list2=eval(input("enter 2nd list"))
result = False
for x in list1:
 for y in list2:
	 if x == y:
		 result = True
print(result)

print()
# 9Write a Python program to convert a list of multiple integers into a single integer.
List1 =eval(input("enter list"))  
var = '' 
for element in List1: 
    # converting integer to string and adding into variable
    var += str(element)
print(int(var))

print()

#10.Write a Python program to remove duplicates from a list.

dup=eval(input("enter a list")) 
print("The initialized list is ",dup)  
temp_list=[]  
for i in dup:  
    if i not in temp_list:  
        temp_list.append(i)   
print(" after removing duplicates is ",temp_list) 
