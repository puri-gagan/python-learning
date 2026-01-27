'''
Give discount on each price by 20% and store discounted price in new list discounted_prices and price after discount in new list price_after_discount
'''

prices = [100, 200, 50, 80]
discount_percentage = 20

discounted_prices = []
price_after_discount = []

for price in prices:
    discounted_prices.append((discount_percentage/100) * price)
    price_after_discount.append(price - (discount_percentage/100) * price)

print(discounted_prices)
print(price_after_discount)