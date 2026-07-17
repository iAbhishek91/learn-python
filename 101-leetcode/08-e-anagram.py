def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2): # sorting in python uses time sort has O(nlogn)
        return True
    return False


# zip is an useful function to use in python that returns two iterable
def is_anagram_optimised(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    count = [0] * 26 # [0, 0, 0, 0, ..., 0]   <- 26 of them # O(26) = O(1)
    for s1, s2 in zip(s1, s2): # O(n)
        count[ord(s1)] += 1 # ord return unicode ord(a) == 96
        count[ord(s2)] -= 1
    return all(c == 0 for c in count) # all returns 0 if everything is [0,0,0]

def practice1(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    char = [0] * 26
    for s1c, s2c in zip(s1, s2):
        char[ord(s1c) - ord('a')] += 1
        char[ord(s2c) - ord('a')] -= 1
    return all(c == 0 for c in char)


def practice2(str1:str, str2:str) -> bool:
    if len(str1) != len(str2): # O(1)
        return False
    alphabet = [0] * 26
    for str1_ch, str2_ch in zip(str1,str2): # O(n) where n is length of string1 and string2
        alphabet[ord(str1_ch) - ord('a')] += 1
        alphabet[ord(str2_ch) - ord('a')] -= 1
    return all(alphabetCount == 0 for alphabetCount in alphabet) # for loop has O(26) which is constant, hence is not considered

print(practice1("telar","later"))
