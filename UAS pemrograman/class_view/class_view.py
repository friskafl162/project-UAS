from class_data import DataTiket
class View:
    def __init__(self):
        self.data_tiket = DataTiket()

    def tampilkan_menu(self):
        print("\nMenu Tiket Bus")
        print("1. Tambah Tiket")
        print("2. Tampilkan Tiket")
        print("3. Keluar")
        return input("Pilih menu: ")

    def input_tiket(self):
        try:
            nama = input("Masukkan Nama Penumpang: ")
            if not nama.strip():
                raise ValueError("Nama tidak boleh kosong.")
            
            tujuan = input("Masukkan Tujuan: ")
            if not tujuan.strip():
                raise ValueError("Tujuan tidak boleh kosong.")
            
            harga = float(input("Masukkan Harga Tiket: "))
            if harga <= 0:
                   raise ValueError("Harga harus lebih besar dari 0.")
            
            self.data_tiket.tambah_tiket(nama, tujuan, harga)
            print("Tiket berhasil ditambahkan.")
        except ValueError as e:
            print(f"Error: {e}")

    def tampilkan_tiket(self):
        self.data_tiket.tampilkan_tiket()