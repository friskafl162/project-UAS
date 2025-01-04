# Class untuk menyimpan data tiket bus
class DataTiket:
    def __init__(self):
        self.tiket = []

    def tambah_tiket(self, nama, tujuan, harga):
        self.tiket.append({
            'Nama': nama,
            'Tujuan': tujuan,
            'Harga': harga
        })

    def tampilkan_tiket(self):
        if not self.tiket:
            print("Belum ada tiket yang terdaftar.")
            return
        print(f"{'No':<5}{'Nama':<20}{'Tujuan':<20}{'Harga':<10}")
        for i, tiket in enumerate(self.tiket, 1):
            print(f"{i:<5}{tiket['Nama']:<20}{tiket['Tujuan']:<20}{tiket['Harga']:<10}")

# Class untuk menampilkan menu dan menerima input dari pengguna
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


# Class untuk mengatur alur program
class Process:
    def __init__(self):
        self.view = View()

    def mulai(self):
        while True:
            pilihan = self.view.tampilkan_menu()
            if pilihan == '1':
                self.view.input_tiket()
            elif pilihan == '2':
                self.view.tampilkan_tiket()
            elif pilihan == '3':
                print("Terima kasih! Program selesai.")
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

# Program utama
if __name__ == "__main__":
    process = Process()
    process.mulai()