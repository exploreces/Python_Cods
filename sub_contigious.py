#Q3

# counting distinct arrays
"""def subarray_sum(nums, k):
   count = 0
   start = 0
    total = 0
    
    for end in range(len(nums)):
        total += nums[end]
        
        while total > k:
            total -= nums[start]
            start += 1
        
        if total == k:
            count += 1
    
    return count

def main():
    nums = [3,4,7,2,-3,1,4,2]
    k = 7
    result = subarray_sum(nums, k)
    print("Total number of contiguous subarrays with sum", k, "is:", result)

if __name__ == "__main__":
    main()
"""

# counting all subarrays

def subarray_sum(nums:list[int], k:int)->int:
    count = 0
    for start in range(len(nums)):
        total = 0
        for end in range(start, len(nums)):
            total += nums[end]
            if total == k:
                count += 1
    return count

def main():
    nums = [3, 4, 7, 2, -3, 1, 4, 2]
    k = 7
    result = subarray_sum(nums, k)
    print("Total number of contiguous subarrays with sum", k, "is:", result)

if __name__ == "__main__":
    main()
