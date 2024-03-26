import streamlit as st
from datetime import date,datetime,time

@st.cache_data
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

@st.cache_data
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

def calculate_time_left(event_datetime):
    now = datetime.now()
    time_left = event_datetime - now
    days_left = time_left.days
    hours_left = time_left.seconds // 3600
    mins_left =(time_left.seconds % 3600 ) // 60
    secs_left=(time_left.seconds % 3600 ) % 60
    return days_left, hours_left ,mins_left,secs_left
    
st.title("Age calculator")

# Current date
current_date = date.today()

# Create date objects for birth date and current date
col1,col2= st.columns([1,1])
with col1:
    birth_date=st.date_input('Enter birth date :baby: :smile:',value=date(2007,3,28),min_value=date(1900,1,1),max_value=current_date)
with col2:
    birth_time= st.time_input("Enter the time of the new event",time(0,00))


# Calculate age
age_years, age_months, age_days = calculate_age(birth_date, current_date)
st.subheader(f"Your age is {age_years} years, {age_months} months, and {age_days} days.")

#time of survival
days=(current_date-birth_date).days

st.subheader(f"You've been learning and exploring for {(days)} days")
col1,col2= st.columns([1,10])
with col1:
    st.write(f'{age_years}/ 100')
    st.write(f'{age_months}/12')
    st.write(f'{age_days}/30')

with col2:
    st.progress(age_years/100)
    st.progress(age_months/12)
    st.progress(age_days/30)

next_birthday = birth_date.replace(year=current_date.year)

if next_birthday.day ==29 and next_birthday.month==2:
    next_birthday.replace(day=28)

elif next_birthday < current_date:
    next_birthday = next_birthday.replace(year=current_date.year + 1)


event_datetime=datetime.combine(next_birthday, birth_time)

if st.button("How much time left for next birth day"):
    days_left, hours_left, mins_left , secs_left= calculate_time_left(event_datetime)
    st.subheader(f"{days_left} days {hours_left}:{mins_left}:{secs_left} left for your next birthday")

    





