# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
 

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

class Solution(object):
    def to_another_array(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        l1 = l2 = 0
        while (l1 < m or l2 < n):
            print(f"l1: {l1}, l2: {l2}")
            # print(f"nums1[l1]: {nums1[l1]}, nums2[i]: {nums2[l2]}")
            if l2 == n:
                temp.extend(nums1[l1:m])
                l1 = m
            elif l1 == m:
                temp.extend(nums2[l2:n])
                l2 = n
            elif nums1[l1] > nums2[l2]:
                temp.append(nums2[l2])
                # l1 += 1
                l2 += 1
            elif nums1[l1] <= nums2[l2]:
                temp.append(nums1[l1])
                l1 += 1
                # nums1.insert(l1, nums2[i])
            print(temp)
            print("-"*20)
        nums1 = temp
        print(nums1 is temp)
        print(nums1)
    
    def in_place(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l1 = -1 if m == 0 else 0
        l2 = -1 if n == 0 else 0
        zero_mark = m
        while ((l1 < m and l1 >= 0) or (l2 < n and l2 >= 0)):
            # no comparision scenario
            if (l2 < 0) or (l2 >= n):
                break
            elif (l1 < 0 and l2 < n) or (l1 > zero_mark):
                print("one")
                l1 += 1
                nums1.insert(l1, nums2[l2])
                nums1.pop()
                l2 += 1
                zero_mark += 1
            # elif l1 >= zero_mark:
                
            elif (zero_mark > l1) and (nums1[l1] > nums2[l2]):
                print("two")
                nums1.insert(l1, nums2[l2])
                nums1.pop()
                l2 += 1
                # l1 =+ 1
                zero_mark += 1
            elif (zero_mark > l1) and (nums1[l1] <= nums2[l2]):
                print("three")
                l1 += 1
                print(f"l1: {l1}, l2: {l2}, zero_mark: {zero_mark}")
                if nums1[l1] < nums2[l2] and l1 < zero_mark:
                    continue
                nums1.insert(l1, nums2[l2])
                nums1.pop()
                l2 += 1
                zero_mark += 1
            print(f"l1: {l1}, l2: {l2}, zero_mark: {zero_mark}")
            print(nums1)
        
    def in_place2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l1 = l2 = 0
        zero_mark = m
        while (n > l2):
            # no comparision scenario
            if n == 0:
                break
            elif m ==0 and n > 0 and l2 < n:
                nums1[l1] = nums2[l2]
                l1 += 1
                l2 += 1
            elif nums1[l1] < nums2[l2]:
                l1 += 1
                if nums1[l1] >= nums2[l2] or l1 >= zero_mark:
                    nums1.insert(l1, nums2[l2])
                    nums1.pop()
                    zero_mark += 1
                    l2 += 1
            elif nums1[l1] >= nums2[l2]:
                nums1.insert(l1, nums2[l2])
                nums1.pop()
                zero_mark += 1
                l1 += 1
                l2 += 1
            print(f"l1: {l1}, l2: {l2}, zero_mark: {zero_mark}")
            print(nums1)

        print(nums1)

        print("-"*30)

if __name__ == "__main__":
    # Solution().in_place2(nums1 = [4,0,0,0,0,0], m = 1, nums2 = [1,2,3,5,6], n = 5)
    # Solution().in_place2(nums1 = [1,2,2,0,0,0], m = 3, nums2 = [1,2,3], n = 3)
    Solution().in_place2(nums1 = [1,0,0,0,0,0], m = 1, nums2 = [0,2,6,8,10], n = 5)
    # Solution().to_another_array(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
    # Solution().to_another_array(nums1 = [0], m = 0, nums2 = [1], n = 1)
    # Solution().to_another_array(nums1 = [1], m = 1, nums2 = [], n = 0)
    # Solution().in_place(nums1 = [], m = 0, nums2 = [], n = 0)
    # Solution().in_place(nums1 = [0], m = 0, nums2 = [1], n = 1)
    # Solution().in_place(nums1 = [0,0], m = 0, nums2 = [1,2,3], n = 2)
    # Solution().in_place(nums1 = [0,0,0], m = 1, nums2 = [1,2,3], n = 2)
    # Solution().in_place(nums1 = [1,2,2,0,0,0], m = 3, nums2 = [1,2,2], n = 3)
    # Solution().in_place(nums1 = [1], m = 1, nums2 = [], n = 0)
    # Solution().in_place(nums1 = [2,0], m = 1, nums2 = [1], n = 1)
