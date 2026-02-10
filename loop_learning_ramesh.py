food_price = {
    "chicken_mom": 100,
    "buff momo": 90,
    "chicken chowmmen": 100,
    "biryani": 100
}

for idx, food_item in enumerate(food_price.keys()):
    if idx < 2:
        food_price[food_item] = food_price[food_item] + food_price[food_item] * 0.02

print(food_price)
print("this code works fine in my system")
