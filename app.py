import streamlit as st
import streamlit.components.v1 as components
import base64

with open("/mnt/user-data/uploads/PHOTO-2026-02-24-22-29-51.jpg", "rb") as f:
    img_data = base64.b64encode(f.read()).decode()

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
</style>
""", unsafe_allow_html=True)

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      font-family: 'DM Sans', sans-serif;
      background: #08082a;
      color: #e8e8ff;
      line-height: 1.75;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }}
    h1,h2,h3,h4 {{ font-family: 'Cormorant Garamond', serif; line-height: 1.15; }}
    .wrap {{ max-width: 860px; margin: 0 auto; padding: 0 2rem; }}
    .divider {{ height: 1px; background: linear-gradient(90deg, transparent, #f0c040, transparent); border: none; margin: 0; }}
    .gold {{ color: #f0c040; }}
    .white {{ color: #ffffff; }}

    /* ── HERO ── */
    .hero {{
      background: linear-gradient(160deg, #0d0d45 0%, #1c1c7a 45%, #0d0d45 100%);
      border-bottom: 3px solid #f0c040;
      padding: 5rem 2rem 4.5rem;
      text-align: center;
      position: relative;
      overflow: hidden;
    }}
    .hero::before {{
      content: '';
      position: absolute; inset: 0;
      background: radial-gradient(ellipse 70% 60% at 50% 30%, rgba(240,192,64,0.13) 0%, transparent 65%);
      pointer-events: none;
    }}
    .hero-inner {{ position: relative; z-index: 2; }}
    .hero-photo {{
      width: 130px; height: 130px; border-radius: 50%;
      object-fit: cover; object-position: center top;
      border: 3px solid #f0c040;
      box-shadow: 0 0 30px rgba(240,192,64,0.45);
      margin: 0 auto 1.2rem;
      display: block;
    }}
    .presenter {{
      font-size: 0.78rem; font-weight: 700; letter-spacing: 3px;
      text-transform: uppercase; color: #f0c040; margin-bottom: 0.6rem;
    }}
    .hero h1 {{
      font-size: clamp(2.4rem, 5.5vw, 4.2rem); font-weight: 700;
      color: #ffffff; margin-bottom: 0.8rem; line-height: 1.1;
    }}
    .hero h1 span {{
      background: linear-gradient(135deg, #f0c040, #f7dc6f, #fff8d6);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    }}
    .hero-sub {{
      font-size: 1.15rem; color: #b0b8f0; max-width: 640px;
      margin: 0.8rem auto 2rem; line-height: 1.8;
    }}
    .hero-quote {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 1.3rem; font-style: italic;
      color: #f0c040; margin-bottom: 2.5rem; max-width: 600px; margin-inline: auto;
    }}

    /* ── PRICE BOX ── */
    .price-wrap {{ margin-bottom: 0.5rem; }}
    .price-box {{
      display: inline-block;
      background: rgba(240,192,64,0.08);
      border: 2px solid #f0c040;
      border-radius: 18px;
      padding: 2rem 3.5rem;
      box-shadow: 0 0 50px rgba(240,192,64,0.2);
    }}
    .price-label {{ font-size: 0.7rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; margin-bottom: 0.5rem; }}
    .price-row {{ display: flex; align-items: center; justify-content: center; gap: 1.2rem; flex-wrap: wrap; }}
    .price-old {{ font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; color: #5555aa; text-decoration: line-through; text-decoration-color: #cc3333; text-decoration-thickness: 3px; }}
    .price-new {{ font-family: 'Cormorant Garamond', serif; font-size: 4.8rem; font-weight: 700; line-height: 1; background: linear-gradient(135deg, #f0c040, #f7dc6f); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }}
    .price-sub {{ font-size: 0.82rem; color: #8888cc; margin-top: 0.4rem; }}

    /* ── SECTIONS ── */
    .sec {{ padding: 4.5rem 0; }}
    .sec-blue {{ background: #060620; }}
    .sec-label {{ font-size: 0.7rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #f0c040; display: block; margin-bottom: 0.8rem; }}
    .sec-title {{ font-size: clamp(1.9rem, 4vw, 2.9rem); font-weight: 700; color: #ffffff; margin-bottom: 0.5rem; }}
    .gold-bar {{ width: 50px; height: 2px; background: linear-gradient(90deg, transparent, #f0c040, transparent); margin: 1rem auto 0; }}
    .gold-bar-left {{ margin-left: 0; }}

    /* ── TRUTH BOX ── */
    .truth-box {{
      background: rgba(240,192,64,0.06);
      border-left: 4px solid #f0c040;
      border-radius: 0 10px 10px 0;
      padding: 1.5rem 2rem;
      margin: 2.5rem 0;
      font-family: 'Cormorant Garamond', serif;
      font-size: 1.35rem; font-style: italic;
      color: #f0c040; line-height: 1.5;
    }}

    /* ── PAIN GRID ── */
    .pain-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px,1fr)); gap: 1.4rem; margin-top: 2.5rem; }}
    .pain-card {{
      background: linear-gradient(135deg, #12124a, #0c0c35);
      border: 1px solid rgba(240,192,64,0.2);
      border-radius: 10px; padding: 1.8rem;
      border-top: 3px solid #f0c040;
    }}
    .pain-card h4 {{ color: #f0c040; font-size: 1.05rem; margin-bottom: 0.5rem; }}
    .pain-card p {{ color: #9090cc; font-size: 0.93rem; max-width: none; line-height: 1.6; }}

    /* ── 3 PARTS STRIP ── */
    .parts-strip {{ display: grid; grid-template-columns: repeat(3,1fr); gap: 1.2rem; margin-top: 2.5rem; }}
    @media(max-width:600px){{ .parts-strip {{ grid-template-columns: 1fr; }} }}
    .part-block {{
      background: linear-gradient(160deg, #1c1c7a, #0d0d45);
      border: 1px solid rgba(240,192,64,0.25);
      border-radius: 12px; padding: 2rem 1.5rem; text-align: center;
      transition: border-color 0.3s, transform 0.3s;
    }}
    .part-block:hover {{ border-color: #f0c040; transform: translateY(-4px); }}
    .part-num {{ font-family: 'Cormorant Garamond', serif; font-size: 3rem; font-weight: 700; background: linear-gradient(135deg,#f0c040,#f7dc6f); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; line-height:1; margin-bottom:0.5rem; }}
    .part-block h4 {{ color: #ffffff; font-size: 1.1rem; margin-bottom: 0.6rem; }}
    .part-block p {{ color: #9090cc; font-size: 0.88rem; max-width: none; line-height: 1.6; }}

    /* ── LESSON ROWS ── */
    .lesson {{ border-bottom: 1px solid rgba(240,192,64,0.12); padding: 2rem 0; }}
    .lesson:last-child {{ border-bottom: none; }}
    .lesson-head {{ display: flex; align-items: flex-start; gap: 1.2rem; margin-bottom: 0.8rem; }}
    .lesson-icon {{ font-size: 1.8rem; flex-shrink: 0; margin-top: 0.1rem; }}
    .lesson-head h4 {{ color: #f0c040; font-size: 1.2rem; margin-bottom: 0.2rem; }}
    .lesson-head p.sub {{ color: #b0b8f0; font-size: 0.95rem; max-width: none; line-height: 1.6; margin: 0; }}
    .lesson-points {{ list-style: none; padding-left: 3.2rem; }}
    .lesson-points li {{ position: relative; padding-left: 1.5rem; color: #9090cc; font-size: 0.93rem; margin-bottom: 0.4rem; }}
    .lesson-points li::before {{ content: '✦'; position: absolute; left: 0; color: #f0c040; font-size: 0.65rem; top: 0.35rem; }}

    /* ── COMPARE TABLE ── */
    .compare {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 2.5rem; }}
    @media(max-width:560px){{ .compare {{ grid-template-columns: 1fr; }} }}
    .compare-col {{ border-radius: 12px; padding: 1.8rem; }}
    .compare-col.old {{ background: rgba(100,100,180,0.08); border: 1px solid rgba(100,100,180,0.2); }}
    .compare-col.new {{ background: rgba(240,192,64,0.07); border: 2px solid #f0c040; }}
    .compare-col h4 {{ font-size: 1rem; margin-bottom: 1rem; padding-bottom: 0.6rem; border-bottom: 1px solid rgba(255,255,255,0.1); }}
    .compare-col.old h4 {{ color: #8888bb; }}
    .compare-col.new h4 {{ color: #f0c040; }}
    .compare-col p {{ font-size: 1.3rem; font-family:'Cormorant Garamond',serif; margin-bottom: 0.8rem; max-width: none; }}
    .compare-col.old p {{ color: #6060aa; }}
    .compare-col.new p {{ color: #f0c040; font-weight: 600; }}
    .compare-col small {{ color: #7070aa; font-size: 0.83rem; }}

    /* ── STATS ── */
    .stats-row {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(160px,1fr)); gap: 1.4rem; margin-top: 2.5rem; }}
    .stat-box {{
      background: linear-gradient(135deg,#12124a,#0c0c35);
      border: 1px solid rgba(240,192,64,0.22);
      border-radius: 10px; padding: 1.8rem 1rem; text-align: center;
      transition: border-color 0.3s, transform 0.3s;
    }}
    .stat-box:hover {{ border-color: #f0c040; transform: translateY(-4px); }}
    .stat-num {{ font-family:'Cormorant Garamond',serif; font-size: 3.2rem; font-weight:700; display: block; margin-bottom: 0.4rem; background: linear-gradient(135deg,#f0c040,#f7dc6f); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; line-height:1; }}
    .stat-box p {{ font-size: 0.82rem; color: #7070aa; max-width: none; }}

    /* ── ZELLE CTA ── */
    .zelle-sec {{
      background: linear-gradient(160deg, #0d0d45 0%, #1c1c7a 50%, #0d0d45 100%);
      border-top: 3px solid #f0c040;
      border-bottom: 3px solid #f0c040;
      padding: 6rem 2rem;
      text-align: center;
      position: relative; overflow: hidden;
    }}
    .zelle-sec::before {{
      content: '';
      position: absolute; top:50%; left:50%;
      transform: translate(-50%,-50%);
      width: 700px; height: 500px;
      background: radial-gradient(ellipse, rgba(240,192,64,0.12) 0%, transparent 70%);
      pointer-events: none;
    }}
    .zelle-inner {{ position: relative; z-index: 2; }}
    .zelle-sec h2 {{ font-size: clamp(2.2rem,5vw,3.5rem); font-weight:700; color:#ffffff; margin-bottom:0.6rem; }}
    .zelle-sec .closer {{
      font-size: 1.1rem; color: #b0b8f0; max-width: 580px;
      margin: 0.5rem auto 2rem; line-height: 1.75;
    }}
    .zelle-price {{ margin-bottom: 2.5rem; }}
    .zelle-price .old2 {{ font-family:'Cormorant Garamond',serif; font-size:2.2rem; color:#4444aa; text-decoration:line-through; text-decoration-color:#cc3333; text-decoration-thickness:3px; margin-right:0.8rem; }}
    .zelle-price .new2 {{ font-family:'Cormorant Garamond',serif; font-size:5rem; font-weight:700; line-height:1; background:linear-gradient(135deg,#f0c040,#f7dc6f); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }}
    .zelle-price .tag {{ display:block; font-size:0.82rem; color:#6666aa; margin-top:0.4rem; }}

    .steps-wrap {{ max-width: 540px; margin: 0 auto; }}
    .step-card {{
      background: linear-gradient(135deg,#12124a,#0c0c35);
      border-radius: 16px; padding: 2.2rem 2rem;
      margin-bottom: 1.2rem;
      text-align: left;
    }}
    .step-card.step1 {{ border: 2px solid #6d1ed4; }}
    .step-card.step2 {{ border: 2px solid rgba(240,192,64,0.5); }}
    .step-top {{ display:flex; align-items:center; gap:0.8rem; margin-bottom:0.8rem; }}
    .step-badge {{
      padding: 0.35rem 1rem; border-radius:50px;
      font-size:0.78rem; font-weight:800; letter-spacing:1px;
    }}
    .step-badge.zelle-b {{ background:linear-gradient(135deg,#6d1ed4,#8b2be2); color:#fff; }}
    .step-badge.text-b {{ background:rgba(240,192,64,0.15); border:1px solid #f0c040; color:#f0c040; }}
    .step-title {{ font-family:'Cormorant Garamond',serif; color:#ffffff; font-size:1.5rem; font-weight:700; }}

    .phone-box {{
      background: rgba(240,192,64,0.08);
      border: 2px solid #f0c040;
      border-radius: 12px; padding: 1.2rem 1.5rem;
      margin-bottom: 0.6rem;
    }}
    .phone-label {{ font-size:0.65rem; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#f0c040; margin-bottom:0.3rem; }}
    .phone-num {{ font-family:'Cormorant Garamond',serif; font-size:2.8rem; font-weight:700; color:#f0c040; letter-spacing:2px; line-height:1; }}
    .step-card p {{ color:#a0a8cc; font-size:0.97rem; line-height:1.7; max-width:none; margin:0; }}
    .step-card strong {{ color:#f0c040; }}
    .secure {{ font-size:0.82rem; color:#4444aa; margin-top:1.5rem; }}

    /* ── GUARANTEE ── */
    .guarantee {{
      background: linear-gradient(135deg,#12124a,#0c0c35);
      border: 1px solid rgba(240,192,64,0.25);
      border-radius: 14px; padding: 3rem;
      text-align: center;
    }}
    .guarantee h3 {{ color:#f0c040; font-size:2rem; margin-bottom:0.8rem; }}
    .guarantee p {{ color:#a0a8cc; font-size:1rem; max-width:520px; margin:0 auto; line-height:1.8; }}

    /* ── FOOTER ── */
    footer {{
      background: #04040f;
      border-top: 1px solid rgba(240,192,64,0.2);
      padding: 2.5rem 0; text-align:center;
    }}
    footer .brand {{ font-family:'Cormorant Garamond',serif; font-size:1.4rem; color:#f0c040; letter-spacing:3px; text-transform:uppercase; margin-bottom:0.3rem; }}
    footer p {{ font-size:0.83rem; color:#333388; max-width:none; }}
    footer a {{ color:#5555aa; }}

    @media(max-width:600px){{
      .zelle-sec {{ padding: 4rem 1.5rem; }}
      .step-card {{ padding: 1.8rem 1.5rem; }}
      .price-box {{ padding: 1.5rem 2rem; }}
    }}
  </style>
</head>
<body>

<!-- ══ HERO ══ -->
<section class="hero">
  <div class="hero-inner">
    <img class="hero-photo" src="data:image/jpeg;base64,{img_data}" alt="Mironda Deel">
    <div class="presenter">Masterclass by Mironda Deel</div>
    <h1>Grow Your Cleaning Biz<br><span>in 2026 — Starting Tomorrow</span></h1>
    <p class="hero-sub">How to Attract Premium Clients, Increase Sales, and Scale Without Burnout</p>
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

<!-- ══ THE HARD TRUTH ══ -->
<section class="sec">
  <div class="wrap">
    <span class="sec-label">Why Most Cleaning Businesses Fail</span>
    <h2 class="sec-title">You're Working Hard.<br>But Are You Building Wealth?</h2>
    <div class="gold-bar"></div>

    <div class="truth-box">
      "If you're always busy but not making money, you don't have a marketing problem. You have a pricing problem."
    </div>

    <div class="pain-grid">
      <div class="pain-card">
        <h4>❌ Wrong Clients</h4>
        <p>Attracting clients who don't value your expertise — constantly haggling and disrespecting your time.</p>
      </div>
      <div class="pain-card">
        <h4>❌ Wrong Prices</h4>
        <p>Charging based on fear and competition instead of the real value you deliver. Staying busy but staying broke.</p>
      </div>
      <div class="pain-card">
        <h4>❌ No Systems</h4>
        <p>Trying to be the cleaner, scheduler, bookkeeper, and boss — all at once. The fast track to burnout.</p>
      </div>
    </div>

    <p style="color:#6060aa;font-size:0.9rem;text-align:center;margin-top:2rem;">
      Success is built on <span class="gold">Systems, Leadership, and Standards.</span>
    </p>
  </div>
</section>

<hr class="divider">

<!-- ══ WHAT WE COVERED ══ -->
<section class="sec sec-blue">
  <div class="wrap">
    <div style="text-align:center;">
      <span class="sec-label">The Masterclass</span>
      <h2 class="sec-title">3 Core Areas We Just Went Through</h2>
      <div class="gold-bar"></div>
    </div>
    <div class="parts-strip" style="margin-top:2.5rem;">
      <div class="part-block">
        <div class="part-num">1</div>
        <h4>Attract Premium Clients</h4>
        <p>Niche positioning, premium communication that filters out 50% of low-value leads, and visible culture that sells for you.</p>
      </div>
      <div class="part-block">
        <div class="part-num">2</div>
        <h4>Increase Revenue</h4>
        <p>Service bundles, outcome-based pricing, and annual reviews that stop you from paying the "growth tax" yourself.</p>
      </div>
      <div class="part-block">
        <div class="part-num">3</div>
        <h4>Retain Without Burnout</h4>
        <p>Clear standards, a systematic follow-up process, and leading your team so you make decisions — not tasks.</p>
      </div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- ══ KEY LESSONS ══ -->
<section class="sec">
  <div class="wrap">
    <span class="sec-label">What You Learned Today</span>
    <h2 class="sec-title">The Strategies That Change Everything</h2>
    <div class="gold-bar" style="margin-bottom:0.5rem;"></div>

    <div class="lesson">
      <div class="lesson-head">
        <div class="lesson-icon">🎯</div>
        <div>
          <h4>Niche Down to Price Up</h4>
          <p class="sub">Stop trying to serve everyone. The "we clean everything" trap is a race to the bottom on price.</p>
        </div>
      </div>
      <ul class="lesson-points">
        <li>Vacation rentals — reliability is the #1 priority, command premium rates</li>
        <li>Residential luxury — busy professionals who value consistency and privacy</li>
        <li>Niche = Trust = Higher Price. Every time.</li>
      </ul>
    </div>

    <div class="lesson">
      <div class="lesson-head">
        <div class="lesson-icon">💬</div>
        <div>
          <h4>Premium Communication Filters Leads</h4>
          <p class="sub">Your first words set the tone. The wrong language attracts the wrong clients.</p>
        </div>
      </div>
      <ul class="lesson-points">
        <li><span class="gold">Instead of:</span> "When do you want cleaning?"</li>
        <li><span class="gold">Say:</span> "We'd love to learn about your property so we can match you with the right team and service level."</li>
        <li>This shift immediately filters out 50% of low-quality leads</li>
      </ul>
    </div>

    <div class="lesson">
      <div class="lesson-head">
        <div class="lesson-icon">💰</div>
        <div>
          <h4>Stop Selling Hours — Sell Outcomes</h4>
          <p class="sub">Selling your time makes you a commodity. Premium clients buy results, not hours.</p>
        </div>
      </div>

      <div class="compare">
        <div class="compare-col old">
          <h4>❌ The Commodity Way</h4>
          <p>"$30 per hour"</p>
          <small>Encourages inefficiency. Makes you replaceable. No ceiling on your time.</small>
        </div>
        <div class="compare-col new">
          <h4>✅ The Premium Way</h4>
          <p>"$180 for a full property reset"</p>
          <small>Clear result. Predictable cost. No surprises. Premium clients love this.</small>
        </div>
      </div>
    </div>

    <div class="lesson">
      <div class="lesson-head">
        <div class="lesson-icon">📦</div>
        <div>
          <h4>Bundle Services for Higher Value</h4>
          <p class="sub">Never sell "just cleaning." Bundle and become a full-service partner, not a vendor.</p>
        </div>
      </div>
      <ul class="lesson-points">
        <li>Vacation Rentals: Deep clean + linen service + restocking + damage checks</li>
        <li>Home Clients: Maintenance plans + seasonal add-ons + oven/fridge services</li>
        <li>Bundling increases ticket size, client commitment, and perceived value</li>
      </ul>
    </div>

    <div class="lesson">
      <div class="lesson-head">
        <div class="lesson-icon">🔄</div>
        <div>
          <h4>Retention is a System, Not Luck</h4>
          <p class="sub">You can't hope clients stay. You build the system that keeps them.</p>
        </div>
      </div>
      <ul class="lesson-points">
        <li><span class="gold">After every service:</span> Short check-in message to confirm standards were met</li>
        <li><span class="gold">Monthly:</span> "How can we improve?" — catch issues before they become churn</li>
        <li><span class="gold">Quarterly:</span> Account reviews + seasonal upsells ("High season is coming — add a deep clean?")</li>
      </ul>
    </div>

    <div class="lesson">
      <div class="lesson-head">
        <div class="lesson-icon">👑</div>
        <div>
          <h4>Lead Your Team — Stop Being the Bottleneck</h4>
          <p class="sub">If everything runs through you, you own a stressful job — not a business.</p>
        </div>
      </div>
      <ul class="lesson-points">
        <li>Clear roles + trained supervisors + documented processes</li>
        <li>Your job becomes: Decisions, not tasks</li>
        <li>Build systems, not dependency — that's how you scale</li>
      </ul>
    </div>

  </div>
</section>

<hr class="divider">

<!-- ══ MIRONDA'S RESULTS ══ -->
<section class="sec sec-blue">
  <div class="wrap" style="text-align:center;">
    <span class="sec-label">Why Listen to Mironda</span>
    <h2 class="sec-title">She Built a 7-Figure Cleaning Business From Scratch</h2>
    <div class="gold-bar"></div>
    <p style="color:#8080cc;margin:1.2rem auto 2rem;max-width:560px;font-size:1rem;line-height:1.8;">
      Founder of VIDeMI Services. Leader of a 40+ person team. She's done exactly what she just taught you — and now she's handing you the blueprint in a private session.
    </p>
    <div class="stats-row">
      <div class="stat-box"><span class="stat-num">7-Fig</span><p>Cleaning Business Built</p></div>
      <div class="stat-box"><span class="stat-num">40+</span><p>Team Members Led</p></div>
      <div class="stat-box"><span class="stat-num">3×</span><p>Avg Revenue Growth</p></div>
      <div class="stat-box"><span class="stat-num">50+</span><p>Hrs/Week Saved with Systems</p></div>
    </div>
  </div>
</section>

<hr class="divider">

<!-- ══ CLOSER COPY ══ -->
<section class="sec">
  <div class="wrap" style="text-align:center;">
    <span class="sec-label">The Next Step</span>
    <h2 class="sec-title">You Just Saw the Blueprint.<br>Now Let's Build Yours.</h2>
    <div class="gold-bar"></div>
    <p style="color:#8080cc;margin:1.5rem auto;max-width:620px;font-size:1.05rem;line-height:1.85;">
      Everything in that masterclass — the premium positioning, the pricing strategy, the retention system — works. But only when it's applied to <em style="color:#f0c040;">your</em> business, your clients, your team.
    </p>
    <p style="color:#8080cc;margin:0 auto 1.5rem;max-width:620px;font-size:1.05rem;line-height:1.85;">
      In your private 60-minute session with Mironda, we take everything you just learned and map it directly to where you are right now — so you leave with a real action plan, not just notes.
    </p>
    <div class="truth-box" style="max-width:600px;margin:1.5rem auto;">
      "Premium clients deserve premium teams. And premium teams deserve a leader who builds systems — not chaos."
    </div>
  </div>
</section>

<hr class="divider">

<!-- ══ ZELLE CTA ══ -->
<section class="zelle-sec">
  <div class="zelle-inner">
    <span class="sec-label" style="color:#f0c040;">It's Tomorrow. Start Today.</span>
    <h2>Claim Your 1-on-1 Session</h2>
    <p class="closer">
      60 minutes. Private. Focused entirely on your business.<br>
      Walk away with your personal roadmap — or your money back.
    </p>

    <div class="zelle-price">
      <span class="old2">$299</span>
      <span class="new2">$99</span>
      <span class="tag">Limited spots available · Book now to lock in your time</span>
    </div>

    <div class="steps-wrap">

      <!-- STEP 1 -->
      <div class="step-card step1">
        <div class="step-top">
          <span class="step-badge zelle-b">⚡ Step 1</span>
          <span class="step-title">Send $99 via Zelle</span>
        </div>
        <div class="phone-box">
          <div class="phone-label">Zelle Number</div>
          <div class="phone-num">770-369-6875</div>
        </div>
        <p>Open your banking app, select Zelle, and send <strong>$99</strong> to the number above to reserve your spot.</p>
      </div>

      <!-- STEP 2 -->
      <div class="step-card step2">
        <div class="step-top">
          <span class="step-badge text-b">📱 Step 2</span>
          <span class="step-title">Text to Confirm</span>
        </div>
        <div class="phone-box">
          <div class="phone-label">Text This Number</div>
          <div class="phone-num">770-369-6875</div>
        </div>
        <p>After sending payment, text your <strong>name + "PAID"</strong> to <strong>770-369-6875</strong> and your appointment time will be confirmed.</p>
      </div>

    </div>

    <p class="secure">🔒 &nbsp; Secure &nbsp;·&nbsp; Instant &nbsp;·&nbsp; No account required to receive Zelle</p>
  </div>
</section>

<hr class="divider">

<!-- ══ GUARANTEE ══ -->
<section class="sec sec-blue">
  <div class="wrap">
    <div class="guarantee">
      <div style="font-size:3rem;margin-bottom:1rem;">🛡️</div>
      <h3>100% Satisfaction Guarantee</h3>
      <p>If you don't walk away with at least 3 clear, actionable steps to grow your cleaning business — we'll refund your $99 in full. No questions asked.</p>
    </div>
  </div>
</section>

<hr class="divider">

<!-- ══ FOOTER ══ -->
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

components.html(html, height=7200, scrolling=False)
