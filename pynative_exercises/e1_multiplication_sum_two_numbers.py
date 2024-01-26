num_1 = int(input("First Number: "))
num_2 = int(input("Second NUmber: "))

def product_sum():
    num_3 = (num_1 + num_2)
    num_4 = (num_1 * num_2)
    if num_4 <= 1000:
        print("\nThe result is " + str(num_4))
    else:
        print("\nThe result is " + str(num_3))

product_sum()

