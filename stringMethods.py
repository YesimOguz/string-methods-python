# indexing slicing
sentence = ('mangoes are green on the outside, yellow on the inside')
print(sentence[6])
print(sentence[0:6])
print(sentence[0:7])
#strings are immutable

print('Dear'+'God')

print('+'*40)

a = 70
print(f'the value of variable is {a}')

#string methods
sentence = ('mangoes are green on the outside, yellow on the inside')
#it it adds 80 whitespace characters to both sides of string
print(sentence.center(80))
#it reomoves whitespaces on the edges of the string
print(sentence.strip())

"""
.center(40) adds 40 whitespace characters to both sides of the string
.strip() removes whitespace on the edges of the string"""

option = input("yes or no?: ").strip().lower() #or.upper()
if option == "yes":
    print("you agreed")
elif option == "no":
    print("you disagreed")
else:
    print("i do not understand you")


option = input("yes or no?: ").strip().upper()
if option[0] == "Y":
    print("you agreed")
elif option[0] == "N":
    print("you disagreed")
else:
    print("i do not understand you")

sentence = ('mangoes are green on the outside, yellow on the inside')
#everything is small character
sentence.lower()
print(sentence.lower())
#put everything is capital letter
sentence.upper()
print(sentence.upper())

print(sentence[0]=='M') 

# it finds where is 'on'  , it will give us index number which is 18
print(sentence.find('on'))


lst_strings = ["beautiful","the","field","beyond","the river"]
# this code converts list to a string
# we can choose the sign what we want to add between word with this sign " "
print(" ".join(lst_strings))

# this code converts a string to a list
string = 'God is gracious and kind'
print(string.split())

lst1 = 'God is gracious and kind'.split()
print(lst1)
print("*".join(lst1))

# this code makes caital first letter each word
print(sentence.title())

string = 'marry jane anne'
print(string.title())

# this code replace eez for is
x = "all is well"
print(x.replace("is","eez"))
#print("All is well".replace("is","eez")) (this is another way)

# this code replace went instead goes
y = "she goes to work"
print(y.replace("goes","went"))

# theese are to convert string to list
# the computer understand that first one is one string and didnt specified
print("1+2+3+5+6".split())
print("1+2+3+5+6".split("+"))
print("1>2>3>5>6".split(">"))

# this code replace k instead c ,zinstead s 
table = str.maketrans("cs","kz")
a = 'this is an icredible test'
print(a.translate(table))

table = str.maketrans("ae","ei")
b = "i am an engineer"
print(b.translate(table))

# this is to covert tuple to string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)