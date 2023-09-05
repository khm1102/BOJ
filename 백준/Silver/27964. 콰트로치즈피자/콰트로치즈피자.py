n = int(input())
toppings = input().split()

count = 0
cheese_set = set()
for topping in toppings:
    if topping.endswith("Cheese"):
        cheese_set.add(topping)
if len(cheese_set) >= 4:
    count = sum([topping.endswith("Cheese") for topping in toppings])
if count >= 4:
    print("yummy")
else:
    print("sad")
