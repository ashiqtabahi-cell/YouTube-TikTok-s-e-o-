import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(
    page_title="YouTube & TikTok SEO Generator", page_icon="🚀", layout="centered"
)

st.title("🚀 YouTube & TikTok SEO & Content Generator")
st.write(
    "Apne video ke liye professional Titles, Descriptions, aur Tags generate karein!"
)

# Groq API Key hardcode kar di hai jo aapne di hai
API_KEY = "Gsk_EfDE6gaDr57pl7xbUbFaWGdyb3FYpL92u1mYVfsLjz5aZe1XmN5V"

# Initialize Groq client
client = Groq(api_key=API_KEY)

# User input
topic = st.text_input(
    "Apne video ka topic ya idea yahan likhein:",
    placeholder="e.g., How to grow fast on TikTok in 2026",
)

platform = st.selectbox("Platform select karein:", ["YouTube", "TikTok"])

if st.button("Generate SEO Content"):
  if topic.strip() == "":
    st.warning("Pehle koi topic ya idea toh likhein!")
  else:
    with st.spinner("Content generate ho raha hai... Thoda intezaar karein!"):
      try:
        prompt = (
            f"Generate catchy SEO optimized Title, Description, and relevant"
            f" Hashtags/Tags for a {platform} video about: {topic}"
        )

        chat_completion = client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": prompt,
            }],
            model="llama-3.3-70b-versatile",
        )

        result = chat_completion.choices[0].message.content

        st.success("Yahan aapka SEO content tayar hai:")
        st.markdown(result)

      except Exception as e:
        st.error(f"Koi error aa gaya hai: {e}")
          
        
        
