from mahasiswa import Mahasiswa
from dosen import Dosen
from Learning import Learning
import operator1 
from uaa import UAA

if __name__ == "__main__":
    mahasiswa1 = Mahasiswa("422023005", "bambang123")
    dosen1 = Dosen("Tubagus Ahmad Marzuqi", "12345")
    learning_instance = Learning()

    print("Selamat datang! Silakan login untuk melanjutkan.")

    
    role = input("Apakah Anda dosen, mahasiswa, atau operator? (d/m/o/u): ")

    if role == 'd':
        
        if dosen1.login():
            print("Login berhasil sebagai dosen.")
            
            dosen1.use_dosen()

            mahasiswa_target = Mahasiswa("NIM_Mahasiswa_Target", "Password_Mahasiswa_Target")
            nilai = 85
            dosen1.beri_nilai(learning_instance, mahasiswa_target, nilai)

           
        else:
            print("Login gagal. Silakan coba lagi.")
    elif role == 'm':
    
        mahasiswa1.use_mahasiswa()
    elif role == 'o':

        operator1.login()

    if role == 'u':
        uaa_instance = UAA("uaa", "uaa123")  # Buat objek uaa
    if uaa_instance.login():  # Panggil metode login dari objek uaa_instance
        print("Login berhasil sebagai uaa.")
        while True:
            print("\nPilih tindakan:")
            print("1. Upload Pendaftaran KRS")
            print("2. Upload Nilai")
            print("3. Upload Jadwal")
            print("4. Keluar")
            choice = input("Masukkan pilihan: ")
            if choice == '1':
                nim = input("Masukkan NIM Mahasiswa: ")
                jenis_krs = input("Masukkan jenis KRS (paket/non paket): ")
                uaa_instance.upload_krs(nim, jenis_krs)
            elif choice == '2':
                nim = input("Masukkan NIM Mahasiswa: ")
                matakuliah = input("Masukkan matakuliah: ")
                nilai = float(input("Masukkan nilai: "))
                uaa_instance.upload_nilai(nim, matakuliah, nilai)
            elif choice == '3':
                hari = input("Masukkan hari: ")
                matakuliah = input("Masukkan matakuliah: ")
                ruang = input("Masukkan ruang: ")
                uaa_instance.upload_jadwal(hari, matakuliah, ruang)
            elif choice == '4':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
else:
    print("Peran tidak valid.")

   
        
