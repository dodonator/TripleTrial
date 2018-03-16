#!/usr/bin/env python3

print("Triple Triad")
print("Karten vergleichen")

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
print()

# Die Werte werden in Integer umgewandelt:
up1 = int(up1)
down1 = int(down1)
left1 = int(left1)
right1 = int(right1)

up2 = int(up2)
down2 = int(down2)
left2 = int(left2)
right2 = int(right2)

# Die bessere Karte wird als Integer gespeichert
winner = 0

# Die Werte der beiden Karten vergleichen:
# Um zu vergleichen welche Karte besser ist, werden die Werte miteinander
# verglichen.
score_1 = up1 + down1 + left1 + right1
score_2 = up2 + down2 + left2 + right2

if score_1 > score_2:
    winner = 1
    up = str(up1)
    down = str(down1)
    left = str(left1)
    right = str(right1)
    number = 1

elif score_2 > score_1:
    winner = 2
    up = str(up2)
    down = str(down2)
    left = str(left2)
    right = str(right2)
    number = 2

if winner == 0:
    print("Die Karten sind gleich gut.")

else:
    print("Karte " + str(winner) + " war die bessere.")

    # Die Ausgabe der Karten geschieht, wie bekannt:
    width = 9

    s_u = width // 2 - len(up) + 1
    s_l = width // 2 - len(left)
    s_r = width // 2 - len(right)
    s_d = width // 2 - len(down) + 1

    print()  # Leerzeile
    print("+" + width*"-" + "+")  # Kopfzeile
    print("|" + s_u*" " + up + (width//2)*" " + "|")
    print("|" + width*" " + "|")  # "leere" Zeile
    print("|" + left + s_l*" " + str(number) + " "*s_r + right + "|")
    print("|" + width*" " + "|")  # "leere" Zeile
    print("|" + s_d*" " + down + (width//2)*" " + "|")
    print("+" + width*"-" + "+")  # FußZeilen
    print()  # Leerzeile
