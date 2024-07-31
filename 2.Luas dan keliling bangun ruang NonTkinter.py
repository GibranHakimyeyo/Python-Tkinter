import math
import os

def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

def hitung_luas_persegi():
    sisi = float(input("Masukkan panjang sisi persegi: "))
    luas = luas_persegi(sisi)
    print(f"Luas Persegi: {luas}")

def hitung_keliling_persegi():
    sisi = float(input("Masukkan panjang sisi persegi: "))
    keliling = keliling_persegi(sisi)
    print(f"Keliling Persegi: {keliling}")

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def hitung_luas_persegi_panjang():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas = luas_persegi_panjang(panjang, lebar)
    print(f"Luas Persegi Panjang: {luas}")

def hitung_keliling_persegi_panjang():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    keliling = keliling_persegi_panjang(panjang, lebar)
    print(f"Keliling Persegi Panjang: {keliling}")

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def hitung_luas_segitiga():
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = luas_segitiga(alas, tinggi)
    print(f"Luas Segitiga: {luas}")

def hitung_keliling_segitiga():
    sisi1 = float(input("Masukkan panjang sisi 1 segitiga: "))
    sisi2 = float(input("Masukkan panjang sisi 2 segitiga: "))
    sisi3 = float(input("Masukkan panjang sisi 3 segitiga: "))
    keliling = keliling_segitiga(sisi1, sisi2, sisi3)
    print(f"Keliling Segitiga: {keliling}")

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari * jari_jari

def keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

def hitung_luas_lingkaran():
    jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
    luas = luas_lingkaran(jari_jari)
    print(f"Luas Lingkaran: {luas}")

def hitung_keliling_lingkaran():
    jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
    keliling = keliling_lingkaran(jari_jari)
    print(f"Keliling Lingkaran: {keliling}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    print("--------------------------------------------")
    print("|Pilih bentuk operasi yang ingin dihitung:  |")
    print("|-------------------------------------------|")
    print("|1. Luas                                    |")    
    print("|2. Keliling                                |")
    print("|3. Keluar                                  |")
    print("--------------------------------------------")
    choice = int(input("Masukkan pilihan (1/2/3): "))
    return choice

def shape_menu():
    print("\nPilih bangun datar yang akan dihitung:")
    print("--------------------------------------------")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Kembali")
    print("--------------------------------------------")
    choice = int(input("Masukkan pilihan (1-5): "))
    return choice

def main():
    while True:
        clear_screen()
        choice = main_menu()
        if choice == 3:
            print("Terima kasih telah menggunakan program ini.")
            break
        elif choice in [1, 2]:
            while True:
                clear_screen()
                shape_choice = shape_menu()
                if shape_choice == 5:
                    break

                if choice == 1:  # Luas
                    options = {
                        1: hitung_luas_persegi,
                        2: hitung_luas_persegi_panjang,
                        3: hitung_luas_segitiga,
                        4: hitung_luas_lingkaran
                    }
                elif choice == 2:  # Keliling
                    options = {
                        1: hitung_keliling_persegi,
                        2: hitung_keliling_persegi_panjang,
                        3: hitung_keliling_segitiga,
                        4: hitung_keliling_lingkaran
                    }

                action = options.get(shape_choice, None)
                if action:
                    action()
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
                input("\nTekan Enter untuk melanjutkan...")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
