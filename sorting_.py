

"""Given the participants' score sheet for your University Sports Day,
 you are required to find the runner-up score.
   You are given  scores. Store them in a list and find the score of the runner-up."""

if __name__ == '__main__':
    n = input("Enter a list of numbers separated by spaces: ")
    arr = n.split()
    arr = [int(num) for num in arr]  # Convert the strings to integers
    arr.sort(reverse=True)  # Sort in descending order
    
    if len(arr) >= 2:
        print("Second highest:", arr[1])
    else:
        print(arr[0])
