import base64
import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="DSC CLUB",
    page_icon="🤖",
)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background("w12.jpg")

st.image("logo1.png", width=200)

csv_file = 'student_info.csv'

# Check if the CSV file exists, create it if it does not
if not os.path.exists(csv_file):
    # Create a new CSV file with headers
    pd.DataFrame(columns=[
        'Full Name', 'Email', 'Roll Number', 'Branch', 'Section', 
        'Technical Domain', 'Skills', 'Phone Number', 'WhatsApp Number', 'Residence'
    ]).to_csv(csv_file, index=False)

# Initialize session state for 'student_info' if not already done
if 'student_info' not in st.session_state:
    st.session_state['student_info'] = pd.read_csv(csv_file)

st.markdown(
    """
    <h1 style="color:white; text-align:center;">DATA SCIENCE CLUB RECRUITMENT</h1>
    """,
    unsafe_allow_html=True
)
st.markdown("# Registration Form")

# Input fields for the form
full_name = st.text_input("Enter your Full Name : ")
email = st.text_input("Email (NIST E-Mail Id) : ")
roll_num = st.text_input("Roll Number : ")
branch = st.radio("Branch", 
("CSE", "CST", "IT", "ECE", "ECS / ELC", "EE / EEE", "CE", "ME"))
section = st.text_input("Section : (example - CSE-C)")
tech_dom = st.radio("Technical Domain", 
("Web Development", "UI/UX", "Artificial Intelligence & Machine Learning", 
"Cloud", "DevOps", "Android Development", "Cybersecurity & Blockchain"))
skills = st.multiselect("Skills you know rather than Technical", 
["Photography", "Videography", "Poster Designing", 
"Public Speaking", "Social Media Handling", "Video Editing"])
phn_no = st.text_input("Phone Number")
wp_no = st.text_input("WhatsApp Number")
residence = st.radio("Residence", ("Hostelite", "Localite"))

# Submit button logic
if st.button("Submit"):
    if full_name and email and roll_num and branch and section and tech_dom and skills and phn_no and wp_no and residence:
        new_entry = pd.DataFrame({
            'Full Name': [full_name],
            'Email': [email],
            'Roll Number': [roll_num],
            'Branch': [branch],
            'Section': [section],
            'Technical Domain': [tech_dom],
            'Skills': [", ".join(skills)],  # Convert list to comma-separated string
            'Phone Number': [phn_no],
            'WhatsApp Number': [wp_no],
            'Residence': [residence]
        })

        try:
            # Append the new data to the existing CSV file
            new_entry.to_csv(csv_file, mode='a', header=False, index=False)
            
            # Update the session state with the new entry
            st.session_state['student_info'] = pd.concat([st.session_state['student_info'], new_entry], ignore_index=True)
            
            st.success("Your details have been submitted successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please fill out all fields.")
