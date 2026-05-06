#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 12 - Graph II: Shortest Path 
#===================================================================================

#===================================================================================
# Latihan 1 : Weighted Graph dan Perhitungan Jalur 
#===================================================================================

# Representasi weighted graph menggunakan dictionary bersarang 
# Setiap node memiliki tetangga beserta bobot (jarak) ke node tersebut
graph = { 
    'A': {'B': 4, 'C': 2}, # Dari A ke B jaraknya 4, ke C jaraknya 2
    'B': {'D': 5}, # Dari B ke D jaraknya 5
    'C': {'D': 1}, # Dari C ke D jaraknya 1
    'D': {} # D tidak punya tetangga (node akhir)
} 

# Menghitung dua kemungkinan jalur dari A ke D

# Jalur 1: A -> B -> D
# Total jarak = A ke B + B ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] 

# Jalur 2: A -> C -> D
# Total jarak = A ke C + C ke D
jalur_2 = graph['A']['C'] + graph['C']['D']

# Menampilkan hasil perhitungan masing-masing jalur
print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 

#===================================================================================
# Jawaban Analisis : 
# 1. Total bobot jalur A → B → D adalah 4 + 5 = 9.
# 2. Total bobot jalur A → C → D adalah 2 + 1 = 3.
# 3. Jalur terpendek adalah A → C → D karena memiliki total bobot paling kecil.
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge paling sedikit karena yang dihitung adalah total bobot (jarak),
# bukan banyaknya langkah. Bisa saja jalurnya lebih panjang tapi bobotnya lebih kecil.
#===================================================================================