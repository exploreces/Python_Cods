#variables
# types -- int; boolean; float here we can store any thing without defining it
#float(); int(); bool();


"""name="Ayushi"
age=19
print(name)
print(age)"""


# to take input

"""
name = input("whats ur name ")
# this will print the name of user in console
print(name)
age=input("say ur age")
print(name+"and her age is " + age)
"""

#to conactenate or to add

"""
old_age = input("ur age")
# new_age = old_age+20 

#this is concatenation but will give error -- TypeError: can only concatenate str (not "int") to str
# as its visulizing old age as a string hence cant concatenate.

new_age = int(old_age)+2
print(new_age)
"""

# predefined functions

'''
name = input()
print (name.upper())
print(name.lower())
print(name.find('s'))
print(name.replace("s","a"))
print('m' in name) #will return true or false
print("ay" in name) # will return true or false

'''

#operators

""" Operator prescedence 
() ; *; / ; +; - ; 
"""

'''
power = 5**2
## power operator -- gives us result of raising first number by second one

divide = 5/2
divide_no_decimal = 5//2

remainder = 5%2

# shortcuts to perform arithmetic
i=5
i+=2
i*=2
i/=2
i-=2

'''
# comparing operators
'''
print(3>2)
print(3==3)
print(3<2)
print(3!=2)

'''
# logical operators

'''
print(2>3 or 2>1)
print(5>3 and 5<3)
print(not 2>4)

'''

#conditional statements

## if condition
'''
age = input("say ur age")
age_ = int(age)
if age_ >=18:
        print("Adult")
        print("u can vote")
elif age_ <10:
        print("u r kid now")
else: 
        print("need some more years to vote")

        '''

#Range
"""
numbers = range(5)
print(numbers)

#to print in sameline 

for i in numbers:
        print(i+1,end="")
 
"""
#loops
'''
i=1
while i <=5:
    print(i * "A")
    i+=1

'''

# for loop

'''
for i in range(5):
        print (i +1)

        '''