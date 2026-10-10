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


# --- Aapki App ka Main Content ---
st.markdown("### 🔍 Kisi bhi App ya Website ki Sachai Check Karein")

# User input field
query = st.text_input("Yahan naam likhein (e.g., Upwork, 5G Share, Big Daddy):")

st.markdown("---")
st.markdown("### 📋 Quick List: Real vs Fake & Scam Methods")

# Tabs for Fake vs Real platforms
tab1, tab2 = st.tabs(["❌ Fake Apps & Unke Dokhe", "✔️ Real Platforms"])

with tab1:
    st.markdown("#### Fake Platforms aur Unka Tarika-e-Wardaat")
    st.markdown("- **5G Share (Investment Scam):** Yeh ek Ponzi scheme hai jo shuru mein thora return de kar logon ka bharosa jeetti hai aur phir bhaag jaati hai.")
    st.markdown("- **Fake Task Based Apps:** Video dekhne ya click karne ke paise dene ka dawa karti hain lekin withdrawal ke waqt fee maangti hain.")

with tab2:
    st.markdown("#### Real Platforms")
    st.markdown("- **Upwork / Fiverr:** Real freelancing platforms jahan mehnat aur skills ki base par earning hoti hai.")

if query:
    st.info(f"Aapne '{query}' search kiya hai. Mazeed tafseel jald update ki jayegi!")
  
