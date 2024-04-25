
from Learning import Learning
from mahasiswa import Mahasiswa

class Dosen:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.mahasiswa = ()

    def login(self):
        input_username = input("Masukkan username: ")
        input_password = input("Masukkan password: ")
        if input_username == self.username and input_password == self.password:
            print("Login berhasil sebagai dosen.")
            return True
        else:
            print("Username atau password salah.")
            return False

    def use_dosen(self):
        print("Anda dapat menggunakan fitur dosen sekarang.")
        while True:
            print("Pilih opsi:")
            print("1. Pergi ke Learning")
            print("2. Lihat Profile")
            print("3. Keluar")
            choice = input("Masukkan pilihan: ")

            if choice == '1':
                self.go_to_learning()
            elif choice == '2':
                self.view_profile()
            elif choice == '3':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def go_to_learning(self):
        learning_instance = Learning()
        learning_instance.check_schedule()

        while True:
            print("\nPilih tindakan di Learning:")
            print("1. Beri Nilai Mahasiswa")
            print("2. Kembali")
            action = input("Masukkan pilihan: ")

            if action == '1':
                self.give_grade(learning_instance)
            elif action == '2':
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def give_grade(self, learning_instance):
        nim = input("Masukkan NIM Mahasiswa: ")
        mahasiswa = Mahasiswa(nim, "")  
        matakuliah = input("Masukkan matakuliah: ")
        mahasiswa.matakuliah = matakuliah
        nilai = float(input("Masukkan nilai: "))
        learning_instance.mahasiswa = mahasiswa  
        learning_instance.isi_nilai(mahasiswa, nilai)

    
    def view_profile(self):
        print("Biodata Dosen:")
        print(f"Nama: {self.username}")
        print("NIDN: 1234567890")  
        print("Jabatan: Dosen Tetap")  
        print("Email: tubagus@example.com")  
        print("No. Telepon: 081234567890")  

