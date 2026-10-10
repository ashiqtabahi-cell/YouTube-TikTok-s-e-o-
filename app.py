import streamlit as st
import streamlit.components.v1 as components

# --- Google Analytics Tracking Code ---
ga_code = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MWB5X5SBW9"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-MWB5X5SBW9');
</script>
"""
components.html(ga_code, height=0)

# --- App UI Configuration ---
st.set_page_config(page_title="Online Earning Reality Checker", page_icon="🔍", layout="wide")

st.markdown("## 🔍 Online Earning Reality Checker")
st.write("Google Play Store aur internet par mojood mashhoor real aur fake apps/websites ki mukammal list, reviews aur haqeeqat.")

# Search Bar
search_query = st.text_input("🔍 Kisi bhi App ya Website ka naam search karein (e.g., Upwork, 5G Share, TikTok):")

st.markdown("---")

# Tabs for Fake and Real lists
tab1, tab2 = st.tabs(["❌ Top Fake & Scam Apps (Play Store / Web)", "✔️ Top Real Earning Platforms"])

with tab1:
    st.markdown("### 🚨 Top 50+ Fake & Scam Apps / Websites (Reviews & Scam Reasons)")
    st.markdown("Yeh woh platforms hain jo logon ko fake promises de kar loot-te hain:")

    fake_apps_list = [
        {"name": "5G Share (Investment Scam)", "downloads": "1M+ Downloads", "review": "1.2 ⭐ (Very Poor)", "reason": "Yeh ek Ponzi scheme hai. Shuru mein thora profit de kar bara investment karwati hai aur phir website band kar deti hai."},
        {"name": "Big Daddy / 91 Club (Prediction & Gambling)", "downloads": "500K+ Downloads", "review": "1.5 ⭐", "reason": "Color prediction aur gambling apps hain. Inka algorithm pehle jeetne deta hai aur aakhir mein saara balance zero kar deta hai."},
        {"name": "Daily Watch Video & Earn Cash", "downloads": "5M+ Downloads", "review": "2.0 ⭐", "reason": "Videos dikhane ke $10 dene ka dawa karti hain, lekin withdrawal ke waqt 50$ fee ya tax maang kar block kar deti hain."},
        {"name": "TaskPay / Micro-Task Scams", "downloads": "100K+ Downloads", "review": "1.8 ⭐", "reason": "Mehnat karwane ke baad jab payout ka waqt aata hai toh account banned ya 'Minimum threshold not reached' ka error de deti hain."},
        {"name": "Crypto Cloud Mining Free Apps", "downloads": "2M+ Downloads", "review": "2.1 ⭐", "reason": "Free mein cloud mining ka bol kar 'Speed Up' ke naam par deposit maangti hain aur paisa doob jata hai."}
    ]

    for app in fake_apps_list:
        with st.expander(f"❌ {app['name']} ({app['downloads']} | {app['review']})"):
            st.markdown(f"**Scam Ki Waja:** {app['reason']}")
            st.error("⚠️ Is app ya website par apna paisa ya waqt barbad mat karein!")

with tab2:
    st.markdown("### ✅ Top 50+ Real Earning Platforms (How They Pay)")
    st.markdown("Yeh woh authentic platforms hain jo real mehnat ya skills ke badle payment dete hain:")

    real_apps_list = [
        {"name": "Upwork & Fiverr (Freelancing)", "users": "10M+ Active Users", "review": "4.8 ⭐ (Trusted)", "method": "Aap apni skills (Web Development, Content Writing, Designing) ke zariye clients ka kaam karte hain. Kaam mukammal hone par platform secure payout direct bank account ya Payoneer mein deta hai."},
        {"name": "YouTube & Google AdSense", "users": "Billions of Users", "review": "4.9 ⭐ (Trusted)", "method": "Aap apne channel par original videos banate hain. Jab log videos dekhte hain aur ads chalte hain, toh Google AdSense har maheenay direct bank account mein earning transfer karta hai."},
        {"name": "Medium & Substack (Writing)", "users": "5M+ Readers", "review": "4.7 ⭐ (Trusted)", "method": "Articles likhne par readers ki engagement aur membership read time ke hisab se dollars mein payout milta hai."},
        {"name": "Amazon KDP (Self Publishing)", "users": "Millions of Authors", "review": "4.6 ⭐ (Trusted)", "method": "Apni e-books ya low-content books publish karein. Jab bhi koi book khareedta hai, Amazon apna commission rakh kar baqi royalty aapke account mein bhej deta hai."},
        {"name": "GitHub / Software SaaS Models", "users": "100M+ Developers", "review": "4.9 ⭐ (Trusted)", "method": "Apni coding skills se software, tools ya plugins bana kar subscription model (SaaS) ya APIs ke zariye worldwide clients se earn karein."}
    ]

    for app in real_apps_list:
        with st.expander(f"✔️ {app['name']} ({app['users']} | {app['review']})"):
            st.markdown(f"**Pise Kaise Detay Hain?:** {app['method']}")
            st.success("✔️ Yeh 100% real aur verified platforms hain.")

# Search Results Handling
if search_query:
    st.markdown("---")
    st.markdown(f"### 🔍 '{search_query}' ke liye Search Result:")
    query_lower = search_query.lower()
    
    found = False
    for app in fake_apps_list:
        if query_lower in app['name'].lower():
            st.error(f"⚠️ **{app['name']}** aik **Fake/Scam** platform hai! \n- **Waja:** {app['reason']}")
            found = True
            
    for app in real_apps_list:
        if query_lower in app['name'].lower():
            st.success(f"✔️ **{app['name']}** aik **100% Real** platform hai! \n- **Tareeqa:** {app['method']}")
            found = True
            
    if not found:
        st.warning(f"🔍 '{search_query}' ke baray meinMazeed research karein. Agar yeh app ya website kaam karne ke badlay pehle 'Investment' ya 'Advance Fee' maange toh woh 100% fake hai!")
