
from registration import Registration
from profiles import Profiles
from Learning import Learning  

class Mahasiswa:
    def __init__(self, username, password):
        self.username = username
        self.password = password 
        self.profiles = Profiles()
        self.learning_instance = Learning() 

    def login(self):
        input_username = input("Masukkan username: ")
        input_password = input("Masukkan password: ")
        if input_username == self.username and input_password == self.password:
            print("Login berhasil sebagai mahasiswa.")
            return True
        else:
            print("Username atau password salah.")
            return False

    def profile(self):
        self.profiles.show_profiles()

    def registration(self):
        registration = Registration()
        jenis_krs = input("Masukkan jenis KRS (paket/non paket): ")
        registration.register_krs(jenis_krs)
        self.profiles.kembali()

    def use_learning(self):
        print("Anda dapat menggunakan fitur learning sekarang:")
        self.learning_instance.check_schedule()
        self.learning_instance.check_grades()
        self.learning_instance.check_classroom()

    def use_mahasiswa(self):
        if self.login():
            self.choose_option()
        else:
            print("Silakan login terlebih dahulu untuk menggunakan fitur.")

    def choose_option(self):
        while True:
            print("Pilih opsi:")
            print("1. Profile")
            print("2. Registrasi")
            print("3. Learning")
            print("4. Keluar")
            option = input("Pilihan: ")
            if option == "1":
                self.profile()
            elif option == "2":
                self.registration()
            elif option == "3":
                self.use_learning()
            elif option == "4":
                print("Keluar dari program.")
                exit()
            else:
                print("Opsi tidak valid.")
