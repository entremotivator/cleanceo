import streamlit as st

# ── PAGE CONFIG ──
st.set_page_config(
    page_title="1-on-1 Strategy Session — Meticulous Quality",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── GLOBAL CSS ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap');

:root {
  --gold: #f0c040;
  --gold-light: #f7dc6f;
  --gold-dark: #c9a227;
  --gold-glow: rgba(240,192,64,0.35);
  --black: #080808;
  --darker: #0d0d0d;
  --card: #161616;
  --border: rgba(240,192,64,0.2);
  --border-hover: rgba(240,192,64,0.7);
  --text: #e8e8e8;
  --text-muted: #999;
}

/* Reset Streamlit defaults */
html, body, [class*="css"], .stApp {
  background-color: #080808 !important;
  color: #e8e8e8 !important;
  font-family: 'DM Sans', sans-serif !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section.main > div { padding: 0 !important; }

/* Noise overlay */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 9999;
  opacity: 0.6;
}

/* Form inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div {
  background: #1e1e1e !important;
  border: 1px solid rgba(240,192,64,0.3) !important;
  color: #e8e8e8 !important;
  border-radius: 8px !important;
  font-family: 'DM Sans', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
  border-color: #f0c040 !important;
  box-shadow: 0 0 0 2px rgba(240,192,64,0.2) !important;
}

/* Labels */
.stTextInput label, .stTextArea label, .stSelectbox label {
  color: #ccc !important;
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.9rem !important;
}

/* Submit button */
.stButton > button {
  width: 100%;
  padding: 1rem 2rem !important;
  font-family: 'DM Sans', sans-serif !important;
  font-size: 1rem !important;
  font-weight: 700 !important;
  letter-spacing: 1px !important;
  text-transform: uppercase !important;
  border-radius: 10px !important;
  background: linear-gradient(135deg, #c9a227 0%, #f0c040 50%, #f7dc6f 100%) !important;
  color: #000 !important;
  border: none !important;
  cursor: pointer !important;
  box-shadow: 0 4px 30px rgba(240,192,64,0.35) !important;
  transition: all 0.35s ease !important;
  margin-top: 1rem !important;
}
.stButton > button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 10px 50px rgba(240,192,64,0.55) !important;
}

/* Success message */
.stSuccess {
  background: rgba(240,192,64,0.1) !important;
  border: 1px solid rgba(240,192,64,0.4) !important;
  color: #f7dc6f !important;
  border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# HERO SECTION
# ══════════════════════════════════════════════
st.markdown("""
<div style="
  min-height: 92vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #080808;
  position: relative;
  overflow: hidden;
  padding: 5rem 2rem 4rem;
  text-align: center;
">
  <!-- radial glow -->
  <div style="
    position: absolute; inset: 0;
    background:
      radial-gradient(ellipse 80% 60% at 20% 15%, rgba(240,192,64,0.12) 0%, transparent 65%),
      radial-gradient(ellipse 60% 50% at 80% 85%, rgba(240,192,64,0.07) 0%, transparent 60%);
    pointer-events: none;
  "></div>

  <div style="position: relative; z-index: 2; max-width: 780px; margin: 0 auto;">

    <!-- Badge -->
    <div style="
      display: inline-flex; align-items: center; gap: 0.5rem;
      background: rgba(240,192,64,0.1);
      border: 1px solid rgba(240,192,64,0.2);
      color: #f7dc6f;
      padding: 0.45rem 1.2rem;
      border-radius: 100px;
      font-size: 0.8rem; font-weight: 600;
      letter-spacing: 1.5px; text-transform: uppercase;
      margin-bottom: 1.5rem;
    ">✦ &nbsp; Limited-Time Offer</div>

    <!-- Brand -->
    <div style="
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(1.3rem, 3vw, 1.9rem);
      font-weight: 600;
      color: #f7dc6f;
      letter-spacing: 3px;
      text-transform: uppercase;
      margin-bottom: 1.2rem;
      opacity: 0.9;
    ">Meticulous Quality</div>

    <!-- Headline -->
    <h1 style="
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(2.8rem, 6vw, 5rem);
      font-weight: 700;
      line-height: 1.1;
      color: #f0c040;
      margin-bottom: 1.5rem;
    ">
      Private 1-on-1<br>
      <span style="
        background: linear-gradient(135deg, #f0c040 0%, #f7dc6f 60%, #fff8d6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
      ">AI Strategy Session</span>
    </h1>

    <!-- Subheadline -->
    <p style="
      font-size: 1.2rem; color: #bbb;
      max-width: 620px; margin: 0 auto 2.5rem;
      line-height: 1.8;
    ">
      Work directly with our AI automation specialists to map out a custom system 
      for your cleaning business — built around your leads, your team, and your growth goals.
    </p>

    <!-- Price Block -->
    <div style="
      display: inline-block;
      background: #161616;
      border: 1px solid rgba(240,192,64,0.35);
      border-radius: 16px;
      padding: 2rem 3.5rem;
      margin-bottom: 2.5rem;
      box-shadow: 0 0 60px rgba(240,192,64,0.12);
    ">
      <div style="font-size: 0.8rem; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; margin-bottom: 0.6rem; font-weight: 700;">Special Offer</div>
      <div style="display: flex; align-items: center; justify-content: center; gap: 1.2rem; flex-wrap: wrap;">
        <span style="
          font-family: 'Cormorant Garamond', serif;
          font-size: 2.2rem;
          color: #666;
          text-decoration: line-through;
          text-decoration-color: #e55;
          text-decoration-thickness: 2px;
        ">$299</span>
        <span style="
          font-family: 'Cormorant Garamond', serif;
          font-size: 4.5rem;
          font-weight: 700;
          background: linear-gradient(135deg, #f0c040, #f7dc6f);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-clip: text;
          line-height: 1;
        ">$99</span>
      </div>
      <div style="font-size: 0.85rem; color: #999; margin-top: 0.5rem;">One private 60-minute consultation · Limited spots available</div>
    </div>

    <!-- Bottom line divider -->
    <div style="width: 60px; height: 2px; background: linear-gradient(90deg, transparent, #f0c040, transparent); margin: 0 auto;"></div>
  </div>
</div>

<!-- Separator line -->
<div style="height: 1px; background: linear-gradient(90deg, transparent, #f0c040, transparent);"></div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# WHAT YOU GET
# ══════════════════════════════════════════════
st.markdown("""
<div style="background: #0d0d0d; padding: 5rem 2rem; text-align: center; border-bottom: 1px solid rgba(240,192,64,0.2);">
  <div style="max-width: 860px; margin: 0 auto;">
    <span style="font-size: 0.75rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; opacity: 0.8;">What's Included</span>
    <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(2rem, 4vw, 3.2rem); font-weight: 700; color: #f0c040; margin: 1rem 0 3rem;">Everything in Your 60-Minute Session</h2>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; text-align: left;">

      <div style="background: #161616; border: 1px solid rgba(240,192,64,0.2); border-radius: 10px; padding: 2rem; transition: all 0.3s;">
        <div style="font-size: 2rem; margin-bottom: 1rem;">🎯</div>
        <h4 style="font-family: 'Cormorant Garamond', serif; color: #f7dc6f; font-size: 1.3rem; margin-bottom: 0.8rem;">Operations Audit</h4>
        <p style="color: #aaa; font-size: 0.97rem; line-height: 1.7; max-width: none;">We review how your business currently runs — leads, scheduling, follow-ups — and pinpoint exactly where you're losing time and revenue.</p>
      </div>

      <div style="background: #161616; border: 1px solid rgba(240,192,64,0.2); border-radius: 10px; padding: 2rem;">
        <div style="font-size: 2rem; margin-bottom: 1rem;">🤖</div>
        <h4 style="font-family: 'Cormorant Garamond', serif; color: #f7dc6f; font-size: 1.3rem; margin-bottom: 0.8rem;">Custom AI Roadmap</h4>
        <p style="color: #aaa; font-size: 0.97rem; line-height: 1.7; max-width: none;">You'll walk away with a prioritized plan for automating the highest-impact areas of your cleaning business — tailored to your size and goals.</p>
      </div>

      <div style="background: #161616; border: 1px solid rgba(240,192,64,0.2); border-radius: 10px; padding: 2rem;">
        <div style="font-size: 2rem; margin-bottom: 1rem;">📈</div>
        <h4 style="font-family: 'Cormorant Garamond', serif; color: #f7dc6f; font-size: 1.3rem; margin-bottom: 0.8rem;">Revenue Growth Plan</h4>
        <p style="color: #aaa; font-size: 0.97rem; line-height: 1.7; max-width: none;">Specific strategies for using AI to triple your lead conversion, retain more clients, and scale without proportionally scaling overhead.</p>
      </div>

      <div style="background: #161616; border: 1px solid rgba(240,192,64,0.2); border-radius: 10px; padding: 2rem;">
        <div style="font-size: 2rem; margin-bottom: 1rem;">💡</div>
        <h4 style="font-family: 'Cormorant Garamond', serif; color: #f7dc6f; font-size: 1.3rem; margin-bottom: 0.8rem;">Tool Recommendations</h4>
        <p style="color: #aaa; font-size: 0.97rem; line-height: 1.7; max-width: none;">We'll identify which AI tools — voice agents, chatbots, CRM automation — will deliver the fastest ROI for your specific operation.</p>
      </div>

      <div style="background: #161616; border: 1px solid rgba(240,192,64,0.2); border-radius: 10px; padding: 2rem;">
        <div style="font-size: 2rem; margin-bottom: 1rem;">🔗</div>
        <h4 style="font-family: 'Cormorant Garamond', serif; color: #f7dc6f; font-size: 1.3rem; margin-bottom: 0.8rem;">Integration Blueprint</h4>
        <p style="color: #aaa; font-size: 0.97rem; line-height: 1.7; max-width: none;">See exactly how new systems connect to your existing tools — Jobber, ServiceTitan, QuickBooks, Google Workspace, and more.</p>
      </div>

      <div style="background: #161616; border: 1px solid rgba(240,192,64,0.2); border-radius: 10px; padding: 2rem;">
        <div style="font-size: 2rem; margin-bottom: 1rem;">📋</div>
        <h4 style="font-family: 'Cormorant Garamond', serif; color: #f7dc6f; font-size: 1.3rem; margin-bottom: 0.8rem;">Session Summary Doc</h4>
        <p style="color: #aaa; font-size: 0.97rem; line-height: 1.7; max-width: none;">You receive a written summary of everything covered — findings, recommendations, and next steps — delivered within 24 hours of your session.</p>
      </div>

    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# PRODUCT IMAGES STRIP
# ══════════════════════════════════════════════
st.markdown("""
<div style="background: #080808; padding: 4rem 2rem; border-bottom: 1px solid rgba(240,192,64,0.2); text-align: center;">
  <div style="max-width: 860px; margin: 0 auto;">
    <span style="font-size: 0.75rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; opacity: 0.8;">Our Systems</span>
    <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(1.8rem, 3.5vw, 2.8rem); font-weight: 700; color: #f0c040; margin: 1rem 0 0.5rem;">We'll Show You Exactly How These Work</h2>
    <p style="color: #999; margin: 0 auto 3rem; max-width: 580px; font-size: 0.97rem;">In your session, we walk through each system that applies to your business.</p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem;">
      <div style="border: 1px solid rgba(240,192,64,0.2); border-radius: 10px; overflow: hidden; background: #161616;">
        <img src="https://meticulousquality.com/wp-content/uploads/2026/01/ai_voice_agent_box.png" alt="AI Voice Agent" style="width:100%; display:block;">
        <div style="padding: 0.8rem; font-size: 0.85rem; color: #ccc; font-weight: 600;">AI Voice Agent</div>
      </div>
      <div style="border: 1px solid rgba(240,192,64,0.2); border-radius: 10px; overflow: hidden; background: #161616;">
        <img src="https://meticulousquality.com/wp-content/uploads/2026/01/ava_chatbot_box.png" alt="AVA Chatbot" style="width:100%; display:block;">
        <div style="padding: 0.8rem; font-size: 0.85rem; color: #ccc; font-weight: 600;">AVA AI Chatbot</div>
      </div>
      <div style="border: 1px solid rgba(240,192,64,0.2); border-radius: 10px; overflow: hidden; background: #161616;">
        <img src="https://meticulousquality.com/wp-content/uploads/2026/01/lead_dashboard_box.png" alt="Lead Dashboard" style="width:100%; display:block;">
        <div style="padding: 0.8rem; font-size: 0.85rem; color: #ccc; font-weight: 600;">Lead Dashboard</div>
      </div>
      <div style="border: 1px solid rgba(240,192,64,0.2); border-radius: 10px; overflow: hidden; background: #161616;">
        <img src="https://meticulousquality.com/wp-content/uploads/2026/01/meticulous_crm_box.png" alt="Meticulous CRM" style="width:100%; display:block;">
        <div style="padding: 0.8rem; font-size: 0.85rem; color: #ccc; font-weight: 600;">Meticulous CRM</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# STATS BAR
# ══════════════════════════════════════════════
st.markdown("""
<div style="background: #0d0d0d; padding: 3.5rem 2rem; border-bottom: 1px solid rgba(240,192,64,0.2);">
  <div style="max-width: 860px; margin: 0 auto;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 2rem; text-align: center;">
      <div>
        <div style="font-family: 'Cormorant Garamond', serif; font-size: 3.2rem; font-weight: 700; background: linear-gradient(135deg, #f0c040, #f7dc6f); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1; margin-bottom: 0.5rem;">3×</div>
        <p style="font-size: 0.85rem; color: #999; max-width: none;">Average Revenue Growth</p>
      </div>
      <div>
        <div style="font-family: 'Cormorant Garamond', serif; font-size: 3.2rem; font-weight: 700; background: linear-gradient(135deg, #f0c040, #f7dc6f); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1; margin-bottom: 0.5rem;">75%</div>
        <p style="font-size: 0.85rem; color: #999; max-width: none;">Time Saved on Operations</p>
      </div>
      <div>
        <div style="font-family: 'Cormorant Garamond', serif; font-size: 3.2rem; font-weight: 700; background: linear-gradient(135deg, #f0c040, #f7dc6f); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1; margin-bottom: 0.5rem;">90%</div>
        <p style="font-size: 0.85rem; color: #999; max-width: none;">Customer Retention Rate</p>
      </div>
      <div>
        <div style="font-family: 'Cormorant Garamond', serif; font-size: 3.2rem; font-weight: 700; background: linear-gradient(135deg, #f0c040, #f7dc6f); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1; margin-bottom: 0.5rem;">24/7</div>
        <p style="font-size: 0.85rem; color: #999; max-width: none;">Automated Lead Response</p>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# VIDEO / ABOUT
# ══════════════════════════════════════════════
st.markdown("""
<div style="background: #080808; padding: 5rem 2rem; border-bottom: 1px solid rgba(240,192,64,0.2);">
  <div style="max-width: 860px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
    <div>
      <span style="font-size: 0.75rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; opacity: 0.8;">About Us</span>
      <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(2rem, 3.5vw, 2.8rem); font-weight: 700; color: #f0c040; margin: 0.8rem 0;">Who You're Talking To</h2>
      <div style="width: 60px; height: 2px; background: linear-gradient(90deg, transparent, #f0c040, transparent); margin-bottom: 1.5rem;"></div>
      <p style="color: #ccc; margin-bottom: 1.2rem; font-size: 1rem; line-height: 1.85; max-width: none;">Meticulous Quality is an AI consulting firm that works <em>exclusively</em> with cleaning companies. We don't serve every industry — that focus is deliberate.</p>
      <p style="color: #ccc; margin-bottom: 1.2rem; font-size: 1rem; line-height: 1.85; max-width: none;">Our specialists have worked with companies ranging from owner-operated residential cleaners to multi-location commercial contractors. We know your business.</p>
      <p style="color: #f7dc6f; font-weight: 600; font-size: 1rem; max-width: none;">In your session, you'll speak directly with a senior consultant — not a sales rep.</p>
    </div>
    <div style="border-radius: 10px; overflow: hidden; border: 1px solid rgba(240,192,64,0.2); box-shadow: 0 20px 60px rgba(0,0,0,0.6);">
      <div style="padding: 56.25% 0 0 0; position: relative;">
        <iframe style="height:100%; left:0; position:absolute; top:0; width:100%;" src="https://embed.wave.video/WbEAwQqB0kBuMTsQ" frameborder="0" allow="autoplay; fullscreen" scrolling="no"></iframe>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# BOOKING — ZELLE CTA ONLY
# ══════════════════════════════════════════════
st.markdown("""
<div style="
  background: linear-gradient(135deg, #1a1400 0%, #0f0b00 40%, #080808 100%);
  border-top: 1px solid rgba(240,192,64,0.25);
  border-bottom: 1px solid rgba(240,192,64,0.25);
  padding: 6rem 2rem 6rem;
  text-align: center;
  position: relative;
  overflow: hidden;
" id="book">

  <!-- glow -->
  <div style="
    position: absolute; top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 700px; height: 500px;
    background: radial-gradient(ellipse, rgba(240,192,64,0.1) 0%, transparent 70%);
    pointer-events: none;
  "></div>

  <div style="position: relative; z-index: 2; max-width: 680px; margin: 0 auto;">

    <!-- Label -->
    <div style="font-size: 0.75rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #c9a227; margin-bottom: 1rem;">Claim Your Spot</div>

    <!-- Headline -->
    <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(2.4rem, 5vw, 3.6rem); font-weight: 700; color: #f0c040; line-height: 1.1; margin-bottom: 1.2rem;">
      Book Your 1-on-1<br>AI Strategy Session
    </h2>

    <!-- Price -->
    <div style="margin-bottom: 2.5rem;">
      <span style="font-family: 'Cormorant Garamond', serif; font-size: 2rem; color: #555; text-decoration: line-through; text-decoration-color: #cc3333; text-decoration-thickness: 2px; margin-right: 0.8rem;">$299</span>
      <span style="font-family: 'Cormorant Garamond', serif; font-size: 4rem; font-weight: 700; background: linear-gradient(135deg, #f0c040, #f7dc6f); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1;">$99</span>
      <div style="font-size: 0.85rem; color: #888; margin-top: 0.4rem; letter-spacing: 0.5px;">One private 60-minute consultation · Limited spots available</div>
    </div>

    <!-- Divider -->
    <div style="width: 60px; height: 1px; background: linear-gradient(90deg, transparent, #f0c040, transparent); margin: 0 auto 2.5rem;"></div>

    <!-- ZELLE CARD -->
    <div style="
      background: #161616;
      border: 1px solid rgba(240,192,64,0.4);
      border-radius: 18px;
      padding: 2.8rem 2.5rem 2.5rem;
      box-shadow: 0 0 80px rgba(240,192,64,0.12), 0 20px 60px rgba(0,0,0,0.6);
      text-align: center;
    ">

      <!-- Zelle logo icon using colored text -->
      <div style="
        display: inline-flex; align-items: center; justify-content: center;
        gap: 0.5rem;
        background: linear-gradient(135deg, #6d1ed4, #8b2be2);
        border-radius: 50px;
        padding: 0.6rem 1.6rem;
        margin-bottom: 1.8rem;
      ">
        <span style="font-size: 1.1rem; font-weight: 800; color: #fff; letter-spacing: 1px; font-family: 'DM Sans', sans-serif;">⚡ Zelle</span>
      </div>

      <h3 style="font-family: 'Cormorant Garamond', serif; color: #f7dc6f; font-size: 1.8rem; margin-bottom: 0.6rem;">Send $99 via Zelle</h3>
      <p style="color: #aaa; font-size: 1rem; margin-bottom: 1.8rem; max-width: none;">To reserve your session, send your payment directly to:</p>

      <!-- Phone number -->
      <div style="
        background: #1e1e1e;
        border: 1px solid rgba(240,192,64,0.35);
        border-radius: 12px;
        padding: 1.4rem 2rem;
        margin-bottom: 1.8rem;
        display: inline-block;
        min-width: 280px;
      ">
        <div style="font-size: 0.7rem; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; margin-bottom: 0.5rem; font-weight: 700;">Zelle Number</div>
        <div style="font-family: 'Cormorant Garamond', serif; font-size: 2.6rem; font-weight: 700; color: #f7dc6f; letter-spacing: 2px; line-height: 1;">770-369-6875</div>
      </div>

      <!-- Step 2 -->
      <div style="
        background: rgba(240,192,64,0.07);
        border: 1px solid rgba(240,192,64,0.25);
        border-radius: 12px;
        padding: 1.4rem 2rem;
        margin-bottom: 0.5rem;
      ">
        <div style="font-size: 0.7rem; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; margin-bottom: 0.6rem; font-weight: 700;">After Payment — Text Us to Confirm</div>
        <p style="color: #ccc; font-size: 1.05rem; line-height: 1.7; max-width: none; margin: 0;">
          Once your $99 Zelle payment is sent, <strong style="color: #f7dc6f;">text your name + "PAID"</strong> to 
          <strong style="color: #f7dc6f; font-size: 1.15rem;">770-369-6875</strong> and we will confirm your appointment time.
        </p>
      </div>

    </div>

    <!-- Reassurance line -->
    <p style="font-size: 0.88rem; color: #666; margin-top: 1.5rem; max-width: none;">
      🔒 &nbsp; Secure · Instant · No account required to receive Zelle
    </p>

  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# GUARANTEE
# ══════════════════════════════════════════════
st.markdown("""
<div style="background: #080808; padding: 4rem 2rem; text-align: center; border-top: 1px solid rgba(240,192,64,0.15);">
  <div style="max-width: 620px; margin: 0 auto;">
    <div style="font-size: 3rem; margin-bottom: 1rem;">🛡️</div>
    <h3 style="font-family: 'Cormorant Garamond', serif; color: #f0c040; font-size: 2rem; margin-bottom: 1rem;">100% Satisfaction Guarantee</h3>
    <p style="color: #ccc; font-size: 1rem; line-height: 1.8; max-width: none;">
      If you don't walk away from your session with at least 3 clear, actionable ideas 
      to improve your cleaning business using AI — we'll refund your $99 in full. No questions asked.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════
st.markdown("""
<div style="
  background: #0d0d0d;
  border-top: 1px solid rgba(240,192,64,0.2);
  padding: 2rem;
  text-align: center;
">
  <div style="font-family: 'Cormorant Garamond', serif; font-size: 1.3rem; color: #f7dc6f; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 0.5rem;">Meticulous Quality</div>
  <p style="font-size: 0.85rem; color: #666; max-width: none;">© 2026 Meticulous Quality · AI Automation for Cleaning Businesses</p>
  <p style="font-size: 0.8rem; color: #555; margin-top: 0.3rem; max-width: none;">
    <a href="https://meticulousquality.com" style="color: #888; text-decoration: none;">meticulousquality.com</a>
  </p>
</div>
""", unsafe_allow_html=True)
