print('Hello World')
pi=3.1416
r=2
area=pi*(r**2) # power=**
print(area)
print(type(area))

#String
print("\n\"String:\"\n")
str="Hello \'Siam\'"
print(f'length of ({str}):{len(str)}')
print(f'subset of str from index 6 to last:{str[6:]}') #subset of str from index 6 to last
print(f'subset of str from index 4 to 0:{str[:5]}') #subset of str from index 4 to 0
print(f'subset of str from index 3 to 7:{str[3:8]}') #subset of str from index 3 to 7
print(f'step size=2 means read the str exceeding 1 character:{str[::2]}') #step size=2 means read the str exceeding 1 character
print(f'read from i=2 to 6 exceeding 1 character:{str[2:7:2]}') #read from i=2 to 6 exceeding 1 character
print(f'read all character from rev:{str[::-1]}') #read all character from rev
print(f'String concat:{"Hi"+(str[5:])}')#string concat
ch='z'
print(f'repeat letter z by 10 times:{ch*10}') #repeat letter 10 times

#string function
print(f'Uppercase of str:{str.upper()}')
print(f'make list based on whitespace:{str.split()}') #make list based on whitespace
print('make split whether l found:{}'.format(str.split('l'))) #make split whether l found

#print formatting with strings
print("\n\"String print with Formatting:\"\n")
print("The {} {} {}".format("fox","quick","brown"))
print("The {1} {2} {0}".format("fox","quick","brown")) #indexing on formatting
print("The {0} {0} {0}".format("fox","quick","brown"))
print("The {q} {b} {f}".format(f="fox",q="quick",b="brown"))

#print formatting with float
result=1000/77
print("The result(precision upto 6) was {r:1.6f}".format(r=result)) #r:1.6f where r=value,1=whitespace,6=precision

#different way of formatting
name="siam"
age="20"
print(f"{name} is {age} years old")

#List
list=["one",'two','three']
list[0]=list[0].upper()
print(f"List: {list}")
list.append("four") #add to last
print(f"after appended \'4\':{list}")
print(f"popped item of index 3: {list.pop(3)}") # by default item popped from last

#dictionaries/object as key value pair

d={'key1':['a','b','c'],'k2':100,'k3':10.5}
print(f'\nDictionaries:{d}')
print(f"index 2 to upper:{d['key1'][2].upper()}")
d['key1'][0]='d'
print(f"Override a by d:{d['key1']}")
print(f"dictionary keys:{d.keys()}")
print(f"Dictionaries values:{d.values()}")
print(f"Dictionary key value pairs:{d.items()}")

#tuples can't override item like lists

t=('a','a','b')
print(f"\nTuples:{t}")
print(f"Count \'a\' in tuples: {t.count('a')}")
print(f"Index of \'a\' in tuples: {t.index('a')}:{t[0]}")

#Set unordered collection of unique elements

myset=set()
myset.add(1)
myset.add(2)
myset.add(1)
print(f"\nSet of unique elements:{myset}")

mylist=[1,1,1,1,2,2,2,2,3,3]
newset=set(mylist)
print(f"List: {mylist}")
print(f"Set from list: {newset}")

#File I/O
with open('myfile.txt',mode='r') as myfile: #using this we don't need to bother about closing the file
    contents=myfile.read()
    myfile.seek(0) #as file read happened cursor positioned must be at 0 position for again read
    list=myfile.readlines()
print(f"\nRead mode:\nFile read:\n{contents}")
print(f"List from file on \\n: {list}")

with open('hello.txt',mode='w+') as newFile:
    newFile.write("One on 1st")
    newFile.write("\nTwo on 2nd")
    newFile.write("\nThree on 3rd")
    newFile.seek(0)
    print(f"\nWrite and read:\n{newFile.read()}")

#statements
print("\n\nStatements if-elif-else:\n")
n=61
if (n%2==0):
    print(f"{n} is even")
elif (n%2!=0):
    if (n<50):
        print(f"{n} is odd and below 50")
    else:
        print(f"{n} is odd and above 50")