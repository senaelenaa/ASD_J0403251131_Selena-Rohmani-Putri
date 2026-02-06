#=========================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 1 : Membuat fungsi load data
#=========================================================

nama_file = "data_mahasiswa.txt"

def baca_data_mahasiswa(nama_file):
    data_dict = {} # inisialisasi data dictionary
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip() # menghilangkan karakter newline
                
                parts = baris.split(",")
                # Melewati baris jika format kolom tidak sesuai (harus 3 kolom)
                if len(parts) != 3:
                    continue
                
                nim, nama, nilai_str = parts
                nilai_int = int(nilai_str)
                # Menyimpan ke dictionary dengan NIM sebagai key
                data_dict[nim] = {"nama": nama, "nilai": nilai_int} 
        return data_dict
    except FileNotFoundError:
        print(f"Error: File {nama_file} tidak ditemukan.")
        return {}

# Memanggil fungsi baca_data_mahasiswa
#buka_data = baca_data_mahasiswa(nama_file)
#print("Jumlah data terbaca:", len(buka_data))

#=========================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 2 : Membuat fungsi menampilkan data
#=========================================================

def tampilkan_data_mahasiswa(data_dict):
    if len(data_dict) == 0:
        print("Data mahasiswa kosong.")
        return
    
    # Membuat header tabel sesuai format f-string
    print("\n==== Daftar Mahasiswa ====")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' : >5}")
    print("-" * 32) # Membuat garis header

    """
    untuk tampilan yang rapi, atur f-string formatting
    {'NIM' : <10} -> rata kiri, lebar 10 karakter
    {'Nama' : <12} -> rata kiri, lebar 12 karakter
    {'Nilai' : >5} -> rata kanan, lebar 5 karakter
    """

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {nilai : >5}")

#Memanggil fungsi menampilkan data
#tampilkan_data_mahasiswa(buka_data)

#=========================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 3 : Membuat fungsi mencari data
#=========================================================

def cari_data(data_dict):
    #Mncari data mahasiswa berdasarkan NIM
    nim_cari = input("\nMasukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n==== Data Mahasiswa Ditemukan ====")
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("\nData tidak ditemukan.")

#Memanggil fungsi cari data
#cari_data(buka_data)

#=========================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 4 : Membuat fungsi update nilai
#=========================================================

def update_nilai(data_dict):

    #cari nim mahasiswa yang akan diupdate nilainya
    nim = input("Masukkan NIM Mahasiswa yang akan diupdate nilainya : ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka, update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru >100 :
        print("Nilai harus ada di antara 0-100,update dibatalkan")
        return
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#update_nilai(buka_data)

#=========================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 5 : Menyimpan perubahan data ke file
#=========================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

# Memanggil fungsi simpan data
#simpan_data(nama_file, buka_data)
print("Data Berhasil Disimpan")

#=========================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 6 : Membuat menu program
#=========================================================

def main():

    #menjalanlan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan NIM")
        print("3. Update nilai mahasiswa")
        print("4. Simpan data ke file")
        print("0. Keluar")

        pilihan = input("Pilihan menu: ").strip()

        if pilihan == "1":
            tampilkan_data_mahasiswa(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            update_nilai(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
        elif pilihan == "0":
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()