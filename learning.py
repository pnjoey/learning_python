thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

