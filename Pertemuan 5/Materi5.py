#============================================================
#Nama : Selena Rohmani Putri
#NIM : J0403251131
#Kelas : B2
#============================================================

#============================================================
# Materi : Backtracking dengan Pruning
# Jika jumlah angka '1' melebihi batas,
# maka cabang dihentikan (pruning).
#============================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    
    # Pruning
    if jumlah_1 > batas:
        return
    
    if len(hasil) == n:
        print(hasil)
        return
    
    biner_batas(n, batas, hasil + "0", jumlah_1)
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

biner_batas(4, 2)