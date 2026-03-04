#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Merge Sort dengan tracing
#===================================================================================

from heapq import merge


def merge_sort(data, depth=0):
    indent = "  " * depth  # indentasi berdasarkan depth
    if len(data) <= 1: 
        return data
    
    # Divide : memabgi data menjadi 2 bagian
    mid = len(data)//2  # membagi data menjadi 2 bagian
    left = data[:mid]   # slicing bagian kiri
    right = data[mid:]  # slicing bagian kanan

    print(f"{indent}divide -> left {left} | right {right}")
    # 8 ==> left 4   right 4
    # left 4 ==> mergesort ==>
    #   letf 2 ==> mergesort 
    #   dan right 2 ==> mergesort

    # recursive call 
    left_sorted = merge_sort(left, depth + 1)
    right_sorted = merge_sort(right, depth + 1)

    merged = merge(left_sorted, right_sorted)
    print(f"{indent}merge -> left {left_sorted} | right {right_sorted} => merged {merged}")
    return merged

def merge(left, right):

    result = []
    i = 0
    j = 0

    # membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Menambahkan elemen yang tersisa
    result.extend(left[i:])
    result.extend(right[j:])

    return result

angka = [13, 7, 28, 5, 19, 36, 4]
print("Hasil Sorting: ", merge_sort(angka))