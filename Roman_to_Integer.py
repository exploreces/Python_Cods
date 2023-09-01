def rom_inte(s:str)->int:
    roms = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    prev =0
    result =0

    for i in reversed(s):
        value = roms[i]
        if value>=prev:
            result+= value
        else:
            result-=value
        prev =value
    return result
        
def main():
    input_str = input("Enter a Roman numeral: ")
    result = rom_inte(input_str)
    print("Converted integer:", result)

if __name__ == "__main__":
    main()
    

"""
def rom_inte(s: str) -> int:
    roms = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    prev = 0
    total = 0  # Corrected variable name
    curr = 0

    for c in range(len(s)):
        curr = roms[s[c]]
        if curr > prev:
            total += curr - (2 * prev)  # Corrected subtraction logic because once prev is added already hence 2 is multiplied before substracting!
        else:
            total += curr  # Corrected addition logic
        prev = curr

    return total

def main():
    input_str = input("Enter a Roman numeral: ")
    result = rom_inte(input_str)
    print("Converted integer:", result)

if __name__ == "__main__":
    main()

"""