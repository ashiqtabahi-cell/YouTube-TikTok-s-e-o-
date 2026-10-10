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

# --- App Styling & Header ---
st.markdown("### 🔍 Kisi bhi App ya Website ki Sachai Check Karein")
st.write("Yahan aap jaan sakte hain ke kaunsa platform asli hai aur kaunsa scam ya dhokha!")

# Search input
query = st.text_input("Yahan kisi app ya website ka naam likhein (e.g., Upwork, 5G Share, Big Daddy):")

st.markdown("---")
st.markdown("### 📋 Quick List: Real vs Fake & Scam Methods")

# Tabs for Fake vs Real platforms
tab1, tab2 = st.tabs(["❌ 100% Fake & Scam Apps", "✔️ 100% Real Earning Platforms"])

with tab1:
    st.markdown("#### 🚨 Fake Platforms aur Unka Tarika-e-Wardaat (Q Scam Hain?)")
    
    st.markdown("##### 1. 5G Share / Investment Schemes")
    st.markdown("- **Kyun Scam hai?** Yeh ponzi schemes hoti hain jo shuru mein thora profit de kar bara investment karwati hain aur phir achanak website band karke bhaag jati hain.")
    
    st.markdown("##### 2. Fake Task-Based & Ad-Clicking Apps")
    st.markdown("- **Kyun Scam hai?** Yeh ads dekhne ya video like karne ke 5 ya 10 dollar dene ka dawa karti hain, lekin jab aap paise nikalne (withdraw) lagte hain toh pehle 'Advance Fee' ya 'Tax' ke naam par mazeed paise maangti hain. Asal mein yeh sirf dhokha hota hai.")

with tab2:
    st.markdown("#### ✅ Real Earning Platforms (Kaise Paise Dete Hain?)")
    
    st.markdown("##### 1. Upwork & Fiverr (Freelancing)")
    st.markdown("- **Kaise Paise Dete Hain?** Yeh real platforms hain jahan aap apni skills (jaise Web Development, Content Writing, Designing) ki base par clients ka kaam karte hain. Kaam mukammal hone ke baad platform secure tareeqay se aapke bank account ya Payoneer mein paise bhejta hai.")
    
    st.markdown("##### 2. YouTube & Google AdSense (Content Creation)")
    st.markdown("- **Kaise Paise Dete Hain?** Yeh mehnat aur views par base karte hain. Jab aap apne channel ya website par original content banate hain aur log usay dekhte hain, toh ads ke zariye Google aapko direct bank account mein payout deta hai.")

# Search result logic
if query:
    q_lower = query.lower()
    if "5g" in q_lower or "big daddy" in q_lower or "fake" in q_lower:
        st.error(f"⚠️ **{query}** aik **Fake/Scam** platform lagta hai! Ismein apna paisa invest karne ya personal info dene se bachein.")
    elif "upwork" in q_lower or "fiverr" in q_lower or "youtube" in q_lower:
        st.success(f"✔️ **{query}** aik **100% Real** platform hai jahan mehnat aur skills ki base par earning hoti hai.")
    else:
        st.info(f"🔍 Aapne '{query}' search kiya hai. Mazeed research karein ke yeh platform kahin advance fee ya investment toh nahi maangta.")
  
