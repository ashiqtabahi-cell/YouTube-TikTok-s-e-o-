import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Universal YouTube & TikTok SEO Generator",
    page_icon="🌍",
    layout="centered",
)

st.title("🌍 Universal Multi-Language SEO Generator")
st.write(
    "Duniya ki kisi bhi zuban mein apnay video ke liye Titles, Detailed"
    " Descriptions, aur Tags generate karein!"
)

# User inputs
topic = st.text_input(
    "Apnay video ka topic ya title kisi bhi zuban mein likhein:",
    placeholder="e.g., Pakistan ka mustaqbil, How to code in Python, إلخ",
)
platform = st.selectbox("Platform chunein:", ["YouTube", "TikTok"])

if st.button("Generate Universal SEO"):
  if topic.strip() == "":
    st.warning("Pehle koi topic ya title zaroor likhein!")
  else:
    with st.spinner(
        "Har zuban ke liye behtareen SEO content taiyar ho raha hai..."
    ):
      st.success("🎉 Aapka mukammal SEO content taiyar hai!")

      clean_topic = topic.strip()
      tag_topic = clean_topic.replace(" ", "")

      if platform == "YouTube":
        st.subheader("📌 YouTube Titles (Catchy & SEO Friendly):")
        st.write(
            f"1. Complete Guide to {clean_topic} (2026 Ultimate Guide)\n2. Why"
            f" Everyone is Talking About {clean_topic}! (Must Watch)\n3. How to"
            f" Master {clean_topic} Step-by-Step"
        )

        st.subheader("📝 Detailed YouTube Description:")
        st.write(
            f"Is video mein hum tafseel se baat karenge **{clean_topic}** ke"
            " baray mein. Agar aap is topic ko mukammal taur par samajhna"
            " chahte hain, toh yeh video aakhir tak lazmi dekhein. Humne isme"
            " tamam zaroori points aur secrets share kiye hain.\n\nTimestamps:\n0:00"
            f" - Introduction\n1:15 - What is {clean_topic}?\n4:30 - Core"
            " Concepts & Strategy\n8:00 - Conclusion & Final Thoughts\n\nVideo"
            " pasand aaye toh Like karein aur channel ko subscribe karna na"
            " bhulein!"
        )

        st.subheader("🏷️ Optimized YouTube Tags:")
        st.write(
            f"{clean_topic}, how to learn {clean_topic}, {clean_topic} tutorial,"
            f" viral {clean_topic}, {clean_topic} 2026, trending topics,"
            f" complete guide {clean_topic}"
        )

      else:  # TikTok
        st.subheader("📌 TikTok Viral Titles / Hooks:")
        st.write(
            f"1. Yeh secret koi nahi batayega about {clean_topic}! 🤫\n2. How I"
            f" mastered {clean_topic} in record time! 🚀\n3. Stop making this"
            f" mistake with {clean_topic} ❌"
        )

        st.subheader("📝 TikTok Caption & Description:")
        st.write(
            f"Aapka is baray mein kya khayal hai? {clean_topic} ki mukammal"
            " tafseel comments mein batayein! Watch till the end for amazing"
            f" results. 🔥 #{clean_topic.replace(' ', '')}"
        )

        st.subheader("🏷️ TikTok Hashtags:")
        st.write(
            f"#viral #{tag_topic} #trending #foryoupage #foryou #growthhacks"
            f" #learnontiktok #viral{tag_topic} #trendingvideo"
          )
          
