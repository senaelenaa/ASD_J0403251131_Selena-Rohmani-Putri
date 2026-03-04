#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Insertion Sort dengan tracing
#===================================================================================

def insertion_sort(data):

    #melihat data
    print("Data Awal : ", data)
    print("="*50)

    #Loop mulai dr data ke 2 (indeks array ke 1)
    for i in range (1, len(data)):

        key = data[i] #Simpan dinilai yang disisipkan
        j = i-1 #indeks elemen terakhir di bagian kiri

        print("Iterasi ke-", i)
        print("Nilai key = ", key)
        print("Bagian Kiri (terurut): ", data[i:])
        print("Bagian kanan (blm terurut) : ", data[i])

        #Geser
        while j>=0 and data[j] > key:
           data[j+1] = data[j]
           j -= 1

        print("")

        #Sisipkan key ke posisi yang benar
        data[j+1] = key
    return data

angka = [7,8,5,2,4,6]
print("Hasil Sorting : ", insertion_sort(angka))