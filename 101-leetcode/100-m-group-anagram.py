# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# Assume up to ~10⁴ strings, each up to ~100 lowercase English letters.

# dont use str(sorted(word)), instead "".join(sorted(word)), or tuples
# "".join(sorted(word)) is not same as tuple(sorted(word))
# but they are hashable, and hence can be used as keys
def group_anagram(words: list[str]) -> list[list[str]]:
    hashmap = {}
    for word in words: # O(n), number of words
        sort = str(sorted(word)) # O(mlog(m)), I dont know how but I know from memory
        if sort in hashmap: # O(1), constant in dictionary
            hashmap[sort].append(word) # O(1)
        else:
            hashmap[sort] = [word]
    return list(hashmap.values()) # O(n) , creates a new list

def practice1(words: list[str]) -> list:
    hashmap = {}
    for word in words: # O(n), n is number of words in the list
        sortedWord = tuple(sorted(word)) # O(mlogm) m is the length of the words
        if sortedWord in hashmap: # O(1) as dict in python is hashmap
            hashmap[sortedWord].append(word) # O(1) append at the last of the hashmap
        else:
            hashmap[sortedWord] = [word]
    return list(hashmap.values()) # O(k), K is the number of unique anagram we get

# to add big O

# O(n) + O(mlogm) + outside the loop = O(n) = constant
# O(n.mlogm) is the answer

print(practice1(["eat", "tea", "tan", "ate", "nat", "bat"]))
