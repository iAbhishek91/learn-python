# Formally: given a list of integers nums, return True if any value appears at least twice, and False if every element is distinct.
# Examples:

# [1, 2, 3, 1] → True (1 appears twice)
# [1, 2, 3, 4] → False (all distinct)



def duplicate(nums: list[int]) -> bool:
    seen = set()
    for val in nums: # O(n) loops through list of elements
        if val in seen: # O(1) in on a set is constant
            return True # O(1)
        seen.add(val) # O(1)
    return False # O(1)

def practise1(nums: list[int]) -> bool:
    result = set()
    for _, num in enumerate(nums):
        if num in result:
            return True
        result.add(num)
    return False
    
print(practise1([1,2,3,4,5, 5]))
