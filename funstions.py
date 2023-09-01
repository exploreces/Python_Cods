

#functions syntax
""" def function_name(parameters):
               // do something        """

#argv use:
'''
def myFun(*argv):
    for arg in argv:
        print(arg)
 
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

'''

#Adding Docstring to the function
"""
# A simple Python function to check
# whether x is even or odd
 
 
def evenOdd(x):
    #Function to check if the number is even or odd
     
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
 
 
# Driver code to call the function
print(evenOdd.__doc__)
"""

# replication

"""
string * number
number * string // output --    "James" * 3 gives "JamesJamesJames"
                                 3 * "an" gives "ananan"
                                5 * "2" (or "2" * 5) gives "22222" (not 10!)
 
 """

 #