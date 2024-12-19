# Odoo 18 - Custom Kundennummer Modul

Dieses Modul fügt Odoo 18 die Funktionalität hinzu, beim Anlegen oder Speichern eines Unternehmens (Kunde oder Lieferant) automatisch eine Kundennummer sowie eine Lieferantennummer zu generieren. 

## Voraussetzungen

**Bevor das Modul installiert wird, müssen folgende Vorbereitungen manuell durchgeführt werden:**

1. **Erstellen der Sequenzen**:
   - Navigieren Sie zu `Einstellungen > Technisch > Sequenzen`.
   - Erstellen Sie zwei neue Sequenzen mit den folgenden IDs:
     - `res.partner.kundennummer.id`
     - `res.partner.lieferantennummer.id`

2. **Erstellen der benutzerdefinierten Felder mit dem Odoo Studio**:
   - Navigieren Sie in Odoo Studio zum `res.partner`-Modell (Kontakte).
   - Erstellen Sie zwei neue Felder:
     - `x_studio_kundennummer` (Typ: Zeichenkette/Text)
     - `x_studio_lieferantennummer` (Typ: Zeichenkette/Text)

## Installation

1. Klonen Sie dieses Repository in Ihr Odoo-Addons-Verzeichnis:
   ```bash
   git clone https://github.com/innossystems/odoo_custom_kundennummer.git custom_kundennummer
