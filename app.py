import streamlit as st

# Page Configuration
st.set_page_config(page_title="Online Earning Reality Checker", page_icon="🛡️", layout="wide")

# Custom CSS for UI styling
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #1e3d59, #17b978);
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
    }
    .main-header h1 {
        font-size: 2.3rem;
        font-weight: bold;
    }
    </style>
    <div class="main-header">
        <h1>🛡️ Online Earning Reality Checker</h1>
        <p style="font-size: 1.1rem; margin-top: 5px;">Duniya ki 100+ Real aur Fake Apps & Websites ki sachai aur Dokhe dene ke tareeqay</p>
    </div>
""", unsafe_allow_html=True)

# Database with Scam Methods Included
database = {
    # --- FAKE / SCAM APPS & WEBSITES ---
    "5g share": {
        "status": "Fake ❌", 
        "cat": "Investment Scam", 
        "desc": "Pehle chota profit de kar bara deposit karwati hain.",
        "scam_method": "Yeh shuru mein thori raqam ka withdrawal de kar user ka bharosa jeettain hain. Phir jab user bari investment karta hai, toh account freeze kar dete hain ya website band karke bhaag jate hain."
    },
    "tron mining": {
        "status": "Fake ❌", 
        "cat": "Crypto Scam", 
        "desc": "Free cloud mining ka dhoka.",
        "scam_method": "Yeh kehte hain ke free mein mining ho rahi hai, lekin jab aap paise nikalne lagte hain toh kehte hain pehle 'Activation Fee' ya 'Gas Fee' jama karwao. Fee dene ke baad bhi kuch nahi milta."
    },
    "Tesla invest": {
        "status": "Fake ❌", 
        "cat": "Ponzi Scheme", 
        "desc": "Tesla ke naam par fake investment plan.",
        "scam_method": "Bari companies ka naam istemal karke fake ads chalate hain aur rozana 50% profit ka lalach de kar logon se raqam e-wallets ya crypto mein transfer karwa lete hain."
    },
    "oxford club": {
        "status": "Fake ❌", 
        "cat": "Investment Scam", 
        "desc": "Daily profit ka jhoot bol kar paisa doobati hai.",
        "scam_method": "WhatsApp aur Telegram groups ke zariye agents rakhte hain jo fake screenshot dikhate hain ke humne itna kama liya. Log unhe dekh kar invest kar dete hain aur wo block kar dete hain."
    },
    "big daddy game": {
        "status": "Fake ❌", 
        "cat": "Color Prediction / Gambling", 
        "desc": "Jua app jis mein 99% log haar jatay hain.",
        "scam_method": "Shuru mein user ko jeetne ka maza dete hain taake usaylat lag jaye. Phir achanak algorithm change karke sara balance zero karwa dete hain aur mazeed deposit ka kehte hain."
    },
    "daman games": {
        "status": "Fake ❌", 
        "cat": "Color Prediction", 
        "desc": "Aadi banane wali aur paisa doobane wali app.",
        "scam_method": "Fake prediction channels chalate hain jo kehte hain ke hamari trick se khelo ge toh kabhi nahi haro ge, jabke asal mein backend par sab controlled hota hai aur user haar jata hai."
    },
    "jazzcash loan scam apps": {
        "status": "Fake ❌", 
        "cat": "Loan App Fraud", 
        "desc": "Personal data blackmailing apps.",
        "scam_method": "Chota sa loan foran de dete hain lekin app download karte waqt mobile ki gallery, contacts aur messages ki access le lete hain. Phir thore se delay par contacts par call karke zaleel karte hain."
    },
    
    # --- REAL / TRUSTED APPS & WEBSITES ---
    "upwork": {
        "status": "Real ✅", 
        "cat": "Freelancing", 
        "desc": "Duniya ka sabse trusted freelancing platform.",
        "scam_method": "Yeh real hai, lekin yahan scammer fake jobs ke naam par bahar le ja kar (jaise Telegram par) task complete karwa ke paise nahi dete. Hamesha platform ke andar reh kar kaam karein."
    },
    "fiverr": {
        "status": "Real ✅", 
        "cat": "Freelancing", 
        "desc": "Skills ki base par kaam aur secure payment.",
        "scam_method": "Yeh 100% real hai. Fake log yahan direct bank transfer ya advance payment ka bol kar scam karne ki koshish karte hain, isliye hamesha Fiverr ki official payment method use karein."
    },
    "youtube": {
        "status": "Real ✅", 
        "cat": "Content Creation", 
        "desc": "Monetization ke zariye real earning source.",
        "scam_method": "YouTube khud real hai, lekin kuch fake log comments mein likhte hain ke 'Mujhe WhatsApp par contact karo, video dekhne ke paise milenge'. Yeh sab scammer hote hain."
    },
    "binance": {
        "status": "Real ✅", 
        "cat": "Crypto Exchange", 
        "desc": "Duniya ki sabse bari crypto exchange.",
        "scam_method": "Binance secure hai, lekin P2P trading mein kuch dhokaybaz fake payment screenshot bhej kar coin release karwa lete hain. Hamesha bank account mein paisa check karke coin release karein."
    }
}

# Search Bar Section
st.subheader("🔍 Kisi bhi App ya Website ki Sachai Check Karein")
query = st.text_input("Yahan naam likhein (e.g., Upwork, 5G Share, Big Daddy):")

if query:
    q_lower = query.strip().lower()
    found = False
    for name, data in database.items():
        if q_lower in name:
            found = True
            st.divider()
            if "Fake" in data["status"]:
                st.error(f"### Naam: {name.title()} — {data['status']}")
                st.write(f"**Category:** {data['cat']}")
                st.write(f"**Reality / Tafseel:** {data['desc']}")
                st.warning(f"⚠️ **Dokha Kaise Deti Hai? (Scam Method):** {data['scam_method']}")
            else:
                st.success(f"### Naam: {name.title()} — {data['status']}")
                st.write(f"**Category:** {data['cat']}")
                st.write(f"**Reality / Tafseel:** {data['desc']}")
                st.info(f"💡 **Mehfooz Rehne Ka Tareeqa:** {data['scam_method']}")
    
    if not found:
        st.warning("Yeh naam abhi direct list mein nahi hai. Neeche apna review add karein!")

# Quick Database View
st.divider()
st.subheader("📋 Quick List: Real vs Fake & Scam Methods")

tab1, tab2 = st.tabs(["❌ Fake Apps & Unke Dokhe", "✅ Real Platforms"])

with tab1:
    st.markdown("### Fake Platforms aur Unka Tarika-e-Wardaat")
    for name, data in database.items():
        if "Fake" in data["status"]:
            st.markdown(f"**{name.title()}** ({data['cat']})")
            st.write(f"- *Waja:* {data['desc']}")
            st.write(f"- *Dokha kaise deti hai:* {data['scam_method']}")
            st.markdown("---")

with tab2:
    st.markdown("### Real Platforms aur unki Hidayat")
    for name, data in database.items():
        if "Real" in data["status"]:
            st.markdown(f"**{name.title()}** ({data['cat']})")
            st.write(f"- *Tafseel:* {data['desc']}")
            st.write(f"- *Tips:* {data['scam_method']}")
            st.markdown("---")

# User Review & Comment Section
st.divider()
st.subheader("💬 User Reviews & Comments Shamil Karein")
with st.form("user_review"):
    u_name = st.text_input("Aapka Naam:")
    app_target = st.text_input("App ya Website ka Naam:")
    verdict = st.selectbox("Aapki Raye:", ["Real ✅", "Fake ❌"])
    user_comment = st.text_input("Unhon ne dokha kaise diya ya aapka tajurba kaisa raha?")
    btn = st.form_submit_button("Review Post Karein")
    
    if btn:
        if u_name and app_target and user_comment:
            st.success("Shukriya! Aapka review database mein shamil kar liya gaya hai.")
        else:
            st.warning("Barah-e-karam sabhi fields ko pur karein.")
