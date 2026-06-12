def transpose_matriks(matriks):
    baris = len(matriks)
    kolom = len(matriks)

    hasil = [[0, 0, 0], 
             [0, 0, 0], 
             [0, 0, 0]]
    
    for i in range(baris):
        for j in range(kolom):
            hasil[j][i] = matriks[i][j]

    return hasil


def penjumlahan_matriks(matriks1, matriks2):
    hasil = [[0, 0, 0], 
             [0, 0, 0], 
             [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
                hasil[i][j] = matriks1[i][j] + matriks2[i][j]
    
    return hasil


def perkalian_matriks(matriks1, matriks2):
    hasil = [[0, 0, 0], 
             [0, 0, 0], 
             [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
           for k in range(3):
                hasil[i][j] += matriks1[i][k] * matriks2[k][j]

    return hasil


def determinan_sarrus(matriks):
    diag_kanan1 = matriks[0][0] * matriks[1][1] * matriks[2][2]
    diag_kanan2 = matriks[0][1] * matriks[1][2] * matriks[2][0]
    diag_kanan3 = matriks[0][2] * matriks[1][0] * matriks[2][1]
    
    total_positif = diag_kanan1 + diag_kanan2 + diag_kanan3

    diag_kiri1 = matriks[2][0] * matriks[1][1] * matriks[0][2]
    diag_kiri2 = matriks[2][1] * matriks[1][2] * matriks[0][0]
    diag_kiri3 = matriks[2][2] * matriks[1][0] * matriks[0][1]
    
    total_negatif = diag_kiri1 + diag_kiri2 + diag_kiri3

    return total_positif - total_negatif


  
