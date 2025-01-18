import streamlit as st
from datetime import datetime
import pandas as pd

def validate_date(date_str):
    """Validate date in DD/MM/YYYY format."""
    try:
        # Check format
        if len(date_str.split('/')) != 3:
            return False
        
        day, month, year = map(int, date_str.split('/'))
        
        # Basic range checks
        if not (1 <= day <= 31):
            return False
        if not (1 <= month <= 12):
            return False
        if not (1900 <= year <= datetime.now().year):
            return False
            
        # Validate actual date
        datetime(year, month, day)
        return True
    except:
        return False
def small_title(text, size=18):
    st.markdown(f"<h1 style='font-size: {size}px;'>{text}</h1>", unsafe_allow_html=True)

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

    # Replace empty lists with "NA" instead of None
    for key, value in numericals.items():
        numericals[key] = ["NA" if not item else item for item in value]

    return Driver, C, k, numericals

# Streamlit App
st.title("Numerological Analysis")

# Input fields with date format hint
name = st.text_input("Enter your name:")
dob = st.text_input("Enter your date of birth (DD/MM/YYYY):", help="Format: DD/MM/YYYY (e.g., 15/08/1985)")
gender = st.radio("Select your gender:", ["Male", "Female"])

if st.button("Analyze"):
    if name and dob and gender:
        # Validate date format first
        if not validate_date(dob):
            st.error("Invalid date format. Please use DD/MM/YYYY format and ensure the date is valid.")
        else:
            try:
                Driver, C, k, numericals = process_dob_and_create_numbers(name, dob, gender)

                st.markdown(f"### Numerological Analysis of {name}")
                st.write(f"Driver: {Driver}, Conductor: {C}, Kua: {k}")

                st.markdown("### Lo Shu Square")
                
                # Create a more readable table format
                rows = [
                    [str(x).replace("[]", "NA") for x in numericals["Four_Nine_Two"]],
                    [str(x).replace("[]", "NA") for x in numericals["Three_Five_Seven"]],
                    [str(x).replace("[]", "NA") for x in numericals["Eight_One_Six"]]
                ]
                
                # Custom formatting for the table
                df = pd.DataFrame(
                    rows,
                    columns=["Column 1", "Column 2", "Column 3"],
                    index=["Row 1", "Row 2", "Row 3"]
                )
                st.table(df)

                Base = {
                    "Four_Nine_Two": [4, 9, 2],
                    "Three_Five_Seven": [3, 5, 7],
                    "Eight_One_Six": [8, 1, 6]
                }

                # Check for planes
                if numericals["Four_Nine_Two"][0] != "NA" and numericals["Three_Five_Seven"][1] != "NA" and numericals["Eight_One_Six"][2] != "NA":
                    st.success("The Maha Raj Yog Plane is fulfilled [4, 5, 6]")
                if numericals["Four_Nine_Two"][2] != "NA" and numericals["Three_Five_Seven"][1] != "NA" and numericals["Eight_One_Six"][0] != "NA":
                    st.success("The Raj Yog Plane is fulfilled [2, 5, 8]")
                if all(x != "NA" for x in numericals["Four_Nine_Two"]):
                    st.success("The Mental Plane is fulfilled [4, 9, 2]")
                if all(x != "NA" for x in numericals["Three_Five_Seven"]):
                    st.success("The Emotional Plane is fulfilled [3, 5, 7]")
                if all(x != "NA" for x in numericals["Eight_One_Six"]):
                    st.success("The Practical Plane is fulfilled [8, 1, 6]")
                if numericals["Four_Nine_Two"][0] != "NA" and numericals["Three_Five_Seven"][0] != "NA" and numericals["Eight_One_Six"][0] != "NA":
                    st.success("The Thought Plane is fulfilled [4, 3, 8]")
                if numericals["Four_Nine_Two"][1] != "NA" and numericals["Three_Five_Seven"][1] != "NA" and numericals["Eight_One_Six"][1] != "NA":
                    st.success("The Will Plane is fulfilled [9, 5, 1]")
                if numericals["Four_Nine_Two"][2] != "NA" and numericals["Three_Five_Seven"][2] != "NA" and numericals["Eight_One_Six"][2] != "NA":
                    st.success("The Action Plane is fulfilled [2, 7, 6]")
                small_title("Individual Numbers and Their Significance:", size=24)
                if numericals["Eight_One_Six"][1] != "NA":
                    small_title("1 - Leadership and Willpower", size=18)
                    st.write("Represents independence, self-reliance, ambition, and determination. It is often seen as the number of leadership and beginnings.")
                if numericals["Four_Nine_Two"][2] != "NA":   
                    small_title("2 - Partnership and Balance", size=18)
                    st.write("Symbolizes duality, harmony, cooperation, sensitivity, and emotional balance. It is associated with relationships and adaptability.")
                if numericals["Three_Five_Seven"][0] != "NA":
                    small_title("3 - Creativity and Expression", size=18)
                    st.write("Reflects creativity, communication, self-expression, and joy. It is often linked to optimism and artistic talent.")
                if numericals["Four_Nine_Two"][0] != "NA":
                    small_title("4 - Stability and Practicality", size=18)
                    st.write("Represents order, discipline, responsibility, and a foundation. It is associated with practicality and hard work.")
                if numericals["Three_Five_Seven"][1] != "NA":
                    small_title("5 - Freedom and Change</h1>", size=18)
                    st.write("Denotes versatility, adaptability, curiosity, and freedom. It represents a dynamic and adventurous spirit.")
                if numericals["Eight_One_Six"][2] != "NA":
                    small_title("6 - Love and Responsibility", size=18)
                    st.write("Symbolizes nurturing, care, harmony, and responsibility, especially in relationships and family.")
                if numericals["Three_Five_Seven"][2] != "NA":
                    small_title("7 - Spirituality and Introspection", size=18)
                    st.write("Represents deep thinking, intuition, spirituality, and introspection. It is often associated with mysticism and knowledge.")
                if numericals["Eight_One_Six"][0] != "NA":
                    small_title("8 - Power and Abundance", size=18)
                    st.write("Reflects material success, ambition, authority, and financial power. It is linked to practicality and management.")
                if numericals["Four_Nine_Two"][1] != "NA":
                    small_title("9 - Compassion and Universal Love", size=18)
                    st.write("Represents altruism, humanitarianism, idealism, and wisdom. It is the number of endings and higher consciousness")
                                  

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please fill out all the fields")