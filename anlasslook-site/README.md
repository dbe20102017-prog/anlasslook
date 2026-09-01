# anlasslook.de

Quelltext der Website [anlasslook.de](https://anlasslook.de) — Anlass-Outfits und Accessoires.
Statische Seite, gebaut mit Python, veröffentlicht über GitHub Pages.

## Aufbau

| Datei | Inhalt |
|---|---|
| `content.py` | alle Texte: `SITE`, `CATEGORIES`, `POSTS`, `PINTITEL` |
| `build.py` | erzeugt die Website nach `dist/` |
| `makepins.py` | erzeugt die Pinterest-Grafiken, drei Varianten je Beitrag |
| `img/` | Beitrags- und Kategoriebilder, je 1500 px breit |

## Bauen

```
pip install -r requirements.txt
python3 build.py      # löscht dist/ und baut neu
python3 makepins.py   # erzeugt dist/assets/pins/
```

**Die Reihenfolge ist zwingend** — `build.py` leert `dist/` vollständig.

Liegt `dist/` in einem Ordner ohne Löschrecht, den Zielordner umlenken:

```
export ANLASSLOOK_DIST="$HOME/build/dist"
```

Fehlen die Schriften Lora und Poppins im System, ihre Pfade übergeben:

```
export ANLASSLOOK_SERIF=fonts/Lora-Variable.ttf
export ANLASSLOOK_SANS=fonts/Poppins-Medium.ttf
```

## Veröffentlichen

Ein Push auf `main` startet den Workflow: bauen, prüfen, auf GitHub Pages veröffentlichen.
Die Prüfliste bricht ab, wenn ein Amazon-Link die Tracking-ID verliert, `og:type` fehlt,
der Feed nicht genau sechs Einträge hat oder zwei Pin-Grafiken bytegleich sind.

## Regeln

- Jeder Beitrag braucht ein eigenes Bild — die Skripte brechen sonst ab
- Jeder Beitrag braucht einen Eintrag in `PINTITEL`: der Pin-Titel ist ein Suchbegriff,
  nicht der Website-Titel
- Keine Amazon-Produktfotos, keine Preise
- Werbekennzeichnung über jedem Beitrag, `rel="sponsored nofollow noopener"` an jedem Link
- Der RSS-Feed bleibt auf sechs Einträge begrenzt
