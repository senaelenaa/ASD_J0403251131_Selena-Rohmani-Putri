#============================================================
#Nama : Selena Rohmani Putri
#NIM : J0403251131
#Kelas : B2
#============================================================

#============================================================
# Materi : Rekursi Pangkat
# Menghitung nilai a pangkat n menggunakan rekursi.
# Fungsi akan terus memanggil dirinya sendiri
# hingga n menjadi 0 (base case).
# Setelah itu hasil dikembalikan bertahap (unwinding).
#============================================================

def pangkat(a, n):
    # Base case: jika n = 0 maka hasilnya 1
    if n == 0:
        return 1
    
    # Recursive case: a dikali dengan pangkat(a, n-1)
    return a * pangkat(a, n - 1)

print("Hasil pangkat:", pangkat(2, 4))