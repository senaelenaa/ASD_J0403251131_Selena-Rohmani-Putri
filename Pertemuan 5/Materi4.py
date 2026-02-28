#============================================================
#Nama : Selena Rohmani Putri
#NIM : J0403251131
#Kelas : B2
#============================================================

#============================================================
# Materi : Backtracking Kombinasi Biner
# Pola Choose → Explore.
# Program mencoba tambah "0" lalu "1" hingga panjang tercapai
#============================================================

def biner(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return
    
    biner(n, hasil + "0")
    biner(n, hasil + "1")

biner(3)