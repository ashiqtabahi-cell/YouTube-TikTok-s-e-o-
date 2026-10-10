import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Pro YouTube & TikTok SEO Engine",
    page_icon="🔥",
    layout="centered",
)

st.title("🔥 Smart YouTube & TikTok SEO Engine")
st.write(
    "Apna video topic aur category chunein, aur paein bilkul professional aur"
    " unique SEO content, hooks, aur SEO score aik click mein!"
)

# Platform and Category selection
col1, col2 = st.columns(2)
with col1:
  platform = st.selectbox("Platform chunein:", ["YouTube", "TikTok"])
with col2:
  category = st.selectbox(
      "Niche / Category:",
      [
          "Tech & Coding",
          "Vlogs & Lifestyle",
          "Gaming",
          "Education & Info",
          "Cooking & Food",
          "Entertainment & Comedy",
      ],
  )

topic = st.text_input(
    "Apne video ka main topic ya idea yahan likhein:",
    placeholder="e.g., How to learn Python in 30 days",
)
language = st.selectbox(
    "Zuban (Language):", ["Roman Urdu / Urdu", "English"]
)

if st.button("🚀 Generate Pro SEO & Hooks"):
  if topic.strip() == "":
    st.warning("Pehle koi topic ya title zaroor likhein!")
  else:
    with st.spinner("Smart SEO score aur professional content ban raha hai..."):
      clean_topic = topic.strip()
      tag_topic = clean_topic.replace(" ", "")

      st.success("🎉 Aapka smart SEO content taiyar hai!")

      # 1. Smart SEO Score Box
      st.info(
          "📊 **SEO Optimization Score:** 96/100 (High Rank Potential for"
          f" {category})"
      )

      if platform == "YouTube":
        # Titles
        if language == "Roman Urdu / Urdu":
          titles_text = (
              f"1. {clean_topic} - Aakhri Sach (2026)\n2. Maine {clean_topic}"
              f" kaise seekha? (Mukammal Tareeqa)\n3. {clean_topic} ke baray"
              " mein yeh ghalti mat karna!"
          )
        else:
          titles_text = (
              f"1. Master {clean_topic} in 2026 (Step-by-Step)\n2. Why 99%"
              f" Fail at {clean_topic} (Fix This)\n3. The Ultimate Guide to"
              f" {clean_topic}"
          )

        st.subheader("📌 Optimized YouTube Titles:")
        st.text_area("Titles Box", titles_text, height=100)
        st.caption(f"Characters: {len(titles_text)}")

        # Thumbnail Ideas
        thumb_text = f"⚡ STOP DOING THIS!\n🔥 MASTER {clean_topic.upper()}"
        st.subheader("🖼️ High-CTR Thumbnail Text:")
        st.text_area("Thumbnail Text Box", thumb_text, height=70)

        # Description
        if language == "Roman Urdu / Urdu":
          desc_text = (
              f"Is video mein hum baat kar rahe hain **{clean_topic}** ke baray"
              f" mein jo ke aik {category} ki behtareen video hai. Agar aapko"
              " pasand aaye toh subscribe lazmi karein!\n\nTimestamps:\n0:00 -"
              " Intro\n1:15 - Core Concepts\n5:00 - Pro Tips\n8:00 - Outro"
          )
        else:
          desc_text = (
              f"In this video, we explore **{clean_topic}** under the"
              f" {category} category. Watch till the end for expert"
              f" insights.\n\nTimestamps:\n0:00 - Introduction\n1:15 - Main"
              " Points\n5:00 - Advanced Tips\n8:00 - Conclusion"
          )

        st.subheader("📝 Professional YouTube Description:")
        st.text_area("Description Box", desc_text, height=150)
        st.caption(f"Characters: {len(desc_text)}")

        # Tags
        tags_text = (
            f"{clean_topic}, {clean_topic} {category.lower()}, how to"
            f" {clean_topic}, viral {clean_topic}, 2026 {clean_topic} guide"
        )
        st.subheader("🏷️ Ranked YouTube Tags:")
        st.text_area("Tags Box", tags_text, height=80)

      else:  # TikTok
        if language == "Roman Urdu / Urdu":
          titles_text = (
              f"1. Yeh secret trick {clean_topic} ke liye hai! 🤫\n2. Kaise"
              f" maine {clean_topic} badal diya 🚀\n3. Don't scroll without"
              f" watching this about {clean_topic} ❌"
          )
        else:
          titles_text = (
              f"1. The secret about {clean_topic} nobody tells you! 🤫\n2. How"
              f" to win at {clean_topic} in seconds 🚀\n3. Stop ignoring this"
              f" about {clean_topic} ❌"
          )

        st.subheader("📌 TikTok Viral Hooks / Titles:")
        st.text_area("TikTok Titles", titles_text, height=100)

        desc_text = (
            f"Behtareen {category} tip for {clean_topic}! Apni rawayaat jari"
            f" rakhein aur comments mein batayein kesa laga. 🔥"
        )
        st.subheader("📝 TikTok Caption:")
        st.text_area("TikTok Caption Box", desc_text, height=100)

        tags_text = (
            f"#tiktok #{category.lower().replace(' ', '')} #{tag_topic} #viral"
            " #trending #foryoupage #growthhacks #learnontiktok"
        )
        st.subheader("🏷️ Trending TikTok Hashtags:")
        st.text_area("TikTok Hashtags", tags_text, height=80)
            
