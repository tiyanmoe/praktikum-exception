def main():
    print("PROGRAM PEMBAGIAN BILANGAN")

    try:
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        hasil = a/b
    except ZeroDivisionError:
        print("\nERROR: Nilai b tidak boleh nol")
    
    except ValueError:
        print("\nERROR: a dan b harus berupa angka")
    
    except KeyboardInterrupt:
        print("\nERROR: Jangan tekan CTRL+C")
    
    else:
        print("nilai a: ", a)
        print("nilai b: ", b)
        print("hasil dari a\b adalah ", hasil)

if __name__ == "__main__":
    main()