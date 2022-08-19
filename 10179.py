# 당신은 어떤 물건이라도 20% 할인해주는 쿠폰을 가지고 있다.

# 원래 가격이 주어질 때, 쿠폰을 사용하면 얼마가 되는지 알려주는 프로그램을 작성하시오.

T = int(input())

for i in range(T):
    price = float(input())

    print("$%0.2f" % round((price * 0.8), 2))