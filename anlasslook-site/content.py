# -*- coding: utf-8 -*-
"""Inhalte für anlasslook.de — hier steht der komplette Text der Website."""

SITE = {
    "name": "Anlasslook",
    "domain": "anlasslook.de",
    "url": "https://anlasslook.de",
    "claim": "Was ziehe ich an?",
    "tagline": "Komplette Outfits für echte Anlässe – vom Standesamt bis zur Weihnachtsfeier.",
    # ---------------------------------------------------------------
    # Nach der PartnerNet-Freigabe hier die eigene Tracking-ID eintragen,
    # z. B. "anlasslook-21". Solange leer, werden ganz normale
    # Amazon-Links ohne Provision erzeugt.
    # ---------------------------------------------------------------
    "amazon_tag": "anlasslook-21",
    "pinterest_tag_id": "",   # Pinterest-Tag-ID, sobald angelegt
    "ga4_id": "G-193HCKPWYG",  # Google-Analytics-4-Mess-ID (Property "anlasslook.de")
    "pinterest_user": "anlasslook",
}

CATEGORIES = [
    {"slug": "hochzeitsgast", "nav": "Hochzeitsgast", "title": "Hochzeitsgast",
     "lead": "Elegant, aber nicht overdressed. Die Looks, mit denen du auf keiner Hochzeit falsch liegst.",
     "img": "cat-hochzeitsgast.jpg",
     "meta": "Hochzeitsgast-Outfits für Damen und Herren – komplette Looks für Sommer- und Herbsthochzeiten, inklusive Accessoires."},
    {"slug": "standesamt", "nav": "Standesamt", "title": "Standesamt & kleine Trauung",
     "lead": "Kleine Feier, große Wirkung. Schlichte Looks, die trotzdem nach Anlass aussehen.",
     "img": "cat-standesamt.jpg",
     "meta": "Was zieht man zum Standesamt an? Komplette Outfits für Braut, Trauzeugin und Gäste bei der kleinen Trauung."},
    {"slug": "buero", "nav": "Büro", "title": "Büro & Business",
     "lead": "Zwischen Kostüm und Kapuzenpulli liegt eine Menge. Hier ist der Mittelweg.",
     "img": "cat-buero.jpg",
     "meta": "Büro-Outfits ohne Kostüm: Quiet-Business-Looks, Capsule Wardrobe und die Regeln für weite Schnitte."},
    {"slug": "herbst", "nav": "Herbst", "title": "Herbst & Übergang",
     "lead": "Die schwierigste Jahreszeit für Outfits – und die dankbarste, wenn man sie beherrscht.",
     "img": "cat-herbst.jpg",
     "meta": "Übergangs-Outfits für den Herbst: Layering, Field Jacket, Cape und die Farbregeln der Saison."},
    {"slug": "festtage", "nav": "Festtage", "title": "Weihnachtsfeier & Silvester",
     "lead": "Festlich, ohne wie verkleidet auszusehen. Sechs Wochen im Jahr braucht man das.",
     "img": "cat-festtage.jpg",
     "meta": "Outfits für Weihnachtsfeier und Silvester: festliche Looks vom Büro bis zum Abend, mit Schmuck und Accessoires."},
    {"slug": "accessoires", "nav": "Accessoires", "title": "Accessoires",
     "lead": "Broschen, Gürtel, Tücher, Schmuck. Die Teile, die aus einem Outfit einen Look machen.",
     "img": "cat-accessoires.jpg",
     "meta": "Accessoires richtig kombinieren: Broschen, breite Gürtel, Seidentücher und Goldschmuck – mit Anleitungen zum Nachstylen."},
]

# --------------------------------------------------------------------------
# Beiträge. Aufbau je Beitrag:
#   slug, title (H1 + Pin-Titel), cat, teaser, img, meta (Description),
#   intro (Absätze), sections [(H2, [Absätze])], products [(Name, Warum, Suchbegriff)]
# --------------------------------------------------------------------------

POSTS = [

# ============================ HOCHZEITSGAST ============================
{
 "slug": "hochzeitsgast-herbst",
 "cat": "hochzeitsgast",
 "title": "Hochzeitsgast im Herbst: 7 Outfits, die nicht overdressed wirken",
 "teaser": "Die Herbsthochzeit hat eigene Regeln: kühle Abende, warmes Licht, oft ein Ortswechsel zwischen Trauung und Feier. Sieben Looks, die den ganzen Tag tragen.",
 "img": "cat-hochzeitsgast.jpg",
 "meta": "Hochzeitsgast im Herbst: 7 komplette Outfits für Damen und Herren, die zwischen Trauung, Sektempfang und Abendfeier funktionieren.",
 "intro": [
   "Eine Herbsthochzeit ist der schwierigste Termin im Gästekalender. Mittags scheint die Sonne, um sieben steht man fröstelnd auf einer Scheunenterrasse, und irgendwo dazwischen soll man auf Fotos gut aussehen. Wer das mit einem einzelnen schönen Kleid lösen will, friert.",
   "Die Lösung ist nicht mehr Stoff, sondern eine bessere Reihenfolge: ein Basisteil, das den ganzen Tag trägt, plus zwei Schichten, die dazukommen und wieder verschwinden können.",
 ],
 "sections": [
   ("Die Grundregel: eine Basis, zwei Schichten", [
     "Such dir ein Teil aus, das du zwölf Stunden lang anbehalten kannst – ein Midikleid, eine gut sitzende Hose mit Seidentop, ein schlichter Anzug. Alles andere kommt darüber und geht wieder ab.",
     "Schicht eins ist der Blazer oder die Strickjacke für den Sektempfang. Schicht zwei ist der Mantel oder das Cape für draußen. Wer das trennt, muss nicht zwischen Frieren und Schwitzen wählen.",
   ]),
   ("Farben, die im Herbstlicht funktionieren", [
     "Herbstlicht ist warm und tief. Reines Weiß ist ohnehin tabu, aber auch kaltes Grau und Eisblau wirken darin fahl. Was trägt: Terracotta, Rostrot, Waldgrün, Camel, tiefes Burgunder und alle Brauntöne.",
     "Die Drei-Farben-Regel hilft: eine Hauptfarbe für das größte Teil, eine Nebenfarbe für die Schicht darüber, eine Metallfarbe für Schmuck und Schuhe. Mehr wird unruhig.",
   ]),
   ("Was Gäste regelmäßig falsch machen", [
     "Zu hohe Absätze. Auf Kies, Wiese und Kopfsteinpflaster wird der Abend lang. Ein Blockabsatz oder ein eleganter flacher Schuh ist keine Niederlage, sondern eine Entscheidung.",
     "Zu große Tasche. Eine kleine Umhängetasche mit langem Riemen hält die Hände frei und sieht auf Fotos besser aus als eine Clutch, die man ständig irgendwo abstellt.",
     "Zu wenig Accessoires. Ein schlichtes Kleid ohne Schmuck wirkt nicht elegant, sondern unfertig. Eine Brosche am Revers oder ein gestapelter Armreif macht mehr Unterschied als ein teureres Kleid.",
   ]),
 ],
 "products": [
   ("Midikleid in Terracotta oder Rostrot", "Das Basisteil, das den ganzen Tag trägt. Fließender Stoff verzeiht Sitzen, Tanzen und ein zweites Stück Torte.", "midikleid damen herbst"),
   ("Cape oder Umhang-Mantel", "Die zweite Schicht. Passt über jeden Blazer, knittert nicht und sieht auf Fotos besser aus als eine Steppjacke.", "B0CWGYQWWQ"),
   ("Blazer in Camel oder Waldgrün", "Die erste Schicht für den Sektempfang. Aufgeknöpft getragen streckt er die Silhouette.", "blazer damen camel"),
   ("Kleine Umhängetasche mit langem Riemen", "Einheitsgröße, hält die Hände frei, passt zu jedem der Looks. Das dankbarste Teil im ganzen Outfit.", "B0DJS6KBVG"),
   ("Brosche fürs Revers", "Das Detail, das ein schlichtes Kleid zum Anlass-Outfit macht. Kostet wenig, verändert viel.", "B0F92YSCBD"),
   ("Schuhe mit Blockabsatz", "Stabil auf Wiese und Kies, elegant genug für die Trauung. Der einzige Kompromiss, den man nicht bereut.", "B0BN9W4Z3W"),
 ],
},

{
 "slug": "hochzeitsgast-ab-40",
 "cat": "hochzeitsgast",
 "title": "Hochzeitsgast ab 40: elegant ohne Kostüm-Effekt",
 "teaser": "Zwischen zu jugendlich und zu streng liegt ein schmaler Grat. Vier Prinzipien, die ihn breiter machen.",
 "img": "post-hochzeitsgast-ab-40.jpg",
 "meta": "Hochzeitsgast-Outfits ab 40: elegante Looks ohne Kostüm-Effekt, mit klaren Regeln zu Schnitt, Farbe und Accessoires.",
 "intro": [
   "Ab einem gewissen Punkt funktioniert das Prinzip „Hauptsache festlich\" nicht mehr. Was mit 25 verspielt wirkt, wirkt mit 45 bemüht – und was seriös gemeint ist, rutscht schnell in Richtung Empfangsdame.",
   "Der Unterschied liegt selten am Preis. Er liegt an vier Entscheidungen, die man vor dem Kauf trifft.",
 ],
 "sections": [
   ("Ein Teil darf auffallen, nicht drei", [
     "Ein leuchtender Blazer, ein Kleid mit Struktur oder ein markantes Schmuckstück – aber nur eines davon. Alles andere tritt zurück. Das ist der wichtigste Unterschied zwischen elegant und überladen.",
   ]),
   ("Schnitt schlägt Größe", [
     "Ein Teil, das an der Schulter sitzt, wirkt teurer als ein Teil, das an der Taille sitzt. Die Schulternaht ist der einzige Punkt, den ein Schneider nur schwer korrigiert – alles andere lässt sich ändern.",
     "Wenn du zwischen zwei Größen liegst: die größere nehmen und enger machen lassen. 25 Euro beim Änderungsschneider verändern mehr als 200 Euro Aufpreis.",
   ]),
   ("Das Kostüm-Signal vermeiden", [
     "Was ein Outfit nach Kostüm aussehen lässt, ist fast immer die Kombination aus glänzendem Stoff, exakt farblich abgestimmten Schuhen und einer Handtasche im selben Ton. Brich einen dieser drei Punkte auf, und der Effekt verschwindet.",
     "Am einfachsten über die Tasche: eine Ledertasche in Cognac oder Braun statt der farblich passenden Clutch.",
   ]),
   ("Accessoires sind hier kein Beiwerk", [
     "Broschen erleben gerade ein Comeback – und sie lösen genau dieses Problem. Sie machen ein schlichtes Teil festlich, ohne dass ein zweites auffälliges Kleidungsstück dazukommt. Getragen am Revers, am Ausschnitt oder an der Schulter.",
   ]),
 ],
 "products": [
   ("Blazer mit klarer Schulterlinie", "Der Schnitt an der Schulter entscheidet über die Wirkung. Aufgeknöpft getragen, nie zu kurz.", "blazer damen elegant"),
   ("Seidiges Midikleid in gedeckter Farbe", "Fließend statt glänzend – das ist der Unterschied zwischen elegant und Kostüm.", "midikleid damen elegant"),
   ("Brosche oder Anstecknadel", "Macht Schlichtes festlich. Einheitsgröße, also kein Fehlkauf möglich.", "brosche vintage gold"),
   ("Ledertasche in Cognac", "Bricht die zu perfekte Abstimmung auf. Trägt sich auch nach der Hochzeit weiter.", "handtasche damen leder cognac"),
   ("Feine Goldkette zum Stapeln", "Zwei Längen übereinander wirken durchdachter als eine einzelne Kette.", "goldkette damen fein"),
 ],
},

{
 "slug": "drei-farben-regel",
 "cat": "hochzeitsgast",
 "title": "Die 3-Farben-Regel für Anlass-Outfits",
 "teaser": "Der einfachste Trick, mit dem ein zusammengewürfeltes Outfit plötzlich nach Absicht aussieht.",
 "img": "post-drei-farben.jpg",
 "meta": "Die 3-Farben-Regel erklärt: So kombinierst du Anlass-Outfits, die zusammenhängend statt zufällig wirken.",
 "intro": [
   "Es gibt einen Grund, warum manche Outfits teuer aussehen, obwohl die Einzelteile es nicht sind: Sie haben eine Farblogik. Und die lässt sich auf eine Regel eindampfen.",
 ],
 "sections": [
   ("Die Regel", [
     "Maximal drei Farben pro Outfit. Eine Hauptfarbe für das größte Teil. Eine Nebenfarbe für die zweite Schicht. Eine Akzentfarbe für Accessoires und Schuhe. Neutraltöne wie Cream, Camel, Grau, Schwarz und Marine zählen dabei nur halb.",
     "Beispiel: Waldgrünes Kleid (Hauptfarbe), camelfarbener Mantel (Neutral, zählt halb), goldener Schmuck und cognacfarbene Tasche (Akzent). Das sind gefühlt vier Farben und funktioniert trotzdem, weil zwei davon Neutraltöne sind.",
   ]),
   ("Warum sie funktioniert", [
     "Das Auge sucht nach Mustern. Drei Farben kann es als Absicht lesen, fünf liest es als Zufall. Deshalb wirken Outfits mit klarer Farbbegrenzung geplant, auch wenn sie aus drei verschiedenen Läden stammen.",
   ]),
   ("Wann man sie brechen darf", [
     "Bei Mustern. Ein gestreiftes oder geblümtes Teil bringt seine eigene Farbfamilie mit – dann gilt: alle weiteren Teile aus den Farben des Musters wählen. Das Muster ist die Palette.",
     "Und bei Metallen: Gold und Silber gleichzeitig ist inzwischen erlaubt, wenn es an einer Stelle bewusst passiert – etwa an einem Armreif-Stapel. Nicht verteilt über Ohrringe, Kette und Uhr.",
   ]),
 ],
 "products": [
   ("Seidentuch mit Muster", "Das einfachste Werkzeug, um drei Farben in ein Outfit zu bringen, die zusammenpassen – die Palette ist schon vorgegeben.", "seidentuch damen gemustert"),
   ("Camel-Mantel", "Der nützlichste Neutralton überhaupt. Passt zu Grün, Burgunder, Marine und allen Brauntönen.", "mantel damen camel"),
   ("Goldene Armreifen zum Stapeln", "Die Akzentfarbe, die kein Risiko trägt. Einheitsgröße.", "armreif gold damen set"),
   ("Tasche in Cognac", "Neutral genug für fast jede Hauptfarbe, wärmer als Schwarz.", "handtasche cognac damen"),
 ],
},

# ============================ STANDESAMT ============================
{
 "slug": "standesamt-schlicht",
 "cat": "standesamt",
 "title": "Standesamt schlicht: 5 Looks für die kleine Trauung",
 "teaser": "Zwanzig Minuten Zeremonie, zwölf Gäste, danach Essen gehen. Für diesen Rahmen braucht es etwas anderes als ein Hochzeitskleid.",
 "img": "cat-standesamt.jpg",
 "meta": "Standesamt-Outfits für die kleine Trauung: fünf schlichte Looks für Braut, Trauzeugin und Gäste – komplett zusammengestellt.",
 "intro": [
   "Die kleine Trauung ist der Anlass mit den unklarsten Regeln. Zu festlich wirkt deplatziert, zu alltäglich wirkt lieblos – und alles spielt sich in einem nüchternen Amtszimmer mit Neonlicht ab.",
   "Was in diesem Rahmen funktioniert, ist nicht Opulenz, sondern Präzision: wenige Teile, gute Stoffe, ein klares Detail.",
 ],
 "sections": [
   ("Der weiße Blazer ist das nützlichste Teil", [
     "Er ist festlich genug für die Zeremonie, funktioniert danach im Restaurant und lässt sich am nächsten Tag ins Büro tragen. Kein anderes Teil hat dieses Verhältnis von Anlass-Wirkung zu Alltagstauglichkeit.",
     "Für die Braut über einem cremefarbenen Slipdress. Für Gäste über einer dunklen Hose oder einem farbigen Kleid – dann bleibt der Blazer das hellste Teil, ohne mit der Braut zu konkurrieren.",
   ]),
   ("Neonlicht ist gnadenlos", [
     "Amtszimmer haben kaltes Deckenlicht. Reinweiß wirkt darin bläulich, Schwarz wirkt hart, glänzende Stoffe reflektieren unvorteilhaft. Cream, Elfenbein, Sand und gedeckte Farben halten dem stand.",
     "Matte Stoffe fotografieren in diesem Licht deutlich besser als Satin.",
   ]),
   ("Ein Detail statt vieler", [
     "Eine gute Brosche am Revers, ein schmales Seidentuch, ein Paar auffällige Ohrringe – eines davon. In einem kleinen Raum mit wenigen Menschen wirkt jedes Detail größer als es ist.",
   ]),
 ],
 "products": [
   ("Weißer oversized Blazer", "Das Kernstück. Festlich, aber nicht kostümiert, und über den Anlass hinaus tragbar.", "blazer damen weiss oversize"),
   ("Slipdress in Creme oder Elfenbein", "Matter Stoff, fließender Fall. Wirkt im Neonlicht deutlich besser als Satin.", "slipdress damen creme"),
   ("Kleine strukturierte Handtasche", "Klein genug für den Raum, fest genug, um nicht in sich zusammenzufallen.", "handtasche damen klein elegant"),
   ("Perlenohrringe oder auffällige Creolen", "Das eine Detail. Einheitsgröße, kein Fehlkauf.", "ohrringe damen perlen"),
   ("Flache elegante Schuhe oder Slingbacks", "Zwanzig Minuten stehen, danach laufen. Absatzhöhe ist hier keine Stilfrage.", "slingback damen"),
 ],
},

{
 "slug": "weisser-blazer",
 "cat": "standesamt",
 "title": "Weißer Blazer: 5 Kombinationen von Standesamt bis Büro",
 "teaser": "Ein Teil, fünf Anlässe. Warum der weiße Blazer gerade der meistgesuchte Artikel der Saison ist – und wie man ihn trägt, ohne dass er nach Kellner aussieht.",
 "img": "post-blazer.jpg",
 "meta": "Weißer Blazer kombinieren: fünf Looks für Standesamt, Büro, Abend und Wochenende, jeweils komplett zusammengestellt.",
 "intro": [
   "Auf Pinterest gehört „white blazer outfits\" zu den am stärksten wachsenden Suchbegriffen der Saison. Der Grund ist praktisch: Kaum ein Teil deckt so viele Anlässe ab, ohne dass man es umstylen muss.",
   "Die Fallstricke sind auch klar: falscher Schnitt, falsches Weiß, falsche Knopfhaltung.",
 ],
 "sections": [
   ("Erstens: nie zugeknöpft", [
     "Ein zugeknöpfter weißer Blazer sieht nach Uniform aus – Kellner, Kreuzfahrt, Empfang. Offen getragen entsteht eine vertikale Linie, die streckt und locker wirkt. Wer die Taille betonen will, nimmt einen Gürtel über den offenen Blazer statt den Knopf.",
   ]),
   ("Zweitens: gebrochenes Weiß statt Reinweiß", [
     "Reinweiß wirkt hart und zeigt jeden Fleck. Cream, Elfenbein und Off-White sind wärmer, schmeichelhafter im Gesicht und deutlich unempfindlicher.",
   ]),
   ("Die fünf Kombinationen", [
     "Standesamt: über cremefarbenem Slipdress, kleine Tasche, flache Schuhe.",
     "Büro: über schwarzem Feinstrick und weiter Hose in Charcoal, Loafer.",
     "Abend: über schwarzem Top und dunkler Jeans, goldene Kette, Absatz.",
     "Wochenende: über Ringelshirt und Cream-Hose, weiße Sneaker – der Coastal-Prep-Look.",
     "Sommerhochzeit: über einem farbigen Midikleid als Schicht für den Abend.",
   ]),
 ],
 "products": [
   ("Weißer Blazer in Cream oder Off-White", "Das Kernstück. Oversize-Schnitt, offen getragen.", "blazer damen creme oversize"),
   ("Gestreiftes Poloshirt oder Ringelshirt", "Macht aus dem Blazer sofort einen Wochenendlook.", "ringelshirt damen gestreift"),
   ("Weite Hose in Charcoal", "Die Büro-Variante. Bundfaltenschnitt wirkt hochwertiger als eine gerade Hose.", "bundfaltenhose damen"),
   ("Weiße Ledersneaker", "Der Schuh, der den Look erwachsen hält, wenn der Rest legerer wird.", "B077MJJM3W"),
   ("Breiter Ledergürtel", "Über dem offenen Blazer getragen ersetzt er den Knopf – ohne die Uniform-Wirkung.", "B08M8T934N"),
 ],
},

# ============================ BÜRO ============================
{
 "slug": "quiet-business",
 "cat": "buero",
 "title": "Quiet Business: 6 Büro-Looks ohne Kostüm",
 "teaser": "Der Anzug ist weg, der Hoodie geht nicht. Sechs Kombinationen für den Bereich dazwischen, den kaum jemand sauber trifft.",
 "img": "cat-buero.jpg",
 "meta": "Büro-Outfits ohne Kostüm: sechs Quiet-Business-Looks für Damen und Herren, komplett zusammengestellt.",
 "intro": [
   "In den meisten Büros gibt es keinen Dresscode mehr, aber sehr wohl eine unausgesprochene Erwartung. Wer sie verfehlt, merkt es erst im Meeting mit externen Gästen.",
   "Quiet Business löst das über Material und Schnitt statt über Förmlichkeit: keine Krawatte, aber guter Stoff. Kein Kostüm, aber saubere Linien.",
 ],
 "sections": [
   ("Das Prinzip: ein formelles Teil pro Outfit", [
     "Ein einziges Teil trägt die Förmlichkeit – meist der Blazer, manchmal die Hose, manchmal die Schuhe. Der Rest darf entspannt sein. Zwei formelle Teile ergeben ein Kostüm, null ergeben Freizeit.",
   ]),
   ("Material entscheidet mehr als Farbe", [
     "Wolle, Leinen, feiner Baumwollköper und Viskose-Mischungen wirken im Büro sofort erwachsener als Jersey und Polyester – unabhängig von der Farbe. Ein grauer Wollpullover schlägt ein schwarzes Jerseyoberteil.",
   ]),
   ("Die sechs Kombinationen", [
     "Feinstrick in Oatmeal + weite Charcoal-Hose + brauner Ledergürtel + Loafer.",
     "Weißes Hemd + Bundfaltenhose in Marine + schmale Uhr.",
     "Blazer in Camel + weißes T-Shirt + dunkle gerade Jeans + Ledertasche.",
     "Utility-Hemd über schlichtem Shirt + Chino in Khaki.",
     "Rollkragen in Charcoal + Wollhose + Chelsea Boots.",
     "Hemdblusenkleid + breiter Gürtel + flache Schuhe.",
   ]),
 ],
 "products": [
   ("Feinstrickpullover in Oatmeal oder Grau", "Wolle statt Jersey – das ist der ganze Unterschied. Alltagstauglich und dennoch büro-tauglich.", "feinstrick pullover damen wolle"),
   ("Bundfaltenhose in Charcoal oder Marine", "Wirkt hochwertiger als jede gerade Hose und verzeiht deutlich mehr.", "bundfaltenhose damen elegant"),
   ("Brauner Ledergürtel", "Bricht die zu perfekte Abstimmung auf und macht Schwarz weniger streng.", "guertel damen leder braun"),
   ("Loafer", "Der Schuh, der zwischen Sneaker und Pumps steht. Genau die richtige Zone.", "loafer damen leder"),
   ("Strukturierte Ledertasche", "Groß genug für Laptop, fest genug, um im Meeting nicht zusammenzusacken.", "laptoptasche damen leder"),
   ("Utility-Hemd", "Das legere Teil, das trotzdem nach Absicht aussieht. Über einem Shirt als leichte Jacke.", "utility hemd damen"),
 ],
},

{
 "slug": "weite-hose-regel",
 "cat": "buero",
 "title": "Weite Hose, schmale Silhouette – die Regel dahinter",
 "teaser": "Weite Schnitte sind zurück. Warum sie bei manchen elegant aussehen und bei anderen nach Schlafanzug – und was der Unterschied ist.",
 "img": "post-weite-hose.jpg",
 "meta": "Weite Hosen richtig kombinieren: die Regel für Proportion, Bundhöhe und Schuhwahl, mit fertigen Outfit-Kombinationen.",
 "intro": [
   "Bundfaltenhosen, Baggy-Schnitte und weite Anzughosen gehören zu den auffälligsten Rückkehrern der Saison. Und zu den riskantesten: Zwischen souverän und formlos liegen wenige Zentimeter.",
 ],
 "sections": [
   ("Die Regel: weit oben, schmal unten – oder umgekehrt", [
     "Eine Silhouette verträgt genau ein weites Element. Weite Hose plus Oversize-Pullover ergibt eine Säule ohne erkennbare Form. Weite Hose plus körpernahes Oberteil ergibt eine Linie, die Größe schafft.",
     "Wer das Oversize-Oberteil trotzdem will: in die Hose stecken, zumindest vorne. Der sichtbare Bund stellt die Taille wieder her.",
   ]),
   ("Die Bundhöhe entscheidet über die Beinlänge", [
     "Je höher der Bund sitzt, desto länger wirkt das Bein. Eine hüftige weite Hose verkürzt fast immer. Hoher Bund plus Schuh in der Farbe der Hose oder der Haut verlängert am stärksten.",
   ]),
   ("Die Länge ist keine Geschmacksfrage", [
     "Weite Hosen brauchen Länge – der Saum sollte auf dem Schuh aufliegen und eine leichte Falle bilden. Zu kurz wirkt sofort wie ein Fehlkauf. Das ist der häufigste Grund, warum weite Hosen im Laden gut und zuhause schlecht aussehen.",
   ]),
 ],
 "products": [
   ("Bundfaltenhose mit hohem Bund", "Der hohe Bund ist nicht Stilfrage, sondern Proportionsfrage.", "B0CGGXP683"),
   ("Körpernaher Feinstrick", "Das Gegengewicht zur Weite. Ohne ihn fehlt die Silhouette.", "B07V3DN7LN"),
   ("Breiter Gürtel", "Macht den Bund sichtbar und die Taille wieder zum Bezugspunkt.", "B08M8T934N"),
   ("Loafer oder Absatz in Hosenfarbe", "Verlängert die Linie. Ein kontrastierender Schuh schneidet sie ab.", "B0CB5ZBZ8L"),
 ],
},

{
 "slug": "capsule-buero",
 "cat": "buero",
 "title": "Capsule Wardrobe fürs Büro: 12 Teile, 20 Outfits",
 "teaser": "Nicht mehr kaufen, sondern besser kombinieren. Die zwölf Teile, aus denen sich drei Wochen Büro bestreiten lassen.",
 "img": "post-capsule-buero.jpg",
 "meta": "Capsule Wardrobe fürs Büro: zwölf Basisteile, aus denen sich über zwanzig Outfits kombinieren lassen – mit Einkaufsliste.",
 "intro": [
   "Der Januar ist auf Pinterest die Zeit der Kleiderschrank-Suche: ausmisten, ordnen, neu anfangen. Der Grund, warum die meisten Versuche scheitern, ist nicht Disziplin, sondern Farbchaos.",
   "Eine Capsule funktioniert nur, wenn jedes Teil mit jedem anderen kann. Das erzwingt eine Entscheidung, die vor dem ersten Kauf fällt: die Grundpalette.",
 ],
 "sections": [
   ("Schritt 1: zwei Neutrale und eine Akzentfarbe", [
     "Wähle zwei Neutraltöne, die zusammen funktionieren – etwa Charcoal und Cream, oder Marine und Camel. Dazu eine einzige Akzentfarbe, in der maximal zwei Teile existieren. Alles außerhalb dieser Palette fliegt raus oder wird nicht gekauft.",
   ]),
   ("Schritt 2: die zwölf Teile", [
     "Zwei Hosen (eine weite, eine gerade), ein Rock oder Kleid, drei Oberteile (Hemd, Feinstrick, T-Shirt), zwei Schichten (Blazer, Cardigan oder Weste), ein Mantel, zwei Paar Schuhe (Loafer und ein eleganterer Schuh), eine Tasche.",
     "Zwölf Teile in einer Palette ergeben rechnerisch über zwanzig tragbare Kombinationen. Zwölf Teile in sechs Farben ergeben etwa fünf.",
   ]),
   ("Schritt 3: Accessoires machen die Wiederholung unsichtbar", [
     "Wer dieselbe Hose dreimal pro Woche trägt, fällt nur auf, wenn der Rest identisch ist. Gürtel, Tuch und Schmuck sind die günstigste Art, Varianz zu erzeugen – und die einzige, die keinen Platz im Schrank braucht.",
   ]),
 ],
 "products": [
   ("Blazer in Charcoal oder Camel", "Die wichtigste Schicht. Trägt allein die Förmlichkeit des ganzen Outfits.", "blazer damen wolle"),
   ("Weite Hose und gerade Hose", "Zwei Schnitte reichen. Beide in Neutraltönen aus der Palette.", "stoffhose damen"),
   ("Feinstrick in zwei Neutraltönen", "Die Arbeitspferde der Capsule. Wolle oder Merino statt Baumwollmix.", "merino pullover damen"),
   ("Ärmellose Weste", "Die unterschätzte dritte Schicht – leichter als ein Blazer, formeller als ein Cardigan.", "weste damen lang"),
   ("Seidentücher in Palettenfarben", "Die günstigste Varianz. Zwei Tücher verändern zwölf Outfits.", "seidentuch damen set"),
   ("Zwei Gürtel, schmal und breit", "Verändern Silhouette und Formalität desselben Teils.", "guertel damen set"),
 ],
},

# ============================ HERBST ============================
{
 "slug": "khaki-coded",
 "cat": "herbst",
 "title": "Khaki Coded: die Herren-Garderobe für Herbst 2026",
 "teaser": "Field Jacket, Utility-Hemd, braunes Leinen, Bundfaltenhose. Der Herrentrend der Saison ist erfreulich unaufwendig.",
 "img": "cat-herbst.jpg",
 "meta": "Khaki Coded: Herren-Outfits für Herbst 2026 mit Field Jacket, Utility-Hemd und Bundfaltenhose – komplett zusammengestellt.",
 "intro": [
   "Der Herrentrend dieser Saison heißt in der Pinterest-Sprache Khaki Coded und ist im Kern eine Rückkehr zu funktionaler Kleidung: Militär- und Arbeitsschnitte in gedeckten Erdtönen, mit sichtbaren Taschen und robusten Stoffen.",
   "Das Praktische daran: Fast alle Teile sind Klassiker, die nicht in zwei Jahren peinlich aussehen.",
 ],
 "sections": [
   ("Die Palette", [
     "Khaki, Oliv, Sand, Braun, Rost und gebrochenes Weiß. Schwarz kommt in diesem Look kaum vor – und genau das macht ihn weicher und weniger streng als der übliche Herbst.",
   ]),
   ("Die vier Schlüsselteile", [
     "Das Field Jacket: die Jacke mit vier aufgesetzten Taschen. Über Hemd und Pullover, offen getragen.",
     "Das Utility-Hemd: dickerer Stoff, Brusttaschen, wird offen als leichte Jacke über einem T-Shirt getragen.",
     "Das braune Leinenhemd: der weichste Teil des Looks, allein oder als Schicht.",
     "Die Bundfaltenhose in Khaki: der Schnitt, der dem Ganzen die Erwachsenheit gibt.",
   ]),
   ("Wie man den Militär-Effekt vermeidet", [
     "Nicht mehr als zwei Utility-Teile gleichzeitig. Field Jacket plus Cargohose plus Springerstiefel ist eine Verkleidung. Field Jacket plus Leinenhemd plus schlichte Hose ist ein Outfit.",
     "Ein weiches Teil pro Look – Leinen, Feinstrick oder Baumwollflanell – nimmt die Härte raus.",
   ]),
 ],
 "products": [
   ("Field Jacket in Oliv", "Das Kernstück. Ein Klassiker, der jede Saison überlebt.", "field jacket herren oliv"),
   ("Braunes Leinenhemd", "Das weiche Gegengewicht. Allein oder als Schicht.", "leinenhemd herren braun"),
   ("Utility-Hemd", "Als leichte Jacke über dem Shirt, offen getragen.", "overshirt herren"),
   ("Bundfaltenhose in Khaki", "Gibt dem funktionalen Look die nötige Struktur.", "bundfaltenhose herren"),
   ("Ledergürtel in Braun", "Verbindet die Erdtöne. Einheitsgröße gibt es hier nicht – Länge vorher messen.", "guertel herren leder braun"),
   ("Schlichte Ledersneaker oder Chukka Boots", "Keine Springerstiefel. Das ist der Unterschied zwischen Look und Kostüm.", "chukka boots herren"),
 ],
},

{
 "slug": "poetcore-cape",
 "cat": "herbst",
 "title": "Poetcore: der Cape-Look für den Herbst",
 "teaser": "Capes, Satchel-Taschen, Krawattendetails und viel Textur. Der romantischste Trend der Saison – und wie man ihn trägt, ohne kostümiert zu wirken.",
 "img": "post-cape.jpg",
 "meta": "Poetcore-Outfits für den Herbst: Cape, Satchel-Tasche und Krawatten-Accessoires alltagstauglich kombiniert.",
 "intro": [
   "Poetcore ist einer der auffälligsten Pinterest-Trends dieser Saison: literarisch, weich, ein bisschen 19. Jahrhundert. Capes, Umhänge, Satchel-Taschen, Tücher am Hals, viel Wolle und Samt.",
   "Wie bei jedem stark aufgeladenen Trend gilt: ein Element genügt. Wer alle gleichzeitig trägt, sieht aus wie auf dem Weg zur Lesung in Kostüm.",
 ],
 "sections": [
   ("Ein Trendteil, drei Basisteile", [
     "Das Cape ist auffällig genug, um allein zu tragen. Darunter reichen schlichte Hose, schlichter Rollkragen, schlichte Stiefel. Wer zusätzlich Rüschenbluse und Samtrock trägt, verliert die Balance.",
   ]),
   ("Die Satchel-Tasche ist der leichtere Einstieg", [
     "Wem das Cape zu viel ist: Die Satchel-Tasche mit Überschlag und Schnalle transportiert dieselbe Stimmung, kostet weniger und lässt sich das ganze Jahr tragen. Auf Pinterest ist sie einer der am stärksten wachsenden Accessoire-Suchbegriffe.",
   ]),
   ("Krawattendetails am Hals", [
     "Ein schmales Seidenband, eine gebundene Schleife am Blusenkragen, ein locker geknotetes Tuch – das dritte Element des Looks. Alle drei sind Einheitsgröße und damit risikofrei zu kaufen.",
   ]),
 ],
 "products": [
   ("Cape oder Umhang-Mantel", "Das eine auffällige Teil. Alles darunter bleibt schlicht.", "cape damen wolle"),
   ("Satchel-Tasche mit Überschlag", "Der leichtere Einstieg in den Look – und ganzjährig tragbar.", "satchel tasche damen leder"),
   ("Bluse mit Schleifenkragen", "Trägt das Krawattendetail bereits eingebaut.", "bluse damen schleife"),
   ("Schmales Seidenband oder Krawattentuch", "Einheitsgröße, kostet wenig, verändert den ganzen Look.", "krawattentuch damen seide"),
   ("Rollkragenpullover in Charcoal", "Das schlichte Gegengewicht unter dem Cape.", "rollkragenpullover damen"),
 ],
},

{
 "slug": "layering-regeln",
 "cat": "herbst",
 "title": "Layering ohne Michelin-Effekt: 4 Regeln",
 "teaser": "Übereinander anziehen kann jeder. Übereinander anziehen und dabei schlanker statt breiter wirken ist eine Technik.",
 "img": "post-layering.jpg",
 "meta": "Layering im Herbst richtig gemacht: vier Regeln zu Länge, Volumen, Material und Farbe, damit Schichten nicht auftragen.",
 "intro": [
   "Der Übergang ist die Jahreszeit, in der man morgens friert und mittags schwitzt. Schichten sind die Lösung – aber jede Schicht kostet Silhouette, wenn man sie falsch stapelt.",
 ],
 "sections": [
   ("Regel 1: unterschiedliche Längen", [
     "Drei Teile, drei Längen. Das innerste kurz, das mittlere länger, das äußere am längsten – oder bewusst genau umgekehrt. Gleiche Längen übereinander erzeugen eine harte, breite Kante an der Hüfte.",
   ]),
   ("Regel 2: nur eine Schicht darf voluminös sein", [
     "Dicker Strick unter Steppjacke unter Wollmantel ist warm und formlos. Feines Merino unter Hemd unter Mantel ist genauso warm und behält die Linie. Wärme entsteht durch die Anzahl der Schichten, nicht durch ihre Dicke.",
   ]),
   ("Regel 3: eine durchgehende vertikale Linie offenlassen", [
     "Ein offener Mantel, ein offener Blazer, eine offene Strickjacke – irgendetwas sollte senkrecht durchlaufen. Diese Linie ist das, was die Silhouette schmal hält.",
   ]),
   ("Regel 4: Farben von innen nach außen dunkler oder heller", [
     "Ein Verlauf wirkt geordnet, ein Wechsel wirkt zufällig. Hell innen, dunkel außen ist der sicherste Weg – oder komplett Ton in Ton.",
   ]),
 ],
 "products": [
   ("Feines Merino-Longsleeve", "Die unterste Schicht. Dünn, warm, trägt nicht auf.", "merino longsleeve damen"),
   ("Hemd in Baumwollflanell", "Die mittlere Schicht, halb offen getragen.", "flanellhemd damen"),
   ("Langer offener Mantel", "Die vertikale Linie, die alles zusammenhält.", "mantel damen lang wolle"),
   ("Langer Schal in Neutralton", "Verlängert die vertikale Linie zusätzlich, wenn er gerade herabhängt statt gewickelt zu werden.", "schal damen lang wolle"),
 ],
},

# ============================ FESTTAGE ============================
{
 "slug": "weihnachtsfeier",
 "cat": "festtage",
 "title": "Weihnachtsfeier-Outfit: 6 Looks vom Büro bis zum Abend",
 "teaser": "Die Firmenfeier ist der Anlass mit dem höchsten Fehlerpotenzial: zu festlich ist unangenehm, zu alltäglich auch. Sechs Kombinationen, die beides vermeiden.",
 "img": "cat-festtage.jpg",
 "meta": "Weihnachtsfeier-Outfits: sechs Looks für die Firmenfeier, die vom Bürotag direkt in den Abend funktionieren.",
 "intro": [
   "Bei den meisten Firmenfeiern geht man direkt aus dem Büro hin. Das heißt: Das Outfit muss acht Stunden Arbeit und vier Stunden Feier überstehen, ohne in einem der beiden Kontexte falsch zu sein.",
   "Der professionelle Trick dafür ist alt und funktioniert immer noch: Man wechselt nicht das Outfit, sondern zwei Teile.",
 ],
 "sections": [
   ("Die Zwei-Teile-Methode", [
     "Das Grundoutfit bleibt bürotauglich. Für den Abend werden genau zwei Dinge getauscht: der Schuh und ein Accessoire – oder das Oberteil und der Schmuck. Mehr passt nicht in die Bürotasche und mehr braucht es auch nicht.",
     "Beispiel: Charcoal-Hose und Feinstrick bleiben. Loafer werden zu Absatzschuhen, dazu kommt eine Brosche und ein Paar auffällige Ohrringe. Fertig.",
   ]),
   ("Was auf Firmenfeiern nicht funktioniert", [
     "Alles, worin man nicht sitzen, essen und stehen kann. Und alles, was am nächsten Morgen im Büro kommentiert wird. Der Maßstab ist nicht „schön\", sondern „will ich darüber sprechen\".",
   ]),
   ("Der Samt-Blazer ist die sicherste Wahl", [
     "Samt ist festlich, ohne glänzend zu sein, und funktioniert in Burgunder, Waldgrün oder Charcoal auch über den Dezember hinaus. Über einem schlichten Oberteil getragen ist er das einzige auffällige Teil und braucht keine weitere Unterstützung.",
   ]),
 ],
 "products": [
   ("Samt-Blazer in Burgunder oder Waldgrün", "Festlich ohne Glanz. Das einzige auffällige Teil im Look.", "samt blazer damen"),
   ("Bluse mit hohem Kragen", "Der Trend der Saison und gleichzeitig büro-tauglich.", "bluse damen stehkragen"),
   ("Brosche mit Steinbesatz", "Das Abend-Accessoire, das in jede Bürotasche passt. Einheitsgröße.", "B08MF2NR3K"),
   ("Goldene Statement-Ohrringe", "Zweites Tauschteil der Zwei-Teile-Methode.", "B0D9RT25LN"),
   ("Absatzschuhe zum Wechseln", "Bleiben bis 17 Uhr unter dem Schreibtisch.", "B0C6YJWY8R"),
   ("Kleine Abendtasche", "Klein genug, dass sie den ganzen Tag in der großen Tasche mitfährt.", "B0B4J3WGWR"),
 ],
},

{
 "slug": "silvester-gold",
 "cat": "festtage",
 "title": "Silvester in Gold: Glamour ohne Kostüm-Effekt",
 "teaser": "Achtziger-Luxus ist zurück: breite Schultern, hoher Kragen, schwerer Goldschmuck. Wie viel davon verträgt ein echter Abend?",
 "img": "post-silvester-gold.jpg",
 "meta": "Silvester-Outfits mit Gold und Glamour: festliche Looks im Achtziger-Stil, alltagstauglich heruntergebrochen.",
 "intro": [
   "„80s luxury\" gehört zu den am stärksten wachsenden Pinterest-Suchbegriffen dieser Saison. Übersetzt heißt das: markante Schultern, hohe Kragen, breite Gürtel, schwerer Goldschmuck, satte Farben.",
   "Vollständig getragen ist das eine Verkleidung. In Dosierung ist es der beste Silvesterlook seit Jahren.",
 ],
 "sections": [
   ("Ein Element, maximal zwei", [
     "Entweder die Schulter oder der Kragen oder der Schmuck. Wer alle drei nimmt, landet im Kostümverleih. Am zugänglichsten ist der Schmuck: ein breiter goldener Armreif transportiert den ganzen Look, ohne dass ein einziges Kleidungsstück auffällig sein muss.",
   ]),
   ("Gold richtig stapeln", [
     "Zwei bis drei Armreifen an einem Arm, unterschiedlich breit, alle in derselben Goldnuance. Der andere Arm bleibt frei oder trägt nur die Uhr. Symmetrie wirkt hier steif.",
     "Bei Ketten dasselbe Prinzip mit unterschiedlichen Längen: kurz, mittel, lang – aber nicht mehr als drei.",
   ]),
   ("Der Kragen als leiseste Variante", [
     "Eine Bluse mit hohem oder markantem Kragen unter einem schlichten dunklen Blazer bringt die Silhouette der Achtziger, ohne dass jemand „Achtziger\" denkt. Die konservativste und tragbarste Version des Trends.",
   ]),
 ],
 "products": [
   ("Breiter goldener Armreif (Cuff)", "Transportiert den ganzen Look allein. Biegbar, also Einheitsgröße.", "armreif gold breit damen"),
   ("Bluse mit hohem Kragen", "Die tragbarste Version des Achtziger-Trends.", "bluse damen hoher kragen"),
   ("Blazer mit markanter Schulter", "Nur wählen, wenn Schmuck und Kragen zurückhaltend bleiben.", "blazer damen schulterpolster"),
   ("Goldketten in drei Längen", "Kurz, mittel, lang – gestapelt, nie symmetrisch.", "B0DC438QJT"),
   ("Breiter Gürtel in Gold oder Schwarz", "Setzt die Taille, wenn der Rest gerade geschnitten ist.", "B0F1MJZ5W5"),
 ],
},

# ============================ ACCESSOIRES ============================
{
 "slug": "brosche-tragen",
 "cat": "accessoires",
 "title": "Brosche richtig tragen: 7 Positionen, die 2026 funktionieren",
 "teaser": "Die Brosche ist zurück – und zwar nicht als Erbstück am Trachtenjanker. Sieben Positionen und was sie jeweils bewirken.",
 "img": "post-brosche.jpg",
 "meta": "Brosche tragen: sieben Positionen für Revers, Kragen, Schulter, Gürtel und Tasche – mit Kaufempfehlungen.",
 "intro": [
   "„Brooch aesthetic\" und „maximalist accessories\" gehören zu den auffälligsten Aufsteigern auf Pinterest. Der Grund ist praktisch: Eine Brosche kostet wenig, hat keine Größe und verändert ein Outfit mehr als ein neues Kleidungsstück.",
   "Was sie schwierig macht, ist nicht die Brosche selbst, sondern die Position.",
 ],
 "sections": [
   ("Die sieben Positionen", [
     "Am linken Revers, etwa auf Höhe des Schlüsselbeins – die klassische Position, wirkt formell und sicher.",
     "Am Blusenkragen, mittig statt seitlich – wirkt moderner und weniger nach Tracht.",
     "An der Schulter, fast auf der Naht – zieht den Blick nach oben und verbreitert optisch, gut bei schmalen Schultern.",
     "An der Taille auf dem Gürtel – ersetzt eine auffällige Schnalle.",
     "Am Mantelkragen statt am Sakko – die einfachste Art, einen schlichten Wollmantel zu individualisieren.",
     "Auf der Tasche, am Überschlag – dort, wo sie garantiert nicht am Stoff zieht.",
     "Als Gruppe: drei kleine statt einer großen, in unregelmäßigem Abstand. Das ist die aktuelle Variante.",
   ]),
   ("Was den Trachten-Effekt erzeugt", [
     "Drei Dinge: perfekte Symmetrie, Blumenmotiv in bunten Emailfarben, und die Position ganz oben am Revers. Wer eines davon bricht, ist raus. Am einfachsten über die Farbe – gedecktes Gold, Perlmutt oder Strass statt bunter Emaille.",
   ]),
   ("Auf welchen Stoffen sie hält", [
     "Wolle, Tweed, Filz, Jeans und dichte Baumwolle tragen eine Brosche ohne zu leiden. Seide, Feinstrick und Jersey nicht – dort zieht die Nadel Löcher. Für diese Stoffe gibt es Magnetbroschen.",
   ]),
 ],
 "products": [
   ("Brosche in gedecktem Gold", "Der sichere Einstieg. Keine Größe, kein Fehlkauf.", "brosche gold vintage"),
   ("Set aus drei kleinen Anstecknadeln", "Die aktuelle Trage-Variante: gruppiert statt einzeln.", "anstecknadel set damen"),
   ("Perlenbrosche", "Am wenigsten trachtenanfällig, passt zu Wolle und Tweed.", "brosche perle elegant"),
   ("Magnetbrosche", "Für Seide und Feinstrick, wo eine Nadel Löcher zieht.", "magnetbrosche damen"),
   ("Wollmantel als Trägerfläche", "Der beste Untergrund: dicht genug für die Nadel, schlicht genug als Hintergrund.", "wollmantel damen schlicht"),
 ],
},

{
 "slug": "breiter-guertel",
 "cat": "accessoires",
 "title": "Ein breiter Gürtel, vier Outfits",
 "teaser": "Der schmale Gürtel war jahrelang Standard. Jetzt ist die Breite zurück – und sie kann mehr, als eine Hose zu halten.",
 "img": "post-guertel.jpg",
 "meta": "Breiten Gürtel kombinieren: vier Outfits mit Blazer, Kleid, Strickjacke und Mantel, plus die Regeln zu Breite und Sitzhöhe.",
 "intro": [
   "„Chunky belt\" ist einer der am stärksten wachsenden Accessoire-Begriffe der Saison – und der Gürtel ist eines der wenigen Accessoires, die eine Silhouette wirklich verändern statt sie nur zu schmücken.",
 ],
 "sections": [
   ("Die vier Kombinationen", [
     "Über dem offenen Blazer: ersetzt den Knopf, setzt die Taille, ohne die Uniform-Wirkung eines geschlossenen Blazers.",
     "Über dem Strickkleid oder der langen Strickjacke: verwandelt ein formloses Teil in eine Silhouette. Der stärkste Effekt von allen.",
     "Über dem Mantel: funktioniert nur bei geradem, ungefüttertem Schnitt – bei einem dicken Wollmantel entstehen Wülste.",
     "In der weiten Hose: macht den hohen Bund sichtbar und damit die Beine optisch länger.",
   ]),
   ("Sitzhöhe entscheidet über die Wirkung", [
     "Auf der schmalsten Stelle der Taille getragen verkürzt der Gürtel den Oberkörper und verlängert die Beine. Auf der Hüfte getragen macht er das Gegenteil. Es gibt keine richtige Höhe – nur eine, die zu dem passt, was man erreichen will.",
   ]),
   ("Breite und Statur", [
     "Faustregel: Je kürzer der Oberkörper, desto schmaler der Gürtel. Ein sehr breiter Gürtel braucht Platz zwischen Rippenbogen und Hüfte. Wer den nicht hat, nimmt vier statt acht Zentimeter – der Effekt bleibt, die Proportion stimmt.",
   ]),
 ],
 "products": [
   ("Breiter Ledergürtel mit schlichter Schnalle", "Das Basisteil. Vorher Länge messen – Gürtel sind keine Einheitsgröße.", "guertel damen breit leder"),
   ("Bindegürtel aus Stoff", "Echte Einheitsgröße, keine Lochreihe, passt über Mantel und Strickjacke.", "bindeguertel damen"),
   ("Strickkleid als Trägerteil", "Das Teil, bei dem der Gürtel den größten Unterschied macht.", "strickkleid damen midi"),
   ("Lange Strickjacke", "Zweite Trägerfläche. Offen mit Gürtel getragen entsteht eine völlig andere Silhouette.", "strickjacke damen lang"),
 ],
},

{
 "slug": "seidentuch-binden",
 "cat": "accessoires",
 "title": "5 Arten, ein Seidentuch zu binden",
 "teaser": "Ein Tuch, fünf Wirkungen – vom unauffälligen Halsband bis zum Statement am Taschengriff.",
 "img": "post-tuch.jpg",
 "meta": "Seidentuch binden: fünf Anleitungen für Hals, Haar, Tasche und Gürtel, plus die passenden Tuchgrößen.",
 "intro": [
   "Ein Seidentuch ist das effizienteste Accessoire überhaupt: Es hat keine Größe, kostet wenig, wiegt nichts und bringt gleichzeitig Farbe, Muster und Textur in ein Outfit. Der Grund, warum es trotzdem in der Schublade liegt, ist meistens Unsicherheit beim Binden.",
 ],
 "sections": [
   ("1. Das schmale Halsband", [
     "Tuch diagonal zu einem schmalen Streifen falten, einmal um den Hals legen, vorne mit einem einfachen Knoten schließen und den Knoten seitlich drehen. Die unauffälligste Variante – funktioniert unter Hemdkragen und über Rollkragen.",
   ]),
   ("2. Der lose Kragenknoten", [
     "Tuch zum Dreieck falten, Spitze auf die Brust, Enden hinten kreuzen und vorne locker verknoten. Wirkt französischer und weniger streng als das Halsband.",
   ]),
   ("3. Das Krawattenband", [
     "Ein schmales, langes Tuch unter dem Blusenkragen durchführen und wie eine lockere Krawatte binden. Das ist die Variante, die diese Saison auf Pinterest am stärksten wächst.",
   ]),
   ("4. Am Taschengriff", [
     "Um den Henkel gewickelt und mit einem kleinen Knoten geschlossen. Macht aus einer schlichten Tasche ein individuelles Teil – und ist die risikoloseste Art, ein auffälliges Muster zu tragen.",
   ]),
   ("5. Im Haar oder als Gürtel", [
     "Als Band im Haar, um einen Pferdeschwanz gewickelt, oder durch die Gürtelschlaufen gezogen und seitlich verknotet. Beide Varianten brauchen ein langes, schmales Tuch statt eines quadratischen.",
   ]),
   ("Welche Größe wofür", [
     "Quadratisch, etwa 50 × 50 cm: Halsband und Kragenknoten. Quadratisch, 90 × 90 cm: Schultertuch und Taschengriff. Lang und schmal: Krawattenband, Haar und Gürtel. Wer nur eines kauft, nimmt das kleine Quadrat – es kann am meisten.",
   ]),
 ],
 "products": [
   ("Seidentuch 50 × 50 cm", "Die vielseitigste Größe. Wer nur eines kauft, nimmt dieses.", "B0BX963Q6V"),
   ("Großes Tuch 90 × 90 cm", "Für Schulter und Taschengriff.", "B09TSZ8MNV"),
   ("Schmales langes Seidenband", "Für Krawattenband, Haar und Gürtel.", "B0B8MF1RRZ"),
   ("Set aus drei Tüchern", "Der günstigste Einstieg, um Muster und Farben auszuprobieren.", "seidentuch set damen"),
   ("Schlichte Tasche als Trägerfläche", "Je einfacher die Tasche, desto stärker wirkt das Tuch daran.", "handtasche damen schlicht leder"),
 ],
},

{
 "slug": "goldschmuck-stapeln",
 "cat": "accessoires",
 "title": "Goldschmuck stapeln, ohne zu übertreiben",
 "teaser": "Layering funktioniert auch beim Schmuck – nach genau drei Regeln, die den Unterschied zwischen kuratiert und überladen machen.",
 "img": "post-goldschmuck.jpg",
 "meta": "Goldschmuck stapeln: drei Regeln für Ketten, Armreifen und Ringe, mit konkreten Kombinationen und Kaufempfehlungen.",
 "intro": [
   "„Gold cuff\" und „heirloom jewelry\" wachsen auf Pinterest deutlich – der Trend geht zu schwererem, weniger filigranem Gold. Und zu mehr davon gleichzeitig.",
   "Der Grat ist schmal. Drei Regeln halten ihn begehbar.",
 ],
 "sections": [
   ("Regel 1: eine Goldnuance", [
     "Gelbgold, Roségold und blasses Gold nebeneinander wirken nicht gestapelt, sondern zusammengesucht. Bei Modeschmuck ist das der häufigste Fehler, weil die Nuancen zwischen Herstellern stark schwanken. Am besten innerhalb einer Serie kaufen.",
   ]),
   ("Regel 2: ungerade Zahlen und ungleiche Breiten", [
     "Drei Armreifen unterschiedlicher Breite wirken kuratiert. Zwei gleiche wirken zufällig, vier symmetrische wirken uniform. Dasselbe gilt für Ketten: drei Längen, drei Stärken.",
   ]),
   ("Regel 3: ein Körperteil pro Look", [
     "Entweder Hals oder Handgelenke oder Ohren tragen den Stapel – nicht alle drei. Wer am Hals stapelt, trägt an den Ohren nur kleine Stecker. Das ist der Unterschied zwischen einer Aussage und einem Auslagentisch.",
   ]),
   ("Womit Gold besonders gut funktioniert", [
     "Auf gedeckten Erdtönen, auf Cream und auf tiefem Grün wirkt warmes Gold am besten. Auf reinem Weiß und kaltem Grau wirkt es schnell billig – dort ist Silber die bessere Wahl.",
   ]),
 ],
 "products": [
   ("Breiter goldener Armreif", "Das Ankerstück des Stapels. Biegbar, also Einheitsgröße.", "armreif gold breit"),
   ("Set aus drei Armreifen", "Löst das Nuancen-Problem, weil alle aus einer Serie stammen.", "armreif set gold damen"),
   ("Goldketten in drei Längen", "Kurz, mittel, lang – nie gleich lang.", "halskette gold layering set"),
   ("Kleine Goldstecker", "Das Gegengewicht, wenn der Stapel am Hals sitzt.", "ohrstecker gold klein"),
   ("Feiner Ring-Set", "Der leiseste Einstieg ins Stapeln.", "ringe set gold damen"),
 ],
},

{'slug': 'weihnachtsmarkt-outfit',
 'cat': 'festtage',
 'title': 'Weihnachtsmarkt-Outfit: warm anziehen, ohne wie ein Bündel auszusehen',
 'teaser': 'Drei Stunden bei vier Grad stehen, Glühwein in der Hand – und trotzdem nicht aussehen wie beim '
           'Skiurlaub. Das ist eine Frage der Reihenfolge, nicht der Anzahl der Schichten.',
 'img': 'post-weihnachtsmarkt.jpg',
 'meta': 'Weihnachtsmarkt-Outfit: warm durch drei Stunden Kälte, ohne unförmig zu wirken. Die '
         'Schichtreihenfolge, die Schuhfrage und vier komplette Looks.',
 'intro': ['Der Weihnachtsmarkt ist der einzige Anlass im Jahr, bei dem man stundenlang draußen steht, ohne '
           'sich zu bewegen. Das ist etwas völlig anderes als ein Winterspaziergang – beim Gehen erzeugt der '
           'Körper Wärme, beim Stehen nicht.',
           'Die meisten ziehen deshalb einfach mehr an. Das funktioniert bis zu einem Punkt, danach wird es '
           'unförmig und man friert trotzdem, weil die Schichten sich gegenseitig zusammendrücken und die '
           'Luft dazwischen verdrängen. Genau diese Luft ist die Wärmedämmung.'],
 'sections': [['Die Reihenfolge entscheidet, nicht die Menge',
               ['Drei Schichten reichen, wenn sie in der richtigen Reihenfolge sitzen. Direkt auf der Haut '
                'etwas, das Feuchtigkeit wegtransportiert – Merinowolle oder ein technisches Funktionsshirt, '
                'niemals Baumwolle. Baumwolle saugt sich voll und kühlt dann aus.',
                'Darüber die Isolationsschicht: Feinstrick aus Wolle oder Kaschmir, locker sitzend. Und '
                'außen der Mantel, der Wind abhält. Wer diese Reihenfolge einhält, kommt mit drei Lagen '
                'weiter als jemand mit fünf.']],
              ['Die Füße sind das eigentliche Problem',
               ['Wer auf dem Weihnachtsmarkt friert, friert fast immer an den Füßen. Die Ursache ist selten '
                'der Schuh, sondern der Boden: Pflaster leitet Wärme sehr gut ab, und man steht darauf, ohne '
                'die Füße zu bewegen.',
                'Was hilft: eine dicke Profilsohle als Abstand zum Boden, eine Nummer größer, damit der '
                'Socken nicht drückt und die Luftschicht bleibt. Ein enger Stiefel mit dicker Socke ist '
                'kälter als ein weiter mit dünner.']],
              ['Vier Kombinationen, die funktionieren',
               ['Für den Abend nach der Arbeit: dunkle Wollhose, Rollkragen, Wollmantel, Chelsea Boots mit '
                'Profil. Sieht nicht nach Ausrüstung aus und hält drei Stunden.',
                'Für das Wochenende mit Kindern: gefütterte Jeans oder eine warme Cordhose, '
                'Fleece-Zwischenschicht unter dem Steppmantel, Schnürstiefel. Hier zählt Funktion mehr als '
                'Form – aber ein Steppmantel in Camel oder Dunkelgrün statt in Neonfarben macht den '
                'Unterschied.',
                'Für den Glühwein mit Freunden: Strickkleid über einer blickdichten Thermostrumpfhose, '
                'langer Mantel, flache Stiefel. Warm und nicht nach Winterjacke aussehend.',
                'Für Herren: Wollmantel über Strickpullover und Hemd, Cordhose, robuste Boots. Der Schal ist '
                'hier kein Accessoire, sondern die Schicht, die den Hals dicht macht.']],
              ['Was man weglassen sollte',
               ['Handschuhe, die man zum Bezahlen ausziehen muss, wandern nach zwanzig Minuten in die Tasche '
                'und sind dann nutzlos. Touchscreen-taugliche Modelle bleiben an.',
                'Und: keine Tasche, die beide Hände braucht. Auf dem Weihnachtsmarkt hat man in einer Hand '
                'einen Becher. Eine Umhängetasche oder ein kleiner Rucksack löst das Problem, eine '
                'Henkeltasche nicht.']]],
 'products': [['Merino-Langarmshirt als erste Schicht',
               'Wärmt auch feucht und riecht nach mehreren Tagen noch nicht. Der wichtigste Teil des Looks, '
               'obwohl man ihn nicht sieht.',
               'merino langarmshirt damen'],
              ['Wollmantel in Camel oder Dunkelgrün',
               'Windfest und lang genug, dass er beim Sitzen nicht auf dem Rücken hochrutscht.',
               'wollmantel damen lang'],
              ['Chelsea Boots mit Profilsohle',
               'Die Sohle ist der Abstand zum kalten Pflaster. Glattes Leder darunter bringt nichts.',
               'chelsea boots damen profilsohle'],
              ['Thermostrumpfhose blickdicht',
               'Macht Kleid und Rock wintertauglich, ohne dass man eine Hose braucht.',
               'thermostrumpfhose blickdicht 200 den'],
              ['Touchscreen-Handschuhe aus Wolle',
               'Bleiben an, wenn man zahlt oder fotografiert. Handschuhe in der Tasche wärmen niemanden.',
               'touchscreen handschuhe wolle'],
              ['Großer Wollschal',
               'Schließt die Lücke zwischen Mantelkragen und Hals. Dort geht die meiste Wärme verloren.',
               'wollschal gross damen']]},
{'slug': 'heiligabend-outfit',
 'cat': 'festtage',
 'title': 'Heiligabend bei der Familie: festlich, aber man muss sich hinsetzen können',
 'teaser': 'Zwischen Kirchgang, Bescherung auf dem Teppich und vier Stunden am Tisch. Ein Outfit, das alles '
           'drei aushält, hat andere Anforderungen als eines für einen Empfang.',
 'img': 'post-heiligabend.jpg',
 'meta': 'Heiligabend-Outfit für die Familie: festlich genug für den Kirchgang, bequem genug für den Abend '
         'am Tisch. Vier Looks für Damen und Herren.',
 'intro': ['Heiligabend ist kein Empfang. Man steht nicht mit einem Glas in der Hand herum, sondern sitzt – '
           'auf dem Sofa, auf dem Boden bei der Bescherung, stundenlang am Esstisch. Das ist die eigentliche '
           'Anforderung, und die meisten Outfit-Ratgeber übersehen sie.',
           'Gleichzeitig ist es der festlichste Abend des Jahres. Jogginghose geht nicht. Der Kompromiss '
           'liegt nicht in der Mitte, sondern in der Materialwahl.'],
 'sections': [['Der Stoff macht die Arbeit',
               ['Ein Wollkleid mit etwas Elasthan sieht aus wie ein Wollkleid und sitzt nach vier Stunden '
                'noch wie am Anfang. Reine Viskose sieht am Anfang besser aus und ist nach zwei Stunden '
                'zerknittert. Das ist der ganze Unterschied.',
                'Dasselbe gilt für Hosen: ein Wollmix mit Stretch statt einer steifen Anzughose. Und für '
                'Herren ein Sakko aus Jersey oder ungefüttertem Wollstrick statt eines konstruierten Blazers '
                'mit Schulterpolster.']],
              ['Festlich wird es über ein einziges Teil',
               ['Der Fehler an Heiligabend ist, alles gleichzeitig festlich zu machen: Samt, Glitzer, '
                'Schmuck, Absatz. Das wirkt schnell verkleidet, besonders im Wohnzimmer der Eltern.',
                'Besser: ein einziges festliches Element, der Rest ruhig. Ein Samtblazer über einer '
                'schlichten dunklen Hose. Oder ein einfaches Wollkleid mit auffälligen Ohrringen. Mehr '
                'braucht der Abend nicht.']],
              ['Die Schuhfrage',
               ['Bei den meisten Familien werden die Schuhe an der Tür ausgezogen. Das heißt: Die Socken '
                'oder Strumpfhosen sind Teil des Outfits, ob man will oder nicht.',
                'Wer dazu neigt, das zu vergessen: dunkle, blickdichte Strumpfhose statt hauttonfarben, und '
                'bei Herren Socken in der Farbe der Hose statt weißer Sportsocken. Es klingt banal und ist '
                'trotzdem der häufigste Bruch im ganzen Look.']],
              ['Vier Kombinationen',
               ['Damen, klassisch: dunkelgrünes oder burgunderrotes Strickkleid, blickdichte Strumpfhose, '
                'flache Stiefeletten. Dazu Ohrringe mit etwas Glanz.',
                'Damen, Hose: schwarze Wollhose mit Stretch, cremefarbene Seidenbluse, Samtblazer. '
                'Funktioniert auch, wenn es beim Kirchgang kalt ist.',
                'Herren, klassisch: dunkelblaue Wollhose, weißes Hemd, Strickjacke aus Feinstrick statt '
                'Sakko. Wärmer, bequemer, sieht abends besser aus als ein aufgeknöpfter Blazer.',
                'Herren, festlicher: Cordhose, Rollkragen, Sakko aus weichem Wollstrick. Der Rollkragen '
                'ersetzt Hemd und Krawatte komplett.']]],
 'products': [['Strickkleid aus Wollmix mit Stretch',
               'Sitzt nach vier Stunden am Tisch noch. Reine Viskose tut das nicht.',
               'strickkleid damen wolle midi'],
              ['Samt-Blazer in Dunkelgrün oder Burgunder',
               'Das eine festliche Teil. Alles andere darf ruhig bleiben.',
               'samt blazer damen'],
              ['Wollhose mit Stretchanteil',
               'Sieht aus wie eine Anzughose, verhält sich wie eine bequeme.',
               'wollhose damen stretch'],
              ['Feinstrick-Strickjacke für Herren',
               'Die bessere Alternative zum Sakko, wenn der Abend im Wohnzimmer stattfindet.',
               'strickjacke herren feinstrick'],
              ['Rollkragenpullover Merino',
               'Ersetzt Hemd und Krawatte, ohne dass es leger wirkt.',
               'rollkragenpullover herren merino'],
              ['Statement-Ohrringe in Gold',
               'Macht ein schlichtes Kleid festlich. Günstiger und flexibler als ein festliches Kleid.',
               'statement ohrringe gold']]},
{'slug': 'silvester-herren',
 'cat': 'festtage',
 'title': 'Silvester für Herren: drei Wege, festlich zu sein, ohne Smoking',
 'teaser': 'Zwischen Anzug und Alltagshemd liegt viel Platz, den kaum jemand nutzt. Drei Kombinationen für '
           'Silvester, die nicht nach Betriebsfeier aussehen.',
 'img': 'post-silvester-herren.jpg',
 'meta': 'Silvester-Outfit für Herren ohne Smoking: drei Kombinationen mit Rollkragen, Samtsakko oder '
         'dunklem Strick, je nach Anlass.',
 'intro': ['Für Herren ist Silvester der Anlass mit den wenigsten Vorgaben und deshalb der schwierigste. Bei '
           'einer Hochzeit ist klar, was gefordert ist. An Silvester steht es nirgends – und die meisten '
           'greifen deshalb zum Bürohemd.',
           'Das Problem am Bürohemd ist nicht, dass es schlecht aussieht. Es ist, dass es nach Arbeit '
           'aussieht. Und der Abend ist das Gegenteil davon.'],
 'sections': [['Weg eins: dunkler Rollkragen statt Hemd',
               ['Ein feiner Rollkragen in Schwarz, Anthrazit oder Dunkelblau unter einem Sakko ist der '
                'schnellste Weg von Büro zu Abend. Er nimmt dem Sakko das Formelle und wirkt trotzdem '
                'sortiert.',
                'Wichtig ist die Feinheit des Stricks. Grober Strick unter einem Sakko sieht nach Notlösung '
                'aus, Merino oder Kaschmir in dünner Ausführung nicht.']],
              ['Weg zwei: Samt, aber nur an einer Stelle',
               ['Ein Samtsakko in Dunkelgrün, Burgund oder Marineblau ist an Silvester angemessen und an '
                'keinem anderen Abend des Jahres. Dazu gehört alles andere ruhig: schwarze Hose, schlichtes '
                'Hemd oder Rollkragen, dunkle Schuhe.',
                'Was nicht funktioniert: Samtsakko plus glänzendes Hemd plus auffällige Schuhe. Dann kippt '
                'es ins Kostüm.']],
              ['Weg drei: durchgehend dunkel',
               ['Die unauffälligste und oft beste Lösung: alles in einer dunklen Farbfamilie, '
                'unterschiedliche Texturen. Schwarze Wollhose, schwarzer Feinstrick, schwarze Lederschuhe – '
                'und ein Mantel, der ins Auge fällt.',
                'Das wirkt teurer als es ist, weil kein Farbbruch ablenkt. Und es funktioniert vom '
                'Hausbesuch bis zur Bar.']],
              ['Die Schuhe',
               ['Sneaker gehen an Silvester nur, wenn sie aus glattem Leder und einfarbig sind. Alles mit '
                'sichtbarer Sohle, Logo oder Kontrastnaht zieht den Look nach unten.',
                'Sicherer: Chelsea Boots oder Derbys aus dunklem Leder. Beide funktionieren zu Hose und '
                'Sakko und halten einen Abend im Stehen aus.']]],
 'products': [['Merino-Rollkragen in Schwarz oder Anthrazit',
               'Unter dem Sakko der schnellste Weg von Büro zu Abend.',
               'rollkragenpullover herren merino schwarz'],
              ['Samtsakko in Dunkelgrün oder Burgund',
               'Das eine Teil, das den Abend festlich macht. Der Rest bleibt ruhig.',
               'samt sakko herren'],
              ['Wollhose in Schwarz',
               'Die Basis für alle drei Wege. Mit Stretchanteil auch nach Mitternacht bequem.',
               'wollhose herren schwarz'],
              ['Chelsea Boots aus dunklem Leder',
               'Halten einen Abend im Stehen aus und passen zu Hose wie zu Sakko.',
               'chelsea boots herren leder'],
              ['Feinstrick-Pullover in Dunkelblau',
               'Für den durchgehend dunklen Look, wenn Rollkragen nicht dein Schnitt ist.',
               'feinstrick pullover herren dunkelblau']]},
{'slug': 'winterhochzeit-gast',
 'cat': 'hochzeitsgast',
 'title': 'Winterhochzeit als Gast: die Lücke zwischen Kirche und Saal',
 'teaser': 'Eine Hochzeit im Dezember hat ein Problem, das im Sommer nicht existiert: die zwanzig Minuten '
           'zwischen Trauung und Empfang, draußen, bei null Grad.',
 'img': 'post-winterhochzeit.jpg',
 'meta': 'Winterhochzeit als Gast: Outfits für Trauung, Empfang und Abend, die auch die kalten Minuten '
         'dazwischen aushalten.',
 'intro': ['Im Sommer plant man ein Hochzeitsoutfit für innen und draußen gleichermaßen. Im Winter plant man '
           'für zwei getrennte Welten: den geheizten Saal, in dem man den Abend verbringt, und die zwanzig '
           'Minuten Sektempfang im Hof, bei denen niemand seinen Mantel holt, weil alle so tun, als sei es '
           'nicht kalt.',
           'Wer das vorher weiß, zieht sich anders an. Wer es nicht weiß, steht zitternd auf den Fotos.'],
 'sections': [['Der Mantel gehört zum Outfit, nicht darüber',
               ['Auf einer Winterhochzeit ist der Mantel auf jedem zweiten Foto zu sehen – beim Ankommen, '
                'beim Sektempfang, beim Rausgehen. Er ist damit Teil des Looks und nicht die Verpackung.',
                'Das heißt konkret: kein Alltagsmantel mit Kapuze. Ein einfarbiger Wollmantel in Camel, '
                'Dunkelgrün, Grau oder Marineblau, lang genug, dass er das Kleid vollständig verdeckt. Ein '
                'Mantel, unter dem der Kleidsaum hervorschaut, sieht immer nach Versehen aus.']],
              ['Die Ärmelfrage',
               ['Ärmellose Kleider funktionieren im Winter nur, wenn eine Lösung für die Arme mitgedacht ist '
                '– und ein Bolero ist es meistens nicht, der wirkt schnell nach 2005.',
                'Besser: langärmelige Kleider aus Wollmix oder Jersey. Oder ein ärmelloses Kleid mit einem '
                'feinen Kaschmir-Cardigan in derselben Farbfamilie, der auch am Tisch anbleiben kann, ohne '
                'wie eine Notlösung auszusehen.']],
              ['Farben, die im Winter funktionieren',
               ['Die Sommerpalette – Pastell, helles Blau, Koralle – wirkt im Dezemberlicht blass und '
                'unpassend. Winterhochzeiten vertragen Tiefe: Burgunder, Waldgrün, Petrol, Anthrazit, tiefes '
                'Blau.',
                'Weiß bleibt tabu, Creme und Champagner ebenfalls. Und Rot ist heikler als sein Ruf: ein '
                'tiefes Burgunder ist unauffällig, ein Signalrot zieht auf Fotos die Aufmerksamkeit von der '
                'Braut weg.']],
              ['Schuhe und der Weg dorthin',
               ['Zwischen Parkplatz und Kirche liegen oft nasses Pflaster oder Kies. Feine Absatzschuhe '
                'überstehen das, aber nicht schön.',
                'Die praktische Lösung: robuste Schuhe für den Weg, die feinen in der Tasche. Das machen '
                'erfahrene Hochzeitsgäste seit jeher, und es sieht niemand.']]],
 'products': [['Wollmantel in Burgunder oder Waldgrün',
               'Auf jedem zweiten Foto zu sehen. Lang genug, dass kein Kleidsaum hervorschaut.',
               'wollmantel damen lang farbig'],
              ['Langärmeliges Wollkleid in Midi-Länge',
               'Löst die Ärmelfrage, ohne dass etwas übergeworfen werden muss.',
               'wollkleid damen midi langarm'],
              ['Kaschmir-Cardigan in gedeckter Farbe',
               'Kann am Tisch anbleiben, ohne nach Notlösung auszusehen.',
               'kaschmir cardigan damen'],
              ['Blickdichte Strumpfhose 60 den',
               'Macht ein Midikleid wintertauglich, ohne dick aufzutragen.',
               'strumpfhose blickdicht 60 den'],
              ['Clutch mit abnehmbarer Kette',
               'Groß genug für Handy und Lippenstift, klein genug für den Stehtisch.',
               'clutch damen abendtasche kette'],
              ['Absatzschuhe mit Blockabsatz',
               'Halten auf Kies und Pflaster, halten auch den Abend.',
               'pumps blockabsatz damen']]},
{'slug': 'weihnachtsfeier-ab-50',
 'cat': 'festtage',
 'title': 'Weihnachtsfeier ab 50: festlich, ohne sich zu verkleiden',
 'teaser': 'Die meisten Festtags-Outfits werden für Zwanzigjährige fotografiert. Was davon übrig bleibt, '
           'wenn man nicht mehr zwanzig ist – und was besser funktioniert.',
 'img': 'post-weihnachtsfeier-ab-50.jpg',
 'meta': 'Weihnachtsfeier-Outfits ab 50: festliche Kombinationen mit klaren Schnitten, ohne Pailletten und '
         'ohne Kostüm-Effekt.',
 'intro': ['Festliche Mode wird überwiegend für sehr junge Körper entworfen und noch häufiger so '
           'fotografiert. Pailletten, Cut-outs, kurze Schnitte, viel Haut. Wer das mit fünfzig trägt, sieht '
           'meistens nicht schlecht aus, aber verkleidet.',
           'Das Gegenmittel ist nicht, unauffällig zu werden. Es ist, den Glanz zu verlagern: weg von der '
           'Fläche, hin zum Material und zur Silhouette.'],
 'sections': [['Glanz über Material statt über Fläche',
               ['Eine Bluse aus Seide glänzt, ohne zu funkeln. Samt glänzt, ohne zu funkeln. Fein gewebter '
                'Jacquard oder ein Wollstoff mit Lurexfaden glänzen ebenfalls – aber alle diese Materialien '
                'reflektieren weich statt punktuell.',
                'Pailletten und Glitzerstoffe reflektieren punktuell und hart. Sie ziehen den Blick auf die '
                'Fläche, auf der sie sitzen. Das ist mit zwanzig gewollt und mit fünfzig meistens nicht.']],
              ['Die Silhouette macht mehr als die Farbe',
               ['Was ab fünfzig fast immer funktioniert: eine klare, durchgehende Linie. Ein gerade '
                'geschnittenes Kleid, ein langer Blazer über schmaler Hose, ein Rock, der auf oder unter dem '
                'Knie endet – nie dazwischen.',
                'Was selten funktioniert: taillierte Teile mit Raffung an der Taille. Sie sollen kaschieren '
                'und betonen dadurch. Ein gerader Schnitt aus festem Stoff tut das Gegenteil.']],
              ['Drei Kombinationen',
               ['Der Blazer-Look: langer Blazer in Marineblau oder Anthrazit über schmaler Hose derselben '
                'Farbe, darunter eine Seidenbluse in Creme oder Champagner. Dazu Absatzschuhe mit '
                'Blockabsatz. Sortiert, festlich, komplett ohne Glanzstoff.',
                'Der Kleid-Look: gerade geschnittenes Kleid in Burgunder, Petrol oder Waldgrün, knielang, '
                'langärmelig. Der Schmuck macht den Abend, nicht das Kleid.',
                'Der Samt-Look: Samthose in Dunkelgrün oder Schwarz, dazu ein schlichter Kaschmirpullover in '
                'Creme. Samt ist an unteren Teilen zurückhaltender als an oberen und wirkt dadurch '
                'eleganter.']],
              ['Der Schmuck ist der Hebel',
               ['Wenn das Outfit ruhig ist, trägt der Schmuck den festlichen Teil – und das ist die '
                'günstigste Art, festlich zu sein. Ein Paar größere Ohrringe kostet einen Bruchteil eines '
                'Abendkleids und lässt sich jedes Jahr neu kombinieren.',
                'Eine Regel, die viel rettet: entweder auffällige Ohrringe oder eine auffällige Kette, nie '
                'beides. Zwei Blickfänge im Gesichtsbereich konkurrieren miteinander.']]],
 'products': [['Langer Blazer in Marineblau oder Anthrazit',
               'Die klare Linie, die fast immer funktioniert. Über schmaler Hose derselben Farbe.',
               'blazer damen lang marineblau'],
              ['Seidenbluse in Creme oder Champagner',
               'Glänzt weich statt punktuell. Der Unterschied zu Pailletten.',
               'seidenbluse damen creme'],
              ['Gerade geschnittenes Wollkleid knielang',
               'Fester Stoff, klare Linie, keine Raffung an der Taille.',
               'etuikleid damen wolle knielang'],
              ['Samthose in Dunkelgrün oder Schwarz',
               'Samt an unteren Teilen wirkt zurückhaltender als an oberen.',
               'samthose damen'],
              ['Kaschmirpullover in Creme',
               'Der ruhige Gegenpart zu Samt. Zusammen teurer wirkend als beides einzeln.',
               'kaschmirpullover damen creme'],
              ['Größere Ohrringe in Gold',
               'Der günstigste Weg, festlich zu sein. Dann aber keine auffällige Kette dazu.',
               'ohrringe gold gross damen']]},
{'slug': 'mantel-ueber-anlass-outfit',
 'cat': 'accessoires',
 'title': 'Der Mantel über dem Anlass-Outfit: das Teil, das alles kippen kann',
 'teaser': 'Vier Stunden Planung für das Kleid, dann der Alltagsmantel darüber. Auf den Ankunftsfotos sieht '
           'man nur den Mantel – und genau die entstehen zuerst.',
 'img': 'hero.jpg',
 'meta': 'Welcher Mantel über ein Anlass-Outfit gehört: Länge, Farbe, Schnitt und die vier Fehler, die den '
         'ganzen Look kippen.',
 'intro': ['Zwischen Oktober und März wird jedes Anlass-Outfit von einem Mantel verdeckt – beim Ankommen, '
           'beim Rausgehen, beim Sektempfang draußen. Zusammengerechnet ist der Mantel bei einer '
           'Winterhochzeit länger sichtbar als das Kleid.',
           'Trotzdem ist er bei den meisten Menschen das einzige Teil im Look, über das nicht nachgedacht '
           'wurde. Er ist einfach der Mantel, den man hat.'],
 'sections': [['Die Länge ist die wichtigste Entscheidung',
               ['Ein Mantel muss länger sein als das, was darunter ist. Ein Midikleid unter einem Kurzmantel '
                'ergibt zwei abgeschnittene Blöcke und wirkt immer unfertig, egal wie gut beide Teile '
                'einzeln sind.',
                'Als Faustregel: Der Mantel endet entweder deutlich über dem Saum – also bei einem kurzen '
                'Kleid – oder deutlich darunter. Der eine Fall, der nie funktioniert, ist derselbe Punkt '
                'oder ein Zentimeter Unterschied.']],
              ['Farbe: einer von beiden muss ruhig sein',
               ['Ein gemusterter Mantel über einem einfarbigen Kleid funktioniert. Ein einfarbiger Mantel '
                'über einem gemusterten Kleid funktioniert. Beides gemustert funktioniert praktisch nie.',
                'Sichere Manteltöne über nahezu allem: Camel, Anthrazit, Marineblau, Waldgrün, Cremeweiß. '
                'Schwarz ist einfacher, aber im Winterlicht härter im Gesicht als Camel oder Grau.']],
              ['Vier Fehler, die häufig sind',
               ['Erstens: eine Kapuze. Sie macht jeden Mantel zum Freizeitmantel, unabhängig vom Material.',
                'Zweitens: sichtbare Funktionsdetails – Kordelzüge, Klettverschlüsse, Reflektorstreifen, '
                'große Außentaschen mit Reißverschluss.',
                'Drittens: ein Gürtel, der beim Sitzen im Auto drückt und dann offen hängt. Ein offener '
                'Gürtel an einem Mantel sieht schlampig aus. Wer sitzen muss, nimmt einen Mantel ohne oder '
                'bindet ihn hinten.',
                'Viertens: der falsche Schal. Ein dicker Wollschal über einem feinen Wollmantel überlagert '
                'die Silhouette. Feiner Mantel, feiner Schal.']],
              ['Was der Mantel nicht leisten muss',
               ['Er muss nicht warm genug für einen Winterspaziergang sein. Bei einem Anlass geht man vom '
                'Auto ins Gebäude und steht vielleicht zwanzig Minuten draußen.',
                'Deshalb ist ein ungefütterter oder leicht gefütterter Wollmantel meist die bessere Wahl als '
                'eine dicke Steppjacke – er sitzt schöner und reicht für die tatsächliche Zeit an der Luft. '
                'Die Wärme kommt von der Schicht darunter.']]],
 'products': [['Wollmantel in Camel, knöchellang',
               'Länger als jedes Midikleid, hell genug fürs Gesicht im Winterlicht.',
               'wollmantel damen camel lang'],
              ['Wollmantel in Waldgrün oder Marineblau',
               'Für alle, denen Camel zu hell ist. Weicher im Gesicht als Schwarz.',
               'wollmantel damen dunkelgruen'],
              ['Kurzmantel in Anthrazit',
               'Nur zu kurzen Kleidern und Hosen. Nie zu Midi.',
               'kurzmantel damen anthrazit'],
              ['Feiner Kaschmirschal',
               'Über feinem Wollmantel. Ein dicker Strickschal überlagert die Silhouette.',
               'kaschmirschal damen'],
              ['Herrenmantel aus Wolle in Anthrazit',
               'Über Anzug oder Sakko. Ohne Kapuze, ohne Außentaschen mit Reißverschluss.',
               'wollmantel herren anthrazit'],
              ['Lederhandschuhe gefüttert',
               'Das Detail, an dem man den durchdachten Look erkennt.',
               'lederhandschuhe damen gefuettert']]},

# ============================ NEU KW34 + KW35 ============================
{
 "slug": "herbsthochzeit-gast",
 "cat": "hochzeitsgast",
 "title": "Herbsthochzeit als Gast: warme Farben, festes Schuhwerk, ein Look für drinnen und draußen",
 "teaser": "Rostrot, Camel, Dunkelgrün — das Farbfeld für Oktober-Trauungen. Dazu ein Kleid mit Ärmel, ein flacher Absatz, eine warme Zwischenschicht.",
 "img": "herbsthochzeit-gast.jpg",
 "meta": "Herbsthochzeit als Gast: Outfit-Idee mit Midikleid, Übergangsjacke und festem Schuhwerk für Trauungen im Oktober.",
 "intro": [
   "Oktober-Hochzeiten sehen auf den Fotos aus, als wäre der Herbst extra dafür erfunden worden — bis der Wind auffrischt und der Trauzeuge Sekt auf dem Kies verschüttet. Für Gäste heißt das: ein Kleid, das eine Jacke verträgt, ohne darunter zu verschwinden. Und Schuhe, die auf Wiese, Kies und Parkett dieselbe Haltung behalten.",
   "Der Grundriss ist einfach: gedeckte Herbstfarbe, halblanger Schnitt mit Ärmel, ein Absatz unter fünf Zentimetern, eine Tasche, die die Kirche und die Tanzfläche übersteht. Alles andere ist Feinarbeit.",
 ],
 "sections": [
   ("Das Kleid: Midi mit Ärmel, warme Farbe", [
     "Rostrot, Bordeaux, Dunkelgrün oder Camel sind die vier Farben, die auf einer Herbsthochzeit nicht altbacken und nicht zu leise wirken. Weiß bleibt tabu, Pastell wirkt fehl am Platz, Schwarz nur mit klarer Akzentfarbe.",
     "Ein Midikleid mit dreiviertellangem oder langem Ärmel deckt die Schulter und lässt die Wade frei — genau die Balance, die für Kirche, Standesamt und Abendfeier gleichzeitig funktioniert. Wickelschnitte fallen bei jeder Figur, gerade geschnittene Etuikleider brauchen einen guten Stoff.",
   ]),
   ("Die Zwischenschicht: kurze Jacke, keine Strickjacke", [
     "Zwischen Zeremonie und Sektempfang liegen oft zwanzig Minuten Umtrunk im Freien. Eine kurze Bouclé-Jacke, ein Blazer in Wollmischung oder ein Cape hält warm, ohne den Kleiderschnitt zu verdecken.",
     "Strickjacken sehen auf Fotos immer nach Wochenend-Café aus. Wer friert, greift zu einer Stola aus Wolle oder Kaschmir in derselben Farbfamilie wie das Kleid — das wirkt gedacht, nicht improvisiert.",
   ]),
   ("Schuhe und Tasche: flach genug für den Kies", [
     "Blockabsatz zwischen drei und fünf Zentimetern, geschlossene Spitze oder Slingback. Pumps mit dünnem Absatz versinken auf Wiese und Kies und ruinieren jeden Fototermin im Garten.",
     "Als Tasche reicht eine kleine Handtasche mit kurzem Henkel oder ein Baguette-Modell. Wildleder oder mattes Leder passen besser zum Herbst als Lack.",
   ]),
   ("Accessoires: dezent, aber warm", [
     "Perlen oder mattes Gold vertragen sich mit fast jeder Herbstfarbe. Silber wirkt kühl und passt nur zu Dunkelgrün oder Bordeaux.",
     "Ein feiner Schal aus Seide um den Hals oder als Haarband ist der Griff, der einen guten Look zu einem eigenen macht — und im Notfall vor Zugluft schützt.",
   ]),
 ],
 "products": [
   ("Midikleid mit Langarm in Rostrot", "Herbstfarbe, deckt die Schulter, fällt auf Fotos ruhig — die sichere Basis für Trauung und Empfang.", "midikleid langarm rostrot damen"),
   ("Kurze Bouclé-Jacke in Camel", "Wärmt zwischen Kirche und Sektempfang, ohne den Kleiderschnitt zu verdecken.", "boucle jacke kurz camel damen"),
   ("Slingback-Pumps mit Blockabsatz", "Absatz unter fünf Zentimetern hält auf Kies und Wiese — geschlossene Spitze für die Zeremonie.", "slingback blockabsatz damen geschlossen"),
   ("Kleine Umhängetasche aus Wildleder", "Wildleder-Optik passt zum Herbst, kurzer Henkel bleibt am Körper während der Umarmungen.", "umhaengetasche wildleder klein damen"),
   ("Wollstola in Bordeaux", "Ersatz für die Strickjacke — wirkt gedacht, wärmt am Abend im Zelt.", "wollstola bordeaux damen"),
   ("Perlenkette kurz mit Verschluss vorn", "Warmer Ton, passt zu Rostrot und Dunkelgrün, kein Konkurrent zum Brautschmuck.", "perlenkette kurz damen"),
 ],
},

{
 "slug": "taufe-gast-herbst",
 "cat": "festtage",
 "title": "Taufe als Gast im Herbst: leise Farben, geschlossene Schulter, ein Outfit für Kirche und Kaffeetafel",
 "teaser": "Creme, Puder, gedecktes Blau — Farben, die neben dem Taufkleid nicht dominieren. Dazu ein Schnitt, der eine Stunde Kirchenbank aushält.",
 "img": "taufe-gast-herbst.jpg",
 "meta": "Taufe als Gast im Herbst: Outfit-Vorschläge mit Kleid oder Bluse und Rock für Zeremonie und anschließendes Kaffeetrinken.",
 "intro": [
   "Eine Taufe ist der einzige Anlass, bei dem das Outfit eines Gastes darauf ausgelegt sein muss, ein Baby auf dem Arm nicht zu erschrecken. Kein Glitzer im Gesicht des Kindes, keine kratzenden Bordüren am Ärmel, keine Farbe, die neben dem weißen Taufkleid brüllt.",
   "Der Rest ist stille Festlichkeit: geschlossene Schulter für die Kirche, ein Stoff, der eine Kerze und einen Krümel Butterkuchen übersteht, Schuhe, in denen man eine Stunde stehen und danach fünf Stufen zur Familienfeier hinaufsteigen kann.",
 ],
 "sections": [
   ("Farbfeld: leise neben dem Taufkleid", [
     "Creme, warmes Sand, Puderrosa, staubiges Blau, sehr helles Salbei — das sind die Töne, die neben dem weißen Taufkleid harmonisch wirken und nicht wie ein Konkurrent. Weiß bleibt der Täufling.",
     "Dunkles Marineblau oder gedecktes Grau funktionieren, wenn der Familienrahmen förmlicher ist. Schwarz vermeidet man traditionell — es wirkt bei einer Taufe unpassend, auch wenn es niemand ausspricht.",
   ]),
   ("Schnitt: geschlossene Schulter, halblanger Rock", [
     "Für die Kirche ist ein Kleid mit Ärmel oder eine Bluse mit langem Arm angenehmer als jedes Träger-Modell. Wer eine Stola nimmt, verliert sie beim ersten Umarmen von Oma.",
     "Ein halblanger Rock oder ein Midikleid bewegt sich unauffällig, wenn man sich zum Kind hinabbeugt. Kurze Kleider machen die Position der Fotografin unnötig kompliziert.",
   ]),
   ("Zwei-Teiler statt Kleid: die unterschätzte Lösung", [
     "Eine feine Bluse in Seide oder Viskose kombiniert mit einem Midirock in gedecktem Ton wirkt bei Taufen oft passender als ein einteiliges Kleid — der Wechsel zwischen Zeremonie und Kaffeetafel gelingt durch Abnehmen der Jacke.",
     "Dieselbe Bluse trägt sich nachher zur Jeans, der Rock zum Blazer im Büro. Anders als ein Anlasskleid landet der Zweiteiler nicht im Schrank hinten links.",
   ]),
   ("Schuhe und Kleinigkeiten", [
     "Geschlossene Pumps mit niedrigem Absatz oder eine schlichte Ballerina in Nappa. Auf dem Kirchenboden klackern hohe Absätze durch das ganze Kirchenschiff, was während der Segnung unangenehm ist.",
     "Als Schmuck reicht ein Paar Perlenohrringe. Ketten mit langen Anhängern gehören nicht in Griffnähe eines Säuglings.",
   ]),
 ],
 "products": [
   ("Midikleid in Puderrosa mit Ärmel", "Leiser Ton neben dem Taufkleid, deckt die Schulter für die Kirche.", "midikleid puderrosa damen langarm"),
   ("Seidenbluse in Creme", "Basis für den Zwei-Teiler, trägt sich nachher zur Jeans weiter.", "seidenbluse creme damen"),
   ("Midirock in staubigem Blau", "Zurückhaltende Farbe, faltet sich gut, sitzt beim Bücken zum Kind ruhig.", "midirock staubblau damen"),
   ("Ballerina aus Nappaleder", "Leise auf dem Kirchenboden, angenehm zum Stehen während der Segnung.", "ballerina nappa leder damen"),
   ("Perlenohrringe klein", "Klassischer Taufschmuck, kein Baumler in Kindernähe.", "perlenohrringe klein stecker"),
   ("Wollstola in Sand", "Für den Kirchweg im Oktober — passt zu Puderrosa und Creme.", "wollstola sand damen"),
 ],
},

{
 "slug": "runder-geburtstag-damen",
 "cat": "festtage",
 "title": "Runder Geburtstag als Gast: ein Outfit, das eine Rede aushält und beim Buffet nicht knittert",
 "teaser": "Ob 40., 50. oder 60. — Gastgeber tragen meist Anzug oder Kleid, Gäste zwischen Bluse und Cocktailkleid. Wie man beides trifft, ohne zu unter- oder überziehen.",
 "img": "runder-geburtstag-damen.jpg",
 "meta": "Runder Geburtstag als Gast: Outfit-Ideen für 40., 50., 60. Geburtstag mit Cocktailkleid oder Bluse und Hose für Restaurant oder Halle.",
 "intro": [
   "Der 50. der Chefin, der 60. des Onkels, der 40. der besten Freundin — jeder runde Geburtstag verlangt eine eigene Entscheidung, weil der Ort so unterschiedlich ist. Ein Restaurant am Abend, eine Feier in der Scheune, ein Sektempfang im Rathaus, eine Location mit DJ. Der Dresscode steht selten auf der Einladung, und selbst wenn, ist er meistens vage.",
   "Die verlässlichste Herangehensweise: eine Stufe unter dem, was die Gastgeberin trägt, aber mit einem klaren Signal, dass es ein Anlass ist. Kein Freizeit-Look, keine Abendrobe.",
 ],
 "sections": [
   ("Cocktailkleid oder Zweiteiler — der Ortsentscheid", [
     "Restaurant am Abend, Feier ab 19 Uhr, Location mit Tanzfläche: ein Cocktailkleid in Dunkelgrün, Bordeaux oder klassischem Schwarz mit einer klaren Farbnote (Ohrringe, Tasche) trifft die Höhe fast immer.",
     "Nachmittagsfeier im Garten, Kaffeetafel, Restaurant am Mittag: ein Zwei-Teiler aus feiner Hose und Seidenbluse wirkt festlich, ohne zu viel zu wollen. Ein Blazer darüber macht ihn abendtauglich.",
   ]),
   ("Länge, Ausschnitt, Ärmel", [
     "Knielang bis midilang funktioniert bei jedem runden Geburtstag. Bodenlange Kleider gehören ins Ballroom, nicht ins Weinlokal.",
     "Ein moderater V-Ausschnitt oder ein Rundhalsschnitt sind in fast jeder Runde richtig. Trägerlos verlangt eine Stola, sonst friert man auf dem Weg vom Auto zum Eingang.",
   ]),
   ("Schuhe: für Buffet und Tanz gleichermaßen", [
     "Ein Blockabsatz zwischen fünf und sieben Zentimetern trägt sich am Buffet und auf der Tanzfläche. Stilettos sehen für zwei Stunden gut aus und werden dann heimlich unter den Tisch gestellt.",
     "Wenn die Location eine Treppe hat (Rathaus, alte Villa, Weingut), lieber eine halbe Nummer flacher — Fotos auf Treppen sind bei jedem runden Geburtstag garantiert.",
   ]),
   ("Was man nicht macht", [
     "Kein Weiß außer bei ausdrücklicher „White Party“ — das gilt auch für runde Geburtstage. Kein pralles Rot, wenn die Jubilarin selbst Rot angekündigt hat.",
     "Kein Business-Look mit Bleistiftrock und Kastenblazer, wenn nicht ausdrücklich ein Firmenjubiläum gefeiert wird. Ein Geburtstag ist privater und verlangt einen weicheren Ton.",
   ]),
 ],
 "products": [
   ("Cocktailkleid in Dunkelgrün, knielang", "Trifft die Höhe für Restaurant und Abendfeier, ist keine Konkurrenz zur Jubilarin.", "cocktailkleid dunkelgruen knielang damen"),
   ("Anzughose in Wollmischung, hoher Bund", "Basis für den Nachmittags-Zweiteiler, wirkt festlich mit Bluse und Blazer.", "anzughose wollmischung damen hoch"),
   ("Seidenbluse mit V-Ausschnitt", "Für den Zweiteiler — unter dem Blazer verschwindet sie nicht, über der Hose bleibt sie festlich.", "seidenbluse damen v ausschnitt"),
   ("Blockabsatz-Pumps 6 cm", "Trägt sich am Buffet und beim Tanzen, hält Treppenfotos aus.", "pumps blockabsatz 6 cm damen"),
   ("Statement-Ohrringe in mattem Gold", "Ersetzen die Halskette, sind auf Fotos das Signal, dass es ein Anlass ist.", "statement ohrringe matt gold"),
   ("Clutch mit Kettenriemen", "Klein genug für den Tisch, freihändig beim Anstoßen mit dem Kettenriemen über der Schulter.", "clutch kettenriemen damen"),
 ],
},

{
 "slug": "vorstellungsgespraech-herbst",
 "cat": "buero",
 "title": "Vorstellungsgespräch im Herbst: ein Outfit, das nicht nach Kostüm aussieht — und einen Mantel verträgt",
 "teaser": "Zwischen Oktober und November wird am meisten eingestellt. Was man anzieht, wenn man mit nassen Schuhen ankommt und trotzdem nach Entscheidung aussehen soll.",
 "img": "vorstellungsgespraech-herbst.jpg",
 "meta": "Vorstellungsgespräch im Herbst: Outfit mit Blazer, Bluse und Mantel — Farben, Schnitte und die häufigsten Fehler bei Bewerbungsgesprächen im Oktober und November.",
 "intro": [
   "Bewerbungsgespräche häufen sich im Herbst. Das Geschäftsjahr geht auf die Zielgerade, Stellen sollen zum Jahreswechsel besetzt sein, und wer wechseln will, tut es jetzt. Gleichzeitig ist es der ungünstigste Moment fürs Outfit: draußen Regen, drinnen überheizte Besprechungsräume, dazwischen ein Mantel, den man irgendwo ablegen muss.",
   "Der Grundgedanke ist deshalb ein anderer als im Sommer: Nicht das schönste Einzelstück gewinnt, sondern die Kombination, die nach fünfzehn Minuten Fußweg noch so aussieht wie zu Hause im Spiegel. Alles andere ist Nebensache, auch wenn Ratgeber gern das Gegenteil behaupten.",
 ],
 "sections": [
   ("Die Basis: Blazer, Bluse, ruhige Hose", [
     "Ein Blazer in Marine, Anthrazit oder gedecktem Braun ist die verlässlichste Wahl. Schwarz wirkt in vielen Branchen zu formell und lässt bei Kunstlicht müde aussehen — Marine tut das nicht.",
     "Darunter eine Bluse oder ein feiner Feinstrick in Creme, Weiß oder Hellgrau. Muster lenken bei Videoaufzeichnungen und in engen Räumen ab. Wer sich unsicher ist: einfarbig gewinnt immer.",
     "Die Hose ruhig und knöchellang, damit man beim Sitzen keine Socken-Diskussion hat. Ein Rock funktioniert genauso, dann aber mit blickdichter Strumpfhose — im Oktober ist blank kein Statement, sondern eine Fehleinschätzung des Wetters.",
   ]),
   ("Der Mantel ist Teil des Outfits", [
     "Man wird im Mantel begrüßt. Der erste Eindruck entsteht also nicht durch den Blazer, sondern durch die Schicht darüber — und die ist bei den meisten Bewerbern die schwächste Stelle der ganzen Zusammenstellung.",
     "Ein gerader Wollmantel in Camel, Marine oder Grau passt über jeden Blazer, ohne an den Schultern zu spannen. Daunenjacken, so warm sie sind, senden das falsche Signal, wenn man gleich über Verantwortung sprechen will.",
     "Praktisch dazu: ein Schirm, der in die Tasche passt, und eine Mappe statt eines Rucksacks. Wer mit tropfendem Rucksack in den Raum kommt, verhandelt die ersten zwei Minuten über Handtücher statt über sich.",
   ]),
   ("Schuhe: dicht, leise, nicht neu", [
     "Herbstwetter heißt geschlossene Schuhe mit Profil. Ein Loafer, ein flacher Stiefel oder ein Pump mit Blockabsatz — alles, was auf nassem Kopfsteinpflaster keine Angst macht.",
     "Nie ein Paar zum ersten Mal am Gesprächstag tragen. Blasen sieht man nicht, aber man hört sie im Gang und merkt sie an der Konzentration.",
     "Die Schuhe am Vorabend putzen. Es ist das Detail, das Personaler in Umfragen am häufigsten nennen — vermutlich, weil es das einzige ist, das sich objektiv beurteilen lässt.",
   ]),
   ("Was man weglässt", [
     "Starkes Parfum. Besprechungsräume im Herbst werden nicht gelüftet, und der Geruch bleibt länger im Raum als das Gespräch dauert.",
     "Auffälligen Schmuck an den Händen — beim Erklären bewegt man sie, und alles, was klappert, zieht die Aufmerksamkeit vom Gesagten weg. Eine Uhr und ein Paar kleine Ohrringe reichen vollständig aus.",
   ]),
 ],
 "products": [
   ("Blazer in Marineblau, gerade geschnitten", "Freundlicher als Schwarz, formell genug für jede Branche, verträgt einen Mantel darüber ohne Faltenwurf.", "blazer damen marineblau gerade"),
   ("Bluse in Creme ohne Muster", "Einfarbig lenkt nicht ab und wirkt bei Kunstlicht wacher als Weiß.", "bluse creme damen einfarbig"),
   ("Wollmantel in Camel, gerader Schnitt", "Der erste Eindruck entsteht im Mantel — Camel passt über Marine und Anthrazit gleichermaßen.", "wollmantel camel damen gerade"),
   ("Loafer aus Glattleder", "Geschlossen und profiliert für nasses Pflaster, leise im Gang, kein Einlaufen nötig.", "loafer damen leder schwarz"),
   ("Blickdichte Strumpfhose 60 den", "Zum Rock im Oktober Pflicht — 60 den ist warm genug und wirkt trotzdem fein.", "strumpfhose blickdicht 60 den"),
   ("Dokumentenmappe aus Leder, A4", "Ersetzt den Rucksack, hält Unterlagen trocken und gibt den Händen im Sitzen eine Aufgabe.", "dokumentenmappe leder a4 damen"),
 ],
},

{
 "slug": "standesamt-winter-braut",
 "cat": "standesamt",
 "title": "Standesamt im Winter: was die Braut trägt, wenn zwischen Auto und Trauzimmer fünf Grad liegen",
 "teaser": "Kurzes Kleid, warme Schicht, geschlossene Schuhe — und ein Plan für die zwanzig Minuten draußen, in denen die Fotos entstehen.",
 "img": "standesamt-winter-braut.jpg",
 "meta": "Standesamt im Winter: Brautoutfit für die kleine Trauung mit Wollkleid, Stola oder Cape und geschlossenen Schuhen — inklusive Farbwahl und Fotoplanung.",
 "intro": [
   "Eine Trauung im November oder Januar hat einen Vorteil, den niemand erwähnt: Die Termine sind frei, der Standesbeamte hat Zeit, und es drängelt keine zweite Hochzeit hinter der Tür. Der Nachteil steht draußen und heißt Wind.",
   "Das Kleid ist bei einer Winter-Trauung deshalb nur die halbe Entscheidung. Die andere Hälfte ist die Schicht darüber — und die sollte nicht wie eine Notlösung aussehen, weil sie auf fast jedem Foto mit drauf ist.",
 ],
 "sections": [
   ("Das Kleid: kurz oder midi, aber aus festem Stoff", [
     "Für das Standesamt ist ein knielanges oder wadenlanges Kleid seit Jahrzehnten die stimmigste Länge. Im Winter kommt die Stoffwahl dazu: Wollkrepp, Cady, dichter Crêpe oder ein feiner Bouclé halten die Form, wenn es draußen zieht — Chiffon und Tüll tun das nicht.",
     "Elfenbein, Creme und ein sehr helles Champagner wirken auf grauem Winterlicht wärmer als reines Weiß, das im Novembergrau schnell kalt aussieht. Wer sich vom klassischen Weiß lösen will, findet in Puder, Perlgrau oder sehr hellem Salbei die winterfestesten Alternativen.",
     "Ein Ärmel ist im Winter kein Kompromiss, sondern die schönere Lösung. Dreiviertel- oder Langarm nimmt dem Kleid nichts und erspart die Stola bei jeder zweiten Bewegung.",
   ]),
   ("Die Schicht darüber: Cape, Kurzmantel oder Stola", [
     "Ein kurzes Cape aus Wollmischung ist die eleganteste Lösung, weil es über den Schultern sitzt und die Kleidersilhouette nicht zerteilt. Es bleibt auf Fotos ein Kleidungsstück und wird nicht zur Jacke.",
     "Ein taillierter Kurzmantel in Elfenbein oder Camel funktioniert genauso und ist danach weiter tragbar — ein Argument, das bei einer kleinen Trauung oft mehr zählt als bei einer großen Hochzeit.",
     "Eine Stola aus Wolle oder Kunstfell wärmt am wenigsten, sieht aber auf Standesamts-Treppen am besten aus. Wer sie wählt, sollte im Auto eine echte Jacke liegen haben und sie zwei Minuten vor dem Foto tauschen.",
   ]),
   ("Schuhe und Strümpfe: die unterschätzte Stelle", [
     "Geschlossene Pumps, ein Slingback mit dichtem Vorderteil oder ein feiner Stiefelette-Schnitt. Offene Sandaletten sind auf Winterfotos das Erste, was ins Auge fällt — und meistens das Einzige, was man im Nachhinein ändern würde.",
     "Eine hautfarbene, sehr feine Strumpfhose ist bei einer Winter-Trauung kein Rückschritt, sondern die Voraussetzung dafür, dass man auf dem Rathausvorplatz noch lächeln kann. 20 bis 40 den fällt auf Fotos nicht auf.",
     "Für den Weg vom Auto zum Eingang: ein zweites Paar flache Schuhe im Kofferraum. Standesamts-Vorplätze sind gestreut, und Streusalz frisst helles Leder in einer einzigen Trauung auf.",
   ]),
   ("Der Strauß und die zwanzig Minuten draußen", [
     "Winterblumen sind haltbarer als Sommerblumen. Trockenblumen, Eukalyptus, Ranunkeln und Amaryllis überstehen Kälte und Autofahrt, ohne die Köpfe hängen zu lassen.",
     "Für die Fotos gilt: Die zwanzig Minuten draußen sind planbar. Wer sie direkt nach der Trauung legt, solange alle noch angezogen und die Frisur unberührt ist, braucht keine zweite Runde bei einbrechender Dunkelheit — im November ist um halb vier Schluss mit gutem Licht.",
   ]),
 ],
 "products": [
   ("Knielanges Brautkleid aus Wollkrepp", "Fester Stoff hält die Form bei Wind, knielang ist die klassische Standesamts-Länge.", "brautkleid standesamt knielang crepe"),
   ("Kurzes Cape in Elfenbein", "Sitzt über den Schultern, zerteilt die Silhouette nicht und bleibt auf Fotos ein Kleidungsstück.", "cape braut elfenbein kurz"),
   ("Stola aus Kunstfell in Creme", "Die Foto-Lösung für die Treppe — zwei Minuten vor der Aufnahme gegen die Jacke getauscht.", "stola kunstfell creme braut"),
   ("Geschlossene Pumps in Ivory", "Offene Sandaletten fallen auf Winterfotos sofort auf — geschlossen ist die einzige stimmige Wahl.", "brautschuhe geschlossen ivory pumps"),
   ("Feine Strumpfhose 20 den, hautfarben", "Auf Fotos unsichtbar, auf dem Vorplatz der Unterschied zwischen Lächeln und Zähneklappern.", "strumpfhose 20 den hautfarben"),
   ("Haarschmuck mit Perlen, schlicht", "Hält bei Wind besser als ein Schleier und passt zu Cape wie Kurzmantel.", "haarschmuck braut perlen schlicht"),
 ],
},

{
 "slug": "schuhe-strumpfhose-anlasskleid",
 "cat": "accessoires",
 "title": "Schuhe und Strumpfhose zum Anlasskleid: die zwei Entscheidungen, an denen im Herbst die meisten Looks scheitern",
 "teaser": "Das Kleid ist gekauft, der Anlass steht — und dann steht man vor der Frage, ob blank, blickdicht oder hautfarben. Eine Entscheidungshilfe nach Anlass, Farbe und Temperatur.",
 "img": "schuhe-strumpfhose-anlasskleid.jpg",
 "meta": "Welche Schuhe und welche Strumpfhose zum Anlasskleid im Herbst und Winter: Regeln nach Anlass, Kleidfarbe und Temperatur, plus die häufigsten Fehlgriffe.",
 "intro": [
   "Es gibt eine wiederkehrende Szene: Das Kleid für die Hochzeit, die Feier oder das Standesamt hängt fertig da, und die halbe Stunde vor dem Losfahren geht für die Frage drauf, was darunter und was darin. Sobald die Temperaturen fallen, ist das keine Stilfrage mehr, sondern eine Rechenaufgabe mit drei Variablen.",
   "Die drei Variablen sind: wie förmlich der Anlass ist, welche Farbe das Kleid hat und ob man draußen steht. Wer sie in dieser Reihenfolge beantwortet, kommt fast immer bei genau einer Kombination heraus.",
 ],
 "sections": [
   ("Die Strumpffrage: blank, hautfarben oder blickdicht", [
     "Blank funktioniert unter fünfzehn Grad nur in beheizten Innenräumen und wenn man vom Parkplatz bis zur Tür keine hundert Meter hat. Alles darüber hinaus sieht auf Fotos nicht mutig aus, sondern kalt.",
     "Eine hautfarbene Feinstrumpfhose zwischen 15 und 30 den ist die unauffälligste Lösung und für förmliche Anlässe — Standesamt, Kirche, Trauung — die richtige. Wichtig ist der Ton: einen Hauch dunkler als die eigene Haut wirkt natürlich, einen Hauch heller wirkt sofort wie Strumpfhose.",
     "Blickdicht in 40 bis 80 den ist die Herbst- und Winterlösung für alles, was nicht ausdrücklich festlich-hell ist. Schwarz zu dunklem Kleid, dunkelgrün oder bordeaux zum passenden Kleid, tiefes Braun zu Camel und Rostrot. Was man nicht macht: blickdicht schwarz zu hellem Kleid — das trennt den Körper optisch in zwei Hälften.",
   ]),
   ("Die Schuhfrage nach Untergrund, nicht nach Kleid", [
     "Der häufigste Fehler ist, den Schuh zum Kleid zu wählen statt zum Boden. Ein Weingut im Oktober, ein Standesamt mit gestreutem Vorplatz und eine Halle mit Parkett verlangen drei verschiedene Absätze, auch wenn das Kleid dasselbe bleibt.",
     "Kies, Wiese, Kopfsteinpflaster: Blockabsatz bis fünf Zentimeter oder ein flacher Stiefel. Ein Pfennigabsatz sinkt ein, und das Bild vom balancierenden Gast ist auf jeder Hochzeit dasselbe.",
     "Parkett und Teppich: hier darf der Absatz höher und schmaler sein. Wer tanzen wird, nimmt trotzdem sechs statt neun Zentimeter — die letzten drei Zentimeter kosten die letzte Stunde des Abends.",
   ]),
   ("Farbe: was zusammenpasst, ohne zu matchen", [
     "Der sicherste Weg im Herbst ist, Schuh und Strumpfhose als eine durchgehende Linie zu denken. Dunkelbraune Strumpfhose zu dunkelbraunen Stiefeletten unter einem rostroten Kleid streckt das Bein; schwarze Strumpfhose zu camelfarbenem Schuh zerschneidet es.",
     "Metallic-Schuhe in mattem Gold oder Silber sind der Notausgang, wenn Kleid und Tasche farblich schon viel erzählen. Sie zählen wie neutral und passen zu fast jedem gedeckten Ton.",
     "Ein Detail, das oft übersehen wird: Der Schuh sollte nicht heller sein als das Kleid, außer bei Brautlooks. Ein weißer Schuh unter einem dunkelgrünen Kleid zieht den Blick nach unten und lässt den Rest verschwinden.",
   ]),
   ("Die drei Fehlgriffe, die man am häufigsten sieht", [
     "Erstens: blickdichte schwarze Strumpfhose zum hellen Sommer-Anlasskleid, weil es kalt geworden ist. Besser ist ein anderes Kleid als eine falsche Strumpfhose — oder eine dunkle Strumpfhose zum ohnehin dunklen Kleid.",
     "Zweitens: neue Schuhe am Anlasstag. Zwei Stunden später steht das Paar unter dem Tisch, und man tanzt in Strümpfen — was man auf Fotos sieht.",
     "Drittens: die halterlose Lösung bei Minusgraden. Sie funktioniert an einem Sommerabend im Garten und an keinem einzigen Novemberabend zwischen Auto und Halle.",
   ]),
 ],
 "products": [
   ("Feinstrumpfhose 20 den, hautfarben", "Die unauffällige Lösung für Standesamt und Kirche — einen Hauch dunkler als die Haut wählen.", "feinstrumpfhose 20 den hautfarben damen"),
   ("Blickdichte Strumpfhose 60 den in Dunkelbraun", "Streckt das Bein unter Rostrot und Camel, wo Schwarz optisch trennen würde.", "strumpfhose blickdicht dunkelbraun 60 den"),
   ("Stiefelette aus Wildleder mit Blockabsatz", "Hält auf Kies und Kopfsteinpflaster, passt unter Midikleid wie unter knielanges Kleid.", "stiefelette wildleder blockabsatz damen"),
   ("Pumps mit 6 cm Blockabsatz in Dunkelgrün", "Höhe für Parkett, Absatzform für den ganzen Abend — Farbe als Akzent zu gedeckten Kleidern.", "pumps blockabsatz dunkelgruen damen"),
   ("Sandalette in mattem Gold", "Zählt farblich als neutral, wenn Kleid und Tasche schon genug erzählen.", "sandalette matt gold damen absatz"),
   ("Fersenpolster und Anti-Rutsch-Sohlen", "Der Grund, warum Schuhe abends anbleiben — kostet wenig und rettet die letzte Stunde.", "fersenpolster schuhe damen set"),
 ],
},

]

# --------------------------------------------------------------------------
# PIN-TITEL — was auf der Pin-Grafik und in der Pin-Beschreibung steht.
#
# Der `title` oben ist der Titel der Website: er darf schön sein.
# Der Pin-Titel ist ein SUCHBEGRIFF: Pinterest ist eine Suchmaschine, und
# niemand sucht nach "die Lücke zwischen Kirche und Saal".
#
# Regel: konkreter Anlass + Zielgruppe + Jahreszahl bei Saisonbezug.
# Fehlt hier ein Slug, nimmt makepins.py automatisch den `title`.
# --------------------------------------------------------------------------

# =====================================================================
# Freitagslauf 04.09.2026 — zwei Kategorien, drei Beiträge
# =====================================================================

CATEGORIES.append(
    {"slug": "trauer", "nav": "Trauerfeier", "title": "Trauerfeier & Kondolenz",
     "lead": "Was zieht man zu einer Trauerfeier an, wenn Schwarz nicht vorgegeben ist oder nicht im Schrank hängt? Ruhige, gedeckte Zusammenstellungen, die angemessen wirken, ohne dass man extra einkaufen müsste.",
     "img": "cat-trauer.jpg",
     "meta": "Trauerfeier-Outfits für Damen und Herren: gedeckte Farben, angemessene Schnitte und was Sie tun, wenn kein Schwarz da ist."})

CATEGORIES.append(
    {"slug": "familienfeier", "nav": "Familienfeier", "title": "Taufe, Geburtstag & Jubiläum",
     "lead": "Taufe, runder Geburtstag, Konfirmation, Hochzeitstag: Anlässe im engen Kreis haben eigene Regeln — festlich genug für die Fotos, bequem genug für einen langen Nachmittag.",
     "img": "cat-familienfeier.jpg",
     "meta": "Outfits für Taufe, runden Geburtstag, Konfirmation und Jubiläum — festlich, aber alltagstauglich zusammengestellt."})

for _q in POSTS:
    if _q["slug"] in ("taufe-gast-herbst", "runder-geburtstag-damen"):
        _q["cat"] = "familienfeier"
del _q

POSTS.append({
    "slug": "trauerfeier-outfit",
    "cat": "trauer",
    "title": "Trauerfeier-Outfit: Was anziehen, wenn nicht Schwarz?",
    "teaser": "Dunkelblau, Anthrazit, Dunkelbraun: Warum gedeckte Farben fast immer angemessen sind — und wie Sie in einer Stunde ein vollständiges Outfit aus dem zusammenstellen, was da ist.",
    "img": "trauerfeier-outfit.jpg",
    "meta": "Trauerfeier-Outfit ohne Schwarz: gedeckte Farben, angemessene Schnitte und eine ruhige Zusammenstellung für Damen und Herren.",
    "intro": [
        "Die häufigste Frage vor einer Trauerfeier lautet nicht „was ziehe ich an“, sondern „muss es wirklich Schwarz sein“. Die ehrliche Antwort: In Deutschland ist Schwarz die sichere Wahl, aber längst nicht die einzige zulässige. Angemessen heißt gedeckt, ruhig und unauffällig — und das leisten Dunkelblau, Anthrazit, Dunkelgrau und Dunkelbraun genauso.",
        "Dieser Beitrag ist für den Fall geschrieben, in dem die Nachricht kurzfristig kam und kein schwarzes Kleid im Schrank hängt. Er zeigt, welche Farben tragen, welche Schnitte ruhig wirken und in welcher Reihenfolge Sie das Outfit zusammenstellen, damit am Ende nichts improvisiert aussieht.",
    ],
    "sections": [
        ("Gedeckt statt schwarz — welche Farben gehen wirklich", [
            "Maßgeblich ist nicht die Farbe an sich, sondern ihre Sättigung. Dunkelblau, Anthrazit, Dunkelgrau, Dunkelbraun und ein sehr dunkles Flaschengrün wirken alle zurückhaltend und werden auf einer Trauerfeier nicht bemerkt — und genau das ist das Ziel. Bemerkt zu werden ist der einzige echte Fehler.",
            "Was nicht geht: kräftige Signalfarben, große Muster, glänzende Oberflächen und alles, was Aufmerksamkeit auf sich zieht. Ein Pailletten-Detail an der Schulter oder eine auffällige Schnalle kippt ein sonst korrektes Outfit sofort.",
            "Grauzone Weiß: Eine weiße Bluse unter dunklem Blazer ist unproblematisch und in vielen Regionen üblich. Ein durchgehend helles Outfit ist es nicht — es sei denn, die Familie hat ausdrücklich darum gebeten. Solche Bitten kommen inzwischen häufiger vor und gehen immer vor.",
        ]),
        ("Die Schnitte: geschlossen, ruhig, nicht körperbetont", [
            "Zwei Regeln decken fast alles ab: die Schultern sind bedeckt und der Ausschnitt ist geschlossen. Ein Etuikleid mit kurzem Arm, ein dunkler Rollkragen unter dem Blazer oder eine hochgeschlossene Bluse erfüllen das ohne Aufwand.",
            "Die Länge liegt am besten am Knie oder darunter. Sehr kurze Röcke, tiefe Rückenausschnitte und stark taillierte Schnitte wirken auf einer Trauerfeier unpassend, auch wenn die Farbe stimmt.",
            "Für Herren gilt das Gleiche in einfacherer Form: dunkler Anzug oder dunkle Hose mit dunklem Sakko, weißes oder hellgraues Hemd, gedeckte Krawatte. Eine Krawatte ist in den meisten Fällen erwartet, ein schwarzer Schlips aber keine Pflicht — dunkelblau oder anthrazit ist ebenso richtig.",
        ]),
        ("Schuhe, Tasche, Schmuck — hier entscheidet sich der Eindruck", [
            "Geschlossene Schuhe mit flachem oder niedrigem Blockabsatz sind die richtige Wahl. Trauerfeiern führen fast immer über Kies, Rasen oder unebene Wege, oft im Stehen und bei Wind. Ein dünner Absatz wird dort zum Problem, und ein Outfit, in dem man sich unsicher bewegt, wirkt sofort angespannt.",
            "Die Tasche bleibt klein und matt. Was hineinmuss: Taschentücher, Schlüssel, Telefon lautlos, und falls eine Kondolenzkarte übergeben wird, diese flach und ungeknickt.",
            "Beim Schmuck gilt: eine Sache, still. Kleine Ohrstecker oder eine schlichte Kette reichen. Was klappert oder blitzt, bleibt zu Hause. Ein dunkler Schal ist praktischer als ein Schmuckstück — er wärmt am Grab und schließt gleichzeitig den Ausschnitt.",
        ]),
        ("In dieser Reihenfolge zusammenstellen", [
            "Beginnen Sie mit dem größten Teil in der dunkelsten Farbe, die Sie besitzen — meist ein Kleid, ein Rock oder eine Hose. Das ist die Grundfarbe des Outfits, und alles Weitere ordnet sich ihr unter.",
            "Legen Sie dann die zweite Schicht dazu: Blazer, Strickjacke oder Mantel. Sie darf dunkler sein als die Grundfarbe, aber nicht heller. Erst danach kommen Schuhe und Tasche, und beide gehören in dieselbe Farbfamilie wie die zweite Schicht, nicht wie die Grundfarbe.",
            "Zum Schluss der Blick von drei Metern Entfernung im Spiegel. Wenn Ihr Auge zuerst auf ein einzelnes Teil fällt, ist dieses Teil zu auffällig. Tauschen Sie es, und das Outfit ist fertig.",
        ]),
    ],
    "products": [
        ("Dunkler Blazer, gerade geschnitten", "Die zweite Schicht, die aus fast jedem dunklen Oberteil ein vollständiges Outfit macht — und im Büro weiterläuft.", "damen blazer dunkelblau gerade geschnitten"),
        ("Etuikleid in Anthrazit oder Dunkelblau", "Knielang und hochgeschlossen: das Teil, das die Frage nach Schwarz gar nicht erst aufkommen lässt.", "etuikleid damen knielang dunkelblau"),
        ("Geschlossene Pumps mit Blockabsatz", "Standfest auf Kies und Rasen, ruhig im Auftritt. Der häufigste Fehlkauf ist der zu dünne Absatz.", "pumps damen blockabsatz geschlossen dunkel"),
        ("Dunkler Wollschal", "Wärmt am Grab, schließt den Ausschnitt und ersetzt jeden Schmuck.", "wollschal damen dunkelgrau uni"),
        ("Kleine matte Handtasche", "Groß genug für Taschentücher und Karte, klein genug, um nicht aufzufallen.", "handtasche damen klein schwarz matt"),
        ("Dunkler Anzug für Herren", "Dunkelblau oder anthrazit ist ebenso angemessen wie schwarz und danach im Berufsalltag tragbar.", "herren anzug dunkelblau slim fit"),
    ],
})

POSTS.append({
    "slug": "weihnachtsfeier-firma-2026",
    "cat": "festtage",
    "title": "Weihnachtsfeier der Firma: Outfits, die am Montag nicht peinlich sind",
    "teaser": "Die Firmenfeier ist kein Silvester. Vier Zusammenstellungen zwischen zu brav und zu viel — für Restaurant, Betriebskantine und den Abend, der länger wird als geplant.",
    "img": "weihnachtsfeier-firma-2026.jpg",
    "meta": "Weihnachtsfeier Firma 2026: Outfit-Ideen für Damen, die festlich wirken und trotzdem zum Arbeitsplatz passen.",
    "intro": [
        "Die betriebliche Weihnachtsfeier ist der schwierigste Anlass des Jahres, weil zwei Regelwerke gleichzeitig gelten. Es ist ein Fest, also darf es festlich sein. Es sind Kolleginnen und Kollegen, also arbeiten Sie am Montag mit allen weiter, die Sie am Freitagabend gesehen haben. Wer das zweite vergisst, merkt es erst hinterher.",
        "Die vier Zusammenstellungen hier lösen das über ein einfaches Prinzip: ein festliches Element, alles andere ruhig. Damit sind Sie eindeutig zurechtgemacht, ohne aus der Rolle zu fallen — und die Teile bleiben nach dem Abend im Schrank benutzbar.",
    ],
    "sections": [
        ("Zuerst klären: Restaurant, Kantine oder Halle?", [
            "Der Ort entscheidet mehr als der Anlass. Ein Menü im Restaurant erlaubt und erwartet mehr als ein Buffet in der eigenen Kantine, und eine gemietete Halle oder ein Weihnachtsmarkt-Rundgang verlangt vor allem, dass Sie nicht frieren.",
            "Fragen Sie im Zweifel jemanden, der im Vorjahr dabei war. Die Antwort „so wie im Büro, nur etwas schicker“ hören Sie in etwa acht von zehn Fällen — und genau darauf sind die folgenden Zusammenstellungen ausgelegt.",
            "Ein praktischer Punkt, der oft untergeht: Wenn der Abend mit einem Stehempfang beginnt, stehen Sie die erste Stunde. Das ist eine Entscheidung über die Schuhe, nicht über das Kleid.",
        ]),
        ("Vier Zusammenstellungen, ein festliches Element", [
            "Erstens, der Samtblazer. Dunkelgrün, Bordeaux oder Marine, dazu eine gerade schwarze Hose und ein einfaches Oberteil. Der Samt macht die gesamte Arbeit; alles andere darf schlicht sein. Diese Kombination ist die zuverlässigste von allen, weil der Blazer auch im Büro funktioniert.",
            "Zweitens, die Satinbluse zur Anzughose. Elfenbein, Champagner oder tiefes Petrol, hineingesteckt, dazu ein schmaler Gürtel. Wirkt festlicher als es ist und lässt sich am Montag mit einem Strickpullover darüber komplett entschärfen.",
            "Drittens, das dunkle Strickkleid mit Statement-Ohrringen. Für Feiern, bei denen es kalt oder informell wird. Das Kleid ist bequem, der Schmuck übernimmt den festlichen Teil — und lässt sich im Auto abnehmen, wenn Sie sich überschätzt haben.",
            "Viertens, der weite Hosenanzug in einer gedeckten Farbe. Die Antwort auf die Frage, die auf Pinterest am häufigsten hinter „Weihnachtsfeier“ steckt: Hose statt Kleid. Wirkt souverän, braucht keine Strumpfhose und ist bei jeder Raumtemperatur tragbar.",
        ]),
        ("Die drei Fehler, die man am Montag noch merkt", [
            "Zu kurz und zu tief ausgeschnitten. Was am Samstagabend privat unproblematisch wäre, verschiebt im beruflichen Umfeld die Wahrnehmung — und zwar länger als einen Abend. Die einfache Regel: was Sie in einem Gespräch mit der Bereichsleitung nicht tragen würden, tragen Sie auch auf der Feier nicht.",
            "Zu viel Glanz. Ein glänzendes Teil ist festlich, zwei sind Silvester. Pailletten-Oberteil und Metallic-Schuhe zusammen kippen jedes Firmenoutfit.",
            "Zu unbequeme Schuhe. Der Abend dauert länger als geplant, es wird gestanden, und irgendwann ist die Frage nach dem Schuh wichtiger als die nach dem Kleid. Ein Blockabsatz oder ein eleganter flacher Schuh löst das, ohne dass es jemand bemerkt.",
        ]),
        ("Mantel, Weg und Kälte mitdenken", [
            "Zwischen Parkplatz und Eingang liegen im Dezember oft ein paar hundert Meter. Ein gerader dunkler Mantel, der über den Blazer passt, ist wichtiger als jedes Detail am Outfit darunter — er ist das Erste, was gesehen wird.",
            "Wenn die Feier über einen Weihnachtsmarkt führt, planen Sie warme Strumpfhosen und feste Sohlen ein. Kalte Füße beenden einen Abend zuverlässiger als jedes andere Problem.",
            "Und legen Sie am Vorabend alles zusammen an einen Platz: Outfit, Schuhe, Mantel, Tasche. Der Freitag vor der Feier ist ein Arbeitstag, und der Zeitpuffer am Abend ist immer kleiner als gedacht.",
        ]),
    ],
    "products": [
        ("Samtblazer in Dunkelgrün oder Bordeaux", "Das eine festliche Element, das den Rest schlicht bleiben lässt — und danach im Büro weitergetragen wird.", "damen samtblazer dunkelgrün"),
        ("Satinbluse in Elfenbein oder Petrol", "Wirkt festlicher als sie ist und lässt sich am nächsten Werktag mit einem Pullover entschärfen.", "damen satinbluse elfenbein langarm"),
        ("Weite Anzughose mit hoher Taille", "Die Antwort auf „Hose statt Kleid“: souverän, warm und ohne Strumpfhosenfrage.", "damen anzughose weit hohe taille"),
        ("Dunkles Strickkleid, knielang", "Für Feiern, bei denen es kühl oder informell wird — bequem, der Schmuck macht den Rest.", "strickkleid damen knielang dunkelgrün"),
        ("Pumps mit Blockabsatz", "Der Abend dauert länger als geplant. Blockabsatz löst das, ohne weniger elegant zu wirken.", "pumps damen blockabsatz schwarz elegant"),
        ("Gerader Wollmantel über Blazerlänge", "Das Erste, was gesehen wird — und im Dezember der eigentliche Unterschied zwischen angenehm und ausgekühlt.", "damen wollmantel gerade geschnitten dunkel"),
    ],
})

POSTS.append({
    "slug": "stiefel-zum-anlasskleid",
    "cat": "accessoires",
    "title": "Stiefel zum Anlasskleid: Wann es funktioniert und wann nicht",
    "teaser": "Ab Oktober ist die Frage nicht mehr, ob Stiefel zum Kleid passen, sondern welche. Drei Schafthöhen, drei Anlässe und die Regel, an der sich alles entscheidet.",
    "img": "stiefel-zum-anlasskleid.jpg",
    "meta": "Stiefel zum Anlasskleid im Herbst 2026: welche Schafthöhe zu welcher Rocklänge passt und bei welchen Anlässen Stiefel gehen.",
    "intro": [
        "Sobald es draußen kalt wird, steht dieselbe Frage im Raum: Kann ich zu einem Anlasskleid Stiefel tragen, oder müssen es Pumps sein? Die Antwort ist seltener ein klares Nein, als die meisten annehmen — sie hängt aber an zwei Dingen, die man kennen muss: der Schafthöhe im Verhältnis zur Rocklänge, und der Formalität des Anlasses.",
        "Dieser Beitrag ordnet beides. Danach wissen Sie, welche Stiefel Sie zu welchem Kleid tragen können, wo die Grenze verläuft und mit welchen zwei Paaren Sie die gesamte kalte Jahreshälfte abdecken.",
    ],
    "sections": [
        ("Die eine Regel: der Zwischenraum entscheidet", [
            "Zwischen Saum und Stiefelschaft entsteht ein sichtbarer Streifen Bein. Dieser Streifen ist das eigentliche Gestaltungselement — und er soll entweder deutlich vorhanden oder gar nicht vorhanden sein. Ein schmaler Streifen von wenigen Zentimetern wirkt fast immer unglücklich, weil das Auge ihn als Zufall liest.",
            "Praktisch heißt das: Zu einem knielangen Kleid gehören entweder Stiefeletten, die deutlich unterhalb der Wade enden, oder Overknee-Stiefel, die über dem Saum beginnen. Der Kniestiefel, der genau am Saum aufhört, ist die einzige Kombination, die man besser meidet.",
            "Zu einem Midikleid, das die Wade zur Hälfte bedeckt, passt die Stiefelette hervorragend, der Kniestiefel dagegen verschwindet darunter und lohnt sich nicht. Zu einem langen Kleid ist der Stiefel ohnehin unsichtbar — dort zählt nur, dass Sie sicher gehen.",
        ]),
        ("Welcher Anlass verträgt welchen Stiefel", [
            "Standesamt, Herbsthochzeit im Freien, Taufe, Firmenfeier und runder Geburtstag: Bei allen fünf sind Stiefeletten aus glattem Leder in einer gedeckten Farbe unproblematisch, solange sie spitz oder leicht spitz zulaufen und einen sauberen Absatz haben. Sie lesen sich als Schuh, nicht als Winterstiefel.",
            "Kirchliche Trauung und Abendveranstaltung mit Menü sind die Grenzfälle. Hier funktioniert ein schmaler, hoher Stiefel aus glattem Leder — grobe Sohlen, Schnürungen, Schnallen und sichtbare Nähte kippen ihn dagegen ins Alltägliche.",
            "Nicht geeignet sind gefütterte Winterstiefel, Wanderstiefel-Anleihen und alles mit Profilsohle. Wenn der Weg zum Ort das verlangt, ist der Wechselschuh in der Tasche die bessere Lösung als der Kompromiss am Fuß.",
        ]),
        ("Farbe und Strumpfhose — der häufigste Fehler", [
            "Stiefel, Strumpfhose und Saum sollten sich farblich nicht widersprechen. Am zuverlässigsten ist die durchgehende dunkle Linie: blickdichte Strumpfhose und Stiefel in derselben Farbfamilie lassen das Bein optisch länger wirken und den Übergang verschwinden.",
            "Kontrast funktioniert, wenn er gewollt aussieht: cognacfarbene Stiefel zu einem rostroten oder cremefarbenen Kleid sind eine bewusste Entscheidung und wirken auch so. Was nicht funktioniert, ist die hautfarbene Strumpfhose zum dunklen Stiefel — der Bruch am Schaft zieht den Blick genau dorthin.",
            "Für alle, die es einfach halten wollen: dunkelbraune oder schwarze Stiefeletten und blickdichte Strumpfhosen in derselben Tiefe decken praktisch jedes Anlasskleid ab, das Sie im Herbst tragen werden.",
        ]),
        ("Zwei Paare reichen für die gesamte Saison", [
            "Das erste Paar: schwarze oder dunkelbraune Stiefeletten aus glattem Leder mit Blockabsatz von etwa fünf Zentimetern. Dieses Paar deckt Standesamt, Familienfeier, Büro und Firmenfeier ab und ist die Anschaffung, die sich am schnellsten rechnet.",
            "Das zweite Paar: ein schmaler Kniestiefel ohne Verzierung, ebenfalls glattes Leder. Er ist der Schuh für lange und knielange Kleider, für kalte Tage und für die Anlässe, bei denen Sie draußen stehen werden.",
            "Was Sie sich sparen können, ist ein dritter, auffälliger Stiefel. Er passt selten zu einem Anlasskleid und wird deshalb genau einmal getragen. Investieren Sie das lieber in eine wirklich gute Strumpfhose — sie ist bei diesen Outfits das Teil, das am schnellsten kaputtgeht.",
        ]),
    ],
    "products": [
        ("Stiefeletten aus glattem Leder mit Blockabsatz", "Das Paar, das Standesamt, Familienfeier und Büro gleichzeitig abdeckt — der wichtigste Schuh der kalten Hälfte.", "damen stiefeletten leder blockabsatz schwarz"),
        ("Schmaler Kniestiefel ohne Verzierung", "Für lange und knielange Kleider, glattes Leder, keine Schnallen — das ist der Unterschied zwischen Anlass und Alltag.", "damen kniestiefel schmal leder"),
        ("Blickdichte Strumpfhose, 60 bis 80 den", "Schließt die Lücke zwischen Saum und Schaft und lässt das Bein länger wirken.", "strumpfhose damen blickdicht 60 den schwarz"),
        ("Midikleid in gedeckter Herbstfarbe", "Die Kleidlänge, zu der Stiefeletten am zuverlässigsten passen.", "midikleid damen langarm herbst rostrot"),
        ("Faltbarer Wechselschuh für die Tasche", "Die bessere Lösung als ein Kompromiss am Fuß, wenn der Weg zum Ort über Kies oder Wiese führt.", "faltbare ballerinas damen tasche"),
        ("Lederpflege-Set für glattes Leder", "Ein Anlassstiefel wird an der Ferse zuerst matt — fünf Minuten Pflege verlängern die Saison um ein Jahr.", "lederpflege set schuhe glattleder"),
    ],
})

# ---------------------------------------------------------------- KW37, 11.09.2026

POSTS.append({
    "slug": "strickjacke-statt-blazer",
    "cat": "herbst",
    "title": "Strickjacke statt Blazer: Wann der Tausch funktioniert – und wann nicht",
    "teaser": "Die feine Strickjacke ist der bequemere Blazer. Sie hält aber nur, was sie verspricht, wenn drei Dinge stimmen: Feinheit, Länge und das Teil darunter.",
    "img": "strickjacke-statt-blazer.jpg",
    "meta": "Strickjacke statt Blazer im Herbst 2026: welche Feinheit, welche Länge und welches Oberteil darunter den Tausch bürotauglich machen.",
    "intro": [
        "Der Blazer ist das Arbeitstier jeder Anlass-Garderobe, und er hat einen Nachteil: Er sitzt. Er zwingt die Schultern in eine Form und die Haltung dazu. Es gibt Tage, an denen das genau richtig ist, und Tage, an denen es sich anfühlt wie eine Verkleidung.",
        "Die feine Strickjacke ist die Antwort darauf. Sie übernimmt die Aufgabe des Blazers — Schultern abschließen, Silhouette rahmen, das Outfit fertig aussehen lassen — ohne die Strenge. Aber sie kann auch ins Gegenteil kippen und nach Sofa aussehen. Woran das liegt, lässt sich an drei Punkten festmachen.",
    ],
    "sections": [
        ("Feinheit entscheidet, ob es Kleidung oder Bequemlichkeit ist", [
            "Die wichtigste Größe ist die Maschenfeinheit. Grober Strick liest sich als Freizeit, unabhängig von Farbe und Schnitt — er hat sichtbare Struktur, und Struktur wirkt lässig. Feiner Strick aus Merino, Kaschmirmischung oder Baumwolle liegt flach und glatt an und verhält sich optisch wie Stoff.",
            "Praktische Prüfung: Wenn Sie die Maschen aus zwei Metern Entfernung einzeln erkennen können, ist die Jacke zu grob für einen Anlass. Erkennen Sie nur eine gleichmäßige Fläche, funktioniert sie überall dort, wo sonst ein Blazer stünde.",
            "Das gilt auch für die Knöpfe. Große Hornknöpfe ziehen jede Strickjacke Richtung Landhaus. Kleine, flache Knöpfe in Tonfarbe verschwinden und lassen den Strick sprechen.",
        ]),
        ("Die Länge ist da, wo der Blazer aufhört", [
            "Ein Blazer endet knapp unter dem Gesäß oder darüber. Eine Strickjacke, die das nicht tut, übernimmt nicht seine Funktion, sondern die eines Mantels — und dann trägt man zwei Oberteile übereinander, ohne dass eines den Abschluss bildet.",
            "Für Anlass und Büro heißt das: hüftlang oder kürzer. Die lange Strickjacke ist ein eigenes Kleidungsstück mit eigener Berechtigung, aber sie ersetzt keinen Blazer, sondern ein Jackett-Ersatzstück für den Abend zu Hause.",
            "Cropped funktioniert, wenn darunter eine hohe Taille sitzt. Über einer tief sitzenden Hose entsteht sonst ein Streifen Bluse zwischen Jacke und Bund, der das Outfit optisch zerteilt.",
        ]),
        ("Was darunter liegt, macht den Unterschied", [
            "Eine Strickjacke über einem T-Shirt bleibt Freizeit. Über einer Seidenbluse, einem feinen Rollkragen oder einem schlichten Top mit rundem Ausschnitt wird sie zum Kleidungsstück. Der Grund ist einfach: Zwei weiche Materialien ergeben einen weichen Gesamteindruck, ein glattes Material darunter setzt den Kontrast, den das Auge als Absicht liest.",
            "Der zweite Hebel ist der Ausschnitt. Eine offen getragene Strickjacke braucht eine senkrechte Linie darunter — einen Ausschnitt, eine Knopfleiste, eine Kette. Ohne diese Linie wirkt die Front leer.",
            "Und ein Detail, das oft übersehen wird: Die Ärmel dürfen nicht zu lang sein. Strick dehnt sich mit dem Tragen, und ein Ärmel, der über den Handrücken rutscht, nimmt jedem Outfit die Kontur. Wer die Ärmel ohnehin schiebt, wählt besser gleich eine Dreiviertel-Länge.",
        ]),
        ("Drei Anlässe, drei Antworten", [
            "Büro: feiner Strick, hüftlang, in Marine, Anthrazit, Camel oder Creme, darunter Bluse oder Rollkragen. Das ist ein vollwertiger Blazer-Ersatz und an den meisten Arbeitsplätzen sogar die angenehmere Wahl.",
            "Familienfeier und Taufe: dieselbe Jacke, aber gern in einer weicheren Farbe und über einem Kleid statt über Hose. Die Strickjacke nimmt einem ärmellosen Kleid die Kühle, ohne die festliche Wirkung zu zerstören.",
            "Abendliche Anlässe und Weihnachtsfeier: hier stößt die Strickjacke an ihre Grenze. Ab einer gewissen Festlichkeit erwartet das Auge glänzendes oder strukturiertes Material — Samt, Satin, Wolle mit klarer Kante. Dann ist der Blazer wieder im Recht.",
        ]),
    ],
    "products": [
        ("Feinstrickjacke aus Merinowolle, hüftlang", "Die Grundform: flach gestrickt, kleine Knöpfe, endet knapp unter der Hüfte. Ersetzt den Blazer, ohne wie ein Kompromiss auszusehen.", "damen feinstrickjacke merino huefte knopfleiste"),
        ("Kaschmirmischung in Camel oder Creme", "Helle Töne lassen feinen Strick sofort teurer aussehen als er ist, weil jede Unregelmäßigkeit im Licht sichtbar wäre — und bei guter Qualität eben nicht sichtbar ist.", "damen strickjacke kaschmir camel"),
        ("Seidenbluse mit V-Ausschnitt", "Das glatte Material unter dem weichen: der Kontrast, der aus Bequemlichkeit ein Outfit macht.", "damen seidenbluse v ausschnitt elegant"),
        ("Feiner Rollkragenpullover", "Die Alternative zur Bluse, wenn es kälter wird. Schließt den Hals und gibt der offenen Strickjacke die senkrechte Linie.", "damen rollkragenpullover feinstrick"),
        ("Schmale Stoffhose mit hoher Taille", "Die hohe Taille ist bei kurzen Strickjacken keine Stilfrage, sondern Statik: Sie schließt die Lücke zwischen Jacke und Bund.", "damen stoffhose high waist schmal"),
        ("Filigrane lange Kette", "Verlängert die senkrechte Linie im Ausschnitt und füllt die Front, ohne aufzutragen.", "damen lange kette fein gold"),
    ],
})

POSTS.append({
    "slug": "weihnachtsfeier-herren-2026",
    "cat": "festtage",
    "title": "Weihnachtsfeier für Herren: drei Stufen zwischen Hemd und Anzug",
    "teaser": "Die Einladung sagt selten, was gemeint ist. Diese drei Stufen decken praktisch jede Firmenweihnachtsfeier ab — und die häufigsten Fehlgriffe liegen dazwischen.",
    "img": "weihnachtsfeier-herren-2026.jpg",
    "meta": "Weihnachtsfeier Outfit Herren 2026: drei abgestufte Looks vom Rollkragen unter dem Sakko bis zum dunklen Anzug, je nach Ort und Uhrzeit.",
    "intro": [
        "Bei Herren ist die Weihnachtsfeier selten eine Frage des Geschmacks und fast immer eine der Einschätzung. Zu leger wirkt gleichgültig, zu formell wirkt angestrengt, und beides fällt auf einer Firmenfeier stärker auf als im Alltag.",
        "Die gute Nachricht: Es gibt nicht zwanzig Möglichkeiten, sondern drei. Welche davon richtig ist, hängt an zwei Angaben, die in jeder Einladung stehen — Ort und Uhrzeit.",
    ],
    "sections": [
        ("Stufe eins: Kantine, Nachmittag, Kollegen in Jeans", [
            "Wenn die Feier im Haus stattfindet und am Nachmittag beginnt, ist der dunkle Anzug falsch. Er markiert einen Abstand, den niemand gewollt hat. Richtig ist hier: dunkle Chino oder Wollhose, feiner Strickpullover oder Hemd, dazu ein Sakko, das man ablegen kann, ohne dass der Rest nackt aussieht.",
            "Der entscheidende Punkt ist das Schuhwerk. Eine Jeans mit Sneakern zieht das ganze Outfit auf Bürotag herunter. Derbys oder Chelsea Boots aus glattem Leder heben dieselbe Hose zwei Stufen an und kosten keine Bequemlichkeit.",
            "Farblich reicht der Bestand: Anthrazit, Marine, dunkles Braun. Weihnachtliche Farben braucht es nicht — ein dunkelgrüner Pullover ist die eleganteste Verbeugung vor der Saison, die möglich ist.",
        ]),
        ("Stufe zwei: Restaurant, Abend, gemischtes Publikum", [
            "Das ist der häufigste Fall und der, bei dem die meisten danebenliegen. Hier funktioniert die Kombination, die im Deutschen keinen guten Namen hat: Sakko und Hose in verschiedenen Farben, darunter ein feiner Rollkragen statt eines Hemds.",
            "Der Rollkragen ist der Trick. Er ist förmlicher als ein offenes Hemd, aber ohne Krawatte, und er löst das Problem, dass ein Hemdkragen ohne Krawatte am Abend oft schlaff aussieht. Merino oder eine Kaschmirmischung, eng anliegend, in Dunkelgrün, Anthrazit, Marine oder Bordeaux.",
            "Dazu ein Sakko aus Wolle mit etwas Struktur — Flanell, feines Tweed, Samt für die Mutigen — und eine Hose in klarem Kontrast dazu. Braune Lederschuhe, eine Uhr mit Lederband, fertig. Kein Einstecktuch, es sei denn, Sie tragen ohnehin eines.",
        ]),
        ("Stufe drei: Hotel, Abendessen mit Menü, Geschäftsführung anwesend", [
            "Erst hier ist der Anzug richtig. Dunkelblau oder Anthrazit, nicht schwarz — Schwarz ist in Deutschland am Abend dem sehr Formellen und der Trauer vorbehalten und wirkt auf einer Feier unnötig streng.",
            "Weißes oder sehr hellblaues Hemd, Krawatte nur, wenn es auf der Einladung steht oder im Unternehmen üblich ist. Ohne Krawatte den obersten Knopf öffnen und es dabei belassen; zwei offene Knöpfe kippen sofort ins Lässige.",
            "Schuhe: glatte schwarze oder dunkelbraune Oxfords, geputzt. Auf dieser Stufe sieht man Schuhe, und ungepflegtes Leder ist der einzige Fehler, den ein guter Anzug nicht ausgleicht.",
        ]),
        ("Die drei Fehlgriffe, die wirklich vorkommen", [
            "Der Weihnachtspullover. Er ist gemeint als Zeichen, dass man es locker nimmt, und liest sich bei allen außer den engsten Kollegen als Verkleidung. Wenn die Firma ihn ausdrücklich ausruft, gern. Sonst nicht.",
            "Der zu große Anzug. Schultern, die über das eigene Gelenk hinausstehen, machen aus jedem Anzug einen geliehenen. Das ist kein Preis-, sondern ein Änderungsschneider-Thema und für unter dreißig Euro zu lösen.",
            "Der Sneaker zum Sakko. Funktioniert in bestimmten Branchen und an bestimmten Orten, aber nie auf Stufe zwei und drei — und die Weihnachtsfeier ist nicht der Abend, an dem man das ausprobiert.",
        ]),
    ],
    "products": [
        ("Feiner Rollkragenpullover aus Merino", "Das Schlüsselstück für Stufe zwei. Dunkelgrün oder Bordeaux ist festlicher als Schwarz und fällt trotzdem niemandem unangenehm auf.", "herren rollkragenpullover merino dunkelgruen"),
        ("Wollsakko in Anthrazit mit leichter Struktur", "Struktur im Stoff ersetzt am Abend das Muster. Trägt sich über Rollkragen wie über Hemd.", "herren sakko wolle anthrazit struktur"),
        ("Dunkelblauer Anzug, schmal geschnitten", "Stufe drei. Marine statt Schwarz, weil Schwarz am Abend streng wirkt und Marine im Licht besser aussieht.", "herren anzug dunkelblau slim fit"),
        ("Derby-Schuhe aus glattem Leder", "Der Schuh, der Stufe eins und zwei trägt. Glattes Leder, dunkelbraun, geschnürt.", "herren derby schuhe leder dunkelbraun"),
        ("Schmale Wollhose in Grau", "Der Gegenpart zum dunklen Sakko. Wolle fällt am Abend besser als Baumwolle und knittert nicht im Sitzen.", "herren wollhose grau schmal"),
        ("Uhr mit braunem Lederarmband", "Das einzige Schmuckstück, das Herren auf einer Firmenfeier kommentarlos tragen können.", "herren armbanduhr leder braun klassisch"),
    ],
})

POSTS.append({
    "slug": "samt-outfit-festlich-2026",
    "cat": "festtage",
    "title": "Samt festlich tragen, ohne dass es nach Theatervorhang aussieht",
    "teaser": "Samt ist das festlichste Material, das man ohne Glitzer tragen kann. Er kippt nur dann ins Kostümhafte, wenn man mehr als ein Teil davon anzieht.",
    "img": "samt-outfit-festlich-2026.jpg",
    "meta": "Samt festlich kombinieren 2026: welche Farben tragbar sind, warum nur ein Samtteil ins Outfit gehört und welche Materialien dazu passen.",
    "intro": [
        "Es gibt wenige Stoffe, die so zuverlässig festlich wirken wie Samt, und keinen, bei dem der Grat zwischen elegant und verkleidet so schmal ist. Der Grund liegt im Material selbst: Samt hat einen Flor, der Licht in zwei Richtungen unterschiedlich zurückwirft. Deshalb verändert er im Gehen die Farbe — und deshalb zieht er Blicke an, ob man will oder nicht.",
        "Daraus folgt die einzige Regel, die man wirklich braucht: Ein Samtteil pro Outfit. Alles andere ist Detailfrage.",
    ],
    "sections": [
        ("Warum nur ein Teil", [
            "Zwei Samtteile ergeben keinen doppelten Effekt, sondern eine Fläche. Das Auge kann die Teilung zwischen Oberteil und Rock nicht mehr lesen, weil beide dasselbe Licht zurückwerfen, und was bleibt, ist eine Silhouette ohne Gliederung. Genau so sehen Kostüme aus.",
            "Ein Samtteil dagegen wirkt wie ein gesetzter Akzent. Der Rest des Outfits wird dadurch nicht langweilig, sondern zum Rahmen — und darf ruhig völlig schlicht sein.",
            "Ausnahme, die die Regel bestätigt: ein Samtkleid in einem Stück. Da gibt es keine Teilung, die verloren gehen könnte, und die Gliederung übernehmen Schnitt und Gürtel.",
        ]),
        ("Die Farben, die tragbar sind", [
            "Samt in tiefen, gedeckten Tönen ist am besten zu tragen: Smaragd, Dunkelblau, Bordeaux, Waldgrün, Anthrazit, Aubergine. Sie profitieren am stärksten vom Flor, weil der Farbwechsel im Licht bei satten Tönen sichtbar ist, bei hellen kaum.",
            "Schwarzer Samt ist die sichere Wahl und zugleich die schwierigste: Er wirkt am Abend sehr formell und zeigt jedes Fussel. Wer Schwarz wählt, sollte eine Fusselrolle einstecken — das ist kein Scherz, sondern die häufigste Panne des Abends.",
            "Helle Töne — Puder, Champagner, Hellgrau — funktionieren, wirken aber weicher und weniger festlich. Sie sind eher eine Frühjahrs- als eine Dezemberwahl.",
        ]),
        ("Was dazu passt und was nicht", [
            "Samt verlangt einen matten Gegenpart. Crêpe, feine Wolle, Baumwollsatin mit stumpfer Oberfläche, glatte Strickware — all das gibt dem Samt den Kontrast, den er braucht.",
            "Schwierig wird es mit anderen glänzenden Materialien. Satin neben Samt konkurriert um dasselbe Licht, Pailletten daneben wirken schnell nach zu viel. Wenn beides sein soll, dann sehr kleinflächig: eine Satinschleife, eine Clutch.",
            "Beim Schmuck gilt dasselbe: Samt trägt Gold besser als Silber, weil warme Metalle den Farbwechsel im Flor aufnehmen. Große Ohrringe funktionieren, große Ketten liegen auf dem Flor auf und drücken ihn platt.",
        ]),
        ("Drei Kombinationen, die sicher funktionieren", [
            "Samtblazer in Smaragd über schwarzer Crêpe-Hose und schlichtem Top. Der Blazer trägt den Abend, der Rest bleibt still. Funktioniert auf der Firmenfeier ebenso wie im Restaurant.",
            "Samtrock in Bordeaux zu feinem Rollkragen in Creme oder Kamel. Die Kombination ist wärmer als sie klingt und eine der wenigen, die tagsüber wie abends geht.",
            "Samtkleid, knielang oder midi, mit schmalem Ledergürtel und geschlossenen Schuhen. Das ist die schnellste festliche Lösung, die es gibt — ein Teil, fertig, und man muss über nichts weiter nachdenken.",
        ]),
    ],
    "products": [
        ("Samtblazer in Smaragd oder Dunkelblau", "Das vielseitigste Samtteil überhaupt: über Hose, über Kleid, über Rock — und man kann ihn ablegen, ohne dass das Outfit zusammenbricht.", "damen samtblazer gruen elegant"),
        ("Midikleid aus Samt mit schmalem Schnitt", "Die Ein-Teil-Lösung. Bei Samtkleidern lohnt ein schlichter Schnitt, weil das Material bereits genug Aufmerksamkeit bindet.", "damen samtkleid midi elegant"),
        ("Samtrock in Bordeaux, knie- oder wadenlang", "Der unterschätzte Gegenentwurf zum Kleid: kombinierbar mit allem, was man ohnehin besitzt.", "damen samtrock bordeaux midi"),
        ("Crêpe-Hose in Schwarz, hoch geschnitten", "Der matte Gegenpart. Crêpe wirkt neben Samt ruhig, wo Satin konkurrieren würde.", "damen crepe hose schwarz high waist"),
        ("Feiner Rollkragen in Creme oder Kamel", "Hellt dunklen Samt auf und macht aus dem Abend-Outfit ein Tages-Outfit.", "damen rollkragenpullover feinstrick creme"),
        ("Ohrringe in Gold mit etwas Länge", "Warmes Metall nimmt den Farbwechsel im Flor auf. Länge statt Fläche, damit nichts auf dem Samt aufliegt.", "damen ohrringe gold haenger elegant"),
    ],
})

POSTS.append({
    "slug": "geschenke-frauen-accessoires",
    "cat": "accessoires",
    "title": "Sechs Accessoires, die Frauen wirklich tragen — und nicht in die Schublade legen",
    "teaser": "Das Problem beim Schenken ist selten die Idee, sondern die Größe. Accessoires lösen das, weil sie fast immer passen — wenn man die drei Fallen kennt.",
    "img": "geschenke-frauen-accessoires.jpg",
    "meta": "Geschenkideen für Frauen: zwölf Accessoires, die getragen statt weggelegt werden, mit den drei häufigsten Fehlgriffen.",
    "intro": [
        "Kleidung zu verschenken ist heikel, weil die Größe stimmen muss und die Rückgabe peinlich ist. Accessoires umgehen beides: Ein Tuch passt jedem, ein Armreif hat höchstens zwei Größen, eine Tasche gar keine. Deshalb landen sie so oft unter dem Baum — und deshalb auch so oft ungetragen in der Schublade.",
        "Der Unterschied zwischen beidem liegt nicht am Preis. Er liegt daran, ob das Stück zu dem passt, was sie ohnehin trägt. Die folgenden zwölf sind danach ausgewählt.",
    ],
    "sections": [
        ("Die drei Fehlgriffe, die jeder macht", [
            "Erstens: zu auffällig. Wer selten Schmuck trägt, fängt nicht mit einer großen Statement-Kette an. Das Geschenk wird bewundert, bedankt und nie angezogen. Die Regel dagegen ist unbequem, aber verlässlich — schenke eine Stufe schlichter, als du denkst.",
            "Zweitens: die falsche Metallfarbe. Fast jede Frau trägt konsequent entweder Gold oder Silber, oft seit Jahren, ohne je darüber gesprochen zu haben. Ein Blick auf ihre Uhr oder ihre Ohrringe beantwortet die Frage in zwei Sekunden.",
            "Drittens: Parfüm, Nagellack und alles, was nach Geschmack riecht oder aussieht. Das sind Entscheidungen, die Menschen für sich selbst treffen. Accessoires sind es nicht — sie ergänzen, statt zu ersetzen.",
        ]),
        ("Was immer funktioniert", [
            "Ein Seidentuch in einer Farbe, die sie schon im Schrank hat. Es ist das einzige Accessoire, das im Haar, am Hals, an der Tasche und am Gürtel funktioniert, und es verzeiht jede Unsicherheit über Stil und Größe.",
            "Feine Ohrringe in ihrer Metallfarbe. Creolen in mittlerer Größe sind die sicherste Wahl, weil sie sowohl zur Jeans als auch zum Anlasskleid gehen und niemanden zwingen, sich neu zu erfinden.",
            "Ein Schal aus echter Wolle statt Mischgewebe. Der Unterschied ist beim ersten Anfassen spürbar, hält Jahre und wird jeden Winter getragen — kein anderes Geschenk hat diese Trefferquote.",
        ]),
        ("Wenn du mehr über sie weißt", [
            "Trägt sie oft Blazer, ist eine Brosche das Geschenk, das ihr niemand sonst macht. Sie sitzt am Revers, kostet keine Gewöhnung und verwandelt ein Alltagssakko in ein Anlassteil.",
            "Pendelt sie zwischen Büro und Terminen, ist eine strukturierte Tasche mit festem Boden praktischer als jede weiche Form. Sie steht von allein, wenn man sie abstellt, und das merkt man erst, wenn man es einmal hatte.",
            "Fährt sie viel Rad oder geht viel zu Fuß, sind gefütterte Lederhandschuhe das Stück, das sie sich selbst nie kauft und dann täglich benutzt.",
        ]),
        ("Wie du es übergibst", [
            "Lege den Kassenbon dazu, ohne Kommentar. Das nimmt dem Umtausch die Peinlichkeit und dem Geschenk nichts von seiner Geste — im Gegenteil, es zeigt, dass dir wichtiger ist, dass sie es trägt, als dass sie es behält.",
            "Verpacke Schmuck nicht in einer riesigen Schachtel. Die Erwartung, die eine große Box aufbaut, kann ein kleines Stück nicht einlösen, und der Moment kippt, bevor sie es in der Hand hält.",
            "Sag beim Übergeben in einem Satz, warum du genau dieses Stück ausgesucht hast. Das ist der Teil, an den sie sich in zwei Jahren noch erinnert.",
        ]),
    ],
    "products": [
        ("Seidentuch, mittleres Format", "Passt jedem, funktioniert an vier Stellen und verlangt keine Größenangabe. Das sicherste Accessoire-Geschenk überhaupt.", "B06XC7MMFQ"),
        ("Creolen in mittlerer Größe", "Die Ohrringgröße, die zur Jeans und zum Anlasskleid passt. In ihrer Metallfarbe kaufen, nicht in deiner.", "B0FR8WK8T2"),
        ("Schal aus reiner Wolle", "Der Unterschied zu Mischgewebe ist beim ersten Anfassen spürbar und hält Jahre. Wird jeden Winter getragen.", "B0BDZM3FR3"),
        ("Brosche für das Revers", "Das Geschenk, das ihr sonst niemand macht. Verwandelt ein Alltagssakko in ein Anlassteil.", "B0F92YSCBD"),
        ("Strukturierte Handtasche", "Steht von allein, wenn man sie abstellt. Klingt banal, merkt man aber jeden Tag.", "handtasche damen strukturiert leder"),
        ("Gefütterte Lederhandschuhe", "Das Stück, das sie sich selbst nie kauft und dann den ganzen Winter trägt.", "B097XZ7HHH"),
    ],
})

POSTS.append({
    "slug": "geschenke-maenner-accessoires",
    "cat": "accessoires",
    "title": "Acht Accessoires für Männer, die tatsächlich benutzt werden",
    "teaser": "Männer kaufen sich Accessoires selten selbst. Genau deshalb sind sie als Geschenk stark — und genau deshalb geht es so oft daneben.",
    "img": "geschenke-maenner-accessoires.jpg",
    "meta": "Geschenkideen für Männer: zehn Accessoires, die im Alltag landen statt in der Schublade, und die Fehler, die man dabei macht.",
    "intro": [
        "Die meisten Männer ersetzen Gürtel, Schal und Geldbörse erst, wenn das alte Stück kaputt ist. Das macht Accessoires zum dankbarsten Geschenk, das es gibt: Es gibt fast immer eine Lücke, und sie wird fast nie freiwillig geschlossen.",
        "Der Haken ist, dass ein Accessoire für Männer noch weniger auffallen darf als für Frauen. Ein Stück, das nach Geschenk aussieht, wird nicht getragen.",
    ],
    "sections": [
        ("Die Regel: ersetzen, nicht hinzufügen", [
            "Schau dir an, was er täglich benutzt, und ersetze das älteste Stück durch eine bessere Ausführung. Derselbe Zweck, dieselbe Farbe, dieselbe Form — nur besser gemacht. Das ist unspektakulär und trifft fast immer.",
            "Ein neuer Ledergürtel in genau der Breite, die er trägt, wird ab dem ersten Tag benutzt. Ein Gürtel mit auffälliger Schnalle bleibt liegen, egal wie gut er ist.",
            "Dasselbe gilt für die Geldbörse: Wer seit zehn Jahren eine flache Klappbörse trägt, will keine mit Münzfach und Reißverschluss. Die Form ist Gewohnheit, nicht Geschmack.",
        ]),
        ("Was bei fast jedem ankommt", [
            "Eine Uhr mit Lederarmband in Braun. Sie passt zu allem außer zu Schwarz, wirkt an Werktagen nicht overdressed und an Festtagen nicht zu leger — der einzige Schmuck, den viele Männer widerspruchslos anziehen.",
            "Ein Kaschmirschal in Marine, Grau oder Anthrazit. Kein Muster, keine Fransen, keine Marke im Blickfeld. Wird vom Mantel bis zum Sakko getragen und hält länger als die Jacke darunter.",
            "Warme Socken aus Merinowolle, mehrere Paare. Das klingt nach Verlegenheitsgeschenk und ist trotzdem das Stück, von dem er am Ende des Winters sagt, dass er mehr davon bräuchte.",
        ]),
        ("Wenn er Anzug trägt", [
            "Ein Einstecktuch in Weiß mit schmalem Rand. Es ist das einzige Accessoire, das ein Sakko festlich macht, ohne dass jemand sagen kann, was sich geändert hat.",
            "Manschettenknöpfe nur dann, wenn er tatsächlich Hemden mit Umschlagmanschette besitzt. Sonst ist es ein Geschenk, das eine Anschaffung nach sich zieht — und die macht er nicht.",
            "Schuhspanner aus Zedernholz sind das unromantischste Geschenk auf dieser Liste und das, mit dem man gute Schuhe verdoppelt. Wer Lederschuhe trägt und keine hat, bekommt hier echten Nutzen.",
        ]),
        ("Finger weg von", [
            "Krawatten, wenn er keine trägt. Und auch dann: Die Krawatte ist das Stück, bei dem Männer den eigenen Geschmack am stärksten verteidigen.",
            "Allem mit sichtbarer Logo-Fläche. Was heute als Marke gefällt, ist in zwei Jahren datiert, und getragen wird es nur so lange wie das Logo.",
            "Technikzubehör, das er schon hat. Der Kabelhalter, die Powerbank, das Kartenetui mit Funkschutz — alles schon dreimal verschenkt bekommen.",
        ]),
    ],
    "products": [
        ("Ledergürtel, schlichte Schnalle", "Ersetzt das älteste Stück im Schrank. Breite und Farbe abschauen, nicht neu erfinden.", "B00NONXQK6"),
        ("Uhr mit braunem Lederarmband", "Der einzige Schmuck, den viele Männer widerspruchslos tragen. Passt werktags wie festlich.", "herren armbanduhr leder braun klassisch"),
        ("Kaschmirschal, einfarbig", "Marine, Grau oder Anthrazit, ohne Muster. Hält länger als die Jacke darüber.", "B08VRRXBRN"),
        ("Merinosocken im Mehrerpack", "Klingt nach Verlegenheit, wird aber den ganzen Winter getragen.", "B013GD9ZLM"),
        ("Einstecktuch weiß", "Macht ein Sakko festlich, ohne dass jemand benennen kann, was sich geändert hat.", "B01N6WDC3V"),
        ("Schuhspanner aus Zedernholz", "Das unromantischste Geschenk hier und das, mit dem gute Schuhe doppelt so lange halten.", "B00K04SU8K"),
    ],
})


POSTS.append({
    "slug": "wichtelgeschenke-ideen",
    "cat": "accessoires",
    "title": "Wichtelgeschenke, bei denen niemand höflich lächeln muss",
    "teaser": "Beim Wichteln kennt man den Beschenkten kaum und trifft trotzdem eine Wahl vor Publikum. Es gibt eine Kategorie, die das löst.",
    "img": "wichtelgeschenke-ideen.jpg",
    "meta": "Wichtelgeschenke für Büro und Familie: zehn Ideen, die im Alltag benutzt werden, und die Kategorien, die zuverlässig danebengehen.",
    "intro": [
        "Wichteln hat eine Eigenheit, die es schwerer macht als jedes andere Geschenk: Man kennt die Person oft kaum, und ausgepackt wird vor allen anderen. Ein Fehlgriff ist damit nicht privat, sondern öffentlich.",
        "Die Lösung liegt nicht in mehr Witz, sondern in weniger Persönlichem. Was gebraucht wird, funktioniert bei jedem — was Geschmack ausdrückt, nur bei wenigen.",
    ],
    "sections": [
        ("Warum Scherzartikel fast immer scheitern", [
            "Ein Witz braucht ein gemeinsames Vorwissen. Im Büro-Wichteln teilen selten alle dasselbe, und was in der einen Abteilung als Anspielung funktioniert, ist in der anderen eine Zumutung. Der Moment des Auspackens verzeiht das nicht.",
            "Dazu kommt: Scherzartikel werden einmal gezeigt und nie wieder angefasst. Wer zwanzig Euro für drei Sekunden Lachen ausgibt, hat schlecht getauscht.",
            "Wenn es lustig sein soll, dann über die Verpackung, nicht über den Inhalt. Das Geschenk bleibt brauchbar, die Pointe passiert trotzdem.",
        ]),
        ("Die sichere Kategorie: Dinge, die verbraucht werden", [
            "Alles, was aufgebraucht wird, kann nicht im Weg stehen und muss nicht zum Einrichtungsstil passen. Guter Tee, gute Schokolade, ein Gewürz, das man sich selbst nicht kauft — das trifft quer durch jede Runde.",
            "Der Unterschied zwischen langweilig und gut liegt in der Qualitätsstufe. Eine Tafel aus dem Supermarktregal ist ein Pflichtgeschenk, eine Tafel von einem Hersteller, den man nicht kennt, ist eine Entdeckung.",
            "Zweitbeste Kategorie: Dinge, die im Alltag kaputtgehen. Ein gutes Notizbuch, ein ordentlicher Stift, feste Handcreme für den Schreibtisch.",
        ]),
        ("Accessoires, die beim Wichteln gehen", [
            "Warme Socken aus Merinowolle. Die Größe ist grob genug, dass sie fast immer passt, und niemand hat genug davon. Das ist das mit Abstand sicherste Kleidungsstück für eine Runde, in der man niemanden kennt.",
            "Ein einfarbiger Schal in Grau oder Marine. Er passt zu jeder Jacke, hat keine Größe und verlangt keine Stilentscheidung.",
            "Ein Schlüsselanhänger aus Leder. Klein, benutzt, unauffällig — und das einzige Stück auf dieser Liste, das man täglich in der Hand hält.",
        ]),
        ("Die Regeln der Runde vorher klären", [
            "Preisrahmen, Termin, ob gewünscht werden darf. Die meisten Enttäuschungen beim Wichteln entstehen nicht durch schlechte Geschenke, sondern durch unterschiedliche Annahmen über den Rahmen.",
            "Wenn Wünsche erlaubt sind, nutze sie. Ein erfüllter Wunsch schlägt jede kreative Eigenidee — auch wenn sich das beim Kaufen falsch anfühlt.",
            "Und pack es ordentlich ein. Beim Wichteln sieht die Verpackung jeder, bevor er den Inhalt sieht, und sie ist der halbe Eindruck.",
        ]),
    ],
    "products": [
        ("Merinosocken im Mehrerpack", "Grobe Größenstufen, hoher Gebrauchswert, niemand hat genug davon. Das sicherste Kleidungsstück für eine fremde Runde.", "B0DHCNW3HG"),
        ("Schal einfarbig Grau oder Marine", "Keine Größe, keine Stilentscheidung, passt zu jeder Jacke.", "B00XPI9BMW"),
        ("Schlüsselanhänger aus Leder", "Klein, unauffällig und das einzige Stück hier, das täglich in der Hand liegt.", "B08L46KSMW"),
        ("Feste Handcreme für den Schreibtisch", "Wird aufgebraucht, steht niemandem im Weg und passt zu keiner Einrichtung — genau richtig.", "B0CGX9JXJD"),
        ("Notizbuch mit festem Einband", "Geht im Alltag kaputt und wird deshalb gebraucht. Fester Einband ist der Unterschied.", "B0D5HRSN1M"),
        ("Teesortiment in Probiergrößen", "Verbraucht sich, trifft quer durch jede Runde und erlaubt eine Qualitätsstufe über dem Üblichen.", "B016IL75S4"),
    ],
})

POSTS.append({
    "slug": "festliches-kleid-figur",
    "cat": "festtage",
    "title": "Sechs festliche Kleiderschnitte und für welche Figur sie gemacht sind",
    "teaser": "Ein Kleid sitzt nicht deshalb gut, weil es teuer ist, sondern weil sein Schnitt die Stelle betont, die tragen kann.",
    "img": "festliches-kleid-figur.jpg",
    "meta": "Festliches Kleid finden: neun Schnitte im Vergleich, welche Figur sie tragen und woran man im Laden erkennt, dass es passt.",
    "intro": [
        "Die meisten Fehlkäufe bei festlichen Kleidern entstehen nicht durch die falsche Größe, sondern durch den falschen Schnitt. Ein Kleid, das an der Schaufensterpuppe fällt, kann am Körper an genau der Stelle spannen, an der es fallen müsste.",
        "Die Schnitte unten sind nach dem geordnet, was sie tun — nicht nach Modenamen. Wer weiß, welche Linie er sucht, findet sie in jeder Preisklasse.",
    ],
    "sections": [
        ("Die drei Schnitte, die fast immer funktionieren", [
            "Das Wickelkleid. Es legt die Taille dort fest, wo sie tatsächlich ist, statt dort, wo der Hersteller sie vermutet — und das ist der Grund, warum es an den meisten Körpern funktioniert. Achte darauf, dass der Wickel bis über die Hüfte reicht, sonst klafft er beim Sitzen.",
            "Das A-Linien-Kleid. Eng an der schmalsten Stelle, ab dort frei fallend. Es verzeiht alles unterhalb der Taille und ist deshalb die ruhigste Wahl für einen langen Abend am Tisch.",
            "Das Etuikleid mit leichtem Stretch. Es zeichnet nach, statt zu formen — vorausgesetzt, der Stoff hat Struktur. Reiner Jersey ohne Futter zeigt jede Naht der Wäsche darunter.",
        ]),
        ("Wenn die Schultern breiter sind als die Hüfte", [
            "Alles, was unten Volumen hat, gleicht aus: A-Linie, Tellerrock, ein Kleid mit Falten ab der Taille. Die Silhouette wird dadurch ausgewogen, ohne dass oben etwas kaschiert werden muss.",
            "Vermeide breite Träger, Puffärmel und waagerechte Ausschnitte. Sie verlängern die Schulterlinie genau dort, wo sie ohnehin schon die breiteste Stelle ist.",
            "Ein V-Ausschnitt arbeitet in die richtige Richtung: Er führt den Blick nach unten zur Mitte statt nach außen.",
        ]),
        ("Wenn die Hüfte die breiteste Stelle ist", [
            "Oben Aufmerksamkeit schaffen: ein Ausschnitt mit Detail, eine Schulterpartie mit Struktur, auffällige Ohrringe. Der Blick bleibt dort, wo er zuerst hinfällt.",
            "Unten glatt und dunkel halten, ohne krampfhaft zu kaschieren. Ein Rock, der ab der Hüfte gerade fällt, wirkt schmaler als einer, der sich anschmiegt, und viel schmaler als einer, der abstehen will.",
            "Finger weg von Taschen auf Hüfthöhe und von großen Mustern genau an dieser Stelle.",
        ]),
        ("Woran du im Laden erkennst, dass es sitzt", [
            "Setz dich hin. Zwei Drittel eines Abends verbringt man sitzend, und genau dort scheitern die meisten Kleider: Der Wickel klafft, der Schlitz wandert, der Bund schneidet.",
            "Heb beide Arme über den Kopf. Rutscht der Saum mehr als eine Handbreit hoch, wird das den ganzen Abend so bleiben.",
            "Schau von der Seite in den Spiegel, nicht nur von vorn. Die Frontalansicht verzeiht Spannungsfalten, die im Profil sofort auffallen — und andere sehen dich überwiegend im Profil.",
        ]),
    ],
    "products": [
        ("Wickelkleid, knielang", "Legt die Taille dort fest, wo sie ist. Auf einen Wickel achten, der über die Hüfte reicht.", "wickelkleid damen knielang festlich"),
        ("Kleid in A-Linie", "Eng an der schmalsten Stelle, ab dort frei fallend. Die ruhigste Wahl für einen langen Abend.", "kleid damen a linie festlich midi"),
        ("Etuikleid mit Struktur", "Zeichnet nach statt zu formen — aber nur mit festem Stoff und Futter.", "etuikleid damen festlich gefuettert"),
        ("Kleid mit V-Ausschnitt", "Führt den Blick zur Mitte statt nach außen. Die richtige Wahl bei breiteren Schultern.", "kleid damen v ausschnitt festlich"),
        ("Formende Unterwäsche ohne Naht", "Entscheidet bei glatten Stoffen mehr über den Sitz als das Kleid selbst.", "shapewear damen nahtlos unsichtbar"),
        ("Unterkleid in Hautton", "Nimmt dünnen Stoffen die Durchsicht und lässt sie besser fallen. Wird fast immer vergessen.", "unterkleid damen hautfarben"),
    ],
})


POSTS.append({
    "slug": "silvester-outfit-damen",
    "cat": "festtage",
    "title": "Silvester-Looks für vier verschiedene Abende",
    "teaser": "Silvester ist der einzige Abend im Jahr, an dem fast jeder Dresscode gleichzeitig gilt. Deshalb hilft es, zuerst zu klären, wo man steht.",
    "img": "silvester-outfit-damen.jpg",
    "meta": "Silvester Outfit Damen 2026: acht Looks nach Anlass sortiert, von der Hausparty bis zum Ball, mit dem Wärmeproblem gelöst.",
    "intro": [
        "Die Frage nach dem Silvesteroutfit lässt sich nicht allgemein beantworten, weil der Abend an fünf verschiedenen Orten stattfindet: im Wohnzimmer von Freunden, im Restaurant, im Club, auf der Straße beim Feuerwerk und auf dem Ball. Zwischen dem ersten und dem letzten liegen Welten.",
        "Was alle teilen, ist ein Problem, das jedes Jahr unterschätzt wird: Um Mitternacht steht man draußen. Jeder Look hier ist so gebaut, dass er das überlebt.",
    ],
    "sections": [
        ("Hausparty bei Freunden", [
            "Der häufigste Fall und der, bei dem man am leichtesten zu viel macht. Auf einem Sofa in einer engen Robe zu sitzen ist der schnellste Weg, den Abend unbequem zu machen.",
            "Die Lösung ist ein Teil mit Glanz und der Rest schlicht: eine Satinhose zu einem feinen Strickpullover, ein Paillettentop zur dunklen Jeans. Das liest sich als Silvester, ohne dass man sich verkleidet fühlt.",
            "Schuhe, die man ausziehen kann, ohne dass der Look zusammenbricht. In vielen Wohnungen ist das nach zwanzig Minuten ohnehin Realität.",
        ]),
        ("Restaurant und Bar", [
            "Hier gilt der klassische festliche Rahmen, aber sitzend. Das heißt: Der Bund darf nicht schneiden, der Schlitz nicht wandern, der Ausschnitt nicht rutschen, wenn man sich nach vorn beugt.",
            "Ein knielanges Kleid in einem tiefen Ton mit Schmuck als einzigem Glanz funktioniert überall zwischen Bistro und Hotelrestaurant. Wer es weniger formell will, tauscht das Kleid gegen weite Hose und Seidenbluse.",
            "Absatz maximal so hoch, wie man zwei Stunden stehen kann — der Übergang zwischen Restaurant und Mitternacht findet oft im Freien statt.",
        ]),
        ("Club und Tanzfläche", [
            "Hier darf das Material auffällig sein: Pailletten, Metallic, Lack. Was nicht auffällig sein darf, ist der Schnitt — alles, was ständig zurechtgezogen werden muss, ruiniert den Abend.",
            "Trägerkleider mit Gummizug am Oberrand sind der häufigste Fehlkauf. Nach drei Liedern sitzen sie woanders.",
            "Tasche klein und quer über der Schulter. Alles andere steht entweder am Rand der Tanzfläche oder verschwindet.",
        ]),
        ("Das Wärmeproblem um Mitternacht", [
            "Das Feuerwerk dauert zwanzig Minuten, und in diesen zwanzig Minuten steht man ohne Bewegung draußen. Eine Jacke, die nur bis zur Taille geht, reicht dafür nicht.",
            "Am besten funktioniert ein Mantel, der länger ist als das Kleid darunter, plus Strumpfhose mit mindestens sechzig Denier. Beides sieht man auf keinem Foto und beides entscheidet, ob man danach noch draußen bleibt.",
            "Wer Stiefel zum Kleid trägt, hat das Problem ohnehin gelöst — und liegt damit seit zwei Wintern auch modisch richtig.",
        ]),
    ],
    "products": [
        ("Satinhose mit weitem Bein", "Der Glanz-Anteil für einen Abend, an dem der Rest schlicht bleiben soll. Sitzt auch auf dem Sofa bequem.", "satinhose damen weit dunkel"),
        ("Paillettentop", "Zur dunklen Jeans oder Wollhose — liest sich als Silvester, ohne verkleidet zu wirken.", "pailletten top damen langarm"),
        ("Knielanges Kleid in tiefem Ton", "Der Restaurant-Look, der zwischen Bistro und Hotel überall funktioniert.", "cocktailkleid damen knielang dunkelgruen"),
        ("Blickdichte Strumpfhose 60 den", "Entscheidet darüber, ob man die zwanzig Minuten Feuerwerk draußen übersteht. Sieht man auf keinem Foto.", "strumpfhose damen 60 den blickdicht"),
        ("Mantel länger als das Kleid", "Die einzige Mantellänge, die zum Anlassoutfit funktioniert. Alles Kürzere zeigt einen Bruch.", "wollmantel damen lang tailliert"),
        ("Kleine Umhängetasche", "Quer über der Schulter, damit sie beim Tanzen nicht am Rand liegen bleibt.", "umhaengetasche damen klein abend"),
    ],
})

POSTS.append({
    "slug": "adventskaffee-outfit",
    "cat": "festtage",
    "title": "Sechs Looks für Adventskaffee, Kirche und die Runde bei den Schwiegereltern",
    "teaser": "Der Advent hat einen eigenen Dresscode, für den es keinen Namen gibt: festlich genug für den Tisch, bequem genug für vier Stunden daran.",
    "img": "adventskaffee-outfit.jpg",
    "meta": "Outfit für Adventskaffee und Adventsgottesdienst: sechs Looks, die festlich wirken und stundenlanges Sitzen aushalten.",
    "intro": [
        "Zwischen Weihnachtsfeier und Heiligabend liegen vier Sonntage, an denen man festlicher aussehen soll als im Alltag, aber deutlich weniger festlich als abends. Für diesen Bereich gibt es keine Regel, und genau deshalb fällt er so schwer.",
        "Der brauchbarste Maßstab: Man sitzt lange, es ist warm drinnen und kalt draußen, und fotografiert wird auch.",
    ],
    "sections": [
        ("Der Grundaufbau", [
            "Ein festliches Oberteil zu einer alltagstauglichen Hose oder einem schlichten Rock. Der Glanz gehört nach oben, weil dort fotografiert wird und weil man dort nicht sitzt.",
            "Feiner Strick in einem satten Ton ist das zuverlässigste Oberteil dieser Wochen. Er wirkt gepflegt, verzeiht Wärme und steht nicht vom Körper ab, wenn man sich an den Tisch lehnt.",
            "Darunter eine Hose mit festem Bund und ohne Stretch-Knick — der Unterschied zwischen festlich und Freizeit entsteht hier, nicht oben.",
        ]),
        ("Für den Gottesdienst", [
            "In der Kirche ist es kalt, auch im Dezember, besonders bei langen Gottesdiensten. Schichten schlagen ein einzelnes dickes Teil, weil man drinnen wieder ablegen kann.",
            "Ein Blazer oder eine lange Strickjacke über dem Oberteil löst das und ist zugleich das Stück, das den Look vom Nachmittagskaffee zur Kirche hebt.",
            "Schuhe mit Sohle, nicht mit Ballerinaboden. Steinböden im Winter sind unangenehmer, als man sich merkt.",
        ]),
        ("Wenn Kinder dabei sind", [
            "Dunkle Farben im unteren Drittel, waschbare Materialien oben. Das klingt nüchtern und ist der Unterschied zwischen einem entspannten und einem angespannten Nachmittag.",
            "Keine langen Ärmel aus Feinstrick, die in Teller hängen, und keine Kette, an der gezogen werden kann. Beides lernt man einmal.",
            "Flache Schuhe, die man in zwei Sekunden anzieht. Der Gang nach draußen kommt öfter, als man plant.",
        ]),
        ("Das eine Teil, das den Unterschied macht", [
            "Eine Brosche, eine Samtschleife im Haar, ein Seidentuch am Hals — ein einziges Detail, das im Alltag nicht vorkommt, macht aus dem Pullover ein Adventsoutfit.",
            "Das ist billiger und wirksamer als ein neues Kleid und funktioniert an allen vier Sonntagen mit unterschiedlicher Basis.",
            "Wenn du nur eine Sache änderst gegenüber dem Alltag: Nimm die auffälligeren Ohrringe. Sie sind auf jedem Foto zu sehen, auf dem man am Tisch sitzt.",
        ]),
    ],
    "products": [
        ("Feinstrickpullover in sattem Ton", "Das zuverlässigste Oberteil dieser Wochen: gepflegt, warm verträglich, steht nicht ab.", "feinstrick pullover damen bordeaux"),
        ("Hose mit festem Bund", "Hier entsteht der Unterschied zwischen festlich und Freizeit — nicht oben.", "stoffhose damen fester bund elegant"),
        ("Lange Strickjacke", "Hebt den Nachmittagslook zur Kirche und lässt sich drinnen ablegen.", "strickjacke damen lang grobstrick"),
        ("Samtschleife fürs Haar", "Ein Detail, das im Alltag nicht vorkommt, verwandelt den Pullover in ein Adventsoutfit.", "haarschleife samt damen"),
        ("Auffälligere Ohrringe", "Auf jedem Foto zu sehen, auf dem man am Tisch sitzt. Die wirksamste einzelne Änderung.", "ohrringe damen statement gold festlich"),
        ("Loafer mit fester Sohle", "Steinböden im Winter sind unangenehmer, als man sie in Erinnerung hat.", "loafer damen leder profilsohle"),
    ],
})


POSTS.append({
    "slug": "wintertaufe-gast",
    "cat": "familienfeier",
    "title": "Taufe im Winter: das Outfit für Kirche, Kälte und Kaffeetafel",
    "teaser": "Eine Wintertaufe hat zwei Räume mit zwanzig Grad Unterschied und einen Fototermin dazwischen. Das Outfit muss alle drei aushalten.",
    "img": "wintertaufe-gast.jpg",
    "meta": "Taufe im Winter als Gast: sieben Outfits für Kirche, Kälte und Kaffeetafel, mit den Farbregeln, die für Taufen gelten.",
    "intro": [
        "Taufen finden auch im Januar statt, und dann gilt alles, was für eine Sommertaufe gilt, plus ein Problem: Die Kirche ist kalt, der Gang zum Auto ist kälter und das Restaurant danach überheizt. Ein einzelnes schönes Teil löst das nicht.",
        "Dazu kommen die Farbregeln, die bei Taufen strenger sind, als viele Gäste vermuten.",
    ],
    "sections": [
        ("Die Farben: was geht und was nicht", [
            "Schwarz von Kopf bis Fuß wirkt bei einer Taufe fehl am Platz — es ist ein Fest, kein Trauerfall. Schwarz als Teil eines Outfits ist dagegen völlig unproblematisch, solange etwas Helles oder Farbiges dazukommt.",
            "Weiß und Creme bleiben dem Täufling vorbehalten. Das ist weniger streng als bei einer Hochzeit, aber ein komplett weißes Outfit wirkt trotzdem, als hätte man die Rolle verwechselt.",
            "Am sichersten sind gedeckte, warme Töne: Kamel, Bordeaux, Tannengrün, Dunkelblau, Rostbraun. Sie passen zum Winterlicht und fotografieren sich in einer Kirche besser als kalte Farben.",
        ]),
        ("Das Schichtenproblem", [
            "Drei Lagen statt einer dicken: Oberteil, Blazer oder Strickjacke, Mantel. In der Kirche bleibt alles an, im Restaurant kommen zwei Lagen weg, und man sieht in beiden Räumen angezogen aus.",
            "Die mittlere Lage ist die wichtigste, weil sie auf den meisten Fotos zu sehen ist. Hier lohnt sich das schönere Teil, nicht beim Mantel.",
            "Eine Strumpfhose mit sechzig bis achtzig Denier in einer Farbe, die zum Schuh passt. Feinstrumpfhosen sind in einer ungeheizten Kirche eine Fehlentscheidung, die man eine Stunde lang spürt.",
        ]),
        ("Kirche, Foto, Kaffeetafel", [
            "In der Kirche steht und sitzt man abwechselnd, oft ohne Kissen. Röcke, die beim Hinsetzen hochrutschen, werden dabei zum Dauerthema.",
            "Der Fototermin findet meist draußen vor dem Portal statt, im Mantel. Deshalb sollte der Mantel farblich zum Rest passen und nicht die Notlösung sein, die gerade greifbar war.",
            "An der Kaffeetafel sitzt man lange und isst. Helle Ärmel und lange, weite Ärmel sind hier dieselbe schlechte Idee wie beim Adventskaffee.",
        ]),
        ("Als Patin oder Pate", [
            "Paten stehen vorn und sind auf jedem Foto. Eine Stufe formeller als die übrigen Gäste ist hier richtig, nicht übertrieben.",
            "Für Patinnen heißt das ein Kleid oder ein Rock-Blazer-Aufbau statt Hose, für Paten ein Sakko mit Hemd, gern ohne Krawatte.",
            "Und etwas, das man behalten kann: Viele Paten tragen an diesem Tag zum ersten Mal ein Schmuckstück, das später mit dem Datum verbunden bleibt.",
        ]),
    ],
    "products": [
        ("Blazer in Kamel oder Bordeaux", "Die mittlere Lage ist auf den meisten Fotos zu sehen — hier lohnt das schönere Teil.", "blazer damen kamel tailliert"),
        ("Kleid in gedecktem Winterton", "Tannengrün, Dunkelblau oder Rostbraun fotografieren sich in einer Kirche besser als kalte Farben.", "kleid damen winter dunkelgruen midi"),
        ("Strumpfhose 80 den", "Eine ungeheizte Kirche verzeiht keine Feinstrumpfhose. Das spürt man eine Stunde lang.", "strumpfhose damen 80 den blickdicht"),
        ("Mantel passend zum Outfit", "Der Fototermin findet im Mantel statt. Er sollte nicht die Notlösung sein.", "wollmantel damen kamel klassisch"),
        ("Schlichte Kette für Patinnen", "Viele Paten tragen an diesem Tag zum ersten Mal ein Stück, das mit dem Datum verbunden bleibt.", "kette damen gold schlicht anhaenger"),
        ("Loafer oder Stiefelette mit Absatz", "Steht und sitzt sich in der Kirche besser als jeder hohe Absatz.", "stiefelette damen blockabsatz leder"),
    ],
})

POSTS.append({
    "slug": "ballkleid-ballsaison-2027",
    "cat": "festtage",
    "title": "Ballsaison 2027: das Ballkleid und alles, was sonst dazugehört",
    "teaser": "Ein Ball ist der einzige Anlass, bei dem der Dresscode tatsächlich geprüft wird. Und der einzige, bei dem die Nebensachen über den Abend entscheiden.",
    "img": "ballkleid-ballsaison-2027.jpg",
    "meta": "Ballkleid für die Saison 2027: sieben Schnitte, die Dresscodes von Black Tie bis festlich erklärt, plus die Ausstattung für den ganzen Abend.",
    "intro": [
        "Die Ballsaison läuft von Januar bis in den März, und anders als bei jeder Weihnachtsfeier steht der Dresscode auf der Einladung. Wer ihn liest und ernst nimmt, hat die halbe Entscheidung schon getroffen.",
        "Die andere Hälfte sind die Dinge, die nicht auf Fotos landen: Schuhe, in denen man tanzen kann, und eine Tasche, in der das Nötigste Platz hat.",
    ],
    "sections": [
        ("Den Dresscode auf der Einladung lesen", [
            "Black Tie heißt bodenlang. Nicht knielang, nicht midi — bodenlang. Das ist die einzige Angabe, bei der es keinen Spielraum gibt, und zugleich die, bei der die meisten Gäste danebenliegen.",
            "Festliche Abendgarderobe oder Abendkleidung lässt auch Wadenlänge und einen sehr festlichen Hosenanzug zu. Hier ist Material wichtiger als Länge: Satin, Samt, Crêpe — nicht Jersey.",
            "Dunkler Anzug für Herren bedeutet dunkelblau oder anthrazit, nicht grau, und mit Krawatte. Wenn Smoking gefordert ist, steht es da.",
        ]),
        ("Die Schnitte, die auf einem Ball funktionieren", [
            "Ein bodenlanges Kleid mit fließendem Fall bewegt sich beim Tanzen mit, statt zu bremsen. Enge, steife Schnitte sehen im Stehen gut aus und sind nach zwei Runden Walzer eine Zumutung.",
            "Ein Schlitz gehört bis maximal zum Knie, wenn getanzt wird — höher wandert er, und das kostet den Abend über Aufmerksamkeit.",
            "Träger sind einem trägerlosen Oberteil vorzuziehen, sobald Bewegung im Spiel ist. Was beim Sitzen hält, hält beim Drehen selten.",
        ]),
        ("Was über den Abend entscheidet und auf keinem Foto ist", [
            "Schuhe mit Riemchen oder geschlossener Ferse. Pumps, die nur vorn halten, verliert man auf dem Parkett — das ist kein Klischee, sondern Physik.",
            "Absatzhöhe, die man drei Stunden trägt, plus ein Paar faltbare Ballerinas in der Garderobe. Fast jeder Ball hat gegen Mitternacht eine Reihe barfüßiger Gäste, die anders geplant hatten.",
            "Eine Clutch, in die Handy, Lippenstift und Garderobenmarke passen. Alles Größere legt man ab und sucht es später.",
        ]),
        ("Die Details, die man vorher regelt", [
            "Das Kleid vor dem Abend einmal anziehen und darin sitzen, aufstehen, die Arme heben und eine Drehung machen. Alles, was dabei stört, stört auf dem Ball zehnmal so sehr.",
            "Klebeband für Träger und ein Nadelkissen gehören in die Garderobe, nicht ins Wunschdenken. Jeder Ball hat mindestens einen gerissenen Träger.",
            "Und die Garderobenmarke gehört in die Clutch, nicht in die Manteltasche. Sonst steht man um zwei Uhr früh in einer Schlange, die man sich hätte sparen können.",
        ]),
    ],
    "products": [
        ("Bodenlanges Kleid mit fließendem Fall", "Bewegt sich beim Tanzen mit, statt zu bremsen. Die einzige Länge, die Black Tie erfüllt.", "abendkleid damen bodenlang fliessend"),
        ("Abendkleid mit Trägern", "Was beim Sitzen hält, hält beim Drehen selten. Träger schlagen trägerlos, sobald getanzt wird.", "abendkleid damen traeger elegant lang"),
        ("Sandalette mit Fesselriemen", "Pumps, die nur vorn halten, verliert man auf dem Parkett. Das ist Physik, kein Klischee.", "sandaletten damen riemchen absatz abend"),
        ("Faltbare Ballerinas", "Gegen Mitternacht steht auf jedem Ball eine Reihe barfüßiger Gäste, die anders geplant hatte.", "faltbare ballerinas damen taschenschuhe"),
        ("Clutch mit Kettenriemen", "Handy, Lippenstift, Garderobenmarke. Alles Größere legt man ab und sucht es später.", "clutch damen abend kette"),
        ("Modeschmuck-Set für den Abend", "Ein Ball verträgt mehr Schmuck als jeder andere Anlass — und nur hier fällt zu wenig auf.", "schmuckset damen abend ohrringe kette"),
    ],
})

PINTITEL = {
    "hochzeitsgast-herbst":          "Hochzeitsgast Outfit Herbst 2026 – 7 Looks",
    "hochzeitsgast-ab-40":           "Hochzeitsgast Outfit ab 40 Damen",
    "drei-farben-regel":             "Anlass-Outfit kombinieren: die 3-Farben-Regel",
    "standesamt-schlicht":           "Standesamt Outfit schlicht – 5 Looks",
    "weisser-blazer":                "Weißer Blazer kombinieren – 5 Outfits",
    "quiet-business":                "Büro Outfit Damen ohne Kostüm",
    "weite-hose-regel":              "Weite Hose kombinieren Damen",
    "capsule-buero":                 "Capsule Wardrobe Büro: 12 Teile, 20 Outfits",
    "khaki-coded":                   "Herren Herbst Outfit 2026 in Khaki",
    "poetcore-cape":                 "Cape Outfit Herbst 2026 Damen",
    "layering-regeln":               "Layering Outfit Herbst Damen",
    "weihnachtsfeier":               "Weihnachtsfeier Outfit Damen 2026",
    "silvester-gold":                "Silvester Outfit Gold Damen 2026",
    "brosche-tragen":                "Brosche richtig tragen: 7 Positionen",
    "breiter-guertel":               "Breiter Gürtel kombinieren Damen",
    "seidentuch-binden":             "Seidentuch binden: 5 Arten",
    "goldschmuck-stapeln":           "Goldschmuck kombinieren und stapeln",
    "weihnachtsmarkt-outfit":        "Weihnachtsmarkt Outfit 2026 Damen",
    "heiligabend-outfit":            "Heiligabend Outfit 2026 festlich",
    "silvester-herren":              "Silvester Outfit Herren 2026",
    "winterhochzeit-gast":           "Winterhochzeit Gast Outfit 2026",
    "weihnachtsfeier-ab-50":         "Weihnachtsfeier Outfit ab 50 Damen",
    "mantel-ueber-anlass-outfit":    "Mantel zum Anlass-Outfit Damen",
    "herbsthochzeit-gast":           "Herbsthochzeit Gast Outfit 2026",
    "taufe-gast-herbst":             "Taufe Outfit Gast Damen Herbst",
    "runder-geburtstag-damen":       "Runder Geburtstag Outfit Damen",
    "vorstellungsgespraech-herbst":  "Vorstellungsgespräch Outfit Damen 2026",
    "standesamt-winter-braut":       "Standesamt Outfit Winter Braut 2026",
    "schuhe-strumpfhose-anlasskleid":"Schuhe und Strumpfhose zum Anlasskleid",
    "trauerfeier-outfit":            "Trauerfeier Outfit Damen nicht schwarz",
    "weihnachtsfeier-firma-2026":    "Weihnachtsfeier Firma Outfit Damen 2026",
    "stiefel-zum-anlasskleid":       "Stiefel zum Anlasskleid Herbst 2026",
    "strickjacke-statt-blazer":       "Strickjacke statt Blazer Outfit Damen",
    "weihnachtsfeier-herren-2026":    "Weihnachtsfeier Outfit Herren 2026",
    "samt-outfit-festlich-2026":      "Samt Outfit festlich Damen 2026",
    "geschenke-frauen-accessoires":      "Geschenke für Frauen: 6 Accessoires, die ankommen",
    "geschenke-maenner-accessoires":     "Geschenke für Männer: 8 Accessoires",
    "wichtelgeschenke-ideen":            "Wichtelgeschenke: 6 Ideen ohne Fremdscham",
    "festliches-kleid-figur":            "Festliches Kleid: 6 Schnitte für jede Figur",
    "silvester-outfit-damen":            "Silvester Outfit Damen 2026 – 4 Looks",
    "adventskaffee-outfit":              "Adventskaffee Outfit: 6 Looks",
    "wintertaufe-gast":                  "Wintertaufe Gast Outfit Damen",
    "ballkleid-ballsaison-2027":         "Ballkleid 2027: Schnitte und Dresscode",
}

for _p in POSTS:
    if "pintitle" not in _p:
        _p["pintitle"] = PINTITEL.get(_p["slug"], _p["title"])
del _p
# Zweiter Suchtitel fuer die c-Variante. Grund: b und c zeigen dasselbe Ziel
# mit anderem Motiv. Tragen beide denselben Titel, konkurrieren sie um
# dieselbe Suchanfrage. Mit einem zweiten Titel deckt jeder Beitrag zwei
# Suchbegriffe ab statt einen. Faellt ein Eintrag weg, nimmt makepins.py
# automatisch PINTITEL - kaputt geht dabei nichts.
PINTITEL_C = {
    "hochzeitsgast-herbst":           "Hochzeit Gast Kleid Herbst 2026 – Ideen",
    "hochzeitsgast-ab-40":            "Festliches Outfit ab 40: Hochzeit als Gast",
    "drei-farben-regel":              "Welche Farben passen zusammen? Outfit-Regel",
    "standesamt-schlicht":            "Was zieht man zum Standesamt an? 5 Looks",
    "weisser-blazer":                 "Blazer Outfit Damen elegant kombinieren",
    "quiet-business":                 "Quiet Luxury Büro Outfit Damen 2026",
    "weite-hose-regel":               "Marlenehose Outfit Damen kombinieren",
    "capsule-buero":                  "Business Basics Damen: Garderobe aufbauen",
    "khaki-coded":                    "Herren Outfit Herbst 2026 casual elegant",
    "poetcore-cape":                  "Poncho Outfit Damen Herbst kombinieren",
    "layering-regeln":                "Zwiebellook Herbst Damen richtig kombinieren",
    "weihnachtsfeier":                "Was zieht man zur Weihnachtsfeier an?",
    "silvester-gold":                 "Silvester Kleid Damen 2026 festlich",
    "brosche-tragen":                 "Brosche am Blazer tragen: Anleitung",
    "breiter-guertel":                "Taillengürtel Outfit Damen kombinieren",
    "seidentuch-binden":              "Halstuch binden Damen: Anleitung in 5 Schritten",
    "goldschmuck-stapeln":            "Layering Ketten Gold Damen kombinieren",
    "weihnachtsmarkt-outfit":         "Winter Outfit Damen warm und schick",
    "heiligabend-outfit":             "Weihnachten Outfit Damen für zu Hause",
    "silvester-herren":               "Silvester Outfit Männer 2026 elegant",
    "winterhochzeit-gast":            "Hochzeit Gast Outfit Dezember Damen",
    "weihnachtsfeier-ab-50":          "Festliches Outfit ab 50 Damen Winter",
    "mantel-ueber-anlass-outfit":     "Welcher Mantel zum Kleid? Damen Anlass",
    "herbsthochzeit-gast":            "Hochzeitsgast Kleid Oktober 2026 Damen",
    "taufe-gast-herbst":              "Taufe Gast Outfit 2026 Damen",
    "runder-geburtstag-damen":        "Outfit runder Geburtstag 50 Damen",
    "vorstellungsgespraech-herbst":   "Bewerbungsgespräch Outfit Damen 2026",
    "standesamt-winter-braut":        "Brautkleid standesamtlich Winter 2026",
    "schuhe-strumpfhose-anlasskleid": "Welche Strumpfhose zum Kleid? Anlass",
    "trauerfeier-outfit":             "Beerdigung Outfit Damen: was anziehen?",
    "weihnachtsfeier-firma-2026":     "Betriebsfeier Outfit Damen 2026",
    "stiefel-zum-anlasskleid":        "Kleid mit Stiefeln kombinieren Damen",
    "strickjacke-statt-blazer":       "Grobstrick Cardigan Outfit Damen Büro",
    "weihnachtsfeier-herren-2026":    "Festliches Outfit Männer Weihnachten 2026",
    "samt-outfit-festlich-2026":      "Samtkleid kombinieren Damen festlich",
    "geschenke-frauen-accessoires":      "Weihnachtsgeschenke für Frauen — Ideen 2026",
    "geschenke-maenner-accessoires":     "Weihnachtsgeschenke Männer: Ideen 2026",
    "wichtelgeschenke-ideen":            "Wichteln im Büro: was schenken?",
    "festliches-kleid-figur":            "Welches Kleid passt zu welcher Figur?",
    "silvester-outfit-damen":            "Was zieht man an Silvester an?",
    "adventskaffee-outfit":              "Outfit Advent Damen: festlich und bequem",
    "wintertaufe-gast":                  "Taufe im Winter: was anziehen als Gast?",
    "ballkleid-ballsaison-2027":         "Was zieht man zu einem Ball an?",
}

for _p in POSTS:
    if "pintitle_c" not in _p:
        _p["pintitle_c"] = PINTITEL_C.get(_p["slug"], _p["pintitle"])
del _p


# --------------------------------------------------------------------------
# Pinterest-Keywords je Beitrag. Kleingeschrieben, komma-getrennt, 4-5 Stueck.
# Pinterest wertet sie als Suchbegriffe aus; leer lassen verschenkt Reichweite.
KEYWORDS = {
    "hochzeitsgast-herbst": "hochzeitsgast outfit herbst, hochzeit gast kleid, herbsthochzeit outfit, hochzeitsgast damen, anlass outfit herbst",
    "hochzeitsgast-ab-40": "hochzeitsgast outfit ab 40, festliches outfit ab 40, hochzeit gast damen, elegantes outfit ab 40, anlasskleid ab 40",
    "drei-farben-regel": "farben kombinieren outfit, welche farben passen zusammen, outfit farbregel, anlass outfit kombinieren, farbkombination kleidung",
    "standesamt-schlicht": "standesamt outfit, standesamt kleid schlicht, was anziehen standesamt, kleine hochzeit outfit, standesamt braut",
    "weisser-blazer": "weißer blazer kombinieren, blazer outfit damen, blazer elegant, weißer blazer damen, blazer look",
    "quiet-business": "büro outfit damen, quiet luxury outfit, business outfit ohne kostüm, arbeitsoutfit damen, büro look elegant",
    "weite-hose-regel": "weite hose kombinieren, marlenehose outfit, palazzohose damen, weite hose damen look, bundfaltenhose outfit",
    "capsule-buero": "capsule wardrobe büro, business basics damen, garderobe aufbauen, minimalistische garderobe, büro kleidung damen",
    "khaki-coded": "herren herbst outfit, khaki outfit männer, herren look herbst, männer outfit elegant casual, herrenmode herbst",
    "poetcore-cape": "cape outfit damen, poncho kombinieren, cape mantel herbst, umhang outfit, poncho damen look",
    "layering-regeln": "layering outfit herbst, zwiebellook damen, schichten kombinieren, übergangsoutfit damen, layering look",
    "weihnachtsfeier": "weihnachtsfeier outfit damen, betriebsfeier outfit, festliches outfit weihnachten, weihnachtsfeier look, firmenfeier kleidung",
    "silvester-gold": "silvester outfit gold, silvester kleid damen, goldenes outfit festlich, silvester look damen, neujahr outfit",
    "brosche-tragen": "brosche tragen, brosche am blazer, anstecknadel outfit, brosche kombinieren, schmuck am revers",
    "breiter-guertel": "breiter gürtel kombinieren, taillengürtel outfit, gürtel damen look, taille betonen outfit, gürtel zum kleid",
    "seidentuch-binden": "seidentuch binden, halstuch binden damen, tuch binden anleitung, seidentuch look, schal binden damen",
    "goldschmuck-stapeln": "goldschmuck kombinieren, ketten layering, schmuck stapeln damen, goldketten kombinieren, layering schmuck",
    "weihnachtsmarkt-outfit": "weihnachtsmarkt outfit, winter outfit damen, warm und schick winter, weihnachtsmarkt look, winterlook damen",
    "heiligabend-outfit": "heiligabend outfit, weihnachten outfit damen, festlich zu hause, weihnachtsoutfit familie, feiertagsoutfit damen",
    "silvester-herren": "silvester outfit herren, silvester männer look, festliches outfit männer, herren silvester, neujahr outfit männer",
    "winterhochzeit-gast": "winterhochzeit gast outfit, hochzeit gast dezember, winterhochzeit kleid, hochzeitsgast winter, hochzeit gast warm",
    "weihnachtsfeier-ab-50": "weihnachtsfeier outfit ab 50, festliches outfit ab 50, elegantes outfit ab 50, winteroutfit ab 50, anlass outfit reife damen",
    "mantel-ueber-anlass-outfit": "mantel zum kleid, welcher mantel zum anlasskleid, mantel über kleid, anlassmantel damen, mantel festlich",
    "herbsthochzeit-gast": "herbsthochzeit gast outfit, hochzeitsgast oktober, hochzeit gast kleid herbst, herbsthochzeit look, hochzeitsgast damen herbst",
    "taufe-gast-herbst": "taufe outfit gast, taufe gast damen, taufe kleidung gast, taufe outfit herbst, taufpatin outfit",
    "runder-geburtstag-damen": "runder geburtstag outfit, outfit 50 geburtstag, geburtstagsoutfit damen, festliches outfit geburtstag, 60 geburtstag outfit",
    "vorstellungsgespraech-herbst": "vorstellungsgespräch outfit damen, bewerbungsgespräch kleidung, jobinterview outfit, bewerbung outfit damen, vorstellungsgespräch look",
    "standesamt-winter-braut": "standesamt outfit winter, brautkleid standesamtlich, standesamt braut winter, winterhochzeit braut, standesamtliche trauung kleid",
    "schuhe-strumpfhose-anlasskleid": "schuhe zum anlasskleid, welche strumpfhose zum kleid, strumpfhose farbe kleid, schuhe zum kleid damen, anlasskleid styling",
    "trauerfeier-outfit": "trauerfeier outfit damen, beerdigung outfit, was anziehen beerdigung, trauerkleidung damen, trauerfeier kleidung",
    "weihnachtsfeier-firma-2026": "weihnachtsfeier firma outfit, betriebsfeier outfit damen, firmenfeier kleidung, weihnachtsfeier büro, weihnachtsfeier dresscode",
    "stiefel-zum-anlasskleid": "stiefel zum kleid, kleid mit stiefeln, stiefel anlasskleid, kleid stiefel kombinieren, herbstoutfit kleid stiefel",
    "strickjacke-statt-blazer": "strickjacke statt blazer, grobstrick cardigan outfit, cardigan büro damen, strickjacke kombinieren, cardigan look elegant",
    "weihnachtsfeier-herren-2026": "weihnachtsfeier outfit herren, festliches outfit männer, männer weihnachtsfeier, herren anlass outfit, betriebsfeier männer",
    "samt-outfit-festlich-2026": "samt outfit festlich, samtkleid kombinieren, samt blazer damen, samt look winter, festliches samtoutfit",
    "geschenke-frauen-accessoires": "geschenke für frauen, weihnachtsgeschenke frauen, accessoires geschenk, geschenkideen damen, geschenk freundin",
    "geschenke-maenner-accessoires": "geschenke für männer, weihnachtsgeschenke männer, accessoires herren geschenk, geschenkideen mann, geschenk für ihn",
    "wichtelgeschenke-ideen": "wichtelgeschenke, wichteln büro ideen, secret santa geschenk, wichtelgeschenk kollegen, kleines geschenk büro",
    "festliches-kleid-figur": "festliches kleid figur, kleid passend zur figur, welches kleid passt mir, abendkleid schnitt, kleid schnittform",
    "silvester-outfit-damen": "silvester outfit damen, silvester look, was anziehen silvester, neujahr outfit damen, silvesterparty outfit",
    "adventskaffee-outfit": "adventskaffee outfit, advent outfit damen, festlich und bequem, weihnachtlicher look damen, adventsoutfit",
    "wintertaufe-gast": "wintertaufe outfit, taufe im winter gast, taufe gast winter damen, taufe outfit warm, winter taufe kleidung",
    "ballkleid-ballsaison-2027": "ballkleid 2027, was anziehen ball, ballsaison outfit, abendkleid ball, ball dresscode damen",
}

for _p in POSTS:
    _p["keywords"] = KEYWORDS.get(_p["slug"], "")
del _p


# --------------------------------------------------------------------------
# Neu am 19.09.2026: Dresscode-Erklaerbeitrag.
# Pinterest DE zeigt bei "dresscode festlich" fast nur deutsche Blog-Pins
# (Dresscode-Uebersicht, Dresscode Hochzeit, freundin.de) - unser Format,
# keine Markenmacht dagegen.
POSTS.append({
    "slug": "dresscode-festlich",
    "cat": "hochzeitsgast",
    "title": "Dresscode entschlüsselt: 6 Angaben auf der Einladung",
    "teaser": "Festlich, Cocktail, Black Tie — was davon wirklich gemeint ist und wo die Grenze zum Overdressed verläuft.",
    "img": "post-dresscode.jpg",
    "meta": "Dresscode auf der Einladung verstehen: Was festlich, Cocktail, Black Tie, White Tie, Business und Smart Casual konkret bedeuten — und was man anzieht, wenn gar nichts dabeisteht.",
    "intro": [
        "Auf der Einladung steht ein Wort, und dieses eine Wort entscheidet, ob man am Abend zu den Gästen gehört oder zu den Ausnahmen. Das Unangenehme daran ist nicht die Kleiderordnung selbst — sondern dass niemand erklärt, was sie bedeutet.",
        "Die gute Nachricht: Es sind sechs Angaben, die in Deutschland überhaupt vorkommen. Alles andere sind Varianten davon. Wer die sechs kennt, liest jede Einladung richtig.",
    ],
    "sections": [
        ("Der Dresscode nennt die Untergrenze, nicht die Obergrenze", [
            "Ein Dresscode sagt, wie festlich man mindestens sein muss. Er sagt nicht, wie festlich man höchstens sein darf. Diese Obergrenze steht woanders: in der Uhrzeit und im Ort.",
            "Deshalb funktioniert die einfachste Faustregel besser als jede Tabelle. Je später der Termin, desto festlicher. Was um 20 Uhr im Schlosssaal richtig ist, wirkt um 11 Uhr im Standesamt wie ein Kostümfest. Bodenlang vor 18 Uhr ist fast immer zu viel — außer die Einladung sagt ausdrücklich Black Tie.",
        ]),
        ("Festlich — die häufigste und die vageste Angabe", [
            "„Festlich\" ist der deutsche Sammelbegriff und meint: bitte kein Alltag. Keine Jeans, keine Sneaker, keine Funktionsjacke. Was es nicht meint: Abendgarderobe. Bodenlang ist nicht verlangt, und ein Smoking wäre zu viel.",
            "Für Damen heißt das ein Kleid oder ein Rock in Knie- bis Wadenlänge, gern in einem Stoff mit etwas Gewicht — Krepp, Satin, Samt. Für Herren ein Anzug, Krawatte nach Anlass. Wer unsicher ist, geht eine halbe Stufe höher als die anderen und nimmt ein Teil mit, das sich ablegen lässt: ein Sakko, eine Stola. Dann lässt sich nach oben und unten korrigieren.",
        ]),
        ("Cocktail — knielang bis wadenlang, nie bodenlang", [
            "Cocktail ist präziser als festlich und eine Stufe darüber. Für Damen: knielang bis wadenlang, feinere Stoffe, mehr Schmuck erlaubt. Bodenlang gehört ausdrücklich nicht dazu — das ist der Unterschied zu Black Tie.",
            "Für Herren bedeutet Cocktail den dunklen Anzug mit Krawatte. Braun und Hellgrau sind hier fehl am Platz, Marine und Anthrazit richtig.",
        ]),
        ("Black Tie — Smoking, und was das für Damen heißt", [
            "Black Tie ist die einzige Angabe, die für Herren eindeutig ist: Smoking, schwarze Fliege, keine Krawatte. Wer keinen besitzt, leiht einen — ein dunkler Anzug ist nicht dasselbe, auch wenn er oft durchgeht.",
            "Für Damen ist Black Tie weniger streng, als viele denken. Bodenlang ist die klassische Antwort, aber ein sehr feines wadenlanges Kleid in Seide oder Samt ist ebenso richtig. Entscheidend sind Stoff und Verarbeitung, nicht die Länge allein.",
        ]),
        ("White Tie — fast nur beim Ball", [
            "White Tie bedeutet Frack für Herren und bodenlange Robe für Damen. In Deutschland begegnet man dem praktisch nur bei klassischen Bällen und Staatsempfängen. Steht es auf einer privaten Einladung, ist es meistens ein Irrtum — dann lohnt eine Rückfrage beim Gastgeber, bevor man einen Frack leiht.",
        ]),
        ("Business und Business Casual — der Firmenfall", [
            "Bei Firmenfeiern steht oft Business oder Business Casual auf der Einladung. Business heißt: das, was man im Büro trägt, in der gepflegten Variante — Anzug, Kostüm, Hosenanzug. Business Casual streicht die Krawatte und erlaubt Strickjacke statt Blazer.",
            "Der Fehler, den fast alle machen: Business Casual mit Freizeit zu verwechseln. Es bleibt eine Arbeitsveranstaltung mit Kollegen und Vorgesetzten. Was man am Samstag beim Einkaufen trägt, ist hier zu wenig.",
        ]),
        ("Smart Casual — die Falle", [
            "Smart Casual klingt entspannt und ist die schwierigste Angabe von allen, weil sie je nach Gastgeber etwas anderes bedeutet. Der gemeinsame Nenner: gepflegt, aber nicht steif. Eine dunkle Jeans ist erlaubt, wenn sie gut sitzt und ein Blazer oder eine schöne Bluse dazukommt.",
            "Was nicht funktioniert: Sportschuhe mit sichtbarer Sohlentechnik, T-Shirts mit Aufdruck, alles Ausgewaschene. Im Zweifel ein Teil mehr anziehen, nicht eines weniger.",
        ]),
        ("Wenn gar nichts dabeisteht", [
            "Das ist der häufigste Fall, und er ist der einfachste. Steht kein Dresscode auf der Einladung, ist der Ort die Antwort. Restaurant am Abend: festlich. Garten am Nachmittag: gepflegt und bequem, aber mit einer Schicht, die es abends wärmer macht. Standesamt am Vormittag: elegant, nicht abendlich.",
            "Und wer es genau wissen will, fragt. Eine kurze Nachricht an die Gastgeber ist keine Blöße — sie ist für die Gastgeber angenehmer als ein Gast, der sich den ganzen Abend falsch angezogen fühlt.",
        ]),
    ],
    "products": [
        ("Einfarbiges Midikleid", "Deckt festlich und Cocktail zugleich ab. Einfarbig, Knie- bis Wadenlänge — das Teil, das drei Dresscodes gleichzeitig bedient.", "midikleid damen elegant"),
        ("Kleine Abendtasche", "Ab Cocktail aufwärts ist die Alltagstasche zu groß. Eine kleine Tasche macht denselben Look eine Stufe festlicher.", "B0B4J3WGWR"),
        ("Pumps mit Blockabsatz", "Der Absatz, der einen ganzen Abend hält. Für alles von festlich bis Black Tie tragbar.", "B0C6YJWY8R"),
        ("Stola oder großes Tuch", "Die Schicht, mit der sich nach oben und unten korrigieren lässt — und die Antwort auf jeden zugigen Saal.", "stola damen abendkleid"),
        ("Schlichte Ohrringe", "Bei Black Tie dürfen sie größer sein, bei Business kleiner. Ein schlichtes Paar funktioniert überall.", "B0D9RT25LN"),
        ("Brosche mit Steinbesatz", "Das Stück, das ein schlichtes Kleid ohne Umziehen festlich macht. Passt ans Revers, an den Gürtel, an die Tasche.", "B08MF2NR3K"),
    ],
    "pintitle": "Dresscode Hochzeit: 6 Angaben erklärt",
    "pintitle_c": "Was heißt festlich? Dresscode verstehen",
    "keywords": "dresscode hochzeit, was heißt festlich, dresscode festlich, cocktail dresscode, black tie damen",
})

PINTITEL["dresscode-festlich"] = "Dresscode Hochzeit: 6 Angaben erklärt"
PINTITEL_C["dresscode-festlich"] = "Was heißt festlich? Dresscode verstehen"
KEYWORDS["dresscode-festlich"] = "dresscode hochzeit, was heißt festlich, dresscode festlich, cocktail dresscode, black tie damen"


# --------------------------------------------------------------------------
# Neu am 24.09.2026: Adventskalender.
# Pinterest DE zeigt bei "adventskalender fuellen erwachsene" fast nur
# Mega-Listen ("444 Fuellideen", "200+", "75+"). Gegen groessere Zahlen
# gewinnen wir nicht - also der Gegenentwurf: wenige Teile, die zusammen
# etwas ergeben.
POSTS.append({
    "slug": "adventskalender-fuellen",
    "cat": "accessoires",
    "title": "Adventskalender füllen: 6 Accessoires statt 24 Kleinigkeiten",
    "teaser": "Vierundzwanzig Türchen, aber nur sechs Dinge kaufen — und am 24. liegt etwas Ganzes da.",
    "img": "post-adventskalender.jpg",
    "meta": "Adventskalender für Erwachsene füllen: sechs Accessoires, die sich auf 24 Türchen aufteilen lassen und am Ende zusammen ein Ganzes ergeben — statt 24 zusammengewürfelter Kleinigkeiten.",
    "intro": [
        "Die Suche nach Füllideen führt zuverlässig zu Listen mit zweihundert, vierhundert, manchmal tausend Vorschlägen. Man arbeitet sie ab, kauft vierundzwanzig kleine Dinge, und am Ende hat der Beschenkte vierundzwanzig kleine Dinge, von denen er drei behält.",
        "Es geht auch andersherum: wenige Sachen kaufen, die zusammengehören, und sie auf die Türchen verteilen. Der Kalender erzählt dann etwas, und am 24. liegt kein weiteres Teelicht da, sondern das Stück, auf das alles hinauslief.",
    ],
    "sections": [
        ("Die Regel: ein Thema, sechs Teile, vierundzwanzig Türchen", [
            "Man braucht keine vierundzwanzig Einkäufe für vierundzwanzig Türchen. Man braucht ein Thema — hier: Accessoires, die getragen werden — und sechs bis acht Dinge, von denen sich mehrere aufteilen lassen.",
            "Der Rest sind Türchen, die nichts kosten: eine Karte mit einem Satz, ein Gutschein über einen gemeinsamen Nachmittag, ein Foto. Diese Türchen sind oft die, an die man sich später erinnert.",
        ]),
        ("Was sich aufteilen lässt", [
            "Sets sind der Trick. Ein Armband-Set mit fünf Teilen füllt fünf Türchen und ergibt am Ende trotzdem einen Look, nicht fünf Einzelteile. Dasselbe gilt für Socken im Mehrerpack oder ein Set aus mehreren kleinen Tüchern.",
            "Wichtig ist nur, dass die Teile zusammenpassen — gleiche Metallfarbe, gleiche Machart. Sonst hat man wieder vierundzwanzig Kleinigkeiten, nur teurer eingekauft.",
        ]),
        ("Das Stück für den 24.", [
            "Ein Kalender braucht ein Ende, sonst hört er einfach auf. Das letzte Türchen bekommt das Stück, das die anderen zusammenhält: ein Seidentuch, eine Brosche, etwas, das man sehen kann.",
            "Es muss nicht das teuerste sein. Es muss das sein, mit dem die vorherigen Türchen im Nachhinein Sinn ergeben.",
        ]),
        ("Was besser nicht hineinkommt", [
            "Kleidung in Größen. Ein Pullover im falschen Schnitt ist ein Umtausch mit Ansage, und der Moment am Türchen ist dahin. Accessoires haben dieses Problem nicht — Tuch, Brosche, Haarspange passen jedem.",
            "Und Essbares nur, wenn es bis Weihnachten hält. Schokolade im geheizten Zimmer über drei Wochen ist keine gute Idee, selbstgebackene Plätzchen aus der ersten Dezemberwoche erst recht nicht.",
        ]),
        ("Wenn man selbst befüllt wird", [
            "Der Kalender für sich selbst ist keine schlechte Idee, und er funktioniert nach derselben Regel: nicht vierundzwanzig Impulskäufe, sondern eine Handvoll Dinge, die man sich sonst nicht kauft, verteilt über den Monat.",
            "Der Unterschied ist nur, dass man beim Packen schon weiß, was drin ist. Das nimmt weniger, als man denkt — die Vorfreude hängt am Datum, nicht an der Überraschung.",
        ]),
    ],
    "products": [
        ("Seidentuch 53 × 53 cm", "Das Stück für das letzte Türchen. Passt jedem, funktioniert an vier Stellen und braucht keine Größenangabe.", "B0BX963Q6V"),
        ("Armband-Set aus mehreren Teilen", "Der eigentliche Trick: ein Kauf, drei bis fünf Türchen — und am Ende trotzdem ein zusammengehörender Look.", "B0CRZDMLPX"),
        ("Haarspange in Gold", "Klein genug fürs Türchen, sichtbar genug, dass sie getragen wird. Eine der wenigen Kleinigkeiten ohne Größenproblem.", "B0CRZRM3LP"),
        ("Schlichte Ohrringe", "In ihrer Metallfarbe kaufen, nicht in der eigenen. Dann passen sie zu allem, was schon im Schmuckkästchen liegt.", "B0D9RT25LN"),
        ("Brosche mit Steinbesatz", "Das Teil, das ein schlichtes Kleid ohne Umziehen festlich macht — und das ihr sonst niemand schenkt.", "B08MF2NR3K"),
        ("Merinosocken im Mehrerpack", "Klingt nach Verlegenheit, wird aber den ganzen Winter getragen. Und der Mehrerpack füllt gleich mehrere Türchen.", "B0DHCNW3HG"),
    ],
    "pintitle": "Adventskalender füllen: 6 Ideen für Erwachsene",
    "pintitle_c": "Was in den Adventskalender für Frauen?",
    "keywords": "adventskalender füllen, adventskalender erwachsene, füllideen adventskalender, adventskalender für frauen, adventskalender ideen",
})

PINTITEL["adventskalender-fuellen"] = "Adventskalender füllen: 6 Ideen für Erwachsene"
PINTITEL_C["adventskalender-fuellen"] = "Was in den Adventskalender für Frauen?"
KEYWORDS["adventskalender-fuellen"] = "adventskalender füllen, adventskalender erwachsene, füllideen adventskalender, adventskalender für frauen, adventskalender ideen"
