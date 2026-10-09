import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="AI Video SEO Pro", page_icon="🚀", layout="centered")

# App Header
st.title("🚀 AI YouTube & TikTok SEO Generator")
st.write("Apna video topic ya keyword niche likhein aur ek click mein viral SEO hasil karein!")

# Dynamic API Key Input Box on App Screen
st.sidebar.header("🔑 Settings")
user_api_key = st.sidebar.text_input("Apni Gemini API Key Yahan Enter Karein:", type="password")

if not user_api_key:
    st.info("💡 Left sidebar mein apni Gemini API key enter karein taake app active ho sakay.")
else:
    try:
        genai.configure(api_key=user_api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # User Input Form
        with st.form("seo_form"):
            video_topic = st.text_input("Video ka Topic ya Keyword likhein (e.g., How to lose weight at home):")
            platform = st.selectbox("Platform Select Karein:", ["YouTube", "TikTok", "Dono (YouTube + TikTok)"])
            submit_btn = st.form_submit_button("Generate SEO 🎯")

        if submit_btn and video_topic:
            with st.spinner("AI SEO generate ho raha hai... Thoda sabr karein! ⏳"):
                try:
                    # Prompt design for AI
                    prompt = f"""
                    Act as a professional Video SEO Expert. Generate SEO data for the topic: '{video_topic}' for platform: '{platform}'.
                    Provide the output in the following clean format:
                    
                    1. Catchy Titles (3 options)
                    2. Optimized Description (with placeholders for links and relevant keywords)
                    3. High-Ranking Tags (comma-separated for YouTube)
                    4. Trending Hashtags (for TikTok/Shorts)
                    5. 3-Second Hook Idea (to grab viewer attention)
                    """
                    
                    response = model.generate_content(prompt)
                    
                    # Display Results
                    st.success("✅ SEO Successfully Generated!")
                    st.markdown("### Aapka SEO Result:")
                    st.write(response.text)
                    
                except Exception as e:
                    st.error(f"API call mein error aa gaya: {e}")
        elif submit_btn:
            st.error("Pehle please koi topic likhein!")
            
    except Exception as e:
        st.error(f"Configuration error: {e}")
        
        
