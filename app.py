import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Grow Your Cleaning Biz in 2026 — Mironda Deel",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
section.main > div {padding: 0 !important;}
iframe {width: 100% !important; border: none !important;}
</style>
""", unsafe_allow_html=True)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: 'DM Sans', sans-serif;
      background: #08082a;
      color: #e8e8ff;
      line-height: 1.75;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }
    h1,h2,h3,h4 { font-family: 'Cormorant Garamond', serif; line-height: 1.15; }

    .wrap { max-width: 860px; margin: 0 auto; padding: 0 2rem; }
    .divider { height: 1px; background: linear-gradient(90deg, transparent, #f0c040, transparent); border: none; margin: 0; }
    .gold { color: #f0c040; }
    .white { color: #ffffff; }

    /* HERO */
    .hero {
      background: linear-gradient(160deg, #0d0d45 0%, #1c1c7a 45%, #0d0d45 100%);
      border-bottom: 3px solid #f0c040;
      padding: 5rem 2rem 4.5rem;
      text-align: center;
      position: relative;
      overflow: hidden;
    }
    .hero::before {
      content: '';
      position: absolute; inset: 0;
      background: radial-gradient(ellipse 70% 60% at 50% 30%, rgba(240,192,64,0.13) 0%, transparent 65%);
      pointer-events: none;
    }
    .hero-inner { position: relative; z-index: 2; }

    .presenter { font-size: 0.78rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; margin-bottom: 0.6rem; }
    .hero h1 { font-size: clamp(2.4rem, 5.5vw, 4.2rem); font-weight: 700; color: #ffffff; margin-bottom: 0.8rem; line-height: 1.1; }
    .hero h1 span { background: linear-gradient(135deg, #f0c040, #f7dc6f, #fff8d6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .hero-sub { font-size: 1.15rem; color: #b0b8f0; max-width: 640px; margin: 0.8rem auto 2rem; line-height: 1.8; }
    .hero-quote { font-family: 'Cormorant Garamond', serif; font-size: 1.3rem; font-style: italic; color: #f0c040; margin-bottom: 2.5rem; max-width: 600px; margin-inline: auto; }

    /* PRICE BOX */
    .price-wrap { margin-bottom: 0.5rem; }
    .price-box {
      display: inline-block;
      background: rgba(240,192,64,0.08);
      border: 2px solid #f0c040;
      border-radius: 18px;
      padding: 2rem 3.5rem;
      box-shadow: 0 0 50px rgba(240,192,64,0.2);
    }
    .price-label { font-size: 0.7rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; margin-bottom: 0.5rem; }
    .price-row { display: flex; align-items: center; justify-content: center; gap: 1.2rem; flex-wrap: wrap; }
    .price-old { font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; color: #5555aa; text-decoration: line-through; text-decoration-color: #cc3333; text-decoration-thickness: 3px; }
    .price-new { font-family: 'Cormorant Garamond', serif; font-size: 4.8rem; font-weight: 700; line-height: 1; background: linear-gradient(135deg, #f0c040, #f7dc6f); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .price-sub { font-size: 0.82rem; color: #8888cc; margin-top: 0.4rem; }

    /* CTA SECTION */
    .cta-sec {
      background: linear-gradient(160deg, #0d0d45 0%, #1c1c7a 50%, #0d0d45 100%);
      border-top: 3px solid #f0c040;
      border-bottom: 3px solid #f0c040;
      padding: 6rem 2rem;
      text-align: center;
      position: relative; overflow: hidden;
    }
    .cta-sec::before {
      content: '';
      position: absolute; top:50%; left:50%;
      transform: translate(-50%,-50%);
      width: 700px; height: 500px;
      background: radial-gradient(ellipse, rgba(240,192,64,0.12) 0%, transparent 70%);
      pointer-events: none;
    }
    .cta-inner { position: relative; z-index: 2; }
    .cta-sec h2 { font-size: clamp(2.2rem,5vw,3.5rem); font-weight:700; color:#ffffff; margin-bottom:0.6rem; }
    .cta-sec .closer { font-size: 1.1rem; color: #b0b8f0; max-width: 580px; margin: 0.5rem auto 2rem; line-height: 1.75; }

    .steps-wrap { max-width: 540px; margin: 0 auto; }
    .step-card {
      background: linear-gradient(135deg,#12124a,#0c0c35);
      border-radius: 16px; padding: 2.2rem 2rem;
      margin-bottom: 1.2rem; text-align: left;
    }
    .step-top { display:flex; align-items:center; gap:0.8rem; margin-bottom:0.8rem; }
    .step-badge {
      padding: 0.35rem 1rem; border-radius:50px;
      font-size:0.78rem; font-weight:800; letter-spacing:1px;
    }
    .step-badge.zelle-b { background:linear-gradient(135deg,#6d1ed4,#8b2be2); color:#fff; }
    .step-badge.wise-b { background:linear-gradient(135deg,#00b0ff,#1ac3ff); color:#fff; }
    .step-badge.text-b { background:rgba(240,192,64,0.15); border:1px solid #f0c040; color:#f0c040; }
    .step-title { font-family:'Cormorant Garamond',serif; color:#ffffff; font-size:1.5rem; font-weight:700; }

    .phone-box { background: rgba(240,192,64,0.08); border: 2px solid #f0c040; border-radius: 12px; padding: 1.2rem 1.5rem; margin-bottom: 0.6rem; }
    .phone-label { font-size:0.65rem; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#f0c040; margin-bottom:0.3rem; }
    .phone-num { font-family:'Cormorant Garamond',serif; font-size:2.8rem; font-weight:700; color:#f0c040; letter-spacing:2px; line-height:1; }
    .step-card p { color:#a0a8cc; font-size:0.97rem; line-height:1.7; max-width:none; margin:0; }
    .step-card strong { color:#f0c040; }
    .secure { font-size:0.82rem; color:#4444aa; margin-top:1.5rem; }

    footer { background: #04040f; border-top: 1px solid rgba(240,192,64,0.2); padding: 2.5rem 0; text-align:center; }
    footer .brand { font-family:'Cormorant Garamond',serif; font-size:1.4rem; color:#f0c040; letter-spacing:3px; text-transform:uppercase; margin-bottom:0.3rem; }
    footer p { font-size:0.83rem; color:#333388; max-width:none; }
    footer a { color:#5555aa; }

    @media(max-width:600px){
      .cta-sec { padding: 4rem 1.5rem; }
      .step-card { padding: 1.8rem 1.5rem; }
      .price-box { padding: 1.5rem 2rem; }
    }
  </style>
</head>
<body>

<!-- HERO -->
<section class="hero">
  <div class="hero-inner">
    <div class="presenter">Masterclass by Mironda Deel</div>
    <h1>Grow Your Cleaning Biz<br><span>in 2026</span></h1>
    <p class="hero-sub">How to attract premium clients, increase sales, and scale without burnout</p>
    <p class="hero-quote">"Freedom in business comes from systems and choosing clients that fit your values."</p>

    <div class="price-wrap">
      <div class="price-box">
        <div class="price-label">Private 1-on-1 Consultation</div>
        <div class="price-row">
          <span class="price-old">$299</span>
          <span class="price-new">$99</span>
        </div>
        <div class="price-sub">One private 60-minute session with Mironda &nbsp;·&nbsp; Limited spots</div>
      </div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- CTA SECTION: ZELLE + WISE -->
<section class="cta-sec">
  <div class="cta-inner">
    <span class="sec-label" style="color:#f0c040;">Book Your Private 1-on-1</span>
    <h2>Claim Your 60-Minute Session With Mironda</h2>
    <p class="closer">
      Work directly on your business, your clients, and your roadmap.  
      Walk away with actionable steps you can implement immediately.
    </p>

    <div class="zelle-price">
      <span class="old2">$299</span>
      <span class="new2">$99</span>
      <span class="tag">Limited spots available · Book now to lock in your time</span>
    </div>

    <div class="steps-wrap">

      <!-- STEP 1: ZELLE -->
      <div class="step-card step1">
        <div class="step-top">
          <span class="step-badge zelle-b">⚡ Option 1</span>
          <span class="step-title">Pay with Zelle</span>
        </div>
        <div class="phone-box">
          <div class="phone-label">Zelle Number</div>
          <div class="phone-num">770-369-6875</div>
        </div>
        <p>Open your banking app, select Zelle, and send <strong>$99</strong> to the number above to reserve your spot.</p>
      </div>

      <!-- STEP 2: WISE -->
      <div class="step-card step2">
        <div class="step-top">
          <span class="step-badge wise-b">💫 Option 2</span>
          <span class="step-title">Pay with Wise</span>
        </div>
        <div class="phone-box">
          <div class="phone-label">Wise Payment Link</div>
          <div class="phone-num"><a href="https://wise.com/pay/me/mirondad" target="_blank" style="color:#00b0ff;text-decoration:underline;">Send $99 via Wise</a></div>
        </div>
        <p>Click the link, follow the secure Wise payment process, and reserve your private session instantly.</p>
      </div>

      <!-- STEP 3: CONFIRM -->
      <div class="step-card step2">
        <div class="step-top">
          <span class="step-badge text-b">📱 Step 3</span>
          <span class="step-title">Text to Confirm</span>
        </div>
        <div class="phone-box">
          <div class="phone-label">Text This Number</div>
          <div class="phone-num">770-369-6875</div>
        </div>
        <p>After sending payment via Zelle or Wise, text your <strong>name + "PAID"</strong> to <strong>770-369-6875</strong> to secure your appointment time.</p>
      </div>

    </div>
    <p class="secure">🔒 Secure · Instant · No account required for Zelle or Wise</p>
  </div>
</section>

<hr class="divider">

<!-- FOOTER -->
<footer>
  <div class="wrap">
    <div class="brand">Meticulous Quality</div>
    <p>© 2026 Mironda Deel · Meticulous Quality · Growth Consulting for Cleaning Businesses</p>
    <p style="margin-top:0.3rem;"><a href="https://meticulousquality.com">meticulousquality.com</a></p>
  </div>
</footer>

</body>
</html>
"""

components.html(html, height=10000)
