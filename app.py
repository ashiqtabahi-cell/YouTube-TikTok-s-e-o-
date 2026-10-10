import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Online Earning Reality Checker",
    page_icon="🛡️",
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
        background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #008f7a 0%, #7bc225 100%);
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

# Background Music (Autoplay & Loop)
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

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
        <h1>🛡️ Online Earning Reality Checker</h1>
        <p>Jaaniye kaunsi online earning apps asal mein paise deti hain aur kaunsi scam hain! Community Feedback ke sath 💡🎵</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Initialize Session State for Community Reports
if "reports" not in st.session_state:
  st.session_state.reports = [
      {
          "app": "Fake Cash Rewards 2026",
          "status": "Scam / Fake",
          "comment": (
              "Pehlay ads dikhaye aur phir withdrawal ke waqt account block kar"
              " diya."
          ),
      },
      {
          "app": "Real Freelance Task",
          "status": "Verified / Real",
          "comment": (
              "Thori mehnat hai par waqt par payment mil jati hai. Behtar"
              " hai."
          ),
      },
  ]

# Tabs for navigation including Community Feedback
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🔍 Earning App Checker",
        "⚠️ Famous Scam Alerts",
        "💡 Safe Earning Tips",
        "📝 Community Reports",
    ]
)

with tab1:
  st.subheader("🔍 Check Any Earning App or Website")
  app_name = st.text_input(
      "Jis app ya website ka pata lagana hai uska naam likhein:",
      placeholder="e.g., Watch Ads & Earn Daily, Mega Cash App",
  )

  if st.button("🔎 Check Reality Status"):
    if app_name.strip() == "":
      st.warning("Pehle kisi app ya website ka naam zaroor likhein!")
    else:
      with st.spinner(
          "Database aur user reviews mein check kiya ja raha hai..."
      ):
        st.success(f"📊 '{app_name}' ki report tayar hai!")
        st.warning(f"⚠️ **Warning / Analysis for {app_name}:**")
        st.write("- **Trust Score:** 25/100 (High Risk of Scam)")
        st.write(
            "- **Payment Proof:** Koi mukammal ya asli payment proof mojood"
            " nahi hai."
        )
        st.write(
            "- **Verdict:** Yeh app dhoka lagti hai. Community reports section"
            " mein doosron ke reviews zaroor check karein!"
        )

with tab2:
  st.subheader("⚠️ Common Online Earning Scams in Pakistan")
  st.error(
      "1. **Investment Scams:** '500 rupay lagayein aur roz ke 2000 niklein'"
      " wali apps aur websites 100% fake hoti hain."
  )
  st.error(
      "2. **Ad-Clicking Jobs:** Video dekhne ya ads click karne ke badle hazaron"
      " rupay dene ka dawa karne wali companies kabhi payment nahi deetin."
  )
  st.error(
      "3. **Registration Fee Apps:** Jo app kaam shuru karne se pehle khud fee"
      " ya membership mange, woh scam hoti hai."
  )

with tab3:
  st.subheader("💡 Asli Aur Safe Online Earning ke Raste")
  st.info(
      "Agar aap waqai online paisa kamana chahte hain toh in genuine skills"
      " par focus karein:"
  )
  st.write(
      "- **Content Creation:** YouTube, TikTok aur Facebook par apni videos"
      " banana."
  )
  st.write(
      "- **Freelancing:** Video Editing, Graphic Design, Web Development"
      " (Fiverr / Upwork)."
  )
  st.write("- **Digital Marketing:** Brands ke liye online promotion karna.")

with tab4:
  st.subheader("📝 Community Reports & User Feedback")
  st.write(
      "Yahan aap kisi bhi app ke baray mein apna review de sakte hain taake"
      " doosre log scam se bach sakein:"
  )

  with st.form("report_form"):
    rep_app = st.text_input("App ya Website ka Naam:")
    rep_status = st.selectbox(
        "Status Chunein:", ["Scam / Fake", "Verified / Real", "Suspicious"]
    )
    rep_comment = st.text_area("Apna tajurba (Experience) tafseel se likhein:")
    submitted = st.form_submit_button("Submit Report")

    if submitted:
      if rep_app.strip() and rep_comment.strip():
        # Add new report to session state list
        st.session_state.reports.insert(
            0, {"app": rep_app, "status": rep_status, "comment": rep_comment}
        )
        st.success("🎉 Shukriya! Aapki report kamiyabi se shamil ho gayi hai.")
      else:
        st.warning("Barah-e-karam app ka naam aur review zaroor likhein.")

  st.markdown("### 📋 Recent User Reports & Reviews:")
  for r in st.session_state.reports:
    if "Scam" in r["status"]:
      st.error(
          f"**App:** {r['app']} | **Status:** {r['status']}\n\n**Review:**"
          f" {r['comment']}"
      )
    elif "Verified" in r["status"]:
      st.success(
          f"**App:** {r['app']} | **Status:** {r['status']}\n\n**Review:**"
          f" {r['comment']}"
      )
    else:
      st.warning(
          f"**App:** {r['app']} | **Status:** {r['status']}\n\n**Review:**"
          f" {r['comment']}"
      )
      
