# The first line contains a single integer n indicating the number of data sets.

# The following n lines each represent a data set. Each data set will be formatted according to the following description:

# A single data set consists of a line "X Y", where X is the number of brains the zombie eats and Y is the number of brains the zombie requires to stay alive.

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    if a >= b:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")