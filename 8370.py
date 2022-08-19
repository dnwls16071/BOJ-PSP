# Byteland Airlines recently extended their aircraft fleet with a new model of a plane. The new acquisition has n1 rows of seats in the business class and n2 rows in the economic class. In the business class each row contains k1 seats, while each row in the economic class has k2 seats.

# Write a program which:

# reads information about available seats in the plane,
# calculates the sum of all seats available in that plane,
# writes the result.

A, B, C, D = map(int, input().split())

temp1 = A * B
temp2 = C * D

print(temp1 + temp2)