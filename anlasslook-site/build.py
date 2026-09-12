# -*- coding: utf-8 -*-
"""Baut die komplette statische Website anlasslook.de nach ./dist"""
import os, re, shutil, html, datetime
from content import SITE, CATEGORIES, POSTS

ROOT = os.path.dirname(os.path.abspath(__file__))
# Zielordner. Standard ist ./dist. Über ANLASSLOOK_DIST lässt sich der Build
# in einen Ordner ausserhalb des iCloud-Ordners legen - dort darf gelöscht
# werden, im verbundenen Ordner nicht.
DIST = os.environ.get("ANLASSLOOK_DIST") or os.path.join(ROOT, "dist")
TODAY = "2026-09-11"
RSS_DATE = "Fri, 11 Sep 2026 09:00:00 +0200"

CATBY = {c["slug"]: c for c in CATEGORIES}

# Fallback-Farbe pro Bild, damit die Seite auch ohne Foto gestaltet aussieht
TINT = {
 "hero.jpg":"#E6D8C9","cat-hochzeitsgast.jpg":"#E2CFC4","cat-standesamt.jpg":"#EDE6DD",
 "cat-buero.jpg":"#D9D6CF","cat-herbst.jpg":"#D7CDB4","cat-festtage.jpg":"#C9B7B0",
 "cat-accessoires.jpg":"#E4D6C2","post-brosche.jpg":"#D6CCC0","post-guertel.jpg":"#DED3C4",
 "post-tuch.jpg":"#E3D2C6","post-blazer.jpg":"#EBE5DC",
}
def tint(img):
    return TINT.get(img, "#F2EAE1")


# ----------------------------------------------------------------- Helfer
def amazon(keyword):
    """Amazon-Suchlink. Tracking-ID wird nur angehängt, wenn sie gesetzt ist."""
    k = re.sub(r"\s+", "+", keyword.strip())
    tag = SITE["amazon_tag"].strip()
    # &i=fashion haelt die Suche in der Abteilung Mode (Bekleidung, Schuhe,
    # Taschen, Schmuck, Uhren) - das ist zugleich die 6-%-Provisionskategorie.
    url = f"https://www.amazon.de/s?k={k}&i=fashion"
    if tag:
        url += f"&tag={tag}"
    return url


def e(s):
    return html.escape(s, quote=True)


def write(path, content):
    full = os.path.join(DIST, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def depth_prefix(path):
    """Relativer Pfad zurück zum Wurzelverzeichnis."""
    d = path.count("/")
    return "../" * d if d else ""


# ----------------------------------------------------------------- Layout
def page(path, title, description, body, og_image=None, extra_head="", og_type="website"):
    p = depth_prefix(path)
    canonical = SITE["url"] + "/" + (path.replace("index.html", "") if path != "index.html" else "")
    og = og_image or "hero.jpg"
    nav = "".join(
        f'<a href="{p}anlaesse/{c["slug"]}/">{e(c.get("nav", c["title"]))}</a>' for c in CATEGORIES
    )
    pin_tag = ""
    if SITE["pinterest_tag_id"]:
        pin_tag = f"""
<script>
!function(e){{if(!window.pintrk){{window.pintrk=function(){{window.pintrk.queue.push(
Array.prototype.slice.call(arguments))}};var n=window.pintrk;n.queue=[],n.version="3.0";
var t=document.createElement("script");t.async=!0,t.src=e;var r=document.getElementsByTagName("script")[0];
r.parentNode.insertBefore(t,r)}}}}("https://s.pinimg.com/ct/core.js");
pintrk('load','{SITE["pinterest_tag_id"]}');pintrk('page');
</script>"""


    ga_tag = ""
    cbanner = ""
    if SITE.get("ga4_id"):
        gid = SITE["ga4_id"]
        ga_tag = """
<script>
(function(){
  var KEY = "al_consent";
  window.alLoadGA = function(){
    if (window.__alga) return; window.__alga = 1;
    var s = document.createElement("script"); s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=__GID__";
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function(){ dataLayer.push(arguments); };
    gtag("js", new Date());
    gtag("config", "__GID__", { anonymize_ip: true, allow_google_signals: false, allow_ad_personalization_signals: false });
  };
  window.alConsent = function(v){
    try { localStorage.setItem(KEY, v); } catch(e){}
    var b = document.getElementById("cbanner"); if (b) b.style.display = "none";
    if (v === "granted") alLoadGA();
  };
  window.alReset = function(){
    try { localStorage.removeItem(KEY); } catch(e){}
    location.reload();
  };
  var v = null; try { v = localStorage.getItem(KEY); } catch(e){}
  if (v === "granted") { alLoadGA(); }
  else if (v !== "denied") {
    document.addEventListener("DOMContentLoaded", function(){
      var b = document.getElementById("cbanner"); if (b) b.style.display = "block";
    });
  }
})();
</script>""".replace("__GID__", gid)
        _btn = ("display:inline-block;font:inherit;font-size:15px;padding:11px 20px;"
                "border-radius:4px;cursor:pointer;border:1px solid #231F1C;")
        cbanner = f'''
<div id="cbanner" role="dialog" aria-label="Hinweis zur Messung" style="display:none;position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#FBF8F4;border-top:1px solid #e3ddd4;padding:18px 20px;box-shadow:0 -6px 24px rgba(0,0,0,.10)">
  <div style="max-width:900px;margin:0 auto;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between">
    <p style="margin:0;font-size:15px;line-height:1.5;flex:1 1 300px">Darf Anlasslook mit Google Analytics messen, über welchen Kanal du hierher gefunden hast? Das ist freiwillig und du kannst es jederzeit widerrufen. <a href="{p}datenschutz/">Mehr dazu</a></p>
    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <button type="button" onclick="alConsent(&quot;denied&quot;)" style="{_btn}background:#FBF8F4;color:#231F1C">Nur notwendig</button>
      <button type="button" onclick="alConsent(&quot;granted&quot;)" style="{_btn}background:#231F1C;color:#FBF8F4">Einverstanden</button>
    </div>
  </div>
</div>'''

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta name="p:domain_verify" content="ed1f2adf1972a38c1ade451b298c23a6">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{e(SITE['name'])}">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:image" content="{SITE['url']}/assets/img/{og}">
<meta property="og:locale" content="de_DE">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="{p}assets/style.css">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="{e(SITE['name'])}" href="{SITE['url']}/feed.xml">
{extra_head}{pin_tag}{ga_tag}
</head>
<body>
<a class="skip" href="#main">Zum Inhalt springen</a>

<header class="site-head">
  <div class="wrap head-inner">
    <a class="logo" href="{p}">
      <span class="logo-mark">Anlasslook</span>
      <span class="logo-sub">Was ziehe ich an?</span>
    </a>
    <input type="checkbox" id="navtoggle" class="navtoggle">
    <label for="navtoggle" class="burger" aria-label="Menü"><span></span><span></span><span></span></label>
    <nav class="site-nav">{nav}<a class="nav-about" href="{p}ueber-uns/">Über uns</a></nav>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="site-foot">
  <div class="wrap foot-grid">
    <div>
      <div class="foot-logo">Anlasslook</div>
      <p class="foot-claim">Komplette Outfits für echte Anlässe.<br>Unabhängig zusammengestellt, jede Woche neu.</p>
    </div>
    <div>
      <h4>Anlässe</h4>
      {"".join(f'<a href="{p}anlaesse/{c["slug"]}/">{e(c["title"])}</a>' for c in CATEGORIES)}
    </div>
    <div>
      <h4>Seite</h4>
      <a href="{p}ueber-uns/">Über uns</a>
      <a href="{p}werbehinweis/">Werbehinweis</a>
      <a href="{p}impressum/">Impressum</a>
      <a href="{p}datenschutz/">Datenschutz</a>
      <a href="https://de.pinterest.com/{SITE['pinterest_user']}/" rel="noopener nofollow" target="_blank">Pinterest</a>
    </div>
  </div>
  <div class="wrap foot-legal">
    <p>Als Amazon-Partner verdienen wir an qualifizierten Verkäufen. Alle mit einem Sternchen (*) gekennzeichneten Links sind Werbelinks – für dich ändert sich der Preis dadurch nicht.</p>
    <p>© {datetime.date.today().year} {SITE['name']} · {SITE['domain']}</p>
  </div>
</footer>
{cbanner}
</body>
</html>"""


# ----------------------------------------------------------------- Bausteine
def ad_notice():
    return """<div class="adnotice"><strong>Werbehinweis:</strong> Dieser Beitrag enthält Werbelinks (mit * markiert).
Kaufst du über einen dieser Links, erhalten wir eine Provision. Für dich ändert sich der Preis nicht.
Als Amazon-Partner verdienen wir an qualifizierten Verkäufen.</div>"""


def product_block(products, heading="Das gehört ins Outfit"):
    items = []
    for name, why, kw in products:
        items.append(f"""    <li class="prod">
      <div class="prod-body">
        <h3>{e(name)}</h3>
        <p>{e(why)}</p>
      </div>
      <a class="prod-btn" href="{amazon(kw)}" rel="sponsored nofollow noopener" target="_blank">Bei Amazon ansehen<span class="star">*</span></a>
    </li>""")
    return f"""<section class="products">
  <h2>{e(heading)}</h2>
  <p class="prod-hint">Die Links führen zu einer Amazon-Suche, damit dir immer die aktuelle Auswahl und der aktuelle Preis angezeigt werden.</p>
  <ul class="prod-list">
{chr(10).join(items)}
  </ul>
</section>"""


def post_card(pst, p=""):
    c = CATBY[pst["cat"]]
    return f"""<article class="card">
  <a href="{p}beitraege/{pst['slug']}/">
    <div class="card-img" style="background-color:{tint(pst['img'])};background-image:url({p}assets/img/{pst['img']})"></div>
    <div class="card-body">
      <span class="card-cat">{e(c['title'])}</span>
      <h3>{e(pst['title'])}</h3>
      <p>{e(pst['teaser'])}</p>
    </div>
  </a>
</article>"""


# ----------------------------------------------------------------- Seiten
def build_home():
    feat = POSTS[0]
    rest = POSTS[1:10]
    cats = "".join(f"""<a class="cat-tile" href="anlaesse/{c['slug']}/">
      <div class="cat-img" style="background-color:{tint(c['img'])};background-image:url(assets/img/{c['img']})"></div>
      <div class="cat-txt"><h3>{e(c['title'])}</h3><p>{e(c['lead'])}</p></div>
    </a>""" for c in CATEGORIES)

    body = f"""
<section class="hero" style="background-color:#E6D8C9;background-image:linear-gradient(90deg,rgba(251,248,244,.96) 0%,rgba(251,248,244,.80) 45%,rgba(251,248,244,.15) 100%),url(assets/img/hero.jpg)">
  <div class="wrap hero-inner">
    <p class="eyebrow">Anlass-Outfits &amp; Accessoires</p>
    <h1>Was ziehe ich an?</h1>
    <p class="hero-sub">Komplette Outfits für echte Anlässe – vom Standesamt über die Weihnachtsfeier bis zum ganz normalen Dienstag im Büro. Zusammengestellt statt aufgezählt.</p>
    <a class="btn" href="#anlaesse">Anlass wählen</a>
  </div>
</section>

<section class="wrap section" id="anlaesse">
  <h2 class="sec-title">Wofür brauchst du ein Outfit?</h2>
  <div class="cat-grid">{cats}</div>
</section>

<section class="wrap section">
  <h2 class="sec-title">Neu auf Anlasslook</h2>
  <a class="feature" href="beitraege/{feat['slug']}/">
    <div class="feature-img" style="background-color:{tint(feat['img'])};background-image:url(assets/img/{feat['img']})"></div>
    <div class="feature-txt">
      <span class="card-cat">{e(CATBY[feat['cat']]['title'])}</span>
      <h3>{e(feat['title'])}</h3>
      <p>{e(feat['teaser'])}</p>
      <span class="more">Weiterlesen</span>
    </div>
  </a>
  <div class="card-grid">{"".join(post_card(x) for x in rest)}</div>
</section>

<section class="band">
  <div class="wrap band-inner">
    <h2>Warum wir Outfits zeigen und keine Einzelteile</h2>
    <p>Ein einzelnes Kleidungsstück löst kein Problem. Die Frage vor dem Kleiderschrank lautet nie „welche Hose", sondern „was ziehe ich zu diesem Termin an". Deshalb steht bei uns am Anfang jedes Beitrags ein Anlass – und am Ende ein vollständiger Look, den du so nachkaufen oder aus dem eigenen Schrank ergänzen kannst.</p>
    <p>Wir verkaufen nichts selbst. Wir verlinken zu Amazon und kennzeichnen jeden dieser Links. Was wir empfehlen, entscheiden wir unabhängig davon, wie hoch die Provision ausfällt.</p>
    <a class="btn ghost" href="ueber-uns/">Mehr über uns</a>
  </div>
</section>
"""
    write("index.html", page("index.html", f"{SITE['name']} – {SITE['claim']} Outfits für jeden Anlass",
        "Komplette Anlass-Outfits für Damen und Herren: Hochzeitsgast, Standesamt, Büro, Herbst, Weihnachtsfeier – jeweils vollständig zusammengestellt mit Accessoires.",
        body))


def build_category(c):
    posts = [x for x in POSTS if x["cat"] == c["slug"]]
    path = f"anlaesse/{c['slug']}/index.html"
    body = f"""
<section class="pagehead" style="background-color:{tint(c['img'])};background-image:linear-gradient(90deg,rgba(251,248,244,.95) 0%,rgba(251,248,244,.6) 60%,rgba(251,248,244,.1) 100%),url(../../assets/img/{c['img']})">
  <div class="wrap">
    <p class="eyebrow">Anlass</p>
    <h1>{e(c['title'])}</h1>
    <p class="hero-sub">{e(c['lead'])}</p>
  </div>
</section>
<section class="wrap section">
  <div class="card-grid">{"".join(post_card(x, "../../") for x in posts)}</div>
</section>
"""
    write(path, page(path, f"{c['title']} – Outfits komplett zusammengestellt | {SITE['name']}",
                     c["meta"], body, og_image=c["img"]))


def build_post(pst):
    c = CATBY[pst["cat"]]
    path = f"beitraege/{pst['slug']}/index.html"
    p = "../../"
    intro = "".join(f"<p>{e(t)}</p>" for t in pst["intro"])
    secs = ""
    for h2, paras in pst["sections"]:
        secs += f"<h2>{e(h2)}</h2>" + "".join(f"<p>{e(t)}</p>" for t in paras)

    related = [x for x in POSTS if x["cat"] == pst["cat"] and x["slug"] != pst["slug"]][:3]
    if len(related) < 3:
        related += [x for x in POSTS if x["slug"] != pst["slug"] and x not in related][:3 - len(related)]

    ld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article",
"headline":{chr(34)}{pst['title']}{chr(34)},
"description":{chr(34)}{pst['meta']}{chr(34)},
"image":"{SITE['url']}/assets/img/{pst['img']}",
"datePublished":"{TODAY}","dateModified":"{TODAY}",
"author":{{"@type":"Organization","name":"{SITE['name']}"}},
"publisher":{{"@type":"Organization","name":"{SITE['name']}"}}}}
</script>"""

    body = f"""
<article class="post">
  <div class="post-head wrap">
    <a class="crumb" href="{p}anlaesse/{c['slug']}/">{e(c['title'])}</a>
    <h1>{e(pst['title'])}</h1>
    <p class="post-teaser">{e(pst['teaser'])}</p>
  </div>
  <div class="post-hero" style="background-color:{tint(pst['img'])};background-image:url({p}assets/img/{pst['img']})"></div>
  <div class="post-body">
    {ad_notice()}
    {intro}
    {secs}
  </div>
  <div class="post-body">
    {product_block(pst['products'])}
  </div>
</article>

<section class="wrap section">
  <h2 class="sec-title">Passt dazu</h2>
  <div class="card-grid">{"".join(post_card(x, p) for x in related)}</div>
</section>
"""
    art = (f'<meta property="article:published_time" content="{TODAY}T09:00:00+02:00">\n'
           f'<meta property="article:modified_time" content="{TODAY}T09:00:00+02:00">\n'
           f'<meta property="article:author" content="{e(SITE["name"])}">\n'
           f'<meta property="article:section" content="{e(c["title"])}">\n')
    write(path, page(path, f"{pst['title']} | {SITE['name']}", pst["meta"], body,
                     og_image=pst["img"], extra_head=art + ld, og_type="article"))


def simple_page(slug, title, meta, inner):
    path = f"{slug}/index.html"
    body = f"""<section class="wrap section narrow">
<h1>{e(title)}</h1>
{inner}
</section>"""
    write(path, page(path, f"{title} | {SITE['name']}", meta, body))


# ----------------------------------------------------------------- CSS
CSS = """
:root{
  --bg:#FBF8F4; --panel:#F2EAE1; --ink:#1c1b1a; --muted:#6b6560;
  --accent:#A8402A; --accent-soft:#FCF0EC; --green:#2E6B4F; --line:#e5ded6;
  --wrap:1120px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4,.logo-mark,.foot-logo{font-family:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;font-weight:600;letter-spacing:-.015em}
img{max-width:100%;display:block}
a{color:inherit}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 24px}
.skip{position:absolute;left:-9999px}
.skip:focus{left:8px;top:8px;background:#fff;padding:8px 14px;z-index:99}

/* ---------- Header ---------- */
.site-head{position:sticky;top:0;z-index:50;background:rgba(251,248,244,.92);
  backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.head-inner{display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:74px}
.logo{text-decoration:none;display:flex;flex-direction:column;line-height:1.1}
.logo-mark{font-size:24px;font-weight:700}
.logo-sub{font-size:10px;letter-spacing:.16em;white-space:nowrap;text-transform:uppercase;color:var(--accent);font-weight:600;margin-top:3px}
.site-nav{display:flex;gap:17px;flex-wrap:wrap;align-items:center}
.site-nav a{text-decoration:none;font-size:14px;font-weight:500;color:var(--muted);
  padding:4px 0;border-bottom:1.5px solid transparent;transition:.15s;white-space:nowrap}
.site-nav a:hover{color:var(--ink);border-color:var(--accent)}
.nav-about{color:var(--ink)!important}
.navtoggle,.burger{display:none}

/* ---------- Hero ---------- */
.hero,.pagehead{background-size:cover;background-position:center;border-bottom:1px solid var(--line)}
.hero-inner{padding:104px 24px 112px;max-width:660px;margin:0}
.hero{background-color:var(--panel)}
.pagehead{padding:72px 0 76px;background-color:var(--panel)}
.pagehead h1{font-size:clamp(32px,5vw,50px);margin:6px 0 12px;max-width:16ch}
.eyebrow{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);
  font-weight:700;margin:0 0 10px}
.hero h1{font-size:clamp(42px,7vw,74px);line-height:1.02;margin:0 0 18px;font-weight:700}
.hero-sub{font-size:18.5px;color:#45403c;max-width:52ch;margin:0 0 26px}
.btn{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;
  padding:13px 26px;border-radius:2px;font-size:14.5px;font-weight:600;letter-spacing:.02em;transition:.15s}
.btn:hover{background:var(--accent)}
.btn.ghost{background:transparent;color:var(--ink);border:1.5px solid var(--ink)}
.btn.ghost:hover{background:var(--ink);color:#fff}

/* ---------- Sections ---------- */
.section{padding:74px 24px}
.section.narrow{max-width:760px}
.sec-title{font-size:clamp(24px,3.4vw,34px);margin:0 0 30px;padding-bottom:14px;
  border-bottom:2px solid var(--ink);display:block}

/* ---------- Kategorien ---------- */
.cat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:22px}
.cat-tile{text-decoration:none;background:#fff;border:1px solid var(--line);
  display:flex;flex-direction:column;transition:.18s;overflow:hidden}
.cat-tile:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(28,27,26,.10)}
.cat-img{height:186px;background-size:cover;background-position:center;background-color:var(--panel)}
.cat-txt{padding:20px 22px 24px}
.cat-txt h3{margin:0 0 7px;font-size:21px}
.cat-txt p{margin:0;color:var(--muted);font-size:15px;line-height:1.55}

/* ---------- Feature + Karten ---------- */
.feature{display:grid;grid-template-columns:1.15fr 1fr;text-decoration:none;background:#fff;
  border:1px solid var(--line);margin-bottom:26px;transition:.18s;overflow:hidden}
.feature:hover{box-shadow:0 14px 34px rgba(28,27,26,.10)}
.feature-img{min-height:330px;background-size:cover;background-position:center;background-color:var(--panel)}
.feature-txt{padding:40px 42px;display:flex;flex-direction:column;justify-content:center}
.feature-txt h3{font-size:clamp(23px,2.8vw,31px);margin:8px 0 12px;line-height:1.2}
.feature-txt p{color:var(--muted);margin:0 0 18px}
.more{color:var(--accent);font-weight:600;font-size:14.5px}
.more:after{content:" →"}

.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:22px}
.card{background:#fff;border:1px solid var(--line);transition:.18s;overflow:hidden}
.card:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(28,27,26,.10)}
.card a{text-decoration:none;display:block;height:100%}
.card-img{height:198px;background-size:cover;background-position:center;background-color:var(--panel)}
.card-body{padding:19px 21px 24px}
.card-cat{font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);font-weight:700}
.card-body h3{margin:8px 0 8px;font-size:19.5px;line-height:1.28}
.card-body p{margin:0;color:var(--muted);font-size:14.5px;line-height:1.55}

/* ---------- Band ---------- */
.band{background:var(--ink);color:#f3efe9;padding:70px 0}
.band-inner{max-width:760px}
.band h2{font-size:clamp(24px,3.4vw,34px);margin:0 0 18px;color:#fff}
.band p{color:#c9c2bb;margin:0 0 16px}
.band .btn.ghost{color:#f3efe9;border-color:#6b645d;margin-top:8px}
.band .btn.ghost:hover{background:#f3efe9;color:var(--ink)}

/* ---------- Beitrag ---------- */
.post-head{padding:54px 24px 26px;max-width:800px}
.crumb{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);
  font-weight:700;text-decoration:none}
.post-head h1{font-size:clamp(30px,4.6vw,46px);line-height:1.13;margin:12px 0 14px}
.post-teaser{font-size:19px;color:#45403c;margin:0}
.post-hero{height:min(52vw,430px);background-size:cover;background-position:center;
  background-color:var(--panel);margin-bottom:44px}
.post-body{max-width:720px;margin:0 auto;padding:0 24px}
.post-body h2{font-size:clamp(21px,2.8vw,27px);margin:40px 0 12px}
.post-body p{margin:0 0 16px}
.adnotice{background:var(--accent-soft);border-left:3px solid var(--accent);
  padding:15px 18px;font-size:14px;color:#5a504c;margin:0 0 32px;line-height:1.55}

/* ---------- Produkte ---------- */
.products{margin:52px 0 10px;background:#fff;border:1px solid var(--line);padding:34px 32px 38px}
.products h2{margin:0 0 6px;font-size:26px}
.prod-hint{font-size:13.5px;color:var(--muted);margin:0 0 22px}
.prod-list{list-style:none;margin:0;padding:0}
.prod{display:flex;gap:22px;align-items:center;justify-content:space-between;
  padding:19px 0;border-top:1px solid var(--line);flex-wrap:wrap}
.prod-body h3{margin:0 0 5px;font-size:18px}
.prod-body p{margin:0;color:var(--muted);font-size:14.5px;line-height:1.55;max-width:56ch}
.prod-btn{white-space:nowrap;text-decoration:none;background:var(--ink);color:#fff;
  padding:11px 20px;font-size:14px;font-weight:600;border-radius:2px;transition:.15s}
.prod-btn:hover{background:var(--accent)}
.star{opacity:.65;margin-left:3px}

/* ---------- Footer ---------- */
.site-foot{background:var(--panel);border-top:1px solid var(--line);margin-top:70px;padding:56px 0 26px}
.foot-grid{display:grid;grid-template-columns:2fr 1fr 1fr;gap:38px}
.foot-logo{font-size:22px;font-weight:700;margin-bottom:10px}
.foot-claim{color:var(--muted);font-size:14.5px;margin:0;max-width:38ch}
.foot-grid h4{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin:0 0 12px}
.foot-grid a{display:block;text-decoration:none;color:var(--muted);font-size:14.5px;padding:3px 0}
.foot-grid a:hover{color:var(--ink)}
.foot-legal{border-top:1px solid var(--line);margin-top:40px;padding-top:20px}
.foot-legal p{font-size:12.5px;color:var(--muted);margin:0 0 6px;line-height:1.6}

/* ---------- Rechtstexte ---------- */
.narrow h1{font-size:clamp(28px,4vw,40px);margin:0 0 22px}
.narrow h2{font-size:21px;margin:34px 0 10px}
.narrow p,.narrow li{color:#3b3733}
.narrow ul{padding-left:20px}
.ph{background:#FFF3CD;padding:1px 6px;border-radius:2px;font-weight:600}

/* ---------- Mobil ---------- */
@media(max-width:900px){
  .feature{grid-template-columns:1fr}
  .feature-img{min-height:230px}
  .feature-txt{padding:28px 26px 32px}
  .foot-grid{grid-template-columns:1fr 1fr}
}
@media(max-width:760px){
  body{font-size:16.5px}
  .burger{display:flex;flex-direction:column;gap:5px;cursor:pointer;padding:8px}
  .burger span{width:24px;height:2px;background:var(--ink);display:block}
  .site-nav{display:none;width:100%;flex-direction:column;gap:0;padding:8px 0 16px}
  .navtoggle:checked ~ .site-nav{display:flex}
  .site-nav a{padding:11px 0;border-bottom:1px solid var(--line);width:100%;font-size:16px}
  .head-inner{flex-wrap:wrap;padding-top:12px;padding-bottom:12px}
  .hero-inner{padding:64px 24px 70px}
  .section{padding:52px 20px}
  .products{padding:24px 20px 28px}
  .prod{flex-direction:column;align-items:flex-start;gap:12px}
  .foot-grid{grid-template-columns:1fr}
}
"""

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" fill="#1c1b1a"/>
<text x="32" y="45" font-family="Georgia,serif" font-size="40" font-weight="700"
 fill="#FBF8F4" text-anchor="middle">A</text>
<rect x="0" y="58" width="64" height="6" fill="#A8402A"/></svg>"""


# ----------------------------------------------------------------- Rechtstexte
IMPRESSUM = """
<p>Angaben gemäß § 5 Digitale-Dienste-Gesetz (DDG).</p>

<h2>Diensteanbieter</h2>
<p>Martin Mothes<br>
Zur Linde 4<br>
04651 Bad Lausick<br>
Deutschland</p>

<h2>Kontakt</h2>
<p>Telefon: 0162 9829885<br>
E-Mail: kontakt@anlasslook.de</p>

<h2>Verantwortlich für den Inhalt</h2>
<p>Martin Mothes, Anschrift wie oben.</p>

<h2>Verbraucherstreitbeilegung</h2>
<p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer
Verbraucherschlichtungsstelle teilzunehmen.</p>

<h2>Haftung für Inhalte und Links</h2>
<p>Als Diensteanbieter sind wir für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen
verantwortlich. Wir sind jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen
zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.</p>
<p>Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben.
Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber verantwortlich.
Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft;
rechtswidrige Inhalte waren nicht erkennbar.</p>

<h2>Urheberrecht</h2>
<p>Die durch den Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem
deutschen Urheberrecht. Beiträge Dritter sind als solche gekennzeichnet.</p>

"""

DATENSCHUTZ = """
<p>Stand: 25. August 2026</p>

<h2>1. Verantwortlicher</h2>
<p>Verantwortlich für die Datenverarbeitung auf dieser Website ist:<br>
Martin Mothes, Zur Linde 4, 04651 Bad Lausick<br>
E-Mail: kontakt@anlasslook.de</p>

<h2>2. Hosting</h2>
<p>Diese Website wird bei Netlify, Inc., 512 2nd Street, Suite 200, San Francisco, CA 94107, USA
gehostet. Beim Aufruf der Seite werden technisch notwendige Server-Logdaten verarbeitet
(IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browsertyp, Betriebssystem, Referrer-URL).
Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO – unser berechtigtes Interesse an einem sicheren
und störungsfreien Betrieb. Mit dem Hoster besteht ein Auftragsverarbeitungsvertrag.</p>

<h2>3. Cookies und Einwilligung</h2>
<p>Technisch notwendige Cookies setzen wir auf Grundlage von § 25 Abs. 2 TDDDG. Alle darüber
hinausgehenden Cookies und Technologien – insbesondere Analyse und Werbe-Tracking – setzen wir
ausschließlich nach deiner ausdrücklichen Einwilligung über unser Consent-Banner ein
(Art. 6 Abs. 1 lit. a DSGVO, § 25 Abs. 1 TDDDG). Du kannst die Einwilligung jederzeit
mit Wirkung für die Zukunft widerrufen.</p>

<h2>4. Google Analytics 4</h2>
<p>Diese Website nutzt Google Analytics 4, einen Webanalysedienst der Google Ireland Limited,
Gordon House, Barrow Street, Dublin 4, Irland. Wir setzen den Dienst ein, um zu verstehen, über
welche Kanäle Besucher zu uns finden (zum Beispiel Pinterest oder die Google-Suche) und welche
Beiträge gelesen werden.</p>
<p><strong>Der Dienst wird erst geladen, nachdem du im Banner ausdrücklich zugestimmt hast.</strong>
Ohne deine Einwilligung werden weder Cookies gesetzt noch Daten an Google übertragen.
Rechtsgrundlage ist Art. 6 Abs. 1 lit. a DSGVO und § 25 Abs. 1 TDDDG.</p>
<p>Verarbeitet werden dabei unter anderem gekürzte IP-Adresse, aufgerufene Seiten, Verweildauer,
Herkunftsquelle (Referrer und Kampagnenparameter), ungefährer Standort auf Stadtebene sowie
Geräte- und Browserangaben. Die IP-Anonymisierung ist aktiviert, Google-Signale und
Werbepersonalisierung sind abgeschaltet. Die Nutzerdaten werden nach 14 Monaten gelöscht.
Eine Übermittlung in die USA an die Google LLC ist nicht ausgeschlossen; Google LLC ist unter dem
EU-US Data Privacy Framework zertifiziert. Mit Google besteht ein Auftragsverarbeitungsvertrag.</p>
<p>Du kannst deine Einwilligung jederzeit mit Wirkung für die Zukunft widerrufen:
<button type="button" onclick="if(window.alReset)alReset()" style="font:inherit;font-size:15px;padding:9px 16px;border:1px solid #231F1C;border-radius:4px;background:#FBF8F4;color:#231F1C;cursor:pointer">Einwilligung widerrufen</button></p>

<h2>5. Amazon-Partnerprogramm</h2>
<p>Wir nehmen am Partnerprogramm von Amazon teil. Dieses Programm ermöglicht es, durch die Platzierung
von Werbelinks zu Amazon.de Werbekostenerstattung zu verdienen. Klickst du auf einen solchen Link,
wirst du zu Amazon weitergeleitet. Amazon setzt dabei ein Cookie, über das die Bestellung unserem
Partnerkonto zugeordnet werden kann. Wir erhalten von Amazon ausschließlich aggregierte, nicht
personenbezogene Auswertungen – wir erfahren also nicht, wer was gekauft hat.</p>
<p>Für die Datenverarbeitung nach dem Klick auf einen Amazon-Link ist Amazon verantwortlich.
Informationen dazu findest du in den Datenschutzhinweisen von Amazon.
Rechtsgrundlage für die Weiterleitung und die damit verbundene Verarbeitung ist Art. 6 Abs. 1 lit. f
DSGVO bzw. – soweit einwilligungspflichtige Technologien betroffen sind – Art. 6 Abs. 1 lit. a DSGVO.</p>

<h2>6. Schriftarten</h2>
<p>Diese Website bindet <strong>keine externen Schriftarten</strong> ein. Es werden ausschließlich
Schriften verwendet, die bereits auf deinem Gerät vorhanden sind. Eine Übertragung deiner IP-Adresse
an Dritte findet dadurch nicht statt.</p>

<h2>7. Kontaktaufnahme</h2>
<p>Wenn du uns per E-Mail kontaktierst, verarbeiten wir deine Angaben zur Bearbeitung der Anfrage
(Art. 6 Abs. 1 lit. b bzw. lit. f DSGVO). Die Daten werden gelöscht, sobald sie nicht mehr benötigt
werden und keine gesetzlichen Aufbewahrungspflichten entgegenstehen.</p>

<h2>8. Deine Rechte</h2>
<ul>
<li>Auskunft über die zu deiner Person gespeicherten Daten (Art. 15 DSGVO)</li>
<li>Berichtigung unrichtiger Daten (Art. 16 DSGVO)</li>
<li>Löschung (Art. 17 DSGVO) und Einschränkung der Verarbeitung (Art. 18 DSGVO)</li>
<li>Datenübertragbarkeit (Art. 20 DSGVO)</li>
<li>Widerspruch gegen Verarbeitungen auf Grundlage berechtigter Interessen (Art. 21 DSGVO)</li>
<li>Widerruf einer erteilten Einwilligung mit Wirkung für die Zukunft (Art. 7 Abs. 3 DSGVO)</li>
<li>Beschwerde bei einer Datenschutz-Aufsichtsbehörde (Art. 77 DSGVO)</li>
</ul>

<div class="adnotice" style="margin-top:36px"><strong>Wichtig:</strong> Dieser Text ist auf den
tatsächlichen Stand der Website abgestimmt (Stand 25.08.2026): keine externen Schriftarten,
Google Analytics 4 ausschließlich nach Einwilligung über das Banner. <strong>Sobald das
Pinterest-Tag eingebaut wird, muss ein weiterer Abschnitt dazu ergänzt werden.</strong>
Diese Erklärung ersetzt keine Rechtsberatung.</div>
"""

WERBEHINWEIS = """
<p>Damit du weißt, woran du bei uns bist – hier steht in einfachen Worten, wie sich diese Seite
finanziert.</p>

<h2>Wir verdienen an Werbelinks</h2>
<p>Auf dieser Website findest du Links zu Amazon. Kaufst du etwas, nachdem du auf einen solchen Link
geklickt hast, erhalten wir von Amazon eine Provision. <strong>Für dich ändert sich der Preis dadurch
nicht</strong> – du zahlst genau denselben Betrag wie ohne unseren Link.</p>
<p>Als Amazon-Partner verdienen wir an qualifizierten Verkäufen.</p>

<h2>Woran du diese Links erkennst</h2>
<p>Jeder Werbelink ist mit einem Sternchen (*) gekennzeichnet. Zusätzlich steht am Anfang jedes
Beitrags ein deutlich sichtbarer Hinweis. Wir verstecken nichts im Kleingedruckten.</p>

<h2>Was das für unsere Empfehlungen bedeutet</h2>
<p>Wir stellen Outfits so zusammen, wie wir sie selbst tragen würden. Die Höhe der Provision spielt
bei der Auswahl keine Rolle – sie ist bei Amazon ohnehin für fast alle Modeartikel gleich hoch.
Wir werden für keinen Beitrag von einer Marke bezahlt und nehmen keine Produktplatzierungen an.</p>

<h2>Preise und Verfügbarkeit</h2>
<p>Wir nennen bewusst keine konkreten Preise auf dieser Seite. Preise bei Amazon ändern sich
mehrmals täglich, und eine veraltete Preisangabe wäre irreführend. Den aktuellen Preis siehst du
immer direkt bei Amazon.</p>

<h2>Fragen?</h2>
<p>Wenn du wissen willst, warum ein bestimmtes Teil in einem Outfit steht: schreib uns.
Die Kontaktdaten stehen im Impressum.</p>
"""

UEBER = """
<p class="post-teaser">Anlasslook beantwortet eine einzige Frage: Was ziehe ich zu diesem Termin an?</p>

<h2>Warum es diese Seite gibt</h2>
<p>Die meisten Modeseiten zeigen Einzelteile. Das hilft nur, wenn man schon weiß, was man sucht.
Die Frage vor dem geöffneten Kleiderschrank lautet aber nie „welche Hose", sondern „ich bin
in drei Wochen Trauzeuge, es ist September, und ich habe keine Ahnung".</p>
<p>Deshalb beginnt bei uns jeder Beitrag mit einem Anlass und endet mit einem vollständigen Look –
inklusive der Accessoires, die die meisten vergessen und die am Ende den größten Unterschied machen.</p>

<h2>Wie wir Outfits zusammenstellen</h2>
<p>Drei Prinzipien:</p>
<ul>
<li><strong>Vollständig statt beispielhaft.</strong> Ein Look besteht aus vier bis sechs Teilen.
Ein einzelnes Kleid ist kein Outfit.</li>
<li><strong>Tragbar statt fotogen.</strong> Wir empfehlen nichts, worin man nicht sitzen, essen
und drei Stunden stehen kann.</li>
<li><strong>Accessoires zuerst.</strong> Broschen, Gürtel, Tücher und Schmuck verändern ein Outfit
stärker als ein teureres Hauptteil – und sie passen immer.</li>
</ul>

<h2>Wie sich die Seite finanziert</h2>
<p>Über Werbelinks zu Amazon. Jeder davon ist gekennzeichnet, für dich wird nichts teurer,
und wir nehmen kein Geld von Marken. Die ausführliche Fassung steht im
<a href="../werbehinweis/">Werbehinweis</a>.</p>

<h2>Kontakt</h2>
<p>Fragen, Themenwünsche oder ein Anlass, den wir übersehen haben? Die Kontaktdaten stehen im
<a href="../impressum/">Impressum</a>.</p>
"""


# ----------------------------------------------------------------- Main

# ----------------------------------------------------------- Duplikat-Wächter
def pruefe_bilder():
    """Bricht ab, wenn zwei Beiträge dasselbe Bild nutzen oder ein Bild fehlt.

    Grund: Pinterest wertet gleiche Motive als Dubletten und drosselt die
    Reichweite. Ein Pin, der einmal hochgeladen ist, lässt sich nachträglich
    NICHT mehr austauschen - Pinterest kopiert das Bild beim Pinnen. Deshalb
    muss der Fehler vor dem Ausliefern auffallen, nicht danach.
    """
    from collections import Counter
    fehler = []

    zaehler = Counter(p["img"] for p in POSTS)
    for img, n in zaehler.items():
        if n > 1:
            betroffen = [p["slug"] for p in POSTS if p["img"] == img]
            fehler.append(f"  Bild '{img}' wird von {n} Beiträgen genutzt: {', '.join(betroffen)}")

    for c in CATEGORIES:
        pass  # Kategoriebilder dürfen sich wiederholen, sie werden nicht gepinnt

    quelle = os.path.join(ROOT, "img")
    if os.path.isdir(quelle):
        vorhanden = set(os.listdir(quelle))
        for p in POSTS:
            if p["img"] not in vorhanden:
                fehler.append(f"  Bilddatei fehlt: {p['img']} (Beitrag {p['slug']})")

    if fehler:
        print("\n!!! ABBRUCH - doppelte oder fehlende Beitragsbilder:\n")
        print("\n".join(fehler))
        print("\nJeder Beitrag braucht ein eigenes Bild. Erst content.py korrigieren,")
        print("dann neu bauen. Sonst entstehen auf Pinterest Dubletten.\n")
        raise SystemExit(1)

    print(f"Bilder geprüft: {len(POSTS)} Beiträge, {len(zaehler)} verschiedene Bilder - keine Dubletten")


def main():
    pruefe_bilder()
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    build_home()
    for c in CATEGORIES:
        build_category(c)
    for p in POSTS:
        build_post(p)

    simple_page("ueber-uns", "Über Anlasslook",
                "Anlasslook stellt komplette Outfits für echte Anlässe zusammen – unabhängig, vollständig und mit Accessoires.", UEBER)
    simple_page("werbehinweis", "Werbehinweis",
                "Wie sich Anlasslook finanziert: Werbelinks zu Amazon, gekennzeichnet und ohne Mehrkosten für dich.", WERBEHINWEIS)
    simple_page("impressum", "Impressum",
                "Impressum und Anbieterkennzeichnung von Anlasslook.", IMPRESSUM)
    simple_page("datenschutz", "Datenschutzerklärung",
                "Datenschutzerklärung von Anlasslook: Hosting, Cookies, Amazon-Partnerprogramm und deine Rechte.", DATENSCHUTZ)

    write("assets/style.css", CSS)
    write("assets/favicon.svg", FAVICON)

    # Bilderordner
    os.makedirs(os.path.join(DIST, "assets", "img"), exist_ok=True)
    src = os.path.join(ROOT, "img")
    if os.path.isdir(src):
        for f in os.listdir(src):
            shutil.copy(os.path.join(src, f), os.path.join(DIST, "assets", "img", f))

    # RSS-Feed – Pinterest kann daraus automatisch Pins erzeugen
    # Nur die neuesten Beiträge in den Feed. Sonst zieht Pinterest bei jedem
    # Neubau alles auf einmal und es sieht nach Spam aus.
    FEED_LIMIT = 6
    items = []
    for p in reversed(POSTS[-FEED_LIMIT:]):
        u = f"{SITE['url']}/beitraege/{p['slug']}/"
        ul = u + "?utm_source=pinterest&amp;utm_medium=pin&amp;utm_campaign=rss"   # &amp; weil der Feed XML ist
        items.append(
            "  <item>\n"
            # Pinterest übernimmt diesen Titel als Pin-Überschrift. Deshalb der
            # Suchtitel aus PINTITEL, nicht der Website-Titel.
            f"    <title>{e(p.get('pintitle') or p['title'])}</title>\n"
            f"    <link>{ul}</link>\n"
            f"    <guid isPermaLink=\"true\">{u}</guid>\n"
            f"    <description>{e(p['teaser'])}</description>\n"
            f"    <enclosure url=\"{SITE['url']}/assets/pins/pin-{p['slug']}.jpg\" type=\"image/jpeg\" length=\"0\"/>\n"
            f"    <pubDate>{RSS_DATE}</pubDate>\n"
            "  </item>")
    write("feed.xml",
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"><channel>\n'
        f"  <title>{SITE['name']} – {SITE['claim']}</title>\n"
        f"  <link>{SITE['url']}/</link>\n"
        f"  <description>{e(SITE['tagline'])}</description>\n"
        "  <language>de-de</language>\n"
        + "\n".join(items) + "\n</channel></rss>\n")

    # robots.txt + sitemap.xml
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")
    urls = [""] + [f"anlaesse/{c['slug']}/" for c in CATEGORIES] + \
           [f"beitraege/{p['slug']}/" for p in POSTS] + \
           ["ueber-uns/", "werbehinweis/", "impressum/", "datenschutz/"]
    sm = "\n".join(
        f"  <url><loc>{SITE['url']}/{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)
    write("sitemap.xml",
          f'<?xml version="1.0" encoding="UTF-8"?>\n'
          f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}\n</urlset>\n')

    # Cloudflare Pages: Sicherheits-Header
    write("_headers", """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: geolocation=(), microphone=(), camera=()
""")

    n = sum(len(files) for _, _, files in os.walk(DIST))
    print(f"Fertig: {n} Dateien in dist/")
    print(f"Beiträge: {len(POSTS)} | Kategorien: {len(CATEGORIES)}")
    print(">>> Jetzt zwingend 'python3 makepins.py' laufen lassen -")
    print(">>> build.py hat dist/ geleert, die Pin-Grafiken fehlen noch.")
    if not SITE["amazon_tag"]:
        print("\n>>> HINWEIS: Amazon-Tracking-ID ist noch leer.")
        print(">>> Nach der PartnerNet-Freigabe in content.py bei 'amazon_tag' eintragen.")


if __name__ == "__main__":
    main()
