import streamlit as st

# Page Configuration
st.set_page_config(page_title="Online Earning Reality Checker", page_icon="🛡️", layout="centered")

# Custom CSS for styling the header banner
st.markdown("""
    <style>
    .main-header {
        background-color: #1e3d59;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 20px;
    }
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: bold;
    }
    </style>
    <div class="main-header">
        <h1>🛡️ Online Earning Reality Checker</h1>
        <p style="font-size: 1.2rem;">Asli aur Nakli (Scam) Earning Apps ka Pata Lagayein</p>
    </div>
""", unsafe_allow_html=True)

# Search Section
st.subheader("🔍 Website ya App Search Karein")
search_query = st.text_input("App ya website ka naam likhein (jaise: appname.com):")

# Sample Data base for Real/Fake apps
db = {
    "fakeapp": {"status": "Fake ❌", "desc": "Yeh app withdrawal nahi deti aur logo ko bewakoof banati hai."},
    "realapp": {"status": "Real ✅", "desc": "Yeh platform trusted hai aur time par payment deta hai."}
}

if search_query:
    key = search_query.strip().lower()
    found = False
    for k, v in db.items():
        if k in key:
            found = True
            if "Fake" in v["status"]:
                st.error(f"Status: {v['status']}")
            else:
                st.success(f"Status: {v['status']}")
            st.write(f"**Details:** {v['desc']}")
    
    if not found:
        st.warning("Yeh app abhi database mein nahi hai. Neeche apna review zaroor dein!")

# Comments and Reviews Section
st.divider()
st.subheader("💬 User Reviews & Comments")

with st.form("review_form"):
    u_name = st.text_input("Aapka Naam:")
    app_name = st.text_input("App/Website ka Naam:")
    review_status = st.selectbox("Aapki Raye:", ["Real ✅", "Fake ❌"])
    review_text = st.text_area("Apna tajurba share karein:")
    submit = st.form_submit_button("Review Submit Karein")

    if submit:
        if u_name and app_name and review_text:
            st.success("Shukriya! Aapka review add ho gaya hai.")
        else:
            st.warning("Barah-e-karam sabhi boxes ko fill karein.")
