#. 1Write a python program to remove a given  character from string
str=input("Enter a string")
ch=input("enter a character to remove")
print(str.replace(ch, ""))
print()

#2.Write a program to check String is Palindrome or not
input_string=input("enter a string")
rev = input_string[::-1]

if input_string == rev:
    print(rev + " is Palindrome")
else:
    print(rev + " is not Palindrome")

print()

#3 Write a python program to check given character is vowel or consonant
x=input("enter a character to check vowel or consonent")
if (x == 'a' or x == 'e' or x == 'i' or 
        x == 'o' or x == 'u' or x == 'A' or 
        x == 'E' or x == 'I' or x == 'O' or 
        x == 'U'):
        print("Vowel")
else:
     print("consonent")

print()

#4.Write a python program to replace string space with given character in Python
s=input("enter a string")
s=s.replace('' , '_')
print(s)

print()

#5  Write a python program to count alphabets, digits, and special characters in the string.

str1 = input("Please Enter your Own String : ")
alphabets = digits = special = 0

for i in range(len(str1)):
    if((str1[i] >= 'a' and str1[i] <= 'z') or (str1[i] >= 'A' and str1[i] <= 'Z')): 
        alphabets = alphabets + 1 
    elif(str1[i] >= '0' and str1[i] <= '9'):
        digits = digits + 1
    else:
        special = special + 1
        
print("Alphabet = ", alphabets)
print("digits = ", digits)
print("special character =", special)

print()


 #6.Write a python program to remove all the blank spaces in a given string.

str2 =input("enter a string") 
   
str2 = str2.replace(" ","");  
          
print("String after removing all the blank spaces" + str2)

print()

#7.Write a python program to find sum of integers in the string.

str1 = input('Enter a string: ')
sum=0
for i in str1:
	#if character is a digit
    if i.isdigit():
		#taking sum of integral digits present in the string 
        sum=sum+int(i)
print("sum of integer =",sum)

print()

#9.Write a python program to count occurrence of given character in string.

my_string = "marolix"
my_char = "r"

print(my_string.count(my_char))

print()


#10.Write a python program to check string is anagrams or not in Python.

a = input("Enter the First String  = ")
b = input("Enter the Second String = ")

if(sorted(a) == sorted(b)):
    print("both Strings are Anagrams.")
else:
    print("both Strings are not Anagrams.")
    print()










