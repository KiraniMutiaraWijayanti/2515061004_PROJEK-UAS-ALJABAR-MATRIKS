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

