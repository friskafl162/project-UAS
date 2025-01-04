from class_view import View 
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