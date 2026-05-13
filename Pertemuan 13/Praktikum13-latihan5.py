#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
#===================================================================================

#===================================================================================
# Latihan 5 : Tugas 1 (Jaringan Jalan Antar Kota)
#===================================================================================

# Representasi weighted graph untuk Kasus 1: Jaringan Jalan Antar Kota
# Format data: (bobot, kota1, kota2)
# Bogor-Jakarta=5, Bogor-Depok=2,
# Depok-Jakarta=3, Jakarta-Bandung=6, Depok-Bandung=4
jalan = [
    (2, 'Bogor', 'Depok'), # Jalan Bogor ke Depok dengan bobot 2
    (3, 'Depok', 'Jakarta'), # Jalan Depok ke Jakarta dengan bobot 3
    (4, 'Depok', 'Bandung'), # Jalan Depok ke Bandung dengan bobot 4
    (5, 'Bogor', 'Jakarta'), # Jalan Bogor ke Jakarta dengan bobot 5
    (6, 'Jakarta', 'Bandung') # Jalan Jakarta ke Bandung dengan bobot 6
]

# Implementasi algoritma Kruskal

# Mengurutkan edge berdasarkan bobot terkecil
jalan.sort()

# Menyimpan edge yang dipilih untuk MST
mst_jalan = []

# Menyimpan total bobot minimum
total_bobot = 0

# Set untuk melacak kota yang sudah terhubung
visited_kota = set()

# Memeriksa setiap edge berdasarkan bobot terkecil
for bobot, u, v in jalan:
    
    # Edge dipilih jika tidak membentuk cycle sederhana
    if u not in visited_kota or v not in visited_kota:
        
        # Menambahkan edge ke MST
        mst_jalan.append((u, v, bobot))
        
        # Menambahkan bobot ke total bobot minimum
        total_bobot += bobot
        
        # Menandai kota sebagai sudah terhubung
        visited_kota.add(u)
        visited_kota.add(v)

# Output hasil pembangunan jalan minimum
print("Rute MST Jaringan Jalan Antar Kota:")

# Menampilkan setiap rute yang dipilih
for rute in mst_jalan:
    print(f"{rute[0]} - {rute[1]} dengan bobot {rute[2]}")

# Menampilkan total bobot minimum
print("Total Bobot Minimum =", total_bobot)

#===================================================================================
# Jawaban Analisis :
# 1. Kasus yang dipilih adalah Kasus 1: Jaringan Jalan Antar Kota.
# 2. Algoritma yang digunakan adalah Kruskal.
# 3. Edge yang dipilih dalam MST adalah:
# Bogor-Depok (2),
# Depok-Jakarta (3),
# dan Depok-Bandung (4).
# 4. Total bobot MST adalah 9.
# 5. Edge Bogor-Jakarta (5) dan Jakarta-Bandung (6) tidak dipilih karena kota-kota tersebut 
# sudah terhubung melalui Depok dengan biaya yang lebih rendah, sehingga tidak perlu jalur tambahan.
#===================================================================================