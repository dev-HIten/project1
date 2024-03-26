import streamlit as st
from datetime import datetime

@st.cache_data
def calculate_time_left(event_datetime):
    now = datetime.now()
    time_left = event_datetime - now
    days_left = time_left.days
    hours_left = time_left.seconds // 3600
    return days_left, hours_left

def main():
    st.title("Event Time Left Calculator")
    
    # Input fields for adding a new event
    new_event_date = st.date_input("Enter the date of the new event")
    new_event_time = st.time_input("Enter the time of the new event")
    new_event_name = st.text_input("Enter the name of the new event")
    new_event_datetime = datetime.combine(new_event_date, new_event_time)
    # st.write(new_event_time)
    # Button to add the new event
    if st.button("Add Event"):
        st.session_state[new_event_name] = new_event_datetime
        st.success(f"Event '{new_event_name}' added successfully!")
    
    # Display the list of events and their time left
    events = st.session_state.keys()
    for event_name in events:
        if event_name not in ["new_event_date", "new_event_time", "new_event_name"]:
            event_datetime = st.session_state[event_name]
            days_left, hours_left = calculate_time_left(event_datetime)
            st.write(f"Event: {event_name}")
            st.write(f"- Time left until the event:")
            st.write(f"  - Days: {days_left} days")
            st.write(f"  - Hours: {hours_left} hours")
            st.write("---")

if __name__ == "__main__":
    main()
