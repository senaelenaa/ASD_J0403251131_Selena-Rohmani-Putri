#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Implementasi BFS (Breadth First Search)
#===================================================================================

# Struktur data untuk membuat antrian, menggunakan library collections bawaan python yaitu deque (double ended queue)

from collections import deque  # Mengimpor deque untuk membuat antrian (queue)


#representasi graph
graph ={  # Membuat dictionary sebagai representasi graph
    'A': ['B', 'C'],  # Node A terhubung ke B dan C
    'B': ['A', 'D',],  # Node B terhubung ke A dan D
    'C': ['A', 'D'],  # Node C terhubung ke A dan D
    'D': ['B', 'C']  # Node D terhubung ke B dan C
}

def bsf(graph, start):  # Mendefinisikan fungsi BFS (Breadth-First Search)
    #fungsi untuk melakukan penelusuran BFS pada graph
    # graph: dictionary yang menyimpan struktur dari graph
    # start: node awal untuk memulai penelusuran
    
    #quque untuk menyimpan node yang akan diproses / di baca
    queue = deque()  # Membuat antrian kosong
    
    # variabel yang digunakan untuk menyimpan node yang sudah diproses/dikunjung
    visited = set()  # Membuat set kosong untuk menyimpan node yang sudah dikunjungi

    #memasukkan node awal ke dalam antrian
    queue.append(start)  # Menambahkan node awal ke queue

    # tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)  # Menandai node awal sebagai sudah dikunjungi

    while queue:  # Selama queue tidak kosong
        #mengambil node paling depan dari queue
        node = queue.popleft()  # Mengambil dan menghapus elemen paling depan dari queue

        #tampilkan node yang sedang dikunjungi
        print(node, end=" ")  # Menampilkan node yang sedang dikunjungi tanpa pindah baris

        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:  # Iterasi semua tetangga dari node
            #jika tetangga belum dikunjungi
            if neighbor not in visited: #jika tetangga belum dikunjungi

                #print(neighbor) #menampilkan tetangga yang dikunjungi
                #tandai sebagai sudah dikunjungi
                visited.add(neighbor)  # Menandai tetangga sebagai sudah dikunjungi
                #masukkan tetangga ke dalam queue untuk diproses nanti
                queue.append(neighbor)  # Menambahkan tetangga ke queue

#menjalankan BFS dari graph A
bsf(graph, 'A')  # Memanggil fungsi BFS mulai dari node A