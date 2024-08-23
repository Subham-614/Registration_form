import streamlit as st
import base64

st.markdown("# Recruitment Details")
st.sidebar.markdown("# Recruitment Details")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set the background image using Base64
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

st.write("# DATA SCIENCE CLUB RECRUITMENT !!!!")

st.markdown("""
### 🤖🤖DATA ENTHUSIASTS, IT'S TIME TO TURN UP THE INNOVATION!🤖🤖
🔥 CORE MEMBERS RECRUITMENT FOR THE DATA SCIENCE CLUB! 🔥
"""
)

st.markdown("""
Hello, Intelligence along with innovative minds of the 2k23 batches! 🌟
"""
)

st.markdown("""
Are you passionate about data and eager to dive into the world of machine learning, analytics, and artificial intelligence?
""")

st.markdown("""
The Data Science Club is thrilled to announce that we are now recruiting motivated second-year students to join our vibrant community. 
""")

st.markdown("""
Whether you're just starting your data science journey or looking to sharpen your skills, this is the perfect platform to collaborate on exciting projects, participate in hackathons, and learn from experienced mentors.
""")

st.markdown("""
🥳🥳🥳Don't miss out on the chance to be part of a dynamic team that’s shaping the future of data science at our university. Apply now and take your first step towards becoming a data science expert!💫💫💫
""")

st.markdown("""
Selection Process:
""")

st.markdown("""
Round 1:Technical Quiz in MCQ on Sunday(25/08/24) consisting of topics like Python, C,Mathematics,Verbal Aptitude(English).
""")

st.markdown("""
Round 2: PI (Personal Interview) round will happen from 26/8/2024 to 28/8/2024.
""")

st.markdown("""
Dive into the world of Data Science with your most innovative ideas and claim your spot once and for all, everyone! Get ready to unleash your full potential and make your mark! 
""")

st.markdown("""
See you there Bright Minds !!!
""")

st.markdown("""
### For Any Queries feel free to contact:
""")

st.markdown("""
Manab :- 7735853550
""")

st.markdown("""
Sitansu :- 9938493570
""")

st.markdown("""
Subham :- 8249114135
""")

st.markdown("""
WhatsApp Group Invite Link
""")

st.markdown("""
LINK - [JOIN FAST](https://chat.whatsapp.com/C46kwraTgY59pLGgouGfFr)
""")

st.markdown("""
🔥 GRAB YOUR SEAT AT THE EARLIEST JUNIORS 🔥
""")