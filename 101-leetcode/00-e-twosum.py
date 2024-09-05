class TwoSum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}
        for i in range(len(nums)):
            search = target - nums[i]
            print(f"nums: {nums[i]}, target: {target - nums[i]}")
            if search in hashMap:
                return [hashMap[search], i]
            else:
                hashMap[nums[i]] = i



if __name__ == "__main__":
    t = TwoSum()
    print(f"result: {t.twoSum([2, 7, 11, 15], 9)}")
