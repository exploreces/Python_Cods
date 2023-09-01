
# PS statement
""">>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra"""


def mutate_string(string, position, character):
    string= string[:position]+character+string[(position+1):]
        
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

    """The line combines these components to achieve the desired mutation:

string[:position]: This extracts the substring of string from the beginning up to (but not including) the specified position.
character: This is the replacement character that you want to insert at the specified position.
string[(position+1):]: This extracts the substring of string starting from the character immediately after the specified position.
By concatenating these three parts, you effectively replace the character at the specified position with the provided character, resulting in the mutated string."""