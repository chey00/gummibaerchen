# Durch die Funktion place_item werden Packungen auf den Beginn des Förderbands gelegt. Der Inhalt der Packung wird
# durch einen String definiert.
def place_item(conveyor, item):
    # Der erste Speicherplatz des Förderbands (Index 0) wird als Anfang des Förderbandes definiert
    conveyor[0] = item

# Variable für das Förderband mit zehn Einheiten. Der Einheitentyp wird als String gespeichert. Leere Förderplätze
# werden über einen leeren String gekennzeichnet. Zu Begin ist das ganze Förderband leer.
conveyor_band = [""] * 10