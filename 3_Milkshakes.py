from collections import deque

chocolate_packages = list(map(int, input().split(', ')))
milk_cups = deque(list(map(int, input().split(', '))))
milkshakes = 0

while chocolate_packages and milk_cups and milkshakes < 5:
    chocolate = chocolate_packages.pop()
    milk = milk_cups.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    if chocolate <= 0:
        milk_cups.appendleft(milk)
        continue
    if milk <= 0:
        chocolate_packages.append(chocolate)
        continue
    if chocolate == milk:
        milkshakes += 1
    else:
        milk_cups.append(milk)
        chocolate_packages.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate_packages:
    print(f'Chocolate:{", ".join([str(x) for x in chocolate_packages])}')
else:
    print(f'Chocolate: empty')
if milk_cups:
    print(f'Milk:{", ".join([str(x) for x in milk_cups])}')
else:
    print(f'Milk: empty')
