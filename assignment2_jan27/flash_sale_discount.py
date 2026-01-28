# Give discount on each price by 20% and store discounted price in a new list discounted_prices and prices after discount in new list price_after_discount

prices = [200, 300, 400, 500, 600]
discounted_prices = []
prices_after_discount = []

discount_rate = 0.20

for price in prices: 
  print(f"Original Price: {price}")
  discounted_price = (price * discount_rate)
  print(f"Discounted Price: {discounted_price}")
  discounted_prices.append(discounted_price)

  price_after_discount = price - discounted_price
  print(f"Price after discount: {price_after_discount}\n")
  prices_after_discount.append(price_after_discount)

print(f"Discounted Prices: {discounted_prices}")
print(f"Prices after Discount: {prices_after_discount}") 