"""
    Diet Calories
A person is tracking their calories for each meal of the day. Each meal (breakfast, lunch, and dinner) consists of 3 food items, and the calorie values for each item are already stored in a list.
Write a program that calculates and displays the total calories for each meal.

Expected Output:

Breakfast calories: 550
Lunch calories: 800
Dinner calories: 650
"""
meals = [
    [300, 150, 100],  # Breakfast
    [500, 200, 100],  # Lunch
    [400, 150, 100]   # Dinner
]

meal_names = ["breakfast", "lunch", "dinner"]

for i in range(len(meals)):
    print(f"{meal_names[i]} calories: {sum(meals[i])}")