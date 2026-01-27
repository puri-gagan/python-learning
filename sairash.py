## This was to learn debugging in day 15.

# animals = ["cat", "dog", "rabbit", "rabbit"]

# for i in range(len(animals)):
#     j = i + 1
#     if j < len(animals) and (animals[i] == animals[j]):
#         print(True)
#     else:
#         print(False)
# print("I am out of the loop")
# print("This is another line of coe")


##------------------to check prime number--------------------##
"""
user enters a number and checks weather it is prime or not
"""
# num = int(input("Enter a number to check prime number: "))
# is_Prime = True
# if num < 2:
#     is_Prime = False
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             is_Prime = False
#             break
# if is_Prime:
#     print(f"{num} is prime.")
# else:
#     print(f"{num} is not prime.")

### The above code is working fine,

##-----------optimized--------------------##
import math


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
    return True


def main():
    try:
        print("Enter a number to check prime number.")
        num = int(input(">> "))

        if is_prime(num):
            print(f"{num} is prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("enter a valid number.")


if __name__ == "__main__":
    main()
