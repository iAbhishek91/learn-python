# # 125
# !-- A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


class Solution(object):
    def isPalindrome(self, s:str):
        """
        :type s: str
        :rtype: bool
        """
        print(f"{ord('0')}, {ord('9')}")
        # return if string is empty
        s = s.strip()
        if s == "":
            return True
        
        s = s.lower()
        temp = [] # sol-1: beats 95% list is better
        # temp = "" # sol-2: beats 8%
        for c in s:
            #  97 a, to z and 48 to 57
            if  97 <= ord(c) <= 97+25 or 48 <= ord(c) <= 48+9:
                temp.append(c) # sol-1
                # temp += c # sol-2
        
        print(f"temp: {temp} and temp: {temp[::-1]}")
        return temp == temp[::-1]

    
    def isPalindrome1(self, s):
        s = s.lower()
        s = [x for x in s if x.isalnum()]
        return s == s[::-1]
        

if __name__ == "__main__":
    print(Solution().isPalindrome1("mad a M  "))
