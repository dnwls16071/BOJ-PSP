# 피보나치 수는 다음과 같은 규칙으로 만들어지는 수열입니다.

#   
#  $\begin{align*}F_{1} &= 1 \\ F_{2} &= 1 \\ F_{n+2} &= F_{n+1} + F_{n}\end{align*}$ 

# 처음 몇 개의 항은 다음과 같습니다.

# 1, 1, 2, 3, 5, 8, 13 ...

# 다음과 같은 합을 구해봅시다.

#  
# $\sum_{i=1}^{n}\sum_{j=1}^{n} \gcd(F_{i}, F_{j})$ 

# 이때 gcd는 최대공약수를 의미합니다. 답이 매우 클 수 있으므로 1,000,000,007로 나눈 나머지를 출력합시다.

fibonacci = [1, 1, 2, 3]
n = int(input())

for i in range(2, 100):
    fibonacci.append(fibonacci[i] + fibonacci[i+1])
