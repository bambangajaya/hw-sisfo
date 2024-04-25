class Operator:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        input_username = input("Masukkan username operator: ")
        input_password = input("Masukkan password operator: ")
        if input_username == self.username and input_password == self.password:
            print("Login berhasil sebagai operator.")
            return True
        else:
            print("Username atau password operator salah.")
            return False

    def maintain_system(self):
        print("Menjaga sistem...")
       

    def support_dosen(self):
        print("Memberikan dukungan kepada dosen...")
       

def login():
    operator = Operator("admin", "admin123")  
    if operator.login():
       print("Login berhasil sebagai operator.")
       while True:
            print("\nPilih tindakan:")
            print("1. Menjaga Sistem")
            print("2. Memberikan Dukungan kepada Dosen")
            print("3. Keluar")
            choice = input("Masukkan pilihan: ")

            if choice == '1':
                operator.maintain_system()
                print("sistem sedang anda pantau!!!")
            elif choice == '2':
                operator.support_dosen()
                print("anda sedang mengaktifkan mode support dosen!!!")
            elif choice == '3':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    else:
        print("Login gagal. Silakan coba lagi.")

if __name__ == "__main__":
    login()
