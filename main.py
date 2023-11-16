def place_item(conveyor, item):
    conveyor[0] = item

# Variable für das Förderband mit zehn Einheiten. Der Einheitentyp wird als String gespeichert. Leere Förderplätze
# werden über einen leeren String gekennzeichnet. Zu Begin ist das ganze Förderband leer.
conveyor_band = [""] * 10