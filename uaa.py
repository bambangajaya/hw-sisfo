class UAA:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.krs_database = {}  # Database untuk menyimpan pendaftaran KRS
        self.jadwal_database = {}  # Database untuk menyimpan jadwal
        self.nilai_database = {}  # Database untuk menyimpan nilai

    def login(self):
        input_username = input("Masukkan username uaa: ")
        input_password = input("Masukkan password uaa: ")
        if input_username == self.username and input_password == self.password:
            print("Login berhasil sebagai uaa.")
            return True
        else:
            print("Username atau password uaa salah.")
            return False
        
    def upload_krs(self, nim, jenis_krs):
        if nim not in self.krs_database:
            self.krs_database[nim] = jenis_krs
            print("Pendaftaran KRS berhasil diunggah.")
        else:
            print("Pendaftaran KRS untuk mahasiswa dengan NIM tersebut sudah ada.")
      
    def upload_jadwal(self, hari, matakuliah, ruang):
        if hari not in self.jadwal_database:
            self.jadwal_database[hari] = {"matakuliah": matakuliah, "ruang": ruang}
            print("Jadwal berhasil diunggah.")
        else:
            print("Jadwal untuk hari tersebut sudah ada.")

    def upload_nilai(self, nim, matakuliah, nilai):
        if nim not in self.nilai_database:
            self.nilai_database[nim] = {matakuliah: nilai}
            print("Nilai berhasil diunggah.")
        else:
            if matakuliah not in self.nilai_database[nim]:
                self.nilai_database[nim][matakuliah] = nilai
                print("Nilai berhasil diunggah.")
            else:
                print("Nilai untuk matakuliah tersebut sudah diunggah sebelumnya.")

