#!/usr/bin/env python3

print("Triple Triad")
print("Karte erstellen")

up = input("Bitte den Wert (1-10) für die obere Seite eingeben: ")
down = input("Bitte den Wert (1-10) für die untere Seite eingeben: ")
left = input("Bitte den Wert (1-10) für die linke Seite eingeben: ")
right = input("Bitte den Wert (1-10) für die rechte Seite eingeben: ")

width = 9

s_u = width // 2 - len(up) + 1
s_lr = width - (len(left) + len(right))
s_d = width // 2 - len(down) + 1

print("+" + width*"-" + "+")
print("|" + s_u*" " + up + (width//2)*" " + "|")
print("|" + width*" " + "|")
print("|" + left + s_lr*" " + right + "|")
print("|" + width*" " + "|")
print("|" + s_d*" " + down + (width//2)*" " + "|")
print("+" + width*"-" + "+")
