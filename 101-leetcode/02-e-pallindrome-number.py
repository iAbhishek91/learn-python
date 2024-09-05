# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        elif x < 10:
            return True

        x_copy = x
        reverse = 0
        while x_copy > 0:
            reverse = reverse*10+x_copy % 10
            x_copy //= 10
            print(f"reverse: {reverse}; x_copy: {x}")
        if x == reverse:
            return True
        return False
    
    
        # rev_x = []
        # x_copy = x
        # while x_copy > 0:
        #     rev_x.append(x_copy % 10)
        #     x_copy //= 10
        #     print(f"num_str: {rev_x}; number {x_copy}")

        # x_copy = x
        # for i in range(len(rev_x) // 2):
        #     number = x_copy//(10**((len(rev_x) -1) - i))
        #     x_copy %=(10**((len(rev_x) -1) - i))
        #     print(f"number: {number}, number_mod: rev number: {rev_x[i]}")

        #     if number != rev_x[i]:
        #         return False
        # return True
        

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(1000021))
