#============================================================
#Nama : Selena Rohmani Putri
#NIM : J0403251131
#Kelas : B2
#============================================================

#============================================================
# Materi : Backtracking Dasar
# Membuat kombinasi huruf A dan B sepanjang n.
# Jumlah kombinasi yang dihasilkan adalah 2^n.
# Untuk n = 2, hasilnya: AA, AB, BA, BB.
#============================================================

def kombinasi(n, hasil=""):
    # Base case: jika panjang hasil sudah n
    if len(hasil) == n:
        print(hasil)
        return
    
    # Choose dan Explore
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)
