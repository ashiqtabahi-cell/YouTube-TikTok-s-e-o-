import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Viral Media & Aesthetic Music Lounge",
    page_icon="🔥",
    layout="centered",
)

# Custom CSS for Beautiful UI & Background Styling
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #ff4b4b 0%, #ff6b6b 100%);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #ff2222. #ff4b4b);
        color: white;
    }
    .hero-box {
        background: linear-gradient(135deg, #1f4068 0%, #162447 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Background Music (Autoplay & Loop) - Soothing Viral Vibe Audio
audio_url = (
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
)  # Aap yahan koi bhi pasandeeda music link laga sakte hain

st.markdown(
    f"""
    <audio autoplay loop controls style="width:100%; margin-bottom: 20px;">
        <source src="{audio_url}" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
""",
    unsafe_allow_html=True,
)

# Hero Banner
st.markdown(
    """
    <div class="hero-box">
        <h1>🔥 Viral Media & Aesthetic Music Lounge</h1>
        <p>Yahan aapko milengi sab se khoobsurat viral pictures, thumbnail designs, aur relaxing background music! 🎵✨</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Tabs for organization
tab1, tab2, tab3 = st.tabs(
    [
        "🔥 Viral & Aesthetic Pictures",
        "🎨 Canva-Style Custom Studio",
        "🚀 Social Media Toolkit",
    ]
)

with tab1:
  st.subheader("📸 Trending Viral Pictures & Thumbnail Gallery")
  st.write(
      "Aap in behtareen aur viral pictures ko dekh sakte hain ya download kar"
      " sakte hain:"
  )

  # Category filter for pictures
  pic_category = st.selectbox(
      "Pictures ki category chunein:",
      [
          "All Viral Styles",
          "Gaming & Action",
          "Vlogs & Lifestyle",
          "Tech & Neon Vibe",
          "Food & Cooking",
      ],
  )

  col1, col2 = st.columns(2)

  with col1:
    st.image(
        "https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=600&auto=format&fit=crop",
        caption="🔥 Trending YouTube & Social Thumbnail Layout",
        use_container_width=True,
    )
    st.image(
        "https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=600&auto=format&fit=crop",
        caption="🎮 High-Energy Gaming Setup & Vibe",
        use_container_width=True,
    )

  with col2:
    st.image(
        "https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=600&auto=format&fit=crop",
        caption="✨ Aesthetic Lifestyle & Vlog Mood",
        use_container_width=True,
    )
    st.image(
        "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=600&auto=format&fit=crop",
        caption="💻 Futuristic Tech & Neon Aesthetics",
        use_container_width=True,
    )

with tab2:
  st.subheader("🎨 Custom Image Uploader & Workspace")
  st.write("Aap apni marzi ki koi bhi tasveer yahan upload kar sakte hain:")

  uploaded_file = st.file_uploader(
      "Apni device se image select karein (JPG/PNG):",
      type=["jpg", "jpeg", "png"],
  )
  if uploaded_file is not None:
    st.success("🎉 Aapki tasveer kamiyabi se load ho gayi hai!")
    st.image(
        uploaded_file, caption="Aapki Custom Uploaded Pic", use_container_width=True
    )

with tab3:
  st.subheader("🚀 Quick Social Media Tools")
  topic = st.text_input(
      "Apne video ya post ka topic likhein:",
      placeholder="e.g., My New Vlog in Lahore",
  )

  if st.button("✨ Generate Viral Hooks"):
    if topic.strip() == "":
      st.warning("Pehle kuch likhein!")
    else:
      st.success("🎉 Aapke viral hooks tayar hain!")
      st.info(f"1. 99% log {topic} ke baray mein yeh nahi jantay! ❌\n2. Kaise maine {topic} ko badal diya! 🚀\n3. The ultimate secret about {topic} 🤫")
      
