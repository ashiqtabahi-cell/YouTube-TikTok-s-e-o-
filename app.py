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
        <p>Asli aur Nakli (Scam) Earning Apps ka Mukammal Database! 💡🎵</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Initialize Session State for Community Reports
if "reports" not in st.session_state:
  st.session_state.reports = [
      {
          "app": "Tesla Power (Fake Investment)",
          "status": "Scam / Fake",
          "comment": "Logon se paise invest karwa kar website band kar ke bhaag gaye.",
      },
      {
          "app": "Fiverr",
          "status": "Verified / Real",
          "comment": "Dunya ka behtareen freelancing platform hai.",
      },
  ]

# Tabs for navigation
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🔍 App & Website Database",
        "⚠️ Famous Scam Alerts",
        "💡 Safe Earning Tips",
        "📝 Community Reports",
    ]
)

with tab1:
  st.subheader("🔍 Earning App & Website Checker")
  st.write("Kisi bhi app ya website ka naam likh kar check karein ke woh Real hai ya Scam:")
  
  app_name = st.text_input(
      "App ya Website ka naam likhein:",
      placeholder="e.g., YouTube, Fiverr, Tesla Power, Fake Cash App",
  )

  if st.button("🔎 Check Reality Status"):
    if app_name.strip() == "":
      st.warning("Pehle kisi app ya website ka naam zaroor likhein!")
    else:
      clean_name = app_name.strip().lower()
      
      # Database of Trusted Platforms
      real_database = {
          "youtube": "Dunya ka sab se bara video platform jo monetization ke zariye asli income deta hai.",
          "fiverr": "100% trusted global freelancing marketplace jahan skills par payment milti hai.",
          "upwork": "Professional freelancers ke liye dunya ka sab se secure platform.",
          "facebook": "Meta ka trusted platform jo creators ko ads aur monetization se earn karwata hai.",
          "instagram": "Brand promotion aur creator monetization ke liye authentic app.",
          "tiktok": "Creator rewards aur brand deals ke liye verified platform.",
          "daraz": "Pakistan ka sab se bara e-commerce store (online shopping & selling).",
          "canva": "Design aur content creation ke liye trusted tool.",
          "freelancer": "Purana aur authentic freelance marketplace."
      }
      
      # Database of Known Scams
      scam_database = {
          "tesla power": "Ponzi scheme thi jo investment ke naam par logon ko loot kar bhaag gayi.",
          "fake cash rewards": "Ad-watching scam jo withdrawal ke waqt account block kar deta hai.",
          "daily cash app": "Jhootha dawa karne wali app jo kabhi paise nahi deti.",
          "ad clicking job": "100% fake task scam, mehnat karwa kar payment nahi dete.",
          "500 invest daily": "Classic investment fraud jo shuru mein thora profit de kar bara scam karta hai."
      }
      
      with st.spinner("Database mein check kiya ja raha hai..."):
        st.success(f"📊 '{app_name}' ki report tayar hai!")
        
        # Check in real database
        found_real = False
        for key in real_database:
          if key in clean_name:
            found_real = True
            st.success(f"✅ **Verified & Trusted Platform ({key.title()})**")
            st.write(f"- **Trust Score:** 95/100 (Safe & Legitimate)")
            st.write(f"- **Details:** {real_database[key]}")
            st.write("- **Verdict:** Yeh aik asli platform hai. Aap is par yaqeen ke sath kaam kar sakte hain.")
            break
            
        # Check in scam database if not found in real
        if not found_real:
          found_scam = False
          for key in scam_database:
            if key in clean_name:
              found_scam = True
              st.error(f"⚠️ **High Risk Scam Alert ({key.title()})**")
              st.write(f"- **Trust Score:** 5/100 (100% Fraud)")
              st.write(f"- **Details:** {scam_database[key]}")
              st.write("- **Verdict:** Yeh aik dhoka hai! Isme apna waqt ya paisa bilkul zaya mat karein.")
              break
              
          if not found_scam:
            st.warning(f"⚠️ **Warning / Unverified App ({app_name})**")
            st.write("- **Trust Score:** 30/100 (Suspicious)")
            st.write("- **Payment Proof:** Is app ka koi mukammal ya qabil-e-etbaar payment proof mojood nahi hai.")
            st.write("- **Verdict:** Yeh app shaq ki bina par mehfooz nahi lagti. Isme investment karne se pehle Community Reports zaroor check karein!")

with tab2:
  st.subheader("⚠️ Famous Online Earning Scams List")
  st.write("In categories aur style ki apps se hamesha door rahein:")
  st.error("1. **Investment & Deposit Schemes:** Jo apps pehle 500 ya 1000 rupay mangwayein aur rozana profit ka jhootha dawa karein.")
  st.error("2. **Ad-Watching / Ad-Clicking Apps:** Video dekhne ya ads click karne ke badle hazaron rupay dene wali fake apps.")
  st.error("3. **Task Completion Scams:** Telegram ya WhatsApp par tasks de kar pehle fee ya security deposit mangne wale log.")

with tab3:
  st.subheader("💡 Asli Aur Safe Online Earning ke Raste")
  st.info("Agar aap waqai internet se paisa kamana chahte hain, toh in asli tareeqon ko seekhein:")
  st.write("- **Content Creation:** YouTube aur Facebook par apni videos ya vlogs banana.")
  st.write("- **Freelancing:** Video Editing, Graphic Design, Web Development (Fiverr aur Upwork par).")
  st.write("- **Digital Marketing:** Social media par brands ki marketing karna.")

with tab4:
  st.subheader("📝 Community Reports & User Feedback")
  st.write("Yahan aap kisi bhi app ke baray mein apna review de sakte hain:")

  with st.form("report_form"):
    rep_app = st.text_input("App ya Website ka Naam:")
    rep_status = st.selectbox("Status Chunein:", ["Scam / Fake", "Verified / Real", "Suspicious"])
    rep_comment = st.text_area("Apna tajurba (Experience) tafseel se likhein:")
    submitted = st.form_submit_button("Submit Report")

    if submitted:
      if rep_app.strip() and rep_comment.strip():
        st.session_state.reports.insert(0, {"app": rep_app, "status": rep_status, "comment": rep_comment})
        st.success("🎉 Shukriya! Aapki report kamiyabi se shamil ho gayi hai.")
      else:
        st.warning("Barah-e-karam app ka naam aur review zaroor likhein.")

  st.markdown("### 📋 Recent User Reports & Reviews:")
  for r in st.session_state.reports:
    if "Scam" in r["status"]:
      st.error(f"**App:** {r['app']} | **Status:** {r['status']}\n\n**Review:** {r['comment']}")
    elif "Verified" in r["status"]:
      st.success(f"**App:** {r['app']} | **Status:** {r['status']}\n\n**Review:** {r['comment']}")
    else:
      st.warning(f"**App:** {r['app']} | **Status:** {r['status']}\n\n**Review:** {r['comment']}")
      
