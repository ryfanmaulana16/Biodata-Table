def pro():
    # try:
     nis1 =  int(input("Nis        : "))
     nama1 = str(input("Nama       : "))
     alamat1 = str(input("Alamat     : "))
     jenkel1 = str(input("JenKel     : "))
     nohp1 = int(input("NoHp       : "))
     berat1 = int(input("Berat      : "))
     tinggi1 = int(input("Tinggi     : "))
     print("")

     nis2 = int(input("Nis        : "))
     nama2 = str(input("Nama       : "))
     alamat2 = str(input("Alamat     : "))
     jenkel2 = str(input("JenKel     : "))
     nohp2 = int(input("NoHp       : "))
     berat2 = int(input("Berat      : "))
     tinggi2 = int(input("Tinggi     : "))

     print("-------------------------------------------------")
     print("BIODATA SISWA SMK BLA BLA")
     print("KELAS 10")
     print("TAHUN 2020")
     print("RYFAN")
     print("-------------------------------------------------")
     from tabulate import tabulate
     print(tabulate([[nis1, nama1, alamat1, jenkel1, nohp1, berat1, tinggi1],
                     [nis2, nama2, alamat2, jenkel2, nohp2, berat2, tinggi2]],
                    headers=['Nis', 'Nama', 'Alamat', 'JK', 'No Hp', 'Berat', 'Tinggi']))

    # except:
    #   print("Kesalahan Penulisan Data")
    #   pro()

if __name__ == "__main__":
        pro()
