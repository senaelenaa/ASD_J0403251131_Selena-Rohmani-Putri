#===================================================================================
#Nama : Selena Rohmani Putri
#NIM : J0403251131
#Kelas : B2
#===================================================================================

#===================================================================================
# Materi Rekursif : Faktoria;
# recursive case => 3! = 3 x 2 x 1
# base case => 0 berhenti
#===================================================================================

def faktorial(n):
    #base case
    if n == 0:
        return 1
    
    #recursive case
    return n*faktorial(n-1) #n-1*n-2*n-3 ... n-?

print("=== Program Faktorial ===")
print("Hasil Faktorial : ", faktorial(3))