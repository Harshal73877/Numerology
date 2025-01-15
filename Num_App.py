import streamlit as st

def get_digital_root(n):
    """Calculate the digital root of a number."""
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def process_dob_and_create_numbers(name, dob, gender):
    clean_dob = [char for char in dob if char != "/"]
    zero, one, two, three, four, five, six, seven, eight, nine = [[] for _ in range(10)]
    number_to_list = {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}

    for digit in clean_dob:
        digit_value = int(digit)
        number_to_list[digit_value].append(digit_value)

    numbers = [int(num) for num in clean_dob]

    C = get_digital_root(sum(numbers))

    first_two_digits = [int(clean_dob[0]), int(clean_dob[1])]
    Driver = get_digital_root(sum(first_two_digits))

    YoB = [int(d) for d in clean_dob[-4:]]
    k = get_digital_root(sum(YoB))

    if gender.lower() == "male":
        k = 11 - k
    elif gender.lower() == "female":
        k += 4
    k = get_digital_root(k)

    number_to_list[k].append(k)
    number_to_list[Driver].append(Driver)
    number_to_list[C].append(C)

    numericals = {
        "Four_Nine_Two": [four, nine, two],
        "Three_Five_Seven": [three, five, seven],
        "Eight_One_Six": [eight, one, six]
    }

    for key, value in numericals.items():
        numericals[key] = [item if item else None for item in value]

    return Driver, C, k, numericals

# Streamlit App
st.title("Numerological Analysis")

# Input fields
name = st.text_input("Enter your name:")
dob = st.text_input("Enter your date of birth (dd/mm/yyyy):")
gender = st.radio("Select your gender:", ["Male", "Female"])

if st.button("Analyze"):
    if name and dob and gender:
        try:
            Driver, C, k, numericals = process_dob_and_create_numbers(name, dob, gender)

            st.markdown(f"### Numerological Analysis of {name}")
            st.write(f"Driver: {Driver}, C: {C}, Kuva: {k}")

            st.markdown("### Lo Shu Square")
            rows = [
                numericals["Four_Nine_Two"],
                numericals["Three_Five_Seven"],
                numericals["Eight_One_Six"]
            ]
            st.table(rows)

            Base = {
                "Four_Nine_Two": [4, 9, 2],
                "Three_Five_Seven": [3, 5, 7],
                "Eight_One_Six": [8, 1, 6]
            }

            if numericals["Four_Nine_Two"][0] and numericals["Three_Five_Seven"][1] and numericals["Eight_One_Six"][2]:
                st.success("The Maha Raj Yog Plane is fulfilled.")
            if numericals["Four_Nine_Two"][2] and numericals["Three_Five_Seven"][1] and numericals["Eight_One_Six"][0]:
                st.success("The Raj Yog Plane is fulfilled.")
            if numericals["Four_Nine_Two"][0] and numericals["Four_Nine_Two"][1] and numericals["Four_Nine_Two"][2]:
                st.success("The Mental Plane is fulfilled.")
            if numericals["Three_Five_Seven"][0] and numericals["Three_Five_Seven"][1] and numericals["Three_Five_Seven"][2]:
                st.success("The Emotional Plane is fulfilled.")
            if numericals["Eight_One_Six"][0] and numericals["Eight_One_Six"][1] and numericals["Eight_One_Six"][2]:
                st.success("The Practical Plane is fulfilled.")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please fill out all the fields.")


