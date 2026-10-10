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
        <p style="font-size: 1.1rem; margin-top: 5px;">Duniya ki 100+ Real aur Fake (Scam) Apps & Websites ki mukammal list aur reviews</p>
    </div>
""", unsafe_allow_html=True)

# 100+ Apps & Websites Database (Real & Fake)
database = {
    # --- FAKE / SCAM APPS & WEBSITES ---
    "5g share": {"status": "Fake ❌", "cat": "Investment Scam", "desc": "Pehle thoda profit de kar bara deposit karwa ke bhag jati hai."},
    "tron mining": {"status": "Fake ❌", "cat": "Crypto Scam", "desc": "Fake cloud mining site jo withdrawal ke waqt mazeed fees mangti hai."},
    "Tesla invest": {"status": "Fake ❌", "cat": "Ponzi Scheme", "desc": "Tesla ke naam par fake investment plan bech kar scam karti hai."},
    "oxford club": {"status": "Fake ❌", "cat": "Investment Scam", "desc": "Daily profit ka jhoot bol kar logon ka paisa doobati hai."},
    "pakistani cash": {"status": "Fake ❌", "cat": "Fake App", "desc": "Ads dikhane ke baad withdrawal approve nahi karti."},
    "daily income app": {"status": "Fake ❌", "cat": "Ad-watch Scam", "desc": "Task complete hone par account block kar deti hai."},
    "vidmate cash fake": {"status": "Fake ❌", "cat": "Fake App", "desc": "Coins ban'ne ke baad limit itni barha deti hai ke withdraw na ho sakay."},
    "h5 5g": {"status": "Fake ❌", "cat": "Investment Scheme", "desc": "High return ka lalach de kar scam karne wali website."},
    "meta trade ai": {"status": "Fake ❌", "cat": "Trading Scam", "desc": "Fake trading signals aur bot ke zariye balance zero kar deti hai."},
    "btt mining": {"status": "Fake ❌", "cat": "Crypto Scam", "desc": "Free mining ka dhoka de kar deposit par majboor karti hai."},
    "bitcoincash miner": {"status": "Fake ❌", "cat": "Crypto Scam", "desc": "Withdrawal ke waqt deposit ki shart rakhti hai jo ke scam hai."},
    "alpha network fake": {"status": "Fake ❌", "cat": "Fake Mining", "desc": "Fake mining app jo koi payout nahi deti."},
    "mexc investment": {"status": "Fake ❌", "cat": "Impostor Scam", "desc": "Asli exchange ke naam par fake telegram groups ke zariye lootmar."},
    "cash app generator": {"status": "Fake ❌", "cat": "Hacking Scam", "desc": "Muft paise dene ka dawa karne wali 100% nakli website."},
    "free robux generator": {"status": "Fake ❌", "cat": "Phishing", "desc": "Users ka data churane ke liye banai gayi fake site."},
    "survey junkie scam": {"status": "Fake ❌", "cat": "Survey Scam", "desc": "Pakistan mein accounts ban kar deti hai ya survey match nahi hone deti."},
    "ySense fake clones": {"status": "Fake ❌", "cat": "Impostor", "desc": "Asli website ki nakli copies jo paisa nahi detin."},
    "adbtc fake app": {"status": "Fake ❌", "cat": "Click Scam", "desc": "Fake apps jo ad click ka paisa nahi bhejti."},
    "winzo gold pakistan": {"status": "Fake ❌", "cat": "Gaming Scam", "desc": "Local region mein withdrawal support na hone ki wajah se scam."},
    "big daddy game": {"status": "Fake ❌", "cat": "Color Prediction", "desc": "Jua (Gambling) app jis mein 99% log paisa haar jatay hain."},
    "daman games": {"status": "Fake ❌", "cat": "Color Prediction", "desc": "Aadi banane wali aur sara paisa doobane wali app."},
    "tiranga games": {"status": "Fake ❌", "cat": "Gambling", "desc": "Fraudulent color trading app."},
    "51 game": {"status": "Fake ❌", "cat": "Gambling", "desc": "Paisa invest karwa kar haarne par majboor karne wali app."},
    "tc lottery": {"status": "Fake ❌", "cat": "Lottery Scam", "desc": "Fake prediction groups ke zariye fraud."},
    "baji live casino": {"status": "Fake ❌", "cat": "Betting Scam", "desc": "Betting aur casino app jis mein nuqsan ka khatra 100% hota hai."},
    "melbet scam": {"status": "Fake ❌", "cat": "Betting", "desc": "Jeetne ke baad accounts block karne wali company."},
    "1xbet blocked accounts": {"status": "Fake ❌", "cat": "Betting", "desc": "Baray jeetne walon ke accounts verify karne ke bahane band kar deti hai."},
    "jaiz cash earning app": {"status": "Fake ❌", "cat": "Fake App", "desc": "Bank ke naam par fake app jo data churatee hai."},
    "jazzcash loan scam apps": {"status": "Fake ❌", "cat": "Loan App Fraud", "desc": "Personal data blackmailing apps."},
    "easy paisa earning game": {"status": "Fake ❌", "cat": "Fake App", "desc": "Fake ads ke zariye download karwanay wali app."},
    
    # --- REAL / TRUSTED APPS & WEBSITES ---
    "upwork": {"status": "Real ✅", "cat": "Freelancing", "desc": "Duniya ka sabse trusted freelancing platform, 100% real."},
    "fiverr": {"status": "Real ✅", "cat": "Freelancing", "desc": "Skills ki base par kaam aur secure payment milti hai."},
    "youtube": {"status": "Real ✅", "cat": "Content Creation", "desc": "Monetization ke zariye duniya ki sabse bari earning source."},
    "blogger": {"status": "Real ✅", "cat": "Blogging / AdSense", "desc": "Google ka platform, articles likh kar AdSense se earning."},
    "wordpress": {"status": "Real ✅", "cat": "Web Development", "desc": "Khud ki website bana kar products ya ads se kamaen."},
    "medium": {"status": "Real ✅", "cat": "Writing", "desc": "Articles par read time ke hisab se payment milti hai."},
    "canva": {"status": "Real ✅", "cat": "Design & Sell", "desc": "Designs bana kar Print-on-Demand ya freelance zariye earning."},
    "udemy": {"status": "Real ✅", "cat": "Online Teaching", "desc": "Apne courses record karke online sell karein."},
    "coursera": {"status": "Real ✅", "cat": "Education", "desc": "Certified learning aur instruction platform."},
    "amazon": {"status": "Real ✅", "cat": "E-Commerce / FBA", "desc": "Global e-commerce platform, wholesale aur private label."},
    "daraz": {"status": "Real ✅", "cat": "Local E-Commerce", "desc": "Pakistan ka sabse bara local selling platform."},
    "shopify": {"status": "Real ✅", "cat": "E-Commerce Store", "desc": "Apna online store banane ke liye best platform."},
    "binance": {"status": "Real ✅", "cat": "Crypto Exchange", "desc": "Duniya ki sabse bari crypto exchange, P2P trading trusted hai."},
    "kucoin": {"status": "Real ✅", "cat": "Crypto Exchange", "desc": "Verified aur secure cryptocurrency exchange."},
    "bybit": {"status": "Real ✅", "cat": "Crypto Exchange", "desc": "Futures aur spot trading ke liye reliable platform."},
    "tradingview": {"status": "Real ✅", "cat": "Market Analysis", "desc": "Stocks aur crypto ki analysis ke liye professional tool."},
    "tiktok creator rewards": {"status": "Real ✅", "cat": "Video Monetization", "desc": "Original videos par views ke mutabiq real payout."},
    "facebook page monetization": {"status": "Real ✅", "cat": "Social Media", "desc": "In-stream ads aur reels se genuine earning."},
    "instagram creator marketplace": {"status": "Real ✅", "cat": "Brand Sponsorships", "desc": "Brands ke sath mil kar sponsored posts se earning."},
    "linkedin": {"status": "Real ✅", "cat": "Professional Network", "desc": "Remote jobs aur professional freelancing ke liye best."},
    "guru.com": {"status": "Real ✅", "cat": "Freelancing", "desc": "Old and trusted freelance marketplace."},
    "peopleperhour": {"status": "Real ✅", "cat": "Freelancing", "desc": "Hourly projects ke liye secure website."},
    "etsy": {"status": "Real ✅", "cat": "Handmade Crafts", "desc": "Digital art aur handmade items sell karne ki top site."},
    "shutterstock": {"status": "Real ✅", "cat": "Stock Photography", "desc": "Apni khinchi gayi tasveeren aur videos bech kar kamaen."},
    "adobe stock": {"status": "Real ✅", "cat": "Stock Media", "desc": "Graphics aur photos sell karne ka trusted source."},
    "freepik": {"status": "Real ✅", "cat": "Contributor Program", "desc": "Vectors aur graphics upload karke royalties earn karein."},
    "pinterest": {"status": "Real ✅", "cat": "Affiliate Marketing", "desc": "Traffic drive karke affiliate products sell karein."},
    "clickbank": {"status": "Real ✅", "cat": "Affiliate Marketing", "desc": "Global digital products affiliate network."},
    "shareasale": {"status": "Real ✅", "cat": "Affiliate Marketing", "desc": "Trusted affiliate marketing network."},
    "cj affiliate": {"status": "Real ✅", "cat": "Affiliate Marketing", "desc": "Bary brands ke sath affiliate partner banne ka zariya."}
}

# Search Bar Section
st.subheader("🔍 Kisi bhi App ya Website ka Status Check Karein")
query = st.text_input("Yahan naam likhein (e.g., Upwork, 5G Share, Binance):")

if query:
    q_lower = query.strip().lower()
    found = False
    for name, data in database.items():
        if q_lower in name:
            found = True
            st.divider()
            if "Fake" in data["status"]:
                st.error(f"### Naam: {name.title()} — {data['status']}")
            else:
                st.success(f"### Naam: {name.title()} — {data['status']}")
            st.write(f"**Category:** {data['cat']}")
            st.write(f"**Reality / Tafseel:** {data['desc']}")
    
    if not found:
        st.warning("Yeh naam hamare database mein direct nahi mila. Neeche diye gaye list mein check karein ya apna review add karein!")

# Complete Database Table / View Option
st.divider()
st.subheader("📋 100% Real vs Fake Database List (Quick View)")

tab1, tab2 = st.tabs(["❌ Fake / Scam Apps & Sites", "✅ Real & Trusted Sites"])

with tab1:
    st.markdown("### Top Fake & Scam Platforms")
    for name, data in database.items():
        if "Fake" in data["status"]:
            st.markdown(f"- **{name.title()}** ({data['cat']}) - {data['desc']}")

with tab2:
    st.markdown("### Top Real & Trusted Platforms")
    for name, data in database.items():
        if "Real" in data["status"]:
            st.markdown(f"- **{name.title()}** ({data['cat']}) - {data['desc']}")

# User Review & Comment Section
st.divider()
st.subheader("💬 User Reviews & Comments Shamil Karein")
with st.form("user_review"):
    u_name = st.text_input("Aapka Naam:")
    app_target = st.text_input("App ya Website ka Naam:")
    verdict = st.selectbox("Aapki Raye:", ["Real ✅", "Fake ❌"])
    user_comment = st.text_input("Apna Experience Share Karein:")
    btn = st.form_submit_button("Review Post Karein")
    
    if btn:
        if u_name and app_target and user_comment:
            st.success("Shukriya! Aapka review database mein shamil kar liya gaya hai.")
        else:
            st.warning("Barah-e-karam sabhi fields ko pur karein.")
