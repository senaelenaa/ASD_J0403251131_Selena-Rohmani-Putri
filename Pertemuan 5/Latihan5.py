#============================================================
#Nama : Selena Rohmani Putri
#NIM : J0403251131
#Kelas : B2
#============================================================

#============================================================
# Materi : Backtracking Generator PIN
# Menghasilkan semua kemungkinan PIN 3 digit
# menggunakan angka 0 sampai 2.
# Total kombinasi yang dihasilkan adalah 3^3 = 27 PIN.
# Untuk mencegah angka yang sama berulang,
# bisa ditambahkan pengecekan sebelum menambah angka.
#============================================================

def buat_pin(panjang, hasil=""):
    # Base case: jika panjang PIN sudah sesuai
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # Choose dan Explore setiap kemungkinan angka
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)