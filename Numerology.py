import pandas as pd
import numpy as np


def get_digital_root(n):
    """Calculate the digital root of a number."""
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def process_dob_and_create_numbers(name, dob, Gender):
    # Clean the date of birth
    clean_dob = [char for char in dob if char != "/"]

    # Initialize digit lists
    zero, one, two, three, four, five, six, seven, eight, nine = [[] for _ in range(10)]

    # Create mapping for easy access
    number_to_list = {
        0: zero, 1: one, 2: two, 3: three, 4: four,
        5: five, 6: six, 7: seven, 8: eight, 9: nine
    }

    # Assign digits to lists based on their value (not position)
    for digit in clean_dob:
        digit_value = int(digit)
        number_to_list[digit_value].append(digit_value)

    # Calculate C (digital root)
    numbers = [int(num) for num in clean_dob]
    C = get_digital_root(sum(numbers))

    # Calculate Driver
    first_two_digits = [int(clean_dob[0]), int(clean_dob[1])]
    Driver = get_digital_root(sum(first_two_digits))

    # Calculate Kuva (k)
    YoB = [int(d) for d in clean_dob[-4:]]
    k = get_digital_root(sum(YoB))

    # Adjust k based on gender
    if Gender.lower() == "male":
        k = 11 - k
    elif Gender.lower() == "female":
        k += 4

    # Ensure k is within the valid range of 0-9
    k = get_digital_root(k)

    # Append calculated values
    number_to_list[k].append(k)
    number_to_list[Driver].append(Driver)
    number_to_list[C].append(C)

    # Create numericals dictionary
    numericals = {
        "Four_Nine_Two": [four, nine, two],
        "Three_Five_Seven": [three, five, seven],
        "Eight_One_Six": [eight, one, six]
    }
    # Replace empty elements with None
    for key, value in numericals.items():
        numericals[key] = [item if item else None for item in value]
    
    # Print results
    print(f"Numerological Analysis of", name)
    print()
    print(f"Reference Lo Shu Square")
    Base = {
        "Four_Nine_Two": [4, 9, 2],
        "Three_Five_Seven": [3, 5, 7],
        "Eight_One_Six": [8, 1, 6]
    }
    print(Base["Four_Nine_Two"])
    print(Base["Three_Five_Seven"])
    print(Base["Eight_One_Six"])
    print()
    rows = [
    numericals["Four_Nine_Two"],
    numericals["Three_Five_Seven"],
    numericals["Eight_One_Six"]
    ]
    from tabulate import tabulate
    # Use tabulate to print
    print(f"Lo Shu Square :", name)
    print(tabulate(rows, tablefmt="grid"))

    print()
    print(f"Driver: {Driver}")
    print(f"C: {C}")
    print(f"Kuva: {k}")
    print()
    if numericals.items() and numericals["Four_Nine_Two"][0] and numericals["Three_Five_Seven"][1] and numericals["Eight_One_Six"][2]:
        print("The Maha Raj Yog Plane is fulfulled ")
        mry = [[[Base["Four_Nine_Two"][0], Base["Three_Five_Seven"][1], Base["Eight_One_Six"][2]]]]
        print(tabulate(mry, tablefmt="grid"))
        print()
    if numericals.items() and numericals["Four_Nine_Two"][2] and numericals["Three_Five_Seven"][1] and numericals["Eight_One_Six"][0]:
        print("The Raj Yog Plane is fulfulled ")
        ry = [[[Base["Four_Nine_Two"][2], Base["Three_Five_Seven"][1], Base["Eight_One_Six"][0]]]]
        print(tabulate(ry, tablefmt="grid"))
        print()
    if numericals.get("Four_Nine_Two") and numericals["Four_Nine_Two"][0] and numericals["Four_Nine_Two"][1] and numericals["Four_Nine_Two"][2]:
        print("The Mental Plane is fulfulled")
        mp = [[[Base["Four_Nine_Two"][0], Base["Four_Nine_Two"][1], Base["Four_Nine_Two"][2]]]]
        print(tabulate(mp, tablefmt = "grid"))
        print()
    if numericals.get("Three_Five_Seven") and numericals["Three_Five_Seven"][0] and numericals["Three_Five_Seven"][1] and numericals["Three_Five_Seven"][2]:
        print("The Emotional Plane is fulfulled ")
        ep = [[[Base["Three_Five_Seven"][0], Base["Three_Five_Seven"][1], Base["Three_Five_Seven"][2]]]]
        print(tabulate(ep, tablefmt = "grid"))
        print()
    if numericals.get("Eight_One_Six") and numericals["Eight_One_Six"][0] and numericals["Eight_One_Six"][1] and numericals["Eight_One_Six"][2]:
        print("The Practical Plane is fulfulled ")
        pp = [[[Base["Eight_One_Six"][0], Base["Eight_One_Six"][1], Base["Eight_One_Six"][2]]]]
        print(tabulate(pp, tablefmt = "grid"))
        print()
    if numericals.items() and numericals["Four_Nine_Two"][0] and numericals["Three_Five_Seven"][0] and numericals["Eight_One_Six"][0]:
        print("The Thought Plane is fulfulled ")
        pp = [[[Base["Four_Nine_Two"][0], Base["Three_Five_Seven"][0], Base["Eight_One_Six"][0]]]]
        print(tabulate(pp, tablefmt = "grid"))
        print()
    if numericals.items() and numericals["Four_Nine_Two"][1] and numericals["Three_Five_Seven"][1] and numericals["Eight_One_Six"][1]:
        print("The Will Pane (Success) is fulfulled ")
        wp = [[[Base["Four_Nine_Two"][1], Base["Three_Five_Seven"][1], Base["Eight_One_Six"][1]]]]
        print(tabulate(wp, tablefmt = "grid"))
        print()
    if numericals.items() and numericals["Four_Nine_Two"][2] and numericals["Three_Five_Seven"][2] and numericals["Eight_One_Six"][2]:
        print("The Action Plane is fulfulled ")
        pp = [[[Base["Four_Nine_Two"][2], Base["Three_Five_Seven"][2], Base["Eight_One_Six"][2]]]]
        print(tabulate(pp, tablefmt = "grid"))


name = "Harshal Lokhande"
dob = "27/04/1991"
gender = "male"
process_dob_and_create_numbers(name, dob, gender)