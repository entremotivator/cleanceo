import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="1-on-1 Strategy Session — Meticulous Quality",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default chrome
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
section.main > div {padding: 0 !important;}
</style>
""", unsafe_allow_html=True)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: 'DM Sans', sans-serif;
      background: #080808;
      color: #e8e8e8;
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }
    img { max-width: 100%; display: block; height: auto; }
    a { color: #f7dc6f; text-decoration: none; }
    h1, h2, h3, h4 { font-family: 'Cormorant Garamond', serif; color: #f0c040; line-height: 1.15; }
    .container { max-width: 900px; margin: 0 auto; padding: 0 2rem; }
    .sec { padding: 5rem 0; }
    .sec-dark { background: #0d0d0d; }
    .divider { height: 1px; background: linear-gradient(90deg, transparent, #f0c040, transparent); border: none; margin: 0; }
    .badge {
      display: inline-flex; align-items: center; gap: 0.5rem;
      background: rgba(240,192,64,0.1); border: 1px solid rgba(240,192,64,0.25);
      color: #f7dc6f; padding: 0.45rem 1.2rem; border-radius: 100px;
      font-size: 0.78rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
      margin-bottom: 1.5rem;
    }
    .sec-label {
      font-size: 0.72rem; font-weight: 700; letter-spacing: 3px;
      text-transform: uppercase; color: #f0c040; opacity: 0.8;
      display: block; margin-bottom: 0.8rem;
    }
    .gold-line { width: 50px; height: 2px; background: linear-gradient(90deg, transparent, #f0c040, transparent); margin: 1.2rem auto 0; }
    .gold-line-left { margin-left: 0; }

    /* HERO */
    .hero {
      background: #080808;
      padding: 7rem 0 5rem;
      text-align: center;
      position: relative;
      overflow: hidden;
      border-bottom: 1px solid rgba(240,192,64,0.2);
    }
    .hero::before {
      content: '';
      position: absolute; inset: 0;
      background:
        radial-gradient(ellipse 80% 60% at 20% 15%, rgba(240,192,64,0.12) 0%, transparent 65%),
        radial-gradient(ellipse 60% 50% at 80% 85%, rgba(240,192,64,0.07) 0%, transparent 60%);
      pointer-events: none;
    }
    .hero-inner { position: relative; z-index: 2; }
    .hero h1 { font-size: clamp(2.8rem, 6vw, 5rem); font-weight: 700; margin-bottom: 1.2rem; }
    .hero h1 span {
      background: linear-gradient(135deg, #f0c040 0%, #f7dc6f 60%, #fff8d6 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    }
    .hero-brand {
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(1.2rem, 2.5vw, 1.7rem); font-weight: 600;
      color: #f7dc6f; letter-spacing: 4px; text-transform: uppercase;
      margin-bottom: 1rem; opacity: 0.9;
    }
    .hero p { font-size: 1.15rem; color: #bbb; max-width: 600px; margin: 1.2rem auto 2.5rem; line-height: 1.8; }

    /* PRICE BOX */
    .price-box {
      display: inline-block;
      background: #161616;
      border: 1px solid rgba(240,192,64,0.35);
      border-radius: 16px;
      padding: 2rem 3.5rem;
      box-shadow: 0 0 60px rgba(240,192,64,0.1);
      margin-bottom: 0.5rem;
    }
    .price-label { font-size: 0.7rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; margin-bottom: 0.6rem; }
    .price-row { display: flex; align-items: center; justify-content: center; gap: 1.2rem; flex-wrap: wrap; }
    .price-old {
      font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; color: #555;
      text-decoration: line-through; text-decoration-color: #cc3333; text-decoration-thickness: 2px;
    }
    .price-new {
      font-family: 'Cormorant Garamond', serif; font-size: 4.5rem; font-weight: 700;
      background: linear-gradient(135deg, #f0c040, #f7dc6f);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
      line-height: 1;
    }
    .price-sub { font-size: 0.85rem; color: #777; margin-top: 0.5rem; }

    /* WHAT YOU GET */
    .includes-grid {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.5rem; margin-top: 3rem;
    }
    .include-card {
      background: #161616; border: 1px solid rgba(240,192,64,0.18);
      border-radius: 10px; padding: 1.8rem;
      transition: border-color 0.3s, transform 0.3s;
    }
    .include-card:hover { border-color: rgba(240,192,64,0.6); transform: translateY(-4px); }
    .include-card .icon { font-size: 1.8rem; margin-bottom: 0.8rem; }
    .include-card h4 { color: #f7dc6f; font-size: 1.15rem; margin-bottom: 0.5rem; }
    .include-card p { color: #aaa; font-size: 0.95rem; max-width: none; line-height: 1.65; }

    /* PRODUCT IMAGES */
    .img-grid {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1.2rem; margin-top: 2.5rem;
    }
    .img-card {
      background: #161616; border: 1px solid rgba(240,192,64,0.18);
      border-radius: 10px; overflow: hidden;
      transition: border-color 0.3s, transform 0.3s;
    }
    .img-card:hover { border-color: rgba(240,192,64,0.6); transform: translateY(-4px); }
    .img-card img { width: 100%; display: block; }
    .img-card p { padding: 0.6rem 1rem; font-size: 0.82rem; color: #ccc; font-weight: 600; text-align: center; }

    /* STATS */
    .stats-grid {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
      gap: 2rem; text-align: center; margin-top: 3rem;
    }
    .stat-num {
      font-family: 'Cormorant Garamond', serif; font-size: 3.5rem; font-weight: 700;
      background: linear-gradient(135deg, #f0c040, #f7dc6f);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
      line-height: 1; display: block; margin-bottom: 0.4rem;
    }
    .stat p { font-size: 0.85rem; color: #888; max-width: none; }

    /* ABOUT */
    .about-wrap { display: grid; gap: 4rem; align-items: center; }
    @media (min-width: 700px) { .about-wrap { grid-template-columns: 1fr 1fr; } }
    .about-wrap p { color: #ccc; font-size: 1rem; line-height: 1.85; max-width: none; margin-bottom: 1rem; }
    .about-highlight { color: #f7dc6f; font-weight: 600; }
    .video-wrap { border-radius: 10px; overflow: hidden; border: 1px solid rgba(240,192,64,0.2); box-shadow: 0 20px 60px rgba(0,0,0,0.6); }
    .video-wrap iframe { width: 100%; height: 280px; display: block; border: none; }

    /* ZELLE CTA */
    .zelle-sec {
      background: linear-gradient(135deg, #1a1400 0%, #0f0b00 40%, #080808 100%);
      padding: 6rem 0;
      text-align: center;
      border-top: 1px solid rgba(240,192,64,0.25);
      border-bottom: 1px solid rgba(240,192,64,0.25);
      position: relative; overflow: hidden;
    }
    .zelle-sec::before {
      content: '';
      position: absolute; top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      width: 600px; height: 500px;
      background: radial-gradient(ellipse, rgba(240,192,64,0.09) 0%, transparent 70%);
      pointer-events: none;
    }
    .zelle-sec .inner { position: relative; z-index: 2; }
    .zelle-sec h2 { font-size: clamp(2.2rem, 5vw, 3.4rem); font-weight: 700; margin-bottom: 1rem; }
    .zelle-card {
      background: #161616;
      border: 1px solid rgba(240,192,64,0.4);
      border-radius: 18px;
      padding: 3rem 2.5rem;
      max-width: 560px;
      margin: 2.5rem auto 0;
      box-shadow: 0 0 80px rgba(240,192,64,0.1), 0 20px 60px rgba(0,0,0,0.5);
    }
    .zelle-badge {
      display: inline-flex; align-items: center; gap: 0.5rem;
      background: linear-gradient(135deg, #6d1ed4, #8b2be2);
      border-radius: 50px; padding: 0.5rem 1.5rem;
      font-size: 1rem; font-weight: 800; color: #fff;
      letter-spacing: 1px; margin-bottom: 1.5rem;
    }
    .zelle-card h3 { color: #f7dc6f; font-size: 1.9rem; margin-bottom: 0.5rem; }
    .zelle-card > p { color: #aaa; font-size: 1rem; margin-bottom: 1.5rem; max-width: none; }
    .phone-box {
      background: #1e1e1e;
      border: 1px solid rgba(240,192,64,0.35);
      border-radius: 12px;
      padding: 1.3rem 2rem;
      margin-bottom: 1.5rem;
    }
    .phone-label { font-size: 0.68rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; margin-bottom: 0.4rem; }
    .phone-num {
      font-family: 'Cormorant Garamond', serif; font-size: 2.8rem; font-weight: 700;
      color: #f7dc6f; letter-spacing: 2px; line-height: 1;
    }
    .confirm-box {
      background: rgba(240,192,64,0.06);
      border: 1px solid rgba(240,192,64,0.22);
      border-radius: 12px;
      padding: 1.5rem 2rem;
    }
    .confirm-label { font-size: 0.68rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; margin-bottom: 0.6rem; }
    .confirm-box p { color: #ccc; font-size: 1rem; line-height: 1.7; max-width: none; margin: 0; }
    .confirm-box strong { color: #f7dc6f; }
    .secure { font-size: 0.85rem; color: #555; margin-top: 1.5rem; }

    /* STEPS */
    .steps { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 0; }
    @media (max-width: 600px) { .steps { grid-template-columns: 1fr; } }
    .step-num-badge {
      width: 42px; height: 42px; border-radius: 50%;
      background: linear-gradient(135deg, #c9a227, #f0c040);
      color: #000; font-weight: 800; font-size: 1.1rem;
      display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;
    }

    /* GUARANTEE */
    .guarantee-box {
      background: #161616;
      border: 1px solid rgba(240,192,64,0.2);
      border-radius: 14px;
      padding: 3rem;
      text-align: center;
      margin-top: 3rem;
    }
    .guarantee-box .icon { font-size: 3rem; margin-bottom: 1rem; }
    .guarantee-box h3 { font-size: 2rem; margin-bottom: 1rem; }
    .guarantee-box p { color: #ccc; font-size: 1rem; max-width: 560px; margin: 0 auto; line-height: 1.8; }

    /* FOOTER */
    footer {
      background: #0d0d0d;
      border-top: 1px solid rgba(240,192,64,0.2);
      padding: 2.5rem 0;
      text-align: center;
    }
    footer .brand { font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; color: #f7dc6f; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 0.4rem; }
    footer p { font-size: 0.85rem; color: #555; max-width: none; }
    footer a { color: #777; }

    @media (max-width: 600px) {
      .hero { padding: 5rem 0 4rem; }
      .price-box { padding: 1.5rem 2rem; }
      .zelle-card { padding: 2rem 1.5rem; }
      .guarantee-box { padding: 2rem 1.5rem; }
    }
  </style>
</head>
<body>

<!-- HERO -->
<section class="hero">
  <div class="container hero-inner">
    <div class="badge">✦ &nbsp; Limited-Time Offer</div>
    <div class="hero-brand">Meticulous Quality</div>
    <h1>Private 1-on-1<br><span>AI Strategy Session</span></h1>
    <p>Work directly with our AI automation specialists to map out a custom system for your cleaning business — built around your leads, your team, and your growth goals.</p>

    <div class="price-box">
      <div class="price-label">Special Offer</div>
      <div class="price-row">
        <span class="price-old">$299</span>
        <span class="price-new">$99</span>
      </div>
      <div class="price-sub">One private 60-minute consultation &nbsp;·&nbsp; Limited spots available</div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- WHAT'S INCLUDED -->
<section class="sec">
  <div class="container">
    <div style="text-align:center;">
      <span class="sec-label">What's Included</span>
      <h2 style="font-size:clamp(2rem,4vw,3rem);">Everything in Your 60-Minute Session</h2>
      <div class="gold-line"></div>
    </div>
    <div class="includes-grid">
      <div class="include-card">
        <div class="icon">🎯</div>
        <h4>Operations Audit</h4>
        <p>We review how your business currently runs — leads, scheduling, follow-ups — and pinpoint exactly where you're losing time and revenue.</p>
      </div>
      <div class="include-card">
        <div class="icon">🤖</div>
        <h4>Custom AI Roadmap</h4>
        <p>You'll walk away with a prioritized plan for automating the highest-impact areas of your cleaning business, tailored to your size and goals.</p>
      </div>
      <div class="include-card">
        <div class="icon">📈</div>
        <h4>Revenue Growth Plan</h4>
        <p>Specific strategies for using AI to triple your lead conversion, retain more clients, and scale without proportionally scaling overhead.</p>
      </div>
      <div class="include-card">
        <div class="icon">💡</div>
        <h4>Tool Recommendations</h4>
        <p>We identify which AI tools — voice agents, chatbots, CRM automation — will deliver the fastest ROI for your specific operation.</p>
      </div>
      <div class="include-card">
        <div class="icon">🔗</div>
        <h4>Integration Blueprint</h4>
        <p>See exactly how new systems connect to Jobber, ServiceTitan, QuickBooks, Google Workspace, and more.</p>
      </div>
      <div class="include-card">
        <div class="icon">📋</div>
        <h4>Session Summary Doc</h4>
        <p>A written summary of findings, recommendations, and next steps — delivered within 24 hours of your session.</p>
      </div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- PRODUCT IMAGES -->
<section class="sec sec-dark">
  <div class="container">
    <div style="text-align:center;">
      <span class="sec-label">Our Systems</span>
      <h2 style="font-size:clamp(1.8rem,3.5vw,2.8rem);">We'll Walk You Through Each One</h2>
      <p style="color:#888;margin-top:0.8rem;font-size:0.97rem;">During your session, we show you exactly how these tools work for your business.</p>
      <div class="gold-line"></div>
    </div>
    <div class="img-grid">
      <div class="img-card">
        <img src="https://meticulousquality.com/wp-content/uploads/2026/01/ai_voice_agent_box.png" alt="AI Voice Agent">
        <p>AI Voice Agent</p>
      </div>
      <div class="img-card">
        <img src="https://meticulousquality.com/wp-content/uploads/2026/01/ava_chatbot_box.png" alt="AVA Chatbot">
        <p>AVA AI Chatbot</p>
      </div>
      <div class="img-card">
        <img src="https://meticulousquality.com/wp-content/uploads/2026/01/lead_dashboard_box.png" alt="Lead Dashboard">
        <p>Lead Dashboard</p>
      </div>
      <div class="img-card">
        <img src="https://meticulousquality.com/wp-content/uploads/2026/01/meticulous_crm_box.png" alt="Meticulous CRM">
        <p>Meticulous CRM</p>
      </div>
      <div class="img-card">
        <img src="https://meticulousquality.com/wp-content/uploads/2026/01/linkedin_outreach_box.png" alt="LinkedIn Outreach">
        <p>LinkedIn Outreach</p>
      </div>
      <div class="img-card">
        <img src="https://meticulousquality.com/wp-content/uploads/2026/01/social_media_tracker_box.png" alt="Social Media">
        <p>Social Media Auto</p>
      </div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- STATS -->
<section class="sec">
  <div class="container">
    <div style="text-align:center;">
      <span class="sec-label">Client Outcomes</span>
      <h2 style="font-size:clamp(1.8rem,3.5vw,2.8rem);">What Our Clients Typically Experience</h2>
      <div class="gold-line"></div>
    </div>
    <div class="stats-grid">
      <div class="stat"><span class="stat-num">3×</span><p>Average Revenue Growth</p></div>
      <div class="stat"><span class="stat-num">75%</span><p>Time Saved on Operations</p></div>
      <div class="stat"><span class="stat-num">90%</span><p>Customer Retention Rate</p></div>
      <div class="stat"><span class="stat-num">50+</span><p>Hours Saved Per Week</p></div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- ABOUT + VIDEO -->
<section class="sec sec-dark">
  <div class="container">
    <div class="about-wrap">
      <div>
        <span class="sec-label">About Us</span>
        <h2 style="font-size:clamp(1.8rem,3.5vw,2.8rem); margin-bottom:1rem;">Who You're Talking To</h2>
        <div class="gold-line gold-line-left" style="margin-bottom:1.5rem;"></div>
        <p>Meticulous Quality is an AI consulting firm that works <strong style="color:#f7dc6f;">exclusively</strong> with cleaning companies. We don't serve every industry — that focus is deliberate.</p>
        <p>Our specialists have worked with companies ranging from owner-operated residential cleaners to multi-location commercial contractors. We know your business.</p>
        <p class="about-highlight">In your session, you'll speak directly with a senior consultant — not a sales rep.</p>
      </div>
      <div class="video-wrap">
        <iframe src="https://embed.wave.video/WbEAwQqB0kBuMTsQ" allow="autoplay; fullscreen" scrolling="no"></iframe>
      </div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- ZELLE CTA -->
<section class="zelle-sec">
  <div class="container inner">
    <span class="sec-label" style="opacity:1;color:#c9a227;">Claim Your Spot</span>
    <h2>Book Your 1-on-1<br>AI Strategy Session</h2>

    <div style="margin:1.2rem 0 0;">
      <span style="font-family:'Cormorant Garamond',serif;font-size:2rem;color:#555;text-decoration:line-through;text-decoration-color:#cc3333;text-decoration-thickness:2px;margin-right:0.8rem;">$299</span>
      <span style="font-family:'Cormorant Garamond',serif;font-size:4rem;font-weight:700;background:linear-gradient(135deg,#f0c040,#f7dc6f);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1;">$99</span>
    </div>
    <p style="color:#888;font-size:0.85rem;margin-top:0.4rem;">60 minutes &nbsp;·&nbsp; Private &nbsp;·&nbsp; Limited spots available</p>

    <div class="zelle-card">
      <div class="zelle-badge">⚡ Zelle</div>
      <h3>Send $99 via Zelle</h3>
      <p>To reserve your session, send your payment directly to:</p>

      <div class="phone-box">
        <div class="phone-label">Zelle Number</div>
        <div class="phone-num">770-369-6875</div>
      </div>

      <div class="confirm-box">
        <div class="confirm-label">Step 2 — Text Us to Confirm</div>
        <p>After sending payment, <strong>text your name + "PAID"</strong> to <strong>770-369-6875</strong> and your appointment time will be confirmed.</p>
      </div>

      <p class="secure">🔒 &nbsp; Secure &nbsp;·&nbsp; Instant &nbsp;·&nbsp; No account required to receive Zelle</p>
    </div>
  </div>
</section>

<hr class="divider">

<!-- GUARANTEE -->
<section class="sec">
  <div class="container">
    <div class="guarantee-box">
      <div class="icon">🛡️</div>
      <h3>100% Satisfaction Guarantee</h3>
      <p>If you don't walk away from your session with at least 3 clear, actionable ideas to improve your cleaning business using AI — we'll refund your $99 in full. No questions asked.</p>
    </div>
  </div>
</section>

<hr class="divider">

<!-- FOOTER -->
<footer>
  <div class="container">
    <div class="brand">Meticulous Quality</div>
    <p>© 2026 Meticulous Quality &nbsp;·&nbsp; AI Automation for Cleaning Businesses</p>
    <p style="margin-top:0.3rem;"><a href="https://meticulousquality.com">meticulousquality.com</a></p>
  </div>
</footer>

</body>
</html>
"""

components.html(html_content, height=5800, scrolling=False)
