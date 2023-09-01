
def longest(s: str) -> int:
    if len(s) == 0:
        return 0

    char_map = {}
    max_length = start = 0

    for i in range(len(s)):
        if s[i] in char_map and start <= char_map[s[i]]:
            start = char_map[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
            char_map[s[i]] = i
    return max_length

def main():
    input_str = input("Enter a string: ")
    result = longest(input_str)
    print( result)

if __name__ == "__main__":
    main()
