import streamlit as st

st.set_page_config(page_title="YouTube TikTok SEO Generator", layout="centered")

st.title("🚀 YouTube & TikTok SEO Generator")

topic = st.text_input("Apne video ka topic likhein:")
platform = st.selectbox("Platform chunein:", ["YouTube", "TikTok"])

if st.button("Generate karein"):
  if topic:
    st.success("Aapka SEO content tayar hai!")
    st.write(f"**Titles:** Best {topic} Guide, How to master {topic}")
    st.write(
        f"**Description:** Learn everything about {topic} on {platform}."
    )
    st.write(f"**Tags:** #{platform} #{topic.replace(' ', '')} #viral #trending")
  else:
    st.warning("Pehle topic likhein!")
      
