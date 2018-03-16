#!/usr/bin/env python3

print("Triple Triad")
print("Karte erstellen")

# Die vier Werte der Karte werden der Reihe nach eingegeben:
up = input("Bitte den Wert (1-10) für die obere Seite eingeben: ")
down = input("Bitte den Wert (1-10) für die untere Seite eingeben: ")
left = input("Bitte den Wert (1-10) für die linke Seite eingeben: ")
right = input("Bitte den Wert (1-10) für die rechte Seite eingeben: ")

# Die Breite einer Kartendarstellung
width = 9

# Die Anzahl an Leerzeichen in den jeweiligen Zeilen
s_u = width // 2 - len(up) + 1  # s_u entspricht "spaces up"
s_lr = width - (len(left) + len(right))  # s_lr entspricht "space left/right"
s_d = width // 2 - len(down) + 1  # s_d entspricht "spaces down"

# Das Ausdrucken der einzelnen Zeilen
print("+" + width*"-" + "+")  # Kopfzeile
print("|" + s_u*" " + up + (width//2)*" " + "|")
print("|" + width*" " + "|")  # "leere" Zeile
print("|" + left + s_lr*" " + right + "|")
print("|" + width*" " + "|")  # "leere" Zeile
print("|" + s_d*" " + down + (width//2)*" " + "|")
print("+" + width*"-" + "+") # FußZeilen
print()  # Leerzeile
