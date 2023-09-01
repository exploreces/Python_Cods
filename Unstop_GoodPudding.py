

"""Bob is going on a 
trip to Japan, where he finds a big pudding shop, where he sees a menu and food challenges. 
Bob accepts the challenge, so here are the game rules.
Pudding assigns an integer number to it. Bob has configured the good pudding.
Good pudding means the associated number has been reversed twice. 
Note:- For example, Reversing 42100 offers 421 as the leading zeros are not retained.

Input Format
The first line contains a Integer n –  Number of Test Cases
The next lines contains n integers

Output Format
Print n lines containing a boolean number – “1” (Accepted) and “0” (Reject) """

# code:

n = int(input())
str = []
for i in range (n):
    str.append(int(input()))

for num in str:
    last_digit = num % 10  # Get the last digit of the number

    if int(last_digit) == 0:
        print("0")
    else:
        print("1")





  