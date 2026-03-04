#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan : 2 (Melengkapi Potongan Kode)
#===================================================================================

# Sorting Ascending
def insertion_sort(data):

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

# Program
data = [9, 3, 7, 1, 5]
print("Ascending :", insertion_sort(data))


# Sortinng Descending
def insertion_sort_desc(data):

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

# Program
data2 = [9, 3, 7, 1, 5]
print("Descending:", insertion_sort_desc(data2))


# #===================================================================================
# Soal dan Jawaban :
# 1. Lengkapi kondisi agar menjadi sorting ascending.
#   Kondisi ascending adalah data[j] > key

# 2. Ubah agar menjadi descending.
#   Untuk descending dibalik menjadi data[j] < key
# #===================================================================================