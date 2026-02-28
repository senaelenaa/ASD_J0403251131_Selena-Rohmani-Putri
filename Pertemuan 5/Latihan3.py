#============================================================
#Nama : Selena Rohmani Putri
#NIM : J0403251131
#Kelas : B2
#============================================================

#============================================================
# Materi : Rekursi pada List
# Mencari nilai maksimum dalam list menggunakan rekursi.
# Fungsi membandingkan satu per satu elemen list
# sampai menemukan nilai terbesar.
#============================================================

def cari_maks(data, index=0):
    # Base case: jika sudah di elemen terakhir
    if index == len(data) - 1:
        return data[index]
    
    # Recursive call untuk mencari maksimum sisa elemen
    maks_sisa = cari_maks(data, index + 1)
    
    # Membandingkan elemen sekarang dengan maksimum sisa
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))