# # sytax penyederhanaan multiple eksepsi
# try:
#     # kode
# except(TipeEksepsi1, TipeEksepsi2, TipeEksepsi3):
#     # penanganan kesalahan pada semua eksepsi
# else:
#     # kode selanjutnya jika tidak terjadi error

def main():
    print("PROGRAM PEMBAGIAN BILANGAN")

    try:
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        hasil = a/b
    except(ZeroDivisionError, ValueError, KeyboardInterrupt):
        print("\nERROR: Anda telah melakukan kesalahan pada inputan")
    
    else:
        print("nilai a: ", a)
        print("nilai b: ", b)
        print("hasil dari a\b adalah ", hasil)

if __name__ == "__main__":
    main()