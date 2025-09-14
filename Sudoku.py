

# Fonction pour vérifier si un chiffre est valide à une position donnée
def est_valide(grille, ligne, col, num):
    # Vérifie la ligne et la colonne
    for i in range(9):
        if grille[ligne][i] == num or grille[i][col] == num:
            return False

    # Vérifie le carré 3x3
    start_ligne = 3 * (ligne // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grille[start_ligne + i][start_col + j] == num:
                return False

    return True

# Fonction principale de résolution avec backtracking
def resoudre_sudoku(grille):
    for ligne in range(9):
        for col in range(9):
            if grille[ligne][col] == 0:
                for num in range(1, 10):
                    if est_valide(grille, ligne, col, num):
                        grille[ligne][col] = num
                        if resoudre_sudoku(grille):
                            return True
                        grille[ligne][col] = 0  # backtrack
                return False
    return True

# Fonction d'affichage de la grille
def afficher_grille(grille):
    for i in range(9):
        ligne = ""
        for j in range(9):
            val = grille[i][j]
            ligne += str(val) if val != 0 else "."
            ligne += " "
            if (j + 1) % 3 == 0 and j != 8:
                ligne += "| "
        print(ligne)
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)

# Exemple de grille à résoudre
grille_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("🧩 Grille initiale :\n")
afficher_grille(grille_sudoku)

if resoudre_sudoku(grille_sudoku):
    print("\n✅ Grille résolue :\n")
    afficher_grille(grille_sudoku)
else:
    print("❌ Aucune solution trouvée.")