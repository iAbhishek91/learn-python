def twoSumMyVersion(nums: list[int], sum: int) -> list[int]:
     #hashmap = {}
    for i in range(len(nums)):
        search = sum - nums[i]
        if search in nums:
            return([i, nums.index(search)])

# print(twoSum([3,2,4], 6)) # doesnt work for this example


def twoSumWithHashMap(nums: list[int], sum: int) -> list[int]:
    hashMap = {}
    for i, value in enumerate(nums):
        target = sum - value
        if target in hashMap: # O(n)
            return [hashMap[target], i]
        hashMap[value] = i
    return []


def practice1(nums: list[int], sum: int) -> list:
    hashmap = {}
    for i, num in enumerate(nums):
        diff = sum - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return []

def practice2(nums: list[int], sum: int) -> list:
    hashmap = {}
    for i, num in enumerate(nums): # O(n)
        diff = sum - num
        if diff in hashmap: # O(1) because python dict are hash maps
            return [hashmap[diff], i] # O(1)
        hashmap[num] = i # O(1)
    return []


def looksBetterButSolution(nums: list[int], sum: int) -> list[int]:
    # hashMap = {}
    for i, value in enumerate(nums):
        target = sum - value
        if target in nums: # O(n)
            if nums.index(target) != i: # O(n)
                return [i, nums.index(target)]
    return []


# time complixity of "in" and index is O(n) in sequence structure like tuple, list, and str
# but one in dictionary and set, where n is the size of the array.

print(practice2([ 3, 2, 5], 7))
