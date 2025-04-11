thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)

nums = [3, 1, 2, 10, 1]
def runningSum(nums):
    res = []
    rsum = 0
    for elem in nums:
        rsum += elem
        res.append(rsum)
    return res

result = runningSum(nums)

accounts = [[1,5],[7,3],[3,5]]
def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    res = []
    wealth = 0
    for cus in accounts:
        for bank in cus:
            wealth += bank
        res.append(wealth)
        wealth = 0
    return max(res)

maxWealth = maximumWealth(accounts)
# print(maxWealth)

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    i = 1
    while i <= n:
        if i % 15 == 0:
            res.append("FizzBuzz")
        elif i%3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
        i += 1
    return res
n = 6
fB = fizzBuzz(n)
# print(fB)

def numberOfSteps(num):
    i = 0
    tmp = num
    while i <= num:
        if num ==0:
            return 0
        if tmp % 2 == 0:
            tmp /= 2
        else:
            tmp -= 1
        i += 1
        if tmp == 0:
            return i
        else:
            continue


def numberOfSteps2(num):
    i = 0
    while num != 0:
        i += 1
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
    return i

num = 14
res = numberOfSteps2(num)
print(res)

