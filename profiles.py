class Profiles:
    def __init__(self):
        self.ipk = 3.75
        self.total_tagihan = 5000000
        self.informasi_pribadi = {
            "Nama": "bambang",
            "NIM": "422023005",
            "Program Studi": "sistem informasi",
            "Fakultas": "Teknik",
            "Alamat": "Jl. Contoh No. 123",
            "Tanggal Lahir": "1 Januari 2000",
        }

    def check_ipk(self):
        print("IPK Anda:", self.ipk)
        self.kembali()

    def check_tagihan(self):
        print("Total Tagihan Anda:", self.total_tagihan)
        self.kembali()

    def show_personal_info(self):
        print("Informasi Pribadi:")
        for key, value in self.informasi_pribadi.items():
            print(f"{key}: {value}")
        self.kembali()

    def kembali(self):
        input("Tekan Enter untuk kembali ke menu sebelumnya...")

    def show_profiles(self):
        while True:
            print("Silakan pilih informasi yang ingin Anda lihat:")
            print("1. IPK")
            print("2. Total Tagihan")
            print("3. Detail Informasi Pribadi")
            print("4. Kembali ke menu utama")
            choice = input("Pilihan: ")

            if choice == "1":
                self.check_ipk()
            elif choice == "2":
                self.check_tagihan()
            elif choice == "3":
                self.show_personal_info()
            elif choice == "4":
                return
            else:
                print("Pilihan tidak valid.")
