# membership operator using in and not in 
a = "good"
string_a = "good morning"
if (a in string_a):
    print("True")
else:
    print("False") # using in method

a = "good"
string_a = "good morning"
if (a not in string_a):
    print("True")
else:
    print("False") # using not in method

print()

# removing space from string
sentence = " hello , good morning   "
space_remove = sentence.strip()
print(space_remove)
print()


# compare two strings
sentence_1 = "python is popular language"
sentence_2 = "python is easy to understand"
length_1 = len(sentence_1)
length_2 = len(sentence_2)
if length_1 > length_2 :
    print("sentence_1 is bigger")
else:
    print("sentence_2 is bigger")

print()

# finding substring by using index method
sentence = "day by day,demand of python is increases"
print(sentence.index("p"))

print()

# finding substring by using rindex method 

sentence = "Marolix technology solution"
print(sentence.rindex("h"))
print()

# finding substring by using find method
sentence = "Marolix technology solution"
substring_of_sentence = "l"
print(sentence.find(substring_of_sentence))
print()

# finding substring using rfind method  
sentence = "my name is ravi mishra"
substring_of_sentence = "n"
print(sentence.find(substring_of_sentence))

print()

# replacing the string 
sentence_1 = "hello,ravi speaking"
new_sentence = "mishra"
sentence_2 = sentence_1.replace("ravi",new_sentence)
print(sentence_2)

print()

# splitting the string 
sentence = "Hello ravi mishra here"
split_sentence = sentence.split(" ")
print(split_sentence)

print()

# joining the string
sentence = "welcome to marolix"
join_sentence = "-".join(sentence)
print(join_sentence)
