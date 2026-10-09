import streamlit as st

# Page configuration
st.set_page_config(
    page_title="YouTube & TikTok SEO Generator", page_icon="🚀", layout="centered"
)

st.title("🚀 YouTube & TikTok SEO & Content Generator")
st.write(
    "Apne video ke liye professional Titles, Descriptions, aur Tags generate"
    " karein!"
)

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
    with st.spinner("Content generate ho raha hai..."):
      # Simulated local generation taake koi API key ka error na aaye
      st.success("Yahan aapka SEO content tayar hai:")

      st.subheader("📌 Recommended Titles:")
      st.write(
          f"1. Ultimate Guide to Master {topic} in 2026!\n2. Why Everyone is"
          f" Talking About {topic}\n3. The Secret Strategy for {platform}"
          " Success"
      )

      st.subheader("📝 Optimized Description:")
      st.write(
          f"In this video, we dive deep into {topic}. Learn the best tips and"
          f" tricks to boost your reach on {platform}. Make sure to watch till"
          " the end for expert advice!"
      )

      st.subheader("tags / Hashtags:")
      st.write(
          f"#{platform.lower()} #viral #trending #{topic.replace(' ', '')}"
          " #growthtips #foryou"
        
        
