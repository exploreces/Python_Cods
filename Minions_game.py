
# Medium Level
"""Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""

def Minion (String):
    vowels= ['A','E', 'I' , 'O', 'U']
    kelvin =0
    stuart =0
    index = -1
    for i in String:
        index +=1
        if ( i not in vowels):
            stuart += (len(String)-index)
        else:
            kelvin += (len(String)-index)
    
    if stuart>kelvin:
        print('Stuart' + str(stuart))
    elif kelvin>stuart:
        print('Kelvin' + str(kelvin))
    else:
        print("draw")


if __name__ == '__main__':
    s = input()
    Minion(s)
##################################################################################
#HACKERRANK DIRECT ---

"""def minion_game(string):
    kevin_score = 0
    staurt_score =0

    index=-1
    for i in s:
        index+=1
        if (i not in ('I','A','O','U','E')):
            staurt_score+=(len(s) - index)

        else:
            kevin_score+=(len(s) - index)



    if kevin_score>staurt_score:
        print('Kevin '+str(kevin_score))

    elif kevin_score<staurt_score:
        print('Stuart '+str(staurt_score))     

    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)"""
