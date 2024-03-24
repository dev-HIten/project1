import streamlit as st
from datetime import date
import random

st.title('Age calculator')

def calculate_age(birth_date, current_date):
    # Calculation
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    # Adjust for negative differences
    if days < 0:
        months -= 1
        days += get_days_in_month(birth_date.month, birth_date.year)
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def get_days_in_month(month, year):
    # Returns the number of days in a given month and year 
    if month == 2:  # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): 
            return 29  # Leap year
        else:
            return 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November 
        return 30
    else:
        return 31

# Current date
current_date = date.today()

# Create date objects for birth date and current date
birth_date=st.date_input('Enter birth date :baby: :smile:',value=date(2007,3,28),min_value=date(1900,1,1),max_value=current_date)

# Calculate age
age_years, age_months, age_days = calculate_age(birth_date, current_date)
st.subheader(f"Your age is {age_years} years, {age_months} months, and {age_days} days.")

#time of survival
days=(current_date-birth_date).days

sent=["Congrats you have succesfully wasted",
      "Congrats you have survived for",
      "You've been learning and exploring for"]

st.subheader(f"{random.choice(sent)} {(days)} days")
st.progress(days/29000)

links = [
  "https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
  "https://storage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",
  "https://storage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4",
  "https://storage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4"
]

video=random.choice(links)

if st.button("Get party"):
    st.video(video)




