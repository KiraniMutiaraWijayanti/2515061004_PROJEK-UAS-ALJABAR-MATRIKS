**Modul**

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


**Program Utama**

import kirani004

A = [[1, 2, 3],
     [4, 5, 6], 
     [7, 8, 9]

]

B = [
    [0, 1, 1],
    [2, 0, 2],
    [3, 3, 0]
]

print("Uji Modul")

hasil_tambah = kirani004.penjumlahan_matriks(A, B)
print("hasil penjumlahan matriks A + B:")
for baris in hasil_tambah:
    print(baris)


hasil_transpose = kirani004.transpose_matriks(A)
print("hasil transpose matriks A:")
for baris in hasil_transpose:
    print(baris)


hasil_perkalian = kirani004.perkalian_matriks(A, B)
print("hasil perkalian matriks A * B")
for baris in hasil_perkalian:
    print(baris)


det_A = kirani004.determinan_sarrus(A)
det_B = kirani004.determinan_sarrus(B)

print("hasil determinan matriks A:", det_A)
print("hasil determinan matriks B:", det_B)



  
