from ast import List


# Q1

def threesum(nums):


      """  res = []
        nums.sort()
        for i in range ((len(nums)-2)):
            for j in range(i + 1, len(nums) - 1):
              for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
  
        return res
    """

def three_sum(nums):
    res = []
    nums.sort()
    length = len(nums)
    
    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # eliminating duplicate ones for i
        l = i + 1
        r = length - 1  # last element of the array given
        
        while l < r:
            total = nums[i] + nums[l] + nums[r]  # finding the total sum
            
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))  # appending
                while l < r and nums[l] == nums[l + 1]:  # eliminating duplicate ones for l
                    l += 1
                while l < r and nums[r] == nums[r - 1]:  # eliminating duplicate ones for r
                    r -= 1
                l += 1
                r -= 1
    
    return res

def main():
    nums = [-1, 0, 1,8,9,3,-8,0, 2, -1, -4]
    result = three_sum(nums)
    print("Triplets with sum 0:", result)

if __name__ == "__main__":
    main()

    
        



