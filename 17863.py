# In the United States of America, telephone numbers within an area code consist of 7 digits: the prefix number is the first 3 digits and the line number is the last 4 digits. Traditionally, the 555 prefix number has been used to provide directory information and assistance as in the following examples:

# 555-1212
# 555-9876
# 555-5000
# 555-7777
# Telephone company switching hardware would detect the 555 prefix and route the call to a directory information operator. Now-a-days, telephone switching is done digitally and somewhere along the line a computer decides where to route calls.

# For this problem, write a program that determines if a supplied 7-digit telephone number should be routed to the directory information operator, that is, the prefix number is 555.

word = input()

if word[0:3] == "555":
    print("YES")
else:
    print("NO")