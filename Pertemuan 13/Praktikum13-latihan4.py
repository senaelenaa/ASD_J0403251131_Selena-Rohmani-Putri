#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
#===================================================================================

#===================================================================================
# Latihan 4 : Studi Kasus: Jaringan Kabel Antar Gedung
#===================================================================================

# Data hubungan gedung dengan biaya pemasangan kabel
# Format data: (biaya, gedung1, gedung2)
# GedungA-GedungB=4, GedungA-GedungC=2,
# GedungB-GedungD=3, GedungC-GedungD=1, GedungA-GedungD=5
edges = [
    (1, 'GedungC', 'GedungD'), # Kabel GedungC ke GedungD biaya 1
    (2, 'GedungA', 'GedungC'), # Kabel GedungA ke GedungC biaya 2
    (3, 'GedungB', 'GedungD'), # Kabel GedungB ke GedungD biaya 3
    (4, 'GedungA', 'GedungB'), # Kabel GedungA ke GedungB biaya 4
    (5, 'GedungA', 'GedungD') # Kabel GedungA ke GedungD biaya 5
]

# Menggunakan algoritma Kruskal untuk menentukan biaya minimum

# Mengurutkan edge dari biaya terkecil
edges.sort()

# Menyimpan edge yang dipilih untuk MST
mst = []

# Menyimpan total biaya minimum
biaya_total = 0

# Set untuk melacak gedung yang sudah terhubung
terhubung = set()

# Memeriksa setiap edge berdasarkan urutan biaya terkecil
for biaya, u, v in edges:
    
    # Edge dipilih jika tidak membentuk cycle sederhana
    if u not in terhubung or v not in terhubung:
        
        # Tambahkan edge ke MST
        mst.append((u, v, biaya))
        
        # Tambahkan biaya ke total biaya
        biaya_total += biaya
        
        # Tandai gedung sebagai sudah terhubung
        terhubung.add(u)
        terhubung.add(v)

# Menampilkan hasil perencanaan jaringan kabel
print("Jaringan Kabel Terpilih:")

# Menampilkan setiap koneksi kabel yang dipilih
for link in mst:
    print(f"{link[0]} - {link[1]} (Biaya: {link[2]})")

# Menampilkan total biaya minimum
print("Total Biaya Minimum =", biaya_total)

#===================================================================================
# Jawaban Analisis :
# 1. Algoritma yang digunakan adalah Kruskal.
# 2. Edge yang dipilih adalah:
# GedungC-GedungD (1),
# GedungA-GedungC (2),
# dan GedungB-GedungD (3).
# 3. Total biaya minimum adalah 6.
# 4. MST sangat cocok karena tujuannya adalah menghubungkan semua lokasi (gedung) 
# dengan total biaya (bobot) yang paling sekecil mungkin tanpa ada pemborosan jalur (cycle).
#===================================================================================