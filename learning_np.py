import numpy as np

# 14. Create a random vector of size 30 and find the mean value
z14 = np.random.random(size=30)

# 15. Create a 2d array with 1 on the border and 0 inside
z15 = np.ones((5,7))
z15[1:-1,1:-1] = 0

# 16. How to add a border (filled with 0's) around an existing array?
z16 = np.arange(20).reshape(4,5)
z16 = np.pad(z16, 1)

z16[:, [0, -1]] = 0
z16[[0, -1], :] = 0

# 17. What is the result of the following expression?
# print(0 * np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(np.nan in set([np.nan]))
# print(0.3 == 3 * 0.1)

# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
z18 = np.arange(25).reshape(5,5)
#np.fill_diagonal(z18, 0)

# 19. Create a 8x8 matrix and fill it with a checkerboard pattern
z19 = np.zeros((8,8))
# np.fill_diagonal(z19[1:, :-1], 1)
# np.fill_diagonal(z19[3:, :-3], 1)
# np.fill_diagonal(z19[5:, :-5], 1)
# np.fill_diagonal(z19[7:, :-7], 1)
# np.fill_diagonal(z19[:7,-7:], 1)
# np.fill_diagonal(z19[:5,3:], 1)
# np.fill_diagonal(z19[:3,5:], 1)
# np.fill_diagonal(z19[:1,7:], 1)

# solution
#The basic slice syntax is i:j:k where i is the starting index, j is the stopping index, and k is the step (k!= 0)
z19[1::2,::2] = 1
z19[::2,1::2] = 1


# 20. consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
# z20 = np.arange(336).reshape(6,7,8)
# print(np.unravel_index(99, (6,7,8)))


#### 22. Normalize a 5x5 random matrix
z22 = np.random.randint(1,30,(5,5))
# print(z22)
z22 = z22 - np.linalg.norm(z22)
# print(z22)
z22 = (z22 - np.mean(z22))/(np.std(z22))
# print(z22)



