import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Professional Video SEO Generator", page_icon="🚀", layout="centered"
)

st.title("🚀 Pro Video Upload & SEO Generator")
st.write(
    "Apni video upload karein aur asani se copy karne ke liye professional"
    " Titles, Descriptions, Thumbnail text, aur Tags hasil karein!"
)

# 1. Video File Uploader
uploaded_file = st.file_uploader(
    "Apni video file yahan upload karein:", type=["mp4", "mov", "avi", "mkv"]
)

platform = st.selectbox("Platform chunein:", ["YouTube", "TikTok"])
language = st.selectbox(
    "Zuban (Language) chunein:", ["Roman Urdu / Urdu", "English"]
)

if uploaded_file is not None:
  # Video ki basic details
  file_size_mb = uploaded_file.size / (1024 * 1024)
  file_details = {
      "FileName": uploaded_file.name,
      "FileType": uploaded_file.type,
      "FileSize": f"{file_size_mb:.2f} MB",
  }

  st.success("🎉 Video kamyabi ke sath upload ho gayi hai!")

  with st.expander("📁 Video ki Maloomat (Metadata) dekhein"):
    st.json(file_details)

  # Video ke naam se topic nikalna
  raw_name = uploaded_file.name.rsplit(".", 1)[0]
  clean_topic = raw_name.replace("_", " ").replace("-", " ")

  if st.button("Generate Professional SEO"):
    with st.spinner("Behtareen SEO content aur thumbnail ideas ban rahe hain..."):

      tag_topic = clean_topic.replace(" ", "")

      if platform == "YouTube":
        # Titles
        if language == "Roman Urdu / Urdu":
          titles_text = (
              f"1. {clean_topic} - Mukammal Video (2026)\n2. Is video mein"
              f" dekhein {clean_topic} ki haqeeqat!\n3. {clean_topic} ki"
              " behtareen tafseel"
          )
        else:
          titles_text = (
              f"1. Complete Guide to {clean_topic} (2026)\n2. Everything You"
              f" Need to Know About {clean_topic}\n3. Mastering {clean_topic}"
              " Step-by-Step"
          )

        st.subheader("📌 YouTube Titles (Copy below):")
        st.text_area("Titles", titles_text, height=100)
        st.caption(f"Characters count: {len(titles_text)}")

        # Thumbnail Ideas
        thumb_text = (
            f"🔥 SECRETS OF {clean_topic.upper()}!\n⚡ MUST WATCH (2026)"
        )
        st.subheader("🖼️ Thumbnail Text Ideas:")
        st.text_area("Thumbnail Text", thumb_text, height=70)

        # Description
        if language == "Roman Urdu / Urdu":
          desc_text = (
              f"Aapki upload ki gayi video (**{clean_topic}**) ke mutabiq yeh"
              " description hai. Is video mein humne tamam zaroori pehluon par"
              " baat ki hai. Video pasand aaye toh like aur channel ko subscribe"
              f" zaroor karein!\n\nFile Name: {uploaded_file.name}\nSize:"
              f" {file_details['FileSize']}\n\nTimestamps:\n0:00 - Intro\n1:30"
              " - Main Topic\n5:00 - Conclusion"
          )
        else:
          desc_text = (
              f"Welcome to this video about **{clean_topic}**. We cover all"
              f" essential details and insights.\n\nFile Name:"
              f" {uploaded_file.name}\nSize:"
              f" {file_details['FileSize']}\n\nTimestamps:\n0:00 -"
              " Introduction\n1:30 - Core Details\n5:00 - Summary"
          )

        st.subheader("📝 YouTube Description (Copy below):")
        st.text_area("Description", desc_text, height=150)
        st.caption(f"Characters count: {len(desc_text)}")

        # Tags
        tags_text = (
            f"{clean_topic}, {clean_topic} video, upload {clean_topic}, viral"
            f" {clean_topic}, youtube growth 2026, trending"
        )
        st.subheader("🏷️ YouTube Tags (Copy below):")
        st.text_area("Tags", tags_text, height=80)

      else:  # TikTok
        # TikTok Titles / Hooks
        if language == "Roman Urdu / Urdu":
          titles_text = (
              f"1. {clean_topic} ki yeh video miss mat karna! 🤫\n2. Amazing"
              f" moments from {clean_topic} 🚀\n3. {clean_topic} ka asal raaz ❌"
          )
        else:
          titles_text = (
              f"1. You won't believe this about {clean_topic}! 🤫\n2. Amazing"
              f" insights on {clean_topic} 🚀\n3. The truth about {clean_topic}"
              " ❌"
          )

        st.subheader("📌 TikTok Viral Titles / Hooks:")
        st.text_area("TikTok Titles", titles_text, height=100)

        # TikTok Caption
        if language == "Roman Urdu / Urdu":
          desc_text = (
              f"New video uploaded: {clean_topic}! Watch till the end and share"
              f" your thoughts in the comments. 🔥 File: {uploaded_file.name}"
          )
        else:
          desc_text = (
              f"New video uploaded: {clean_topic}! Watch till the end and share"
              f" your thoughts in the comments. 🔥 File: {uploaded_file.name}"
          )

        st.subheader("📝 TikTok Caption & Description:")
        st.text_area("TikTok Description", desc_text, height=100)

        # Hashtags
        tags_text = (
            f"#tiktok #viral #{tag_topic} #trending #foryoupage #foryou"
            f" #uploadvideo #viral{tag_topic}"
        )
        st.subheader("🏷️ TikTok Hashtags:")
        st.text_area("TikTok Hashtags", tags_text, height=80)
else:
  st.info(
      "👆 Pehle upar diye gaye button se apni video (MP4/MOV) select karke upload"
      " karein."
            )
            
