# CLAUDE.md - Silvesterfeier Anmeldungswebsite

## Projekt-Übersicht

Anmeldungswebsite für die Silvesterfeier 2025 der Lübecker Freimaurer. Ermöglicht Mitgliedern die Anmeldung mit Begleitung, Buffet-Beiträgen und Helfer-Einteilung.

**Zielgruppe:** Freimaurer-Logen in Lübeck und deren Gäste
**Event:** Silvesterfeier 2025 im Logenhaus Lübeck

## Architektur

```
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│   Frontend (Browser)    │────▶│  nginx Reverse-Proxy    │────▶│   n8n Webhooks          │
│  sommerfest.frankrath.de│     │  /api/silvester         │     │  automatisierung.       │
│  silvester.freimaurer-  │     │  Coolify Deployment     │     │  frankrath.de           │
│  hl.de                  │     │                         │     │                         │
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
```

### Technologie-Stack

- **Frontend:** Statisches HTML/CSS/JavaScript (kein Build-System)
- **Backend:** n8n Workflows mit Webhooks
- **Deployment:** Coolify mit Docker (nginx:alpine)
- **Datenspeicherung:** Via n8n (externe Datenbank/Sheets)

## Wichtige Dateien

| Datei | Beschreibung |
|-------|--------------|
| `index.html` | **Hauptanmeldeformular** - Persönliche Daten, Begleitung, Buffet-Beiträge, Getränke-Präferenzen |
| `helfer.html` | **Helfer-Abfrage** - Aufbau-/Abbau-Bereitschaft, Bemerkungen |
| `abschluss.html` | **Bestätigungsseite** - Zusammenfassung aller Anmeldedaten |
| `admin.html` | **Dashboard** - Teilnehmer-Übersicht, Statistiken, E-Mail-Versand, Exports |
| `nginx.conf` | nginx-Konfiguration mit CORS-Proxy für n8n |
| `Dockerfile` | Docker-Build für Coolify-Deployment |

### Anmeldefluss

```
index.html ──▶ helfer.html ──▶ abschluss.html
    │               │               │
    ▼               ▼               ▼
 Daten sammeln   Helfer-Info     Bestätigung
 (Buffet, Gäste) erfragen        + E-Mail
```

## n8n Webhook-Endpunkte

**WICHTIG:** Diese Endpunkte nicht ändern - sie sind im n8n-Workflow konfiguriert!

| Webhook | Methode | Beschreibung |
|---------|---------|--------------|
| `/webhook/silvester-anmeldung` | POST | Speichert Anmeldung |
| `/webhook/silvester-get-participants` | GET | Lädt Teilnehmerliste |
| `/webhook/silvester-get-preferences` | GET | Lädt Präferenzen-Statistik |
| `/webhook/silvester-buffet-uebersicht` | GET | Lädt Buffet-Übersicht |
| `/webhook/silvester-helfer-statistik` | GET | Lädt Helfer-Zahlen |
| `/webhook/silvester-orga-login` | GET | Dashboard-Login |
| `/webhook/silvester-send-smart-reminder` | POST | Versendet Erinnerungs-E-Mails |

**Base-URL:** `https://automatisierung.frankrath.de`

## WICHTIG - Regeln für Änderungen

### API-Endpunkte NICHT ändern
- Die Webhook-URLs sind fest in n8n konfiguriert
- Feldnamen in den POST-Requests müssen mit n8n übereinstimmen

### Datenformat beachten
- `buffet`: JSON-Array mit `{item, quantity}` Objekten
- `grillbuffet_praeferenzen`: JSON-Array von Strings
- `getraenke_praeferenzen`: JSON-Array von Strings
- `personen`: Gesamtzahl inkl. Anmelder (1 + Anzahl Gäste)

### CORS-Handling
- Frontend sendet direkt an n8n (nicht über nginx-Proxy)
- POST-Requests nutzen `application/x-www-form-urlencoded` um Preflight zu vermeiden

### Bekannte Eigenheiten
- Dashboard (`admin.html`) ist öffentlich zugänglich (kein Login mehr)
- Konfetti-Animation kann auf schwachen Geräten Performance-Probleme verursachen
- Buffet-Validierung ist optional (freiwillige Beiträge)
- Getränke-Auswahl ist Pflicht für Anmeldung

## Hilfsdateien (können gelöscht werden)

Diese Dateien sind Entwicklungs-Artefakte und nicht für Production relevant:

```
# Python-Skripte (einmalige Fixes)
fix_structure_final.py
fix_tab_structure.py
clean_structure.py

# JavaScript-Patches (bereits integriert)
admin_new_billing_export.js
apply_guest_fix.js
guest_calculation_fix.js
get_request_fix.js
temp_script.js
temp_originaldata.js

# Debug-Seite
helfer-debug.html
```

## Backup-Dateien (zur Löschung empfohlen)

Das Repository enthält **über 70 Backup-Dateien**, die gelöscht werden sollten:

### admin.html Backups (38 Dateien)
- `admin.html.backup*` - diverse Backup-Versionen

### index.html Backups (21 Dateien)
- `index.html.backup*` - diverse Backup-Versionen

### helfer.html Backups (7 Dateien)
- `helfer.html.backup*`
- `helfer_backup_*.html`

### abschluss.html Backups (2 Dateien)
- `abschluss.html.backup`
- `abschluss.html.backup4`

### admin.html Sonderdatei
- `admin.html.before_email` - kann gelöscht werden

**Empfohlener Löschbefehl:**
```bash
# Alle Backup-Dateien löschen
rm -f *.backup* *.backup-* *.before_* helfer_backup_*.html
```

## Deployment

### Lokale Entwicklung
```bash
# Einfacher HTTP-Server
python3 -m http.server 8000
# oder
npx serve .
```

### Production (Coolify)
1. Repository als Quelle in Coolify konfigurieren
2. Dockerfile wird automatisch erkannt
3. nginx-Konfiguration wird über `nginx.conf` eingebunden
4. Port 80 wird exponiert

## Styling-Konventionen

- **Primärfarbe:** `#d4af37` (Gold)
- **Sekundär:** `#1a1a1a` (Schwarz)
- **Akzent:** `#a0c4ff` (Hellblau)
- **Schriftart:** Georgia (Serif)
- CSS ist inline in den HTML-Dateien (kein separates Stylesheet für Hauptseiten)

## Kontakt

- **E-Mail:** silvester@freimaurer-hl.de
- **Event:** 31. Dezember 2025, Logenhaus Lübeck

---

*Letzte Aktualisierung: November 2025*
