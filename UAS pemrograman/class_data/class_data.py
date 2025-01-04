class DataTiket:
    def _init_(self):
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