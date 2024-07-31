import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen penjualan barang")
        self.items = {}

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10, padx=10)

        self.title_label = tk.Label(self.frame, text="DATA STOK BARANG", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.tree_frame = tk.Frame(self.frame)
        self.tree_frame.grid(row=1, column=0, columnspan=2, pady=5)

        self.tree_scroll = tk.Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(self.tree_frame, columns=("Nama", "Harga", "Stok"), show='headings', yscrollcommand=self.tree_scroll.set)
        self.tree.heading("Nama", text="Nama Barang")
        self.tree.heading("Harga", text="Harga")
        self.tree.heading("Stok", text="Stok")
        self.tree.column("Nama", width=150, anchor=tk.W)
        self.tree.column("Harga", width=100, anchor=tk.CENTER)
        self.tree.column("Stok", width=100, anchor=tk.CENTER)
        self.tree.pack()

        self.tree_scroll.config(command=self.tree.yview)

        self.add_button = tk.Button(self.frame, text="Input Data Barang", command=self.input_item)
        self.add_button.grid(row=2, column=0, pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Data Barang", command=self.delete_item)
        self.delete_button.grid(row=2, column=1, pady=5)

        self.search_button = tk.Button(self.frame, text="Mencari Data Barang", command=self.search_item)
        self.search_button.grid(row=3, column=0, pady=5)

        self.purchase_button = tk.Button(self.frame, text="Hitung Jumlah Pembelian", command=self.purchase_item)
        self.purchase_button.grid(row=3, column=1, pady=5)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.root.quit, bg='red', fg='white')
        self.exit_button.grid(row=4, column=0, columnspan=2, pady=8, padx=25,sticky=tk.E)

    def input_item(self):
        name = simpledialog.askstring("Input Data Barang", "Nama Barang:")
        if not name:
            return
        price = simpledialog.askfloat("Input Data Barang", "Harga Barang:")
        if price is None:
            return
        stock = simpledialog.askinteger("Input Data Barang", "Stok Barang:")
        if stock is None:
            return

        self.items[name] = {'price': price, 'stock': stock}
        self.update_treeview()
        messagebox.showinfo("Info", f"Barang '{name}' berhasil ditambahkan.")

    def update_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for name, data in self.items.items():
            self.tree.insert('', 'end', values=(name, data['price'], data['stock']))

    def delete_item(self):
        name = simpledialog.askstring("Delete Data Barang", "Nama Barang yang akan dihapus:")
        if not name:
            return

        if name in self.items:
            del self.items[name]
            self.update_treeview()
            messagebox.showinfo("Info", f"Barang '{name}' berhasil dihapus.")
        else:
            messagebox.showinfo("Info", f"Barang '{name}' tidak ditemukan.")

    def search_item(self):
        name = simpledialog.askstring("Mencari Data Barang", "Nama Barang yang dicari:")
        if not name:
            return

        if name in self.items:
            data = self.items[name]
            messagebox.showinfo("Data Barang", f"Nama: {name}, Harga: {data['price']}, Stok: {data['stock']}")
        else:
            messagebox.showinfo("Info", f"Barang '{name}' tidak ditemukan.")

    def purchase_item(self):
        name = simpledialog.askstring("Hitung Jumlah Pembelian", "Nama Barang yang akan dibeli:")
        if not name:
            return

        if name in self.items:
            quantity = simpledialog.askinteger("Hitung Jumlah Pembelian", "Jumlah yang dibeli:")
            if quantity is None:
                return

            if quantity > self.items[name]['stock']:
                messagebox.showinfo("Info", f"Stok barang '{name}' tidak mencukupi.")
                return

            self.items[name]['stock'] -= quantity
            total_price = self.items[name]['price'] * quantity
            self.update_treeview()
            messagebox.showinfo("Info", f"Total harga untuk {quantity} {name} adalah {total_price}.")
        else:
            messagebox.showinfo("Info", f"Barang '{name}' tidak ditemukan.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
