{
    'name': 'Kundennummer Management',
    'version': '1.1',
    'summary': 'Automatische Generierung von Kundennummern und Lieferantennummern für Unternehmen.',
    'description': '''
Dieses Modul ermöglicht die automatische Generierung von Kundennummern und Lieferantennummern für Unternehmen. 
Zusätzlich bietet es die Möglichkeit, zu entscheiden, ob die Daten bei Deinstallation gelöscht werden sollen.
    ''',
    'author': 'Innos',
    'website': 'https://innos.systems/',  # Optional: füge eine Website hinzu, falls gewünscht.
    'category': 'Custom',
    'depends': ['base'],
    #'data': [
    #    'views/res_partner_views.xml',  # Hier wird die View-XML-Datei hinzugefügt.
    #],
    'installable': True,
    'auto_install': False,
    'application': False,
    'post_init_hook': None,  # Optional: Falls keine spezielle Initialisierung benötigt wird.
}