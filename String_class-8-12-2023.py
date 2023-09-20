




# string methods
#---------------



#1)it is denoted by '' or " "  or """ """

#2)it can be datatype

#3)it is immutable



#String methods


#1)captilize



txt =  "hi karthik good morning welcome to india"


x =txt.capitalize()

print(x) #Hi karthik good morning welcome to india





#2)casefold()  is used convert lower to upper case and vice versa


txt = "Hi venya good morning welcome to India"


x = txt.casefold()

print(x)  #hi venya good morning welcome to india



txt1 = "hi venya good morning welcome to india"

x = txt1.casefold()

print(x)


txt2 = "HI GOOD MORNING WELCOME TO INDIA"

x = txt2.casefold()

print(x)  #hi good morning welcome to india


txt3 = "HI GOOD MORNING welcome to india"

x = txt3.casefold()

print(x)  #hi good morning welcome to india


#3)center() #it will returns a centre string


txt = "Hi Venya"

x = txt.center(20)

print(x)    #Hi Venya


txt = "Hi Venya"

x = txt.center(100)

print(x)    #Hi Venya


txt = "Hi Venya"

x = txt.center(1000)

print(x)    #Hi Venya


#4)count() #we can the number of items

txt = "Im in India, India is good in Traditional values, finally India is best"



x = txt.count("India")

print(x)


#5)encode()  #it returns the encoded version of the string

txt = "My name is Venya and staying in Singpore"

x = txt.encode()

print(x)   #b'My name is Venya and staying in Singpore'


#6)endswith()  #this methods returns True if the string ends with the specified value otherwise it returns false

txt = "Hello, welcome to singpore"

x = txt.endswith("singpore") #True
print(x)

x = txt.endswith("hyderabad") #False
print(x)


#7)expandtabs() The expandtabs() method sets the tab size to the specified number of spaces

txt = "H\te\tl\tl\to"

x =txt.expandtabs(7)

print(x)  #H      e      l      l      o


txt = "K\tA\tR\tT\tH\tI\tK"

x =txt.expandtabs(7)

print(x)  #K      A      R      T      H      I      K


txt = "V\tE\tN\tY\tA"

x =txt.expandtabs(7)

print(x)  #V      E      N      Y      A


#8)find() #
#1)The find method find the first occurrence of the specified value 
#2)The find method returns -1 if the value is not found


#Syntax string.find(value,start,end)

#"Hello, welcome to singpore"
# 0123456789


txt = "Hello, welcome to singpore"

x = txt.find("e")

print(x) #1

txt = "Hello, welcome to singpore"

x = txt.find("o")

print(x) #4

txt = "Hello, welcome to singpore"

x = txt.find("welcome")

print(x) #7


txt = "Hello, welcome to singpore and karthik working in Google"


x = txt.find("e",5,10)

print(x) #8

txt = "Hello, welcome to singpore and venya working in facebook"


x = txt.find("s",5,10)

print(x) #-1


#9)format()
'''The format method formats the specified value(s)
and insert them inside the string placeholder'''

#Method -1
txt = "My name is {name} working in {company}".format(name="venya", company ="Amazon")

print(txt) #My name is venya working in Amazon

#Method -2

txt = "My name is {0} working in {1}".format("venya","Amazon")

print(txt) #My name is venya working in Amazon

#Method-3

txt = "My name is {} working in {}".format("venya","Amazon")

print(txt) #My name is venya working in Amazon

#10)format_map()


print("-----------------#11)index()------------------")
#The index method() finds the first occurence of the specified value
#Ihe indexmethod() method raises exception if value is not found
#The index() is almost similar to find() method
#Index if value is not found it returns exception
#find() if value is not found it returns -1

#syntax  string.index(vlaue,start,end)

         #value -required
         #start,end- Optional

txt = "Hi karthik good morning welcome to india"
#      0123

x = txt.index("k")

print("The index position of k is:",x) #The index position of k is: 3

txt = "Hi karthik good morning welcome to india"
#      0123

x = txt.index("o")

print("The index position of o is:",x) #The index position of o is: 12

txt = "Hi karthik good morning welcome to india"
#      0123

x = txt.index("i")

print("The index position of i is:",x) #The index position of i is: 1

txt = "Hi karthik good morning welcome to india"
#      0123

x = txt.index("a")


print("The index position of a is:",x) #The index position of a is: 4


txt = "Hi karthik good morning welcome to india"
#      0123

x = txt.index("a",3,8)

print("The index position of a is:",x) #The index position of a is: 4



 
#12)isalnum()   #al-alphabetical  abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
                #num-numrical  0123456789
                #is - for checking the condition


txt = "google555"

x = txt.isalnum()

print(x)  #True


txt = "google"

x = txt.isalnum()

print(x)  #True

txt = "555"

x = txt.isalnum()

print(x)  #True

txt = "@#$%^"

x = txt.isalnum()

print(x) #False


#13)is alpha()     ##al-alphabetical  abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ


txt = "google555"


x = txt.isalpha()

print(x)  #False


txt = "google"

x = txt.isalpha()

print(x)  #True


txt = "GOOGLE"

x = txt.isalpha()

print(x) #True



#14)isascii()












#15)isdecimal()  #if all the characters in a string are decimals (0-9)




txt = "555"

x = txt.isdecimal()

print(x) #True

txt = "google555"

x = txt.isdecimal()

print(x) #False


txt = "GOOGLE555"

x = txt.isdecimal()

print(x) #False


txt = "@#$%^&"

x = txt.isdecimal()

print(x) #False





#16)isdigit()
#The is digit() method retuens True if all the characters are digits otherwise returns False


txt = "233734"


x = txt.isdigit()

print(x)  #True


txt = "abcdfes6666"
x = txt.isdigit()
print(x) #False


txt = "@#$%^&*"
x = txt.isdigit()
print(x) #False



#17)isidentifier

#The isidentifier() method returns True if the string is valid identifier otherwise False

#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9) and underscores

#A valid identifier cannot start with underscore and any spaces


txt = "Singpore"

x = txt.isidentifier()

print(x) #True


txt = " Singpore"

x = txt.isidentifier()

print(x) #False


#18)islower() The islower() method returns True if all the characters are in lowercase otherwise returns False

#Note islower() only applicable to alphabet characters not Numbers,symbols and spaces


#syntax string.islower()

txt = "HI KARTHIK GOOD MORNING"

print(txt.islower())  #False

txt ="Hi Venya Welcome to India"

print(txt.islower()) #False

txt ="hello 123"

print(txt.islower()) #True

txt = "123 $$$"

print(txt.islower()) #False



#19)isnumeric() The is numeric method returns True if all the characters are numeric(0-9) otherwise False

#-1 and "1.5" not considered as a numeric values because all the characters in the string


#syntax string.isnumeric()


txt = "1000"
print(txt.isnumeric()) #True


txt = "1000Singpore"
print(txt.isnumeric()) #False


txt ="Singlore"
print(txt.isnumeric()) #False



#20)isprintable() The isprintable() method returns True if all the Characters are printable otherwise False


#Syntax  string.isprintable()

txt = "Hello! Welcome to India"

x =txt.isprintable()

print(x) #True


txt = "Hello! Welcome to India  123456"

x =txt.isprintable()

print(x) #True



#21)isspace() The isspace() method returns True if all the characters in string are whitespaces otherwise false

#syntax string.isspace()

txt =" "

x = txt.isspace()

print(x) #True


txt =""

x = txt.isspace()

print(x) #False

txt ="            "

x = txt.isspace()

print(x) #True



#22)istitle() The istitle method returns True if all words in a text start with Uppercase and rest of the words are lower case letters otherwise false.


#syntax string.istitle()


txt = "HI KARTHIK GOOD MORNING WELCOME TO INDIA"

x = txt.istitle()

print(x) #False


txt = "Hi Karthik Good Morning Welcome To India"

x = txt.istitle()

print(x) #True



txt = "Hi Karthik GOOD Morning Welcome To India"

x = txt.istitle()

print(x) #False


#23)isupper() #The isupper() method returns True if all the character are in upper case otherwise it will returns False

#Numbers symbols and spaces are not checked only alaphabet characters checked

#syntax   string.isupper()



txt = "HI VENYA GOOD MORNING"

print(txt.isupper()) #True


txt = "hi venya good morning"

print(txt.isupper()) #False


txt = "hi venya GOOD MORNING"

print(txt.isupper())#False


#24)join() The join method takes all items in an iterable and joins them into one string

#A string must be specified as the seperator

#syntax string.join(iterable)


txt ="HI VENYA"

x = "--*--".join(txt)

print(x) #H--*--I--*-- --*--V--*--E--*--N--*--Y--*--A


txt ="good morning"

x = "*****".join(txt)

print(x) #g*****o*****o*****d***** *****m*****o*****r*****n*****i*****n*****g



#25)lower() The lower method returns a string where all characters are lowercase


#Symbols and Numbers are Ignored

#syntax string.lower()


txt = "HI KARTHIK WELCOME TO INDIA"

x = txt.lower()

print(x) #hi karthik welcome to india


txt = "HI VENYA GOOD MORNING"

x = txt.lower()

print(x)  #hi venya good morning

txt = "hi venya GOOD MORNING"

x = txt.lower()

print(x)



#26)lstrip()



#27)parition()


#28)rfind()



#29)strip()


#30)rstrip()



#31)split()


#32)splitlines()



#33)startswith()



#34)swapcase()



#35)title()



#36)translate()



#37)upper()




#38)zfill()


