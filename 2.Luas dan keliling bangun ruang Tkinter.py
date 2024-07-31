import math
import tkinter as tk
from tkinter import messagebox, simpledialog

def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari * jari_jari

def keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

def input_shape_params(params):
    return [float(simpledialog.askstring("Input", f"Masukkan {param}:")) for param in params]

def hitung_luas_persegi():
    sisi = input_shape_params(["panjang sisi persegi"])[0]
    luas = luas_persegi(sisi)
    messagebox.showinfo("Hasil", f"Luas Persegi: {luas}")

def hitung_keliling_persegi():
    sisi = input_shape_params(["panjang sisi persegi"])[0]
    keliling = keliling_persegi(sisi)
    messagebox.showinfo("Hasil", f"Keliling Persegi: {keliling}")

def hitung_luas_persegi_panjang():
    panjang, lebar = input_shape_params(["panjang persegi panjang", "lebar persegi panjang"])
    luas = luas_persegi_panjang(panjang, lebar)
    messagebox.showinfo("Hasil", f"Luas Persegi Panjang: {luas}")

def hitung_keliling_persegi_panjang():
    panjang, lebar = input_shape_params(["panjang persegi panjang", "lebar persegi panjang"])
    keliling = keliling_persegi_panjang(panjang, lebar)
    messagebox.showinfo("Hasil", f"Keliling Persegi Panjang: {keliling}")

def hitung_luas_segitiga():
    alas, tinggi = input_shape_params(["panjang alas segitiga", "tinggi segitiga"])
    luas = luas_segitiga(alas, tinggi)
    messagebox.showinfo("Hasil", f"Luas Segitiga: {luas}")

def hitung_keliling_segitiga():
    sisi1, sisi2, sisi3 = input_shape_params(["panjang sisi 1 segitiga", "panjang sisi 2 segitiga", "panjang sisi 3 segitiga"])
    keliling = keliling_segitiga(sisi1, sisi2, sisi3)
    messagebox.showinfo("Hasil", f"Keliling Segitiga: {keliling}")

def hitung_luas_lingkaran():
    jari_jari = input_shape_params(["panjang jari-jari lingkaran"])[0]
    luas = luas_lingkaran(jari_jari)
    messagebox.showinfo("Hasil", f"Luas Lingkaran: {luas}")

def hitung_keliling_lingkaran():
    jari_jari = input_shape_params(["panjang jari-jari lingkaran"])[0]
    keliling = keliling_lingkaran(jari_jari)
    messagebox.showinfo("Hasil", f"Keliling Lingkaran: {keliling}")

def main_menu():
    clear_screen()
    main_menu_frame.pack()

def clear_screen():
    for widget in root.winfo_children():
        widget.pack_forget()

def show_shape_menu(calc_type):
    clear_screen()
    shape_menu_frame.pack()
    global calculation_type
    calculation_type = calc_type

def handle_shape_choice(shape_choice):
    clear_screen()
    if calculation_type == "Luas":
        options = {
            "Persegi": hitung_luas_persegi,
            "Persegi Panjang": hitung_luas_persegi_panjang,
            "Segitiga": hitung_luas_segitiga,
            "Lingkaran": hitung_luas_lingkaran
        }
    elif calculation_type == "Keliling":
        options = {
            "Persegi": hitung_keliling_persegi,
            "Persegi Panjang": hitung_keliling_persegi_panjang,
            "Segitiga": hitung_keliling_segitiga,
            "Lingkaran": hitung_keliling_lingkaran
        }

    action = options.get(shape_choice, None)
    if action:
        action()
    main_menu()

def exit_program():
    root.quit()

root = tk.Tk()
root.title("Kalkulator Bangun Datar")
root.geometry("400x300")

calculation_type = None

main_menu_frame = tk.Frame(root)
shape_menu_frame = tk.Frame(root)

tk.Label(main_menu_frame, text="Pilih bentuk operasi yang ingin dihitung:", font=("Helvetica", 14)).pack(pady=20)
tk.Button(main_menu_frame, text="Luas", width=20, command=lambda: show_shape_menu("Luas")).pack(pady=10)
tk.Button(main_menu_frame, text="Keliling", width=20, command=lambda: show_shape_menu("Keliling")).pack(pady=10)
tk.Button(main_menu_frame, text="Keluar", width=20, command=exit_program).pack(pady=10)

tk.Label(shape_menu_frame, text="Pilih bangun datar:", font=("Helvetica", 14)).pack(pady=20)
tk.Button(shape_menu_frame, text="Persegi", width=20, command=lambda: handle_shape_choice("Persegi")).pack(pady=5)
tk.Button(shape_menu_frame, text="Persegi Panjang", width=20, command=lambda: handle_shape_choice("Persegi Panjang")).pack(pady=5)
tk.Button(shape_menu_frame, text="Segitiga", width=20, command=lambda: handle_shape_choice("Segitiga")).pack(pady=5)
tk.Button(shape_menu_frame, text="Lingkaran", width=20, command=lambda: handle_shape_choice("Lingkaran")).pack(pady=5)
tk.Button(shape_menu_frame, text="Kembali", width=20, command=main_menu).pack(pady=5)

main_menu()

root.mainloop()
