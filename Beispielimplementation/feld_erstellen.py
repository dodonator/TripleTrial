#!/usr/bin/env python3

print("Triple Triad")
print("Feld erstellen")

# Das Feld wird als dreidimensionale Liste erstellt:
board = []
for column in range(3):
    board.append([])
    for row in range(3):
        board[column].append([])

# Feld ausgeben
for column in board:
    print(column)
