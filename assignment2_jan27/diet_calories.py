# Diet calories, traking calories for each meal of the day, each mean(breakfast, lunch, dinner) consists of 3 food items. 
# Calories values for each item are already stored in a list. 
# Calculate and display total calories for each meal.

# meal_info = {
#     "breakfast": [30, 40, 100], 
#     "lunch": [200, 240, 140],
#     "dinner": [210, 230, 80]
# }

meal_info = [
    [30, 40, 100],
    [200, 240, 140],
    [210, 230, 80]
]

total_calories = 0

meal_names = ["breakfast", "lunch", "dinner"]

for meal_id in range(len(meal_info)): 
  # print(meal_id) 
  print(f"{meal_names[meal_id]}: {meal_info[meal_id]}")
  total_calories += sum(meal_info[meal_id])
  print(f"Total calories for {meal_names[meal_id]} : {sum(meal_info[meal_id])}")
  

print(f"Total calories for the day: {total_calories}")
