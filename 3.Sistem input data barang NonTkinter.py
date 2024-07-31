class InventoryApp:
    def __init__(self):
        self.items = {}

    def input_item(self):
        name = input("Nama Barang: ")
        if not name:
            print("Nama barang tidak boleh kosong.")
            return
        try:
            price = float(input("Harga Barang: "))
            stock = int(input("Stok Barang: "))
        except ValueError:
            print("Harga dan stok harus berupa angka.")
            return

        self.items[name] = {'price': price, 'stock': stock}
        print(f"Barang '{name}' berhasil ditambahkan.")

    def display_items(self):
        if not self.items:
            print("Tidak ada data barang.")
            return

        print("Data Barang:")
        for name, data in self.items.items():
            print(f"Nama: {name}, Harga: {data['price']}, Stok: {data['stock']}")

    def delete_item(self):
        name = input("Nama Barang yang akan dihapus: ")
        if not name:
            print("Nama barang tidak boleh kosong.")
            return

        if name in self.items:
            del self.items[name]
            print(f"Barang '{name}' berhasil dihapus.")
        else:
            print(f"Barang '{name}' tidak ditemukan.")

    def search_item(self):
        name = input("Nama Barang yang dicari: ")
        if not name:
            print("Nama barang tidak boleh kosong.")
            return

        if name in self.items:
            data = self.items[name]
            print(f"Nama: {name}, Harga: {data['price']}, Stok: {data['stock']}")
        else:
            print(f"Barang '{name}' tidak ditemukan.")

    def purchase_item(self):
        name = input("Nama Barang yang akan dibeli: ")
        if not name:
            print("Nama barang tidak boleh kosong.")
            return

        if name in self.items:
            try:
                quantity = int(input("Jumlah yang dibeli: "))
            except ValueError:
                print("Jumlah harus berupa angka.")
                return

            if quantity > self.items[name]['stock']:
                print(f"Stok barang '{name}' tidak mencukupi.")
                return

            self.items[name]['stock'] -= quantity
            total_price = self.items[name]['price'] * quantity
            print(f"Total harga untuk {quantity} {name} adalah {total_price}.")
        else:
            print(f"Barang '{name}' tidak ditemukan.")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Input Data Barang")
            print("2. Tampil Data Barang")
            print("3. Delete Data Barang")
            print("4. Mencari Data Barang")
            print("5. Hitung Jumlah Pembelian")
            print("6. Keluar")
            choice = input("Pilih menu (1-6): ")

            if choice == '1':
                self.input_item()
            elif choice == '2':
                self.display_items()
            elif choice == '3':
                self.delete_item()
            elif choice == '4':
                self.search_item()
            elif choice == '5':
                self.purchase_item()
            elif choice == '6':
                print("Terima kasih telah menggunakan aplikasi ini.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    app = InventoryApp()
    app.menu()
