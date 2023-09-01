
def str_to_inte(s: str) -> int:
    numeric_str = ''.join([i for i in s if i.isdigit() or (i == '-' and s.index(i) == 0)])
# if +, - is not important then we can also use this--
# numeric_str = int(''.join([c for c in s if not (ord(c) < 48 or ord(c)>57)]))
    
    
    if numeric_str:
        numeric_value = int(numeric_str)
        if numeric_value > (2**31) - 1:
            return (2**31) - 1
        elif numeric_value < -2**31:
            return -2**31
        else:
            return numeric_value
    else:
        return 0  # Return 0 if no numeric characters are found

def main():
    input_str = input("Enter a string containing numbers: ")
    result = str_to_inte(input_str)
    print("Converted integer:", result)  

if __name__ == "__main__":
    main()
