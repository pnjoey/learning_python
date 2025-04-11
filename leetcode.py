

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    j = i+1
    res = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                res.append(i)
                res.append(j)
    return res

def twoSum_fast(nums, target): #hash map
    num_dict = {}
    for i, num in enumerate(nums):
        if target-num in num_dict:
            return [num_dict[target-num], i]
        num_dict[num] = i

def twoSum_II(numbers, target):
    l = 0
    r = len(numbers) - 1
    for l in range(len(numbers)):
        sum = numbers[l] + numbers[r]
        while sum > target:
            r -= 1
            sum = numbers[l] + numbers[r]
        if sum == target:
            return [l+1, r+1]

