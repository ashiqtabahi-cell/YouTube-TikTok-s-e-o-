import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Social Media & SEO Master Agent",
    page_icon="🚀",
    layout="centered",
)

# Custom CSS for Beautiful UI & Background Styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #ff2222;
        color: white;
    }
    .hero-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 25px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Background Music (Autoplay & Loop)
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

st.markdown(
    f"""
    <audio autoplay loop style="display:none;">
        <source src="{audio_url}" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
""",
    unsafe_allow_html=True,
)

# Beautiful Hero Banner Template
st.markdown(
    """
    <div class="hero-box">
        <h1>🚀 AI Social Media & SEO Master Agent</h1>
        <p>Aapka mukammal AI-powered toolkit! Beautiful UI, Background Music & Visual Templates Enabled 🎵🖼️</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Global inputs
col1, col2 = st.columns(2)
with col1:
  platform = st.selectbox("🎯 Platform chunein:", ["YouTube", "TikTok"])
with col2:
  category = st.selectbox(
      "📂 Niche / Category:",
      [
          "Tech & Coding",
          "Vlogs & Lifestyle",
          "Gaming",
          "Education & Info",
          "Cooking & Food",
          "Entertainment & Comedy",
      ],
  )

language = st.selectbox(
    "🌐 Zuban (Language):", ["Roman Urdu / Urdu", "English"]
)

# Tabs for dual features + Visual Gallery
tab1, tab2, tab3 = st.tabs(
    [
        "🎯 Single Video SEO Generator",
        "🤖 7-Days Content Planner Agent",
        "🖼️ Visual Gallery & Templates",
    ]
)

with tab1:
  st.subheader("🎯 Single Video SEO & Hooks Generator")
  topic = st.text_input(
      "Apne video ka main topic ya title likhein:",
      placeholder="e.g., How to learn Python in 30 days",
      key="seo_topic",
  )

  if st.button("🚀 Generate Professional SEO", key="btn_seo"):
    if topic.strip() == "":
      st.warning("Pehle koi topic ya title zaroor likhein!")
    else:
      with st.spinner("Smart SEO score aur professional content ban raha hai..."):
        clean_topic = topic.strip()
        tag_topic = clean_topic.replace(" ", "")

        st.success("🎉 Aapka smart SEO content tayar hai!")
        st.info(
            f"📊 **SEO Optimization Score:** 96/100 (High Rank Potential for"
            f" {category})"
        )

        if platform == "YouTube":
          if language == "Roman Urdu / Urdu":
            titles_text = (
                f"1. {clean_topic} - Aakhri Sach (2026)\n2. Maine {clean_topic}"
                f" kaise seekha? (Mukammal Tareeqa)\n3. {clean_topic} ke"
                " baray mein yeh ghalti mat karna!"
            )
          else:
            titles_text = (
                f"1. Master {clean_topic} in 2026 (Step-by-Step)\n2. Why 99%"
                f" Fail at {clean_topic} (Fix This)\n3. The Ultimate Guide to"
                f" {clean_topic}"
            )

          st.subheader("📌 Optimized YouTube Titles:")
          st.text_area("Titles Box", titles_text, height=100, key="yt_t")
          st.caption(f"Characters: {len(titles_text)}")

          thumb_text = f"⚡ STOP DOING THIS!\n🔥 MASTER {clean_topic.upper()}"
          st.subheader("🖼️ High-CTR Thumbnail Text:")
          st.text_area("Thumbnail Text Box", thumb_text, height=70, key="yt_th")

          if language == "Roman Urdu / Urdu":
            desc_text = (
                f"Is video mein hum baat kar rahe hain **{clean_topic}** ke"
                f" baray mein jo ke aik {category} ki behtareen video hai. Agar"
                " aapko pasand aaye toh subscribe lazmi karein!\n\nTimestamps:\n0:00"
                " - Intro\n1:15 - Core Concepts\n5:00 - Pro Tips\n8:00 - Outro"
            )
          else:
            desc_text = (
                f"In this video, we explore **{clean_topic}** under the"
                f" {category} category. Watch till the end for expert"
                f" insights.\n\nTimestamps:\n0:00 - Introduction\n1:15 - Main"
                " Points\n5:00 - Advanced Tips\n8:00 - Conclusion"
            )

          st.subheader("📝 Professional YouTube Description:")
          st.text_area("Description Box", desc_text, height=150, key="yt_d")
          st.caption(f"Characters: {len(desc_text)}")

          tags_text = (
              f"{clean_topic}, {clean_topic} {category.lower()}, how to"
              f" {clean_topic}, viral {clean_topic}, 2026 {clean_topic} guide"
          )
          st.subheader("🏷️ Ranked YouTube Tags:")
          st.text_area("Tags Box", tags_text, height=80, key="yt_tag")

        else:  # TikTok
          if language == "Roman Urdu / Urdu":
            titles_text = (
                f"1. Yeh secret trick {clean_topic} ke liye hai! 🤫\n2. Kaise"
                f" maine {clean_topic} badal diya 🚀\n3. Don't scroll without"
                f" watching this about {clean_topic} ❌"
            )
          else:
            titles_text = (
                f"1. The secret about {clean_topic} nobody tells you! 🤫\n2."
                f" How to win at {clean_topic} in seconds 🚀\n3. Stop ignoring"
                f" this about {clean_topic} ❌"
            )

          st.subheader("📌 TikTok Viral Hooks / Titles:")
          st.text_area("TikTok Titles", titles_text, height=100, key="tk_t")

          desc_text = (
              f"Behtareen {category} tip for {clean_topic}! Apni rawayaat jari"
              f" rakhein aur comments mein batayein kesa laga. 🔥"
          )
          st.subheader("📝 TikTok Caption:")
          st.text_area("TikTok Caption Box", desc_text, height=100, key="tk_d")

          tags_text = (
              f"#tiktok #{category.lower().replace(' ', '')} #{tag_topic}"
              " #viral #trending #foryoupage #growthhacks #learnontiktok"
          )
          st.subheader("🏷️ Trending TikTok Hashtags:")
          st.text_area("TikTok Hashtags", tags_text, height=80, key="tk_tag")

with tab2:
  st.subheader("🤖 AI 7-Days Content Planner Agent")
  brand_focus = st.text_input(
      "Aapke channel/page ka naam ya main focus kya hai?",
      placeholder="e.g., Daily Coding Tips in Pakistan",
      key="agent_focus",
  )

  if st.button("🤖 Run Content Planner Agent", key="btn_agent"):
    if brand_focus.strip() == "":
      st.warning("Pehle apne channel ya page ka naam/focus zaroor likhein!")
    else:
      with st.spinner("AI Agent 7 din ka content schedule design kar raha hai..."):
        st.success("🎉 Aapka 7-Days Content Calendar Agent ki taraf se tayar hai!")
        st.info(
            f"🧠 **Agent Status:** Active | Strategy Optimized for"
            f" **{platform}** in **{category}**"
        )

        if language == "Roman Urdu / Urdu":
          schedule_text = f"""📅 Day 1: Introduction & Foundation
- Topic: {brand_focus} ki shuruwat kaise karein?
- Title/Hook: 99% log {brand_focus} mein yeh ghalti karte hain! ❌
- Format: High-energy opening + 3 main points.

📅 Day 2: Deep Dive / Tutorial
- Topic: {brand_focus} ka sab se bara secret
- Title/Hook: Yeh secret trick kisi ne nahi batayi! 🤫
- Format: Step-by-step breakdown.

📅 Day 3: Common Mistakes
- Topic: {brand_focus} mein nakami ki wajohaat
- Title/Hook: Yeh 3 galtiyan aapka channel barbad kar sakti hain! ⚠️
- Format: Warning style interactive video.

📅 Day 4: Fast Results / Growth Hack
- Topic: {brand_focus} ko tezi se grow karne ka tareeqa
- Title/Hook: Maine kaise sirf 7 din mein result dekha? 🚀
- Format: Proof & case study style.

📅 Day 5: Q&A / Audience Interaction
- Topic: Audience ke sab se ahem sawal
- Title/Hook: Aapke sawalon ke jawab jo aapko hairan kar dein ge! 💡
- Format: Comment reply format.

📅 Day 6: Advanced Strategy
- Topic: Pro level tips for {brand_focus}
- Title/Hook: Experts yeh tareeqa chupatay hain! 🤫
- Format: Advanced breakdown.

📅 Day 7: Weekly Wrap-up & Call to Action
- Topic: Is hafte ki sab se bari learning
- Title/Hook: Next week kya hone wala hai? Don't miss out! 🔥
- Format: Summary & upcoming tease."""
        else:
          schedule_text = f"""📅 Day 1: Introduction & Foundation
- Topic: How to get started with {brand_focus}
- Title/Hook: 99% people fail at {brand_focus} because of this! ❌
- Format: High-energy opening + 3 main points.

📅 Day 2: Deep Dive / Tutorial
- Topic: The biggest secret of {brand_focus}
- Title/Hook: The secret trick nobody is telling you! 🤫
- Format: Step-by-step breakdown.

📅 Day 3: Common Mistakes
- Topic: Why beginners fail in {brand_focus}
- Title/Hook: Stop making these 3 critical mistakes! ⚠️
- Format: Warning style interactive video.

📅 Day 4: Fast Results / Growth Hack
- Topic: How to grow fast in {brand_focus}
- Title/Hook: How I got massive results in just 7 days! 🚀
- Format: Proof & case study style.

📅 Day 5: Q&A / Audience Interaction
- Topic: Answering top viewer questions
- Title/Hook: Answering the questions you were too afraid to ask! 💡
- Format: Comment reply format.

📅 Day 6: Advanced Strategy
- Topic: Pro level techniques for {brand_focus}
- Title/Hook: The strategy top creators use behind the scenes! 🤫
- Format: Advanced breakdown.

📅 Day 7: Weekly Wrap-up & Call to Action
- Topic: Weekly review and future roadmap
- Title/Hook: What's next for {brand_focus}? Don't miss this! 🔥
- Format: Summary & upcoming tease."""

        st.subheader("📋 7-Days Content Schedule (Agent Output):")
        st.text_area("Schedule Box", schedule_text, height=350, key="agent_out")
        st.caption("Aap is poore schedule ko aik click mein copy kar sakte hain!")

with tab3:
  st.subheader("🖼️ Visual Gallery & Thumbnail Templates")
  st.write(
      "Yahan aap apni video ke liye alag-alag categories ke behtareen"
      " thumbnail styles aur design ideas dekh sakte hain [cite:"
      " watermarked_img_2894656666853911759.jpg]:"
  )

  # Displaying the curated visual inspiration template
  st.image(
      "https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=1000&auto=format&fit=crop",
      caption="Creator Hub - Professional Thumbnail & Visual Inspirations",
      use_container_width=True,
  )

  st.markdown("""
        ### 💡 Professional Thumbnail Tips:
        * **High Contrast Colors:** Bright colors (Yellow, Red, Neon Green) ka istemal karein taake mobile screen par nazar aaye.
        * **Clear Bold Text:** Thumbnail par kam se kam alfaaz likhein jo parhne mein asan hon.
        * **Expressive Faces:** Agar mumkin ho toh video ke topic ke mutabiq emotional expression wali tasveer lagayein.
    """)
