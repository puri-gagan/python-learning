"""
Product review
A dictionary contains products and a list of review scores (0 to 5). Print average score per product.

Hint: It is required that you should be using nested for loop to calculate total sum of reviews of each product, take length of total reviews and calculate the average
"""
reviews = {
    "Phone": [4, 5, 3, 4],
    "Laptop": [5, 4, 4],
    "Headphones": [3, 4, 2]
}

for product, ratings in reviews.items():
    sum = 0
    for each_rating in ratings:
        sum = sum + each_rating
    print(f"The average rating of {product} is {sum/len(ratings)}")
    