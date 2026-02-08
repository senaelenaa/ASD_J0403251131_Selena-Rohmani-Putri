# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama  : (Selena Rohmani Putri)
# NIM   : (J0403251131)
# Kelas : (B2)
# ==========================================================

nama_file = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    stok_dict = {}

    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                baris = baris.strip()

                if baris == "":
                    continue

                parts = baris.split(",")
                if len(parts) != 3:
                    continue

                kode, nama, stok_str = parts

                try:
                    stok = int(stok_str)
                except ValueError:
                    continue

                stok_dict[kode] = {
                    "nama": nama,
                    "stok": stok
                }

    except FileNotFoundError:
        print("File stok_barang.txt belum ada. Data masih kosong.")

    return stok_dict


# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            f.write(f"{kode},{nama},{stok}\n")


# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    if len(stok_dict) == 0:
        print("Stok barang kosong.")
        return

    print("\n=== DAFTAR STOK BARANG ===")
    print(f"{'Kode':<10} | {'Nama Barang':<15} | {'Stok':>5}")
    print("-" * 36)

    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<15} | {stok:>5}")


# --------------------
# Fungsi: Cari barang
# --------------------
def cari_barang(stok_dict):
    kode = input("Masukkan kode barang: ").strip()

    if kode == "":
        print("Kode tidak boleh kosong.")
        return

    if kode in stok_dict:
        print("Kode :", kode)
        print("Nama :", stok_dict[kode]["nama"])
        print("Stok :", stok_dict[kode]["stok"])
    else:
        print("Barang tidak ditemukan.")


# ----------------------
# Fungsi: Tambah barang
# ----------------------
def tambah_barang(stok_dict):
    kode = input("Masukkan kode barang baru: ").strip()

    if kode == "":
        print("Kode tidak boleh kosong.")
        return

    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return

    nama = input("Masukkan nama barang: ").strip()
    if nama == "":
        print("Nama barang tidak boleh kosong.")
        return

    try:
        stok_awal = int(input("Masukkan stok awal: ").strip())
    except ValueError:
        print("Stok harus berupa angka.")
        return

    if stok_awal < 0:
        print("Stok tidak boleh negatif.")
        return

    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    print("Barang berhasil ditambahkan.")


# --------------------
# Fungsi: Update stok
# --------------------
def update_stok(stok_dict):
    kode = input("Masukkan kode barang: ").strip()

    if kode == "":
        print("Kode tidak boleh kosong.")
        return

    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return

    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Pilih (1/2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: ").strip())
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    if jumlah <= 0:
        print("Jumlah harus lebih dari 0.")
        return

    if pilihan == "1":
        stok_dict[kode]["stok"] += jumlah
        print("Stok berhasil ditambahkan.")

    elif pilihan == "2":
        if stok_dict[kode]["stok"] - jumlah < 0:
            print("Stok tidak boleh negatif.")
            return
        stok_dict[kode]["stok"] -= jumlah
        print("Stok berhasil dikurangi.")

    else:
        print("Pilihan tidak valid.")


# --------------
# Program Utama
# --------------
def main():
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang")
        print("3. Tambah barang")
        print("4. Update stok")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            simpan_stok(nama_file, stok_barang)
            print("Data disimpan. Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()