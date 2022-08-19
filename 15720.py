# 윤진이는 이번에 카우버거 알바생으로 뽑히게 되었다. 그녀는 카우버거를 평소에 이용하면서 들었던 의문점 한가지가 있었다.

# "카우버거에는 왜 세트 메뉴에 대한 할인이 존재하지 않는가?"

# 따라서 윤진이의 아이디어로 카우버거에 세트 할인을 도입하고자 한다. 세트 메뉴는 버거 1개, 사이드 메뉴 1개, 음료 1개를 선택 할 경우 각각의 제품에 대해서 10%의 세트 할인을 적용하는 방식으로 진행된다.

# 하지만 카우버거 점주는 POS기의 소프트웨어가 오래되어 세트 할인에 대한 내용을 추가할 수가 없었다. 따라서 소프트웨어학부에 재학 중인 윤진이는 전공을 살려 직접 프로그램을 만들어보려고 한다. 윤진이를 도와 POS기에 들어갈 세트 할인에 대한 프로그램을 작성해보자.

B, C, D = map(int, input().split())
burger_price = list(map(int, input().split()))
sidemenu_price = list(map(int, input().split()))
beverage_price = list(map(int, input().split()))

min_num = min(len(burger_price), len(sidemenu_price), len(beverage_price))
before_set_price = sum(burger_price) + sum(sidemenu_price) + sum(beverage_price)

after_set_price = 0
for i in range(min_num):
    max_burger = max(burger_price)
    max_sidemenu = max(sidemenu_price)
    max_beverage = max(beverage_price)
    discount_price = int((max_burger + max_sidemenu + max_beverage) * 0.9)
    after_set_price += discount_price
    burger_price.remove(max_burger)
    sidemenu_price.remove(max_sidemenu)
    beverage_price.remove(max_beverage)
after_set_price += sum(burger_price) + sum(sidemenu_price) + sum(beverage_price)

print(before_set_price)
print(after_set_price)