import streamlit as st
import streamlit.components.v1 as components

# --- Google Analytics Tracking Code ---
ga_code = """
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MWB5X5SBW9"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-MWB5X5SBW9');
</script>
"""
components.html(ga_code, height=0)

# --- App UI ---
st.markdown("## 🔍 Ultimate Real vs Fake Earning & Apps Checker")
st.write("Duniya aur internet ke tamam mashhoor Real aur Fake platforms ki mukammal database.")

query = st.text_input("🔍 Kisi bhi App ya Website ka naam likhein (e.g., Facebook, 5G Share, Upwork):")

st.markdown("---")

# --- Comprehensive Database of Fake Platforms ---
fake_database = {
    "5g share": {"downloads": "1M+ Downloads", "rating": "1.2 ⭐", "reason": "Ponzi scheme hai. Shuru mein chota profit de kar bara investment karwati hai aur bhaag jati hai."},
    "big daddy": {"downloads": "500K+ Downloads", "rating": "1.5 ⭐", "reason": "Color prediction aur gambling app hai. Algorithm shuru mein jeetne deta hai aur aakhir mein sab dooba deta hai."},
    "91 club": {"downloads": "800K+ Downloads", "rating": "1.4 ⭐", "reason": "Online gambling aur illegal betting app hai jo logon ka paisa loot leti hai."},
    "taskpay": {"downloads": "200K+ Downloads", "rating": "1.8 ⭐", "reason": "Task karwane ke baad withdrawal ke waqt fee ya tax maangti hai aur payment nahi deti."},
    "daily watch video": {"downloads": "5M+ Downloads", "rating": "2.0 ⭐", "reason": "Videos dekhne par dollars dene ka jhoota dawa karti hai aur aakhir mein account block kar deti hai."},
    "h5 5g": {"downloads": "300K+ Downloads", "rating": "1.3 ⭐", "reason": "Fake investment website jo daily profit ka lalach de kar scam karti hai."},
    "free bitcoin mining": {"downloads": "10M+ Downloads", "rating": "2.2 ⭐", "reason": "Free crypto mining ke naam par deposit ya speed-up fee maangti hai."},
    "pakistani ad clicking apps": {"downloads": "1M+ Downloads", "rating": "1.9 ⭐", "reason": "Registration fee ya membership fee le kar bhaag jati hain."}
}

# --- Comprehensive Database of Real Platforms ---
real_database = {
    "facebook": {"users": "3 Billion+ Users", "rating": "4.5 ⭐", "method": "Meta ka official social media network hai. Yeh earning nahi deta balki business promotion aur marketing ke liye 100% real hai."},
    "instagram": {"users": "2 Billion+ Users", "rating": "4.6 ⭐", "method": "Visual social media platform. Influencers sponsorships aur brand deals ke zariye earn karte hain."},
    "whatsapp": {"users": "2.5 Billion+ Users", "rating": "4.7 ⭐", "method": "Secure messaging app, communication ke liye 100% trusted hai."},
    "youtube": {"users": "2.5 Billion+ Users", "rating": "4.9 ⭐", "method": "Videos banayein, monetization on karein aur Google AdSense ke zariye direct bank account mein payout lein."},
    "upwork": {"users": "18M+ Users", "rating": "4.8 ⭐", "method": "World-class freelancing platform jahan skills (coding, writing, design) ke badle secure payment milti hai."},
    "fiverr": {"users": "4M+ Users", "rating": "4.7 ⭐", "method": "Gigs banayein, international clients ka kaam karein aur direct bank/Payoneer mein paise receive karein."},
    "google": {"users": "Billions of Users", "rating": "4.9 ⭐", "method": "Duniya ka sabse bara search engine aur tech giant jo 100% trusted hai."},
    "daraz": {"users": "50M+ Downloads", "rating": "4.3 ⭐", "method": "E-commerce marketplace (Pakistan/South Asia), online shopping aur selling ke liye real platform hai."},
    "amazon": {"users": "Billions of Users", "rating": "4.8 ⭐", "method": "Global e-commerce aur FBA/KDP ke zariye e-arning ka sabse bara zariya."},
    "netflix": {"users": "260M+ Users", "rating": "4.5 ⭐", "method": "Legal streaming platform (Paid subscription, no fake earning promises)."}
}

# --- Search & Detection Logic ---
if query:
    q_clean = query.lower().strip()
    found = False
    
    # Check in Fake Database
    for key, data in fake_database.items():
        if key in q_clean:
            st.error(f"⚠️ **{query.capitalize()}** aik **100% Fake / Scam** platform hai!")
            st.markdown(f"- **Downloads / Popularity:** {data['downloads']}")
            st.markdown(f"- **Play Store Rating:** {data['rating']}")
            st.markdown(f"- **Scam Ki Waja:** {data['reason']}")
            found = True
            break
            
    # Check in Real Database
    if not found:
        for key, data in real_database.items():
            if key in q_clean:
                st.success(f"✔️ **{query.capitalize()}** aik **100% Real aur Trusted** platform hai!")
                st.markdown(f"- **Users / Scale:** {data['users']}")
                st.markdown(f"- **Rating:** {data['rating']}")
                st.markdown(f"- **Earning / Kaam Ka Tareeqa:** {data['method']}")
                found = True
                break
                
    # Fallback Smart Check for unlisted names
    if not found:
        # General safety check keywords
        if any(w in q_clean for w in ["invest", "fee", "deposit", "prediction", "task", "bonus", "shart"]):
            st.error(f"⚠️ **{query}** ke baray mein ahtiyat karein! Aisi apps jo pehle investment ya fee mangti hain, woh **100% Scam** hoti hain.")
        else:
            st.info(f"🔍 **{query}** hamari direct list mein nahi hai, lekin agar yeh app kaam karne ke badlay pehle **Investment, Deposit ya Advance Tax** maange toh yeh 100% Fake hai. Agar yeh aam social media ya utility app hai toh safe ho sakti hai.")
