#!/usr/bin/env python3

print("Triple Triad")
print("Karte wählen")

# Die vier Werte der ersten Karte werden der Reihe nach eingegeben:
print("Bitte die vier Werte (1-10) der ersten Karte eingeben: ")
up1 = input("Oben: ")
down1 = input("Unten: ")
left1 = input("Links: ")
right1 = input("Rechts: ")

print()

# Die vier Werte der zweiten Karte werden der Reihe nach eingegeben:
print("Bitte die vier Werte (1-10) der zweiten Karte eingeben: ")
up2 = input("Oben: ")
down2 = input("Unten: ")
left2 = input("Links: ")
right2 = input("Rechts: ")

# Auswahl der Karte
answer = input("Bitte eine der Karten der auswählen (1 oder 2): ")
if answer == "1":
    # Die Werte werden auf die Werte der ersten Karte gesetzt
    up = up1
    down = down1
    left = left1
    right = right1
    print("Erste Karte: ")

elif answer == "2":
    # Die Werte werden auf die Werte der zweiten Karte gesetzt
    up = up2
    down = down2
    left = left2
    right = right2
    print("Zweite Karte: ")

else:
    print("Ungültige Antwort")
    print("Damit kein Fehler auftritt wird die erste Karte ausgegeben")
    print()
    answer = "1"
    up = up1
    down = down1
    left = left1
    right = right1

# Die Ausgabe der Karten geschieht, wie bekannt, jedoch wird in der Mitte die
# Nummer der Karte angezeigt:
width = 9

s_u = width // 2 - len(up) + 1
s_l = width // 2 - len(left)
s_r = width // 2 - len(right)
s_d = width // 2 - len(down) + 1

print()  # Leerzeile
print("+" + width*"-" + "+")  # Kopfzeile
print("|" + s_u*" " + up + (width//2)*" " + "|")
print("|" + width*" " + "|")  # "leere" Zeile
print("|" + left + s_l*" " + answer + " "*s_r + right + "|")
print("|" + width*" " + "|")  # "leere" Zeile
print("|" + s_d*" " + down + (width//2)*" " + "|")
print("+" + width*"-" + "+")  # FußZeilen
print()  # Leerzeile
