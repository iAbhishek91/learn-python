# What a heap actually is
# A heap is a binary tree with two rules:

# Shape rule: it's complete — every level is full except possibly the last, which fills left to right. No gaps.
# Order rule (min-heap): every parent ≤ its children. That's it. Siblings have no relationship to each other.

# there are two type of heap : min heap and max heap.
# priority queue is also exactly the same thing.

# DS wise its a list:
# (2*i+1) - left node
# (2*i+2) - right node

# Python doesnt have a heap class inbuilt. so use heapq (min heap ONLY)
# Build in place heapq.heapify(lst)O(n)Cheaper than n pushes — common interview probe
# Push           heapq.heappush(heap, item)O(log n)Bubble up
# Pop smallest   heapq.heappop(heap) O(log n)Bubble down
# Peek smallest. heap[0]  O(1)Look, don't remove
# Push-then-pop. heapq.heappushpop(heap, item) O(log n) Faster than separate calls
# Pop-then-push. heapq.heapreplace(heap, item) O(log n) Always pops first
# Top/bottom k   heapq.nlargest(k, it, key=...) / nsmallestO(n log k)Convenience helpers
# data structure wise, heap is just a list.

# time complexity of each heap action
# create a heap is O(n), n is the number of element of in the list
# push an element to the heap is O(logn)
# pop an elemement from the pop is O(logn)
# look at heap O(1) as you dont traverse just look at min or max value which is at root.

# The most commonly reported heap question in Google SRE loops, at every level from L4 to staff, is some skin of this: "Here's a massive access log. Find the top K IP addresses / endpoints / error codes by request count." Sometimes it's framed as a file too big for memory, sometimes as a live stream, sometimes as "our dashboard needs the 10 noisiest services." The second most common: "Merge K sorted log files into one timeline" — which is Merge K Sorted Lists, already sitting in your progression at problem #5.
# Look at the first one again. Counter over the log lines, size-k min-heap, bouncer eviction, return the survivors. That is character for character the problem you've been circling for five turns. The cold rep I keep asking for isn't prep for the Google question — it is the Google question, with nums swapped for IPs. You asked me for a real-world problem; you already have it, with your own services as test data and a known expected output.
# So here's the deal, and I'm holding it with the same directness you'd want from a good interviewer: this is the fifth consecutive turn where a new question has arrived in place of the rep. Each question has been genuinely good — and each one has kept me producing while you evaluate. That ratio is inverted from the interview, where you produce for 45 minutes while someone else evaluates. I'm not opening another thread, drawing another diagram, or writing another line of code until yours lands.
# The staff-level framing, since you asked about level: at staff, they're not checking whether you know heaps — this conversation proves you do, your questions today were better than most candidates'. They're checking whether you can produce working code under observation with no safety net. Knowledge is your strength; production under pressure is the untested muscle. Every turn spent here strengthens the strong one.

# First example: heapify a list
import heapq

first_nums = [0,1,2,3,4,5,4,3,2,1,0]
nums_copy = first_nums
heapq.heapify(nums_copy) # O(n)
print("heapify: " + str(nums_copy)) # [0, 0, 2, 2, 1, 5, 4, 3, 3, 1, 4]
print("heapify: " + str(first_nums)) # [0, 0, 2, 2, 1, 5, 4, 3, 3, 1, 4]
#                 0
#           0            2
#      2         1  5          4
#    3   3     1   4

# Second example: push instead of heapify
second_nums = [0,1,2,3,4,5,4,3,2,1,0]
nums_copy = []
for n in second_nums: # O(n)
    heapq.heappush(nums_copy, n) # O(logn)
print("heapPush: " + str(nums_copy)) # [0, 0, 2, 2, 1, 5, 4, 3, 3, 4, 1]

# third example: heap sort
third_nums = [0,1,2,3,4,5,4,3,2,1,0]
sorted_third_nums = []
heapq.heapify(third_nums)
for _ in third_nums: # mutating a list
    sorted_third_nums.append(heapq.heappop(third_nums)) # mutating the list, and iterating
print("sorted: " + str(sorted_third_nums)) # wrong:[0, 0, 1, 1, 2, 2]

# fourth example: heap sort
fourth_nums = [0,1,2,3,4,5,4,3,2,1,0]
sorted_fourth_nums = []
heapq.heapify(third_nums)
while fourth_nums: # mutating a list
    sorted_fourth_nums.append(heapq.heappop(fourth_nums)) # mutating the list, and iterating
print(f"sorted: {sorted_fourth_nums}") # [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]

## SCENARIO BASED
# Kth Largest Element in an Array (Medium) — same size-k min-heap, but return the bouncer itself (heap[0]) instead of the whole heap.
# Kth Largest Element in a Stream (Easy) — same heap, but wrapped in a class with an add() method; the heap persists between calls. Very SRE: streaming percentile-ish tracking.
# K Closest Points to Origin (Medium) — priority is a computed value (distance), so you push (-distance, point) — the max-heap negation trick appears.
# Sort Characters by Frequency (Medium) — counting + heap again, but you rebuild an output string from the popped order.
# Merge K Sorted Lists (Hard) — heap holds one head per list; pop the global minimum, push its successor.
# Find K Pairs with Smallest Sums (Medium) — lazy expansion: only push a pair's neighbors when it's popped, so the heap stays small.

# fifth problem - return n largest element in an array
fifth_nums = [3,2,4,2,6,3,7,4,8,6,1,0,9,9]
target = 4
heapq.heapify(fifth_nums)
max_n = []
print(heapq.nlargest(target,fifth_nums))

# ["cart","auth","billing","auth","cart","auth","billing","cart"], k=2 → ["auth", "cart"]. Blank page. Go.
sixth_strs = ["cart","auth","billing","auth","cart","auth","billing","cart"]
k = 2
hashmap = {} # memory, O(m), unique number of service
for s in sixth_strs: # time, O(n), number of item in the list
    hashmap[s] = hashmap.get(s,0) + 1

min_heap = []
for svc, count in hashmap.items(): # time, O(k), given by k
    heapq.heappush(min_heap,(count, svc))
    if len(min_heap) > k:
        heapq.heappop(min_heap)

# total time = O(n) + O(m) + O(k) * O(log k) = O(n+m+klogk) = since n>m, we consider O(n+klogk)
# total mem. = O(m) + O(k) = O(m+k) = O(m) is considered
print([svc for count, svc in min_heap ])

# sixth problem - Kth largest element in a stream(easy)
class KthLargestItemInStream:
    def __init__(self,k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, value: int) -> int:
        heapq.heappushpop(self.min_heap, value)
        return self.min_heap[0]

stream = KthLargestItemInStream(3, [4, 5, 8, 2])
print(stream.add(3))
print(stream.add(5))
print(stream.add(10))
print(stream.add(9))
print(stream.add(4))
