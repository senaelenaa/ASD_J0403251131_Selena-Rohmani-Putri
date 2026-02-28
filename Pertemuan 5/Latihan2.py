#==============================================================
#Nama : Selena Rohmani Putri
#NIM : J0403251131
#Kelas : B2
#==============================================================

#==============================================================
# Materi : Tracing Rekursi
# Menampilkan proses masuk (stacking) dan keluar (unwinding).
# "Masuk" dicetak saat fungsi dipanggil.
# "Keluar" dicetak setelah fungsi rekursif selesai.
# Output keluar terbalik karena mengikuti prinsip stack (LIFO).
#==============================================================

def countdown(n):
    # Base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)