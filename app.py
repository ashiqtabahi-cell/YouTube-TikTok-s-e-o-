import streamlit as st

# Page configuration
st.set_page_config(
    page_title="YouTube & TikTok SEO Generator", page_icon="🚀", layout="centered"
)

st.title("🚀 YouTube & TikTok Professional SEO Generator")
st.write(
    "Apne video ke liye mukammal aur professional Titles, Description, aur"
    " Hashtags generate karein!"
)

# User inputs
topic = st.text_input(
    "Apne video ka topic ya idea yahan likhein:",
    placeholder="e.g., How to grow fast on TikTok in 2026",
)
platform = st.selectbox("Platform chunein:", ["YouTube", "TikTok"])
language = st.selectbox(
    "Language chunein:", ["English", "Urdu / Roman Hindi"]
)

if st.button("Generate Professional SEO"):
  if topic.strip() == "":
    st.warning("Pehle koi topic ya idea zaroor likhein!")
  else:
    with st.spinner("Professional SEO content taiyar ho raha hai..."):
      st.success("🎉 Aapka mukammal SEO content taiyar hai!")

      # Detailed Professional Output based on platform
      if platform == "YouTube":
        st.subheader("📌 Catchy YouTube Titles:")
        st.write(
            f"1. Ultimate Guide to Master {topic} (Step-by-Step for 2026)\n2."
            f" Why Everyone is Wrong About {topic}! (Must Watch)\n3. How to"
            f" Get Started With {topic} and Grow Fast"
        )

        st.subheader("📝 Detailed YouTube Description:")
        st.write(
            f"Welcome back to our channel! In this video, we are diving deep"
            f" into **{topic}**. Agar aap {platform} par kamyabi hasil karna"
            " chahte hain, toh yeh video aapke liye bohat zaroori hai. Hum"
            "ne isme tamam tips, tricks, aur secrets share kiye hain jo aapko"
            " zaroor madad karenge.\n\nTimestamps:\n0:00 - Introduction\n1:30"
            f" - Understanding {topic}\n3:45 - Pro Tips & Tricks\n6:00 - Final"
            " Thoughts\n\nDon't forget to Like, Share, and Subscribe for more"
            " amazing content!"
        )

        st.subheader("🏷️ Optimized YouTube Tags:")
        st.write(
            f"{topic}, {topic} tutorial, how to learn {topic}, {platform}"
            f" growth 2026, viral {topic}, best tips for {topic}, trending"
            " topics"
        )

      else:
        st.subheader("📌 Viral TikTok Titles / Hooks:")
        st.write(
            f"1. Yeh secret koi nahi batayega about {topic}! 🤫\n2. How I"
            f" mastered {topic} in just 7 days! 🚀\n3. Stop making this mistake"
            f" with {topic} ❌"
        )

        st.subheader("📝 TikTok Caption & Description:")
        st.write(
            f"Aap bhi {topic} ke baray mein yeh nahi jante honge! Watch till"
            f" the end to see the amazing results. Let me know in the comments"
            f" what you want to see next on {platform}! 🔥"
        )

        st.subheader("🔥 Trending TikTok Hashtags:")
        st.write(
            f"#{platform.lower()} #{topic.replace(' ', '')} #viral"
            " #trendingvideo #foryoupage #foryou #growthhacks #learnontiktok"
        )
        
