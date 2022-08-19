# e는

#  
 
# \[e=\sum_{i=0}^{n} {\frac{1}{i!}}\] 

# 이다. 여기서 n은 무한대이다.

# 매우 작은 n에 대해서, e의 근사값을 구해보자.

import math

print("n e")
print("- -----------")
lst = []
for i in range(0, 10):
    lst.append(math.factorial(i))
    
    res = 0
    for j in range(len(lst)):
        res += sum(lst[0:j])
    print(i, 1/res)
