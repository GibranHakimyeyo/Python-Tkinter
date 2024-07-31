import tkinter as tk
from tkinter import messagebox

def calculate_payment():
    try:
        name_staff = entry_name_staff.get().strip()
        name_customer = entry_name_customer.get().strip()
        check_in_date = entry_check_in_date.get().strip()
        room_code = entry_room_code.get().strip().upper()
        rental_days_str = entry_rental_days.get().strip()
        payment_amount_str = entry_payment_amount.get().strip()

        if not (name_staff and name_customer and check_in_date and room_code and rental_days_str and payment_amount_str):
            raise ValueError("All fields must be filled")

        rental_days = int(rental_days_str)
        payment_amount = float(payment_amount_str)

        if rental_days <= 0 or payment_amount < 0:
            raise ValueError("Lama sewa harus lebih dari 0!")

        room_details = {
            'M': ('Melati', 650000),
            'S': ('Sakura', 550000),
            'L': ('Lily', 400000),
            'A': ('Anggrek', 350000)
        }

        if room_code in room_details:
            room_name, room_rate = room_details[room_code]
            rent_amount = room_rate * rental_days

        
            ppn = 0.10 * rent_amount

            total_payment = rent_amount + ppn
            change = payment_amount - total_payment

            if change < 0:
                messagebox.showwarning("Peringatan", "Uang bayar tidak cukup!")
            else:
                result_text.set(
                    f"{' ' * 10}Bukti Pemesanan Kamar\n"
                    f"{' ' * 10}  Hotel SEJUK ASRI\n"
                    f"{' ' * 12}{'  =========== '}\n"
                    f"\n"
                    f"Nama Petugas           :  {name_staff}\n"
                    f"Nama Customer          :  {name_customer}\n"
                    f"Tanggal Check-in       :  {check_in_date}\n"
                    f"{'=' * 30}\n"
                    f"Nama Kamar Yang dipesan:  {room_name}\n"
                    f"Harga Sewa per Malam   :  Rp. {room_rate:,}\n"
                    f"Lama Sewa              :  {rental_days} malam\n"
                    f"PPN 10%                :  Rp. {ppn:,}\n"
                    f"Jumlah Bayar           :  Rp. {rent_amount:,}\n"
                    f"Total Bayar            :  Rp. {total_payment:,}\n"
                    f"Uang Bayar             :  Rp. {payment_amount:,}\n"
                    f"Uang Kembali           :  Rp. {change:,}\n\n"
                    f"Terimakasih sudah memilih penginapan kami."
                    
                )
                clear_button.grid(row=13, column=1, pady=10)
        else:
            messagebox.showerror("Error", "Kode Kamar tidak valid.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def clear_fields():
    entry_name_staff.delete(0, tk.END)
    entry_name_customer.delete(0, tk.END)
    entry_check_in_date.delete(0, tk.END)
    entry_room_code.delete(0, tk.END)
    entry_rental_days.delete(0, tk.END)
    entry_payment_amount.delete(0, tk.END)
    result_text.set("")
    clear_button.grid_remove()


def exit_application():
    root.quit()


root = tk.Tk()
root.title("System pembayaran hotel Sejuk Asri")


tk.Label(root, text="Hotel SEJUK ASRI", font=("Helvetica", 16)).grid(row=0, columnspan=2, pady=10)
tk.Label(root, text="============================").grid(row=1, columnspan=2)

tk.Label(root, text="Nama Petugas:").grid(row=2, column=0, sticky='w', padx=10)
entry_name_staff = tk.Entry(root)
entry_name_staff.grid(row=2, column=1, padx=10)

tk.Label(root, text="Nama Customer:").grid(row=3, column=0, sticky='w', padx=10)
entry_name_customer = tk.Entry(root)
entry_name_customer.grid(row=3, column=1, padx=10)

tk.Label(root, text="Tanggal Check-in (dd/mm/yy):").grid(row=4, column=0, sticky='w', padx=10)
entry_check_in_date = tk.Entry(root)
entry_check_in_date.grid(row=4, column=1, padx=10)

tk.Label(root, text="============================================").grid(row=5, columnspan=2)

tk.Label(root, text="Pilih Kode Kamar [M/S/L/A]:").grid(row=6, column=0, sticky='w', padx=10)
entry_room_code = tk.Entry(root)
entry_room_code.grid(row=6, column=1, padx=10)

tk.Label(root, text="Lama Sewa (hari):").grid(row=7, column=0, sticky='w', padx=10)
entry_rental_days = tk.Entry(root)
entry_rental_days.grid(row=7, column=1, padx=10)

tk.Label(root, text="Nominal pembayaran :").grid(row=8, column=0, sticky='w', padx=10)
entry_payment_amount = tk.Entry(root)
entry_payment_amount.grid(row=8, column=1, padx=10)

tk.Button(root, text=" Selesaikan Pembayaran ", command=calculate_payment).grid(row=9, column=1, columnspan=1, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.grid_remove()

exit_button = tk.Button(root, text="Exit", command=exit_application, bg='red', fg='white')
exit_button.grid(row=9, column=2, columnspan= 2,pady=3, padx=5)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", font=("Courier", 10))
result_label.grid(row=11, columnspan=3, pady=10, padx=10)


root.mainloop()
