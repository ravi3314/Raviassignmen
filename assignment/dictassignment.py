#1.Write a Python script to add a key to a dictionary.

num ={1:10,2:20}
num[3] =30
print(num)


#2.Write a Python script to check whether a given key already exists in a dictionary
my_dict ={1:'i' , 2:'n' , 3:'d' ,4:'i' , 5:'a'}
if 1 in my_dict:
 print("present in dictionary")

 print()

 #3.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

n = 15 
numbers = {} 
for i in range(1, n+1):
	numbers[i] = i * i
print (numbers)

print()

#4Write a Python program to sum all the items in a dictionary.

dic={ 'a':455, 'b':223, 'c':300, 'd':908 }

print("Dictionary: ", dic)

print("sum: ",sum(dic.values())) 

#5.Write a Python program to combine two dictionary by adding values for common keys.

dict1 = {'a': 100, 'b': 200, 'c':300}  
dict2 = {'a': 300, 'b': 200, 'd':400}  
new_dict = dict2  
for i, j in dict1.items():  
    if i in dict2:  
        new_dict[i] = j + dict2[i]  
    else:   
        new_dict[i] = j  
print("The new dict is:", new_dict) 

print()

 #6.Write a Python program to iterate over dictionaries using for loops
dis = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dis:
    print(key, dis[key])

#7.Write a Python program to access dictionary key's element by index.
sub= {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(sub)[0])
print(list(sub)[1])
print(list(sub)[2])

#89.Write a Python program to remove a key from a dictionary.
myDict = {'a':1,'b':2,'c':3,'d':4}
print("Before removing" ,myDict)
if 'a' in myDict: 
    del myDict['a']
print("after removing" ,myDict)

print()

#10.Write a Python script to merge two Python dictionaries.d

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)