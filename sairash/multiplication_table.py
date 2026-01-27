'''
Multiplication Table
Print the multiplication table for 1 to 3.

Hint: Use nested for loop. in first outer loop, use range(1,4) to get 1, 2, 3 as a iterables for the loop and use range(1, 11) for second child loop to get 1 to 10
'''

for i in range(1,4):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print("\n___________________\n")