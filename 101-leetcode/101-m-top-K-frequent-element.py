# Top K Frequent Elements — your first taste of heaps, and a genuinely high-frequency interview problem. Let's run the usual format: verbal approach first, no code.
# Here's the SRE framing:
# The problem. You're triaging an incident. You've parsed an hour of logs into a list of service IDs — one entry per error, so a service appears once for each error it threw. Given that list and an integer k, return the k services with the most errors. Order among the answer doesn't matter, and you can assume the answer is always unique (no ties to break at the boundary).
# Example:
# errors = ["auth", "billing", "auth", "cart", "auth", "billing"]
# k = 2
# → ["auth", "billing"]     # auth: 3, billing: 2, cart: 1
# Constraints worth noting: the list can be large (say up to 10⁵ entries), and k is guaranteed to be between 1 and the number of distinct services.
# Before any code, talk me through it like it's the real shared-doc round:

# What's your brute-force idea, and its complexity?
# Can you do better — what data structure comes to mind for "top k of something"?
# And the question an interviewer will definitely ask: can you beat O(n log n)?
from collections import Counter

def find_top_k(services: list[str], k) -> list[str]:
    svc_count = {} # O(m), memory complexity
    for svc in services: # O(n) time complexity, n is number of entry 
        if svc in svc_count: # O(1)
            svc_count[svc] += 1
        else:
            svc_count[svc] = 1
    
    sorted_svc_count = sorted(svc_count.items(), key=lambda svc:svc[1], reverse= True) # O(mlogm)- m is unique svc, memory 

    return [svc[0] for svc in sorted_svc_count[:k]] # O(k), number of service required
# total time complexity: O(n) + O(mlogm) + O(k) = O(n + mlogm). K ignored (as its smaller than mlogm and cant grow beyond, its only for addition)
# total memory complexity O(m) + O(m) = O(2m) = O(m)

# iteration one
def find_top_k1(services: list[str], k) -> list[str]:
    svc_count = {} # O(m), memory complexity
    for svc in services: # O(n) time complexity, n is number of entry 
        svc_count[svc] = svc_count.get(svc, 0) # get takes a default value
    
    top = sorted(svc_count.items(), key=lambda svc:svc[1], reverse= True) # O(mlogm)- m is unique svc, memory 

    return [svc for svc, _ in top[:k]] # O(k), number of service required



# iteration two
def find_top_k2(services: list[str], k) -> list[str]:
    svc_count = {} # O(m), memory complexity
    svc_count = Counter(services)
    top = sorted(svc_count.items(), key=lambda svc:svc[1], reverse= True) # O(mlogm)- m is unique svc, memory 
    return [svc for svc, _ in top[:k]] # O(k), number of service required






def practice1(services:list[str], target:int)->list[str]:
    hashmap = {}
    for _,svc in enumerate(services): # O(n)
        hashmap[svc] = hashmap.get(svc,0) + 1
    
    top=sorted(hashmap.items(), key=lambda svc:svc[1] ,reverse=True) # O(mlogm)
    return [svc[0] for svc in top[:target]]
    




# heap implementaion

print(practice1(["cart", "auth", "billing", "auth", "cart", "auth", "billing", "cart"], 2))
