import streamlit as st

# Page Configuration
st.set_page_config(page_title="Online Earning Portal", page_icon="💰", layout="centered")

# App Header
st.title("💰 Online Earning Hub")
st.write("Welcome! Complete simple tasks and start earning daily.")

# User Input Section
st.subheader("User Login / Registration")
username = st.text_input("Enter your Name:")
email = st.text_input("Enter your Email:")

if st.button("Register & Start Earning"):
    if username and email:
        st.success(f"Welcome {username}! Your account has been created successfully.")
        st.balloons()
    else:
        st.warning("Please fill in both fields to continue.")

# Earning Options Section
st.divider()
st.subheader("Available Tasks")
st.info("1. Watch Videos - Earn $5")
st.info("2. Complete Surveys - Earn $10")
st.info("3. Refer Friends - Earn $15 per referral")

# Balance Section
st.sidebar.title("Account Stats")
st.sidebar.metric(label="Current Balance", value="$0.00")
st.sidebar.text("Status: Active")

