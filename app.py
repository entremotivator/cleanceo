import streamlit as st

# ── PAGE CONFIG ──
st.set_page_config(
    page_title="1-on-1 Strategy Session — Meticulous Quality",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ══════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════
st.markdown("#### ✦  LIMITED-TIME OFFER  ✦")
st.markdown("## METICULOUS QUALITY")
st.title("Private 1-on-1 AI Strategy Session")
st.subheader("Custom AI automation roadmap — built exclusively for your cleaning business.")
st.write(
    "Work directly with our specialists to map out the exact AI systems "
    "your cleaning company needs to triple leads, retain more clients, and "
    "reclaim 50+ hours per week."
)

st.divider()

# ── PRICE ──
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("### ~~$299~~ &nbsp;&nbsp; 🏷️ **$99**")
    st.caption("One private 60-minute consultation · Limited spots available")

st.divider()

# ══════════════════════════════════════════════
# WHAT YOU GET
# ══════════════════════════════════════════════
st.subheader("✦  What's Included in Your Session")

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("**🎯 Operations Audit**")
    st.write("We review how your business runs — leads, scheduling, follow-ups — and pinpoint exactly where you're losing time and revenue.")

    st.markdown("**🤖 Custom AI Roadmap**")
    st.write("Walk away with a prioritized plan for automating the highest-impact areas of your cleaning business, tailored to your size and goals.")

    st.markdown("**📈 Revenue Growth Plan**")
    st.write("Specific strategies using AI to triple lead conversion, retain more clients, and scale without proportionally scaling overhead.")

with col_b:
    st.markdown("**💡 Tool Recommendations**")
    st.write("We identify which AI tools — voice agents, chatbots, CRM automation — will deliver the fastest ROI for your specific operation.")

    st.markdown("**🔗 Integration Blueprint**")
    st.write("See exactly how new systems connect to Jobber, ServiceTitan, QuickBooks, Google Workspace, and more.")

    st.markdown("**📋 Session Summary Doc**")
    st.write("A written summary of findings, recommendations, and next steps — delivered within 24 hours of your session.")

st.divider()

# ══════════════════════════════════════════════
# PRODUCT IMAGES
# ══════════════════════════════════════════════
st.subheader("✦  Our AI Systems — We'll Walk You Through Each One")
st.caption("During your session, we show you exactly how these work for your business.")

img1, img2, img3, img4 = st.columns(4)
with img1:
    st.image("https://meticulousquality.com/wp-content/uploads/2026/01/ai_voice_agent_box.png", caption="AI Voice Agent")
with img2:
    st.image("https://meticulousquality.com/wp-content/uploads/2026/01/ava_chatbot_box.png", caption="AVA AI Chatbot")
with img3:
    st.image("https://meticulousquality.com/wp-content/uploads/2026/01/lead_dashboard_box.png", caption="Lead Dashboard")
with img4:
    st.image("https://meticulousquality.com/wp-content/uploads/2026/01/meticulous_crm_box.png", caption="Meticulous CRM")

st.divider()

# ══════════════════════════════════════════════
# STATS
# ══════════════════════════════════════════════
st.subheader("✦  What Our Clients Typically Experience")

s1, s2, s3, s4 = st.columns(4)
with s1:
    st.metric(label="Revenue Growth", value="3×")
with s2:
    st.metric(label="Time Saved", value="75%")
with s3:
    st.metric(label="Client Retention", value="90%")
with s4:
    st.metric(label="Lead Response", value="24/7")

st.divider()

# ══════════════════════════════════════════════
# ABOUT + VIDEO
# ══════════════════════════════════════════════
about_col, video_col = st.columns(2)

with about_col:
    st.subheader("Who You're Talking To")
    st.write(
        "Meticulous Quality is an AI consulting firm that works **exclusively** "
        "with cleaning companies. We don't serve every industry — that focus is deliberate."
    )
    st.write(
        "Our specialists have worked with companies ranging from owner-operated "
        "residential cleaners to multi-location commercial contractors. We know your business."
    )
    st.info("In your session, you'll speak directly with a senior consultant — not a sales rep.")

with video_col:
    st.video("https://embed.wave.video/WbEAwQqB0kBuMTsQ")

st.divider()

# ══════════════════════════════════════════════
# ZELLE CTA — MAIN CALL TO ACTION
# ══════════════════════════════════════════════
st.subheader("✦  Book Your Session — 2 Simple Steps")
st.markdown("### ~~$299~~ &nbsp;&nbsp; **Only $99 Today**")
st.caption("60 minutes · Private · Focused entirely on your business · Limited spots")

st.divider()

# Step 1
st.markdown("### Step 1 — Send $99 via Zelle")

col_left, col_mid, col_right = st.columns([1, 2, 1])
with col_mid:
    st.success("⚡  Zelle Number:  **770-369-6875**")

st.write("Open your banking app, select Zelle, and send **$99** to the number above.")

st.divider()

# Step 2
st.markdown("### Step 2 — Text Us to Confirm")

col_left2, col_mid2, col_right2 = st.columns([1, 2, 1])
with col_mid2:
    st.info("📱  Text: **770-369-6875**")

st.write(
    'After sending payment, text your **name + "PAID"** to **770-369-6875** '
    "and your appointment time will be confirmed."
)

st.caption("🔒  Secure · Instant · No account required to receive Zelle")

st.divider()

# ══════════════════════════════════════════════
# GUARANTEE
# ══════════════════════════════════════════════
st.subheader("🛡️  100% Satisfaction Guarantee")
st.write(
    "If you don't walk away from your session with at least 3 clear, actionable ideas "
    "to improve your cleaning business using AI — we'll refund your $99 in full. No questions asked."
)

st.divider()

# ══════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════
st.markdown("#### METICULOUS QUALITY")
st.caption("© 2026 Meticulous Quality · AI Automation for Cleaning Businesses · [meticulousquality.com](https://meticulousquality.com)")
