# A dictionary contains products and list of review scores(0 - 5). 
# Print average score per product. 

products_and_reviews = {
  "Laptop": [4, 5, 3, 2, 1, ], 
  "Mobile": [2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3], 
  "Tablet": [2, 3, 4, 4, 5, 3],
  "Keyboard": [2, 3, 4, 5, 5, 4, 3, 2, 5, 4]
}

for product in products_and_reviews:
  product_review = products_and_reviews[product]
  print(f"Product review for {product}: {product_review}")
  average_review = round(sum(product_review) / len(product_review), 2)
  print(f"Average review score for {product} : {average_review}\n")
    