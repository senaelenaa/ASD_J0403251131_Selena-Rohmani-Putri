#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
#===================================================================================

#===================================================================================
# Latihan 1 : Memahami Konsep Spanning Tree
#===================================================================================

# Daftar edge pada graph awal yang mengandung cycle
# Setiap tuple menunjukkan hubungan antar node
edges = [
    ('A', 'B'), # Edge antara A dan B
    ('A', 'C'), # Edge antara A dan C
    ('A', 'D'), # Edge antara A dan D
    ('C', 'D'), # Edge antara C dan D
    ('B', 'D') # Edge antara B dan D
]

# Contoh spanning tree yang menghubungkan semua node tanpa cycle
# Edge dipilih secukupnya agar semua node tetap terhubung
spanning_tree = [
    ('A', 'C'), # Menghubungkan A ke C
    ('C', 'D'), # Menghubungkan C ke D
    ('D', 'B') # Menghubungkan D ke B
]

# Menampilkan daftar seluruh edge pada graph
print("Edge pada graph:")

# Perulangan untuk menampilkan setiap edge
for edge in edges:
    print(edge)

# Menampilkan edge yang dipilih untuk membentuk spanning tree
print("\nSpanning Tree:")

# Perulangan untuk menampilkan edge pada spanning tree
for edge in spanning_tree:
    print(edge)

# Menampilkan perbandingan jumlah edge antara graph awal dan spanning tree
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

#===================================================================================
# Jawaban Analisis :
# 1. Perbedaan utamanya adalah graph awal memiliki cycle (siklus) dan jumlah edge lebih banyak, 
# sedangkan spanning tree menghubungkan semua node tanpa ada cycle sama sekali.
# 2. Spanning tree tidak boleh memiliki cycle karena tujuan utamanya adalah efisiensi; 
# cycle menyebabkan penggunaan edge berlebih dan meningkatkan biaya tanpa menambah konektivitas.
# 3. Jumlah edge spanning tree selalu lebih sedikit (n-1) karena itu adalah jumlah minimal 
# yang dibutuhkan untuk menghubungkan seluruh node tanpa membentuk jalur ganda atau siklus.
#===================================================================================