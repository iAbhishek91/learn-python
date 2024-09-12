# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

class Solution(object):
    def bruteForce(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # O(n) - linear
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target > nums[i]:
                continue
            else:
                return i
        return len(nums)
    
    def searchInsert(self, nums, target):
        # O(log n) - linear
        # implement binary search tree
        l = 0
        r = len(nums) - 1
        m = 0
        print(f"l: {l}, m: {m}, r: {r}")
        while l <= r:
            m = (l + r)//2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
            print(f"l: {l}, m: {m}, r: {r}")

        return l
        

if __name__ == "__main__":
    s  = Solution()
    # print(s.searchInsert([1,2,4,6], 7))
    print(s.searchInsert([1,3,5,7], 6))
