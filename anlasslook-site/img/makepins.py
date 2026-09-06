from PIL import Image, ImageDraw, ImageFont, ImageOps
import os, sys, textwrap, csv, hashlib
sys.path.insert(0,'.')
from content import SITE, POSTS, CATEGORIES

CREAM="#FBF8F4"; DARK="#231F1C"; ACCENT="#A8402A"; MUTED="#6b645d"
LIGHT_ACCENT="#E8A98F"          # Akzent auf dunklem Foto
# Schriftpfade. Auf Martins Rechner liegen sie im System, auf einem
# GitHub-Actions-Läufer werden sie vorher heruntergeladen und per
# ANLASSLOOK_SERIF / ANLASSLOOK_SANS übergeben.
SER=os.environ.get("ANLASSLOOK_SERIF") or "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
SAN=os.environ.get("ANLASSLOOK_SANS")  or "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
W,H=1000,1500; IMGH=880
DIST=os.environ.get("ANLASSLOOK_DIST") or "dist"
OUT=f"{DIST}/assets/pins"; os.makedirs(OUT,exist_ok=True)
CAT={c["slug"]:c for c in CATEGORIES}

# ---------------------------------------------------------------------------
# DREI VARIANTEN JE BEITRAG
#
# Pinterest belohnt verschiedene Motive zum selben Ziel und bestraft dieselbe
# Grafik doppelt. Deshalb bekommt jeder Beitrag drei Grafiken mit
# unterschiedlichem Bildausschnitt und Aufbau, aber demselben Suchtitel:
#
#   a  Foto oben, Text unten auf Creme      -> pin-<slug>.jpg   (RSS-Feed)
#   b  Foto ganzflächig, Text auf Verlauf   -> pin-<slug>-b.jpg (CSV)
#   c  Text oben, Foto unten                -> pin-<slug>-c.jpg (CSV)
#
# Variante a behält ihren Dateinamen, weil build.py sie im Feed verlinkt.
# ---------------------------------------------------------------------------
VARIANTEN = ("a","b","c")


def pfad(slug, v):
    return f"{OUT}/pin-{slug}.jpg" if v=="a" else f"{OUT}/pin-{slug}-{v}.jpg"


def url(slug, v):
    return f"{SITE['url']}/assets/pins/" + (f"pin-{slug}.jpg" if v=="a" else f"pin-{slug}-{v}.jpg")


def fit(draw,text,font_path,maxw,start,minsize=34,maxlines=4):
    size=start
    while size>minsize:
        f=ImageFont.truetype(font_path,size)
        lines=[]; cur=""
        for w in text.split():
            t=(cur+" "+w).strip()
            if draw.textlength(t,font=f)<=maxw: cur=t
            else:
                if cur: lines.append(cur)
                cur=w
        if cur: lines.append(cur)
        if len(lines)<=maxlines: return f,lines
        size-=3
    f=ImageFont.truetype(font_path,minsize)
    return f,textwrap.wrap(text,28)[:maxlines]


def gesperrt(d,x,y,text,font,fill,extra=4):
    for ch in text:
        d.text((x,y),ch,font=font,fill=fill); x+=d.textlength(ch,font=font)+extra
    return x


def foto(post, groesse, centering):
    im=Image.open(f"{DIST}/assets/img/{post['img']}").convert("RGB")
    return ImageOps.fit(im,groesse,Image.LANCZOS,centering=centering)


def pintitel(post):
    return post.get("pintitle") or post["title"]


# --- Variante a: Foto oben, Text unten auf Creme (der bisherige Aufbau) -----
def variante_a(post):
    canvas=Image.new("RGB",(W,H),CREAM)
    canvas.paste(foto(post,(W,IMGH),(0.5,0.4)),(0,0))
    d=ImageDraw.Draw(canvas)
    pad=72; y=IMGH+78
    gesperrt(d,pad,y,CAT[post["cat"]]["title"].upper(),ImageFont.truetype(SAN,25),ACCENT)
    y+=64
    ft,lines=fit(d,pintitel(post),SER,W-2*pad,74)
    for ln in lines:
        d.text((pad,y),ln,font=ft,fill=DARK); y+=ft.size+16
    y+=14
    d.line([(pad,y),(pad+110,y)],fill=ACCENT,width=3)
    y+=40
    fs=ImageFont.truetype(SER,31)
    fw,sub=fit(d,post["teaser"],SER,W-2*pad,31,29)
    LIMIT=H-150
    for i,ln in enumerate(sub[:2]):
        if y+44>LIMIT: break
        if i==1 and len(sub)>2:
            while ln and d.textlength(ln+" ...",font=fs)>W-2*pad: ln=ln[:-1]
            ln=ln.rstrip(" ,;")+" ..."
        d.text((pad,y),ln,font=fs,fill=MUTED); y+=44
    gesperrt(d,pad,H-88,"ANLASSLOOK.DE",ImageFont.truetype(SAN,27),DARK,5)
    return canvas


# --- Variante b: Foto ganzflächig, Text auf dunklem Verlauf -----------------
def variante_b(post):
    base=foto(post,(W,H),(0.5,0.28)).copy()
    pad=72
    # Erst den Textblock ausmessen, dann den Verlauf genau darunter legen -
    # sonst steht heller Text auf hellem Foto.
    ft,lines=fit(ImageDraw.Draw(base),pintitel(post),SER,W-2*pad,80,40)
    block=64+len(lines)*(ft.size+16)
    ytop=H-190-block
    ramp=max(260,ytop-240)
    maske=Image.new("L",(W,H),0)
    md=ImageDraw.Draw(maske)
    for i in range(ramp,H):
        if i<ytop:
            a=218*(((i-ramp)/max(1,ytop-ramp))**1.2)
        else:
            a=218+34*((i-ytop)/max(1,H-ytop))
        md.line([(0,i),(W,i)],fill=int(min(252,a)))
    canvas=Image.composite(Image.new("RGB",(W,H),"#14110F"),base,maske)
    d=ImageDraw.Draw(canvas)
    y=ytop
    gesperrt(d,pad,y,CAT[post["cat"]]["title"].upper(),ImageFont.truetype(SAN,25),LIGHT_ACCENT)
    y+=64
    for ln in lines:
        d.text((pad,y),ln,font=ft,fill=CREAM); y+=ft.size+16
    y+=18
    d.line([(pad,y),(pad+110,y)],fill=LIGHT_ACCENT,width=3)
    gesperrt(d,pad,H-88,"ANLASSLOOK.DE",ImageFont.truetype(SAN,27),CREAM,5)
    return canvas


# --- Variante c: Text oben auf Creme, Foto unten ---------------------------
IMGH_C=960

def variante_c(post):
    canvas=Image.new("RGB",(W,H),CREAM)
    canvas.paste(foto(post,(W,IMGH_C),(0.5,0.72)),(0,H-IMGH_C))
    d=ImageDraw.Draw(canvas)
    pad=72
    ft,lines=fit(d,pintitel(post),SER,W-2*pad,60,34,maxlines=3)
    block=62+len(lines)*(ft.size+14)+16+38
    y=max(72,(H-IMGH_C-block)//2)
    gesperrt(d,pad,y,CAT[post["cat"]]["title"].upper(),ImageFont.truetype(SAN,25),ACCENT)
    y+=62
    for ln in lines:
        d.text((pad,y),ln,font=ft,fill=DARK); y+=ft.size+14
    y+=16
    d.line([(pad,y),(pad+110,y)],fill=ACCENT,width=3)
    y+=34
    gesperrt(d,pad,y,"ANLASSLOOK.DE",ImageFont.truetype(SAN,25),MUTED,5)
    return canvas


BAUER={"a":variante_a,"b":variante_b,"c":variante_c}


def make(post, v):
    p=pfad(post["slug"],v)
    BAUER[v](post).save(p,quality=88,optimize=True,progressive=True)
    return p


# ---------------------------------------------------------------------------
# Muss mit FEED_LIMIT in build.py übereinstimmen. Diese Beiträge pinnt der
# RSS-Feed von allein - Variante a darf deshalb nicht zusätzlich in die
# Bulk-CSV, sonst hängt dieselbe Grafik zweimal auf Pinterest.
#
# Die Varianten b und c sind KEINE Dubletten: anderes Motiv, dasselbe Ziel.
# Genau das belohnt Pinterest. Sie stehen in einer eigenen CSV und werden
# portionsweise hochgeladen, nicht auf einmal.
FEED_LIMIT = 6
GEPINNT = "pinterest-gepinnt.txt"


def zeile(p, v="a"):
    zusatz={"a":"", "b":" Look zum Nachstylen.", "c":" Alle Teile im Beitrag."}[v]
    return {
      "Title": pintitel(p)[:100],
      "Media URL": url(p["slug"],v),
      "Pinterest board": CAT[p["cat"]]["title"],
      "Description": (p["meta"] + zusatz + " Mehr Outfit-Ideen auf anlasslook.de. Enthält Werbelinks.")[:500],
      "Link": f"{SITE['url']}/beitraege/{p['slug']}/?utm_source=pinterest&utm_medium=pin&utm_campaign=variante-{v}",
      "Publish date": "",
      "Keywords": "",
    }


def schreibe_csv(pfad_, zeilen):
    felder = ["Title","Media URL","Pinterest board","Description","Link","Publish date","Keywords"]
    with open(pfad_,"w",newline="",encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=felder)
        w.writeheader(); w.writerows(zeilen)


# --- Wächter 1: kein Foto darf zwei Beiträgen zugeordnet sein ---
from collections import Counter as _C
_z=_C(p["img"] for p in POSTS)
_mehrfach={img:[p["slug"] for p in POSTS if p["img"]==img] for img,n in _z.items() if n>1}
if _mehrfach:
    print("\n!!! ABBRUCH - dasselbe Foto bei mehreren Beiträgen:\n")
    for img,slugs in _mehrfach.items():
        print(f"  '{img}': {', '.join(slugs)}")
    print("\nDie Pin-Grafiken wären dann zwar verschiedene Dateien, würden auf")
    print("Pinterest aber gleich aussehen - und das drosselt die Reichweite.")
    print("Erst in content.py eigene Bilder zuordnen, dann neu bauen.\n")
    raise SystemExit(1)

# --- Pins erzeugen ---
erzeugt={}
for p in POSTS:
    for v in VARIANTEN:
        f=make(p,v)
        h=hashlib.sha256(open(f,"rb").read()).hexdigest()
        erzeugt.setdefault(h,[]).append(f"{p['slug']}-{v}")

# --- Wächter 2: keine zwei inhaltsgleichen Pin-Dateien ---
dubletten=[v for v in erzeugt.values() if len(v)>1]
if dubletten:
    print("\n!!! ABBRUCH - inhaltsgleiche Pin-Grafiken:\n")
    for v in dubletten:
        print("  identisch: " + ", ".join(v))
    print("\nPinterest wertet gleiche Motive als Dubletten und drosselt die Reichweite.")
    print("Ein bereits hochgeladener Pin lässt sich nicht mehr austauschen.\n")
    raise SystemExit(1)

# --- Wächter 3: trägt jeder Beitrag einen eigenen Pin-Titel? ---
ohne=[p["slug"] for p in POSTS if not p.get("pintitle") or p["pintitle"]==p["title"]]
if ohne:
    print("\nHinweis - diese Beiträge nutzen den Website-Titel als Pin-Titel:")
    print("  " + ", ".join(ohne))
    print("  Website-Titel dürfen schön sein, Pin-Titel müssen Suchbegriffe sein.")
    print("  Eintrag in PINTITEL in content.py ergänzen.\n")

# --- CSV: Variante a nach der bisherigen Logik ---
bereits=set()
if os.path.exists(GEPINNT):
    bereits={z.strip() for z in open(GEPINNT,encoding="utf-8") if z.strip() and not z.startswith("#")}

feed_slugs={p["slug"] for p in POSTS[-FEED_LIMIT:]}
offen=[p for p in POSTS if p["slug"] not in bereits and p["slug"] not in feed_slugs]

schreibe_csv(f"{DIST}/pinterest-bulk-alle.csv", [zeile(p) for p in POSTS])
schreibe_csv(f"{DIST}/pinterest-bulk.csv",      [zeile(p) for p in offen])

# --- CSV: die Varianten b und c, ältester Beitrag zuerst ---
varianten_zeilen=[zeile(p,v) for v in ("b","c") for p in POSTS]
schreibe_csv(f"{DIST}/pinterest-varianten.csv", varianten_zeilen)

anzahl=len(POSTS)*len(VARIANTEN)
print(f"{anzahl} Pin-Grafiken erzeugt ({len(POSTS)} Beiträge x {len(VARIANTEN)} Varianten), alle inhaltlich verschieden")
print(f"bereits gepinnt: {len(bereits)} | über RSS-Feed: {len(feed_slugs)} | offen für Bulk-Upload: {len(offen)}")
if offen:
    print("  -> " + ", ".join(p["slug"] for p in offen))
    print("\nNach dem Hochladen von dist/pinterest-bulk.csv einmal ausführen:")
    print("  python3 makepins.py --gepinnt")
else:
    print("  -> dist/pinterest-bulk.csv ist leer: nichts Neues zu pinnen. Das ist richtig so.")
print(f"\nVarianten b und c: dist/pinterest-varianten.csv ({len(varianten_zeilen)} Zeilen)")
print("  ACHTUNG: nicht auf einmal hochladen. 10 bis 15 Zeilen pro Woche,")
print("  sonst sieht das Konto nach Massenupload aus. Datei oben abschneiden,")
print("  Kopfzeile behalten, den Rest beim nächsten Mal.")
print("Vollständige Liste für einen Neuaufbau des Kontos: dist/pinterest-bulk-alle.csv")

# --- Slugs als gepinnt vormerken ---
if "--gepinnt" in sys.argv:
    neu=sorted(bereits | {p["slug"] for p in offen} | feed_slugs)
    with open(GEPINNT,"w",encoding="utf-8") as fh:
        fh.write("# Slugs, die auf Pinterest bereits einen Pin haben.\n")
        fh.write("# Verhindert, dass derselbe Beitrag ein zweites Mal gepinnt wird.\n")
        fh.write("# Gilt nur für Variante a. Die Varianten b und c laufen über\n")
        fh.write("# dist/pinterest-varianten.csv und werden hier nicht vermerkt.\n")
        fh.write("\n".join(neu) + "\n")
    print(f"\n{GEPINNT} aktualisiert: {len(neu)} Slugs gelten jetzt als gepinnt.")
