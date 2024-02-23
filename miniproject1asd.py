class Baju :
    def __init__ (self,warna,ukuran,stok,harga,jeniskelamin):
        self.warna = warna
        self.ukuran = ukuran
        self.stok = stok
        self.harga = harga
        self.jeniskelamin = jeniskelamin

class Stokk :
    def __init__(self):
        self.jumlahstok = []
    def kriet(self, warna,ukuran,stok,harga,jeniskelamin):
        tambah = Baju(warna,ukuran,stok,harga,jeniskelamin )
        self.jumlahstok.append(tambah)
    def delet(self,hapus):
        if hapus <= len(self.jumlahstok):
            del self.jumlahstok[hapus - 1]
            print ("Data Berhasil Dihapus")
    def readd(self):
        if self.jumlahstok:
            for index,baju in enumerate(self.jumlahstok):
                print(f"\nBaju {index + 1}:")
                self.read(baju)
        else:
            print ("daftar kosong")
    def read(self,baju):
        print("======================================")
        print("Warna:",baju.warna)
        print("Ukuran:",baju.ukuran)
        print("Stok:",baju.stok)
        print("Harga:",baju.harga)
        print("Jenis Kelamin:", baju.jeniskelamin)
        print("======================================")
    def updet(self,ganti):
        if ganti <= len(self.jumlahstok):
            baju = self.jumlahstok[ganti -1]
            baju.warna = input("Silahkan masukkan warna baru : ")
            baju.ukuran = input ("Silahkan masukkan ukuran baru : ")
            baju.stok = int(input ("Silahkan masukkan jumlah stok baru : "))
            baju.harga = int(input("Silahkan masukkan harga baru : "))
            baju.jeniskelamin = input("Silahkan masukkan jenis kelamin aju : ")
            print ("Data berhasil diupdate")

def main ():
    tes = Stokk()
    while True:
        print ("+========================================================+")
        print ("| Selamat datang di toko baju david, silahkan pilih menu |")
        print ("|                1. Buat barang baru                     |")
        print ("|                2. Lihat daftar barang                  |")
        print ("|                3. Update list barang                   |")
        print ("|                4. Hapus barang                         |")
        print ("|                5. Keluar Program                       |")
        print ("+========================================================+")
        mau = int(input("Silahkan pilih menu 1/2/3/4/5 : "))
        if mau == 1:
            print ("======================================")
            print ("|          MEMBUAT DATA BARU         |")
            print ("======================================")
            print ("|        SILAHKAN MASUKKAN DATA      |")
            print ("======================================")
            warna = input ("Masukkan Warna Baju : ")
            ukuran = input("Masukkan Ukuran Baju : ")
            stok = int(input("Masukkan Jumlah Stock : "))
            harga = int(input("Masukkan Harga Baju : "))
            jeniskelamin = input("Masukkan Jenis Kelamin Baju : ")
            tes.kriet(warna,ukuran,stok,harga,jeniskelamin)
            print ("Penambahan Stok Berhasil!")
        elif mau == 2:
            tes.readd()
        elif mau == 3:
            print ("==================================================")
            ganti = int(input("Masukkan Nomor Baju Yang Mau Diganti : "))
            print ("==================================================")
            tes.updet(ganti)
        elif mau == 4:
            hapus = int(input ("Masukkan nomor baju yang ingin dihapus : "))
            if hapus >= 1 :
                if tes.delet(hapus):
                    print ("Data berhasil dihapus")
                else :
                    print ("Data baju tidak ada")
            else :
                print ("Silahkan input angka yang valid")
        elif mau == 5:
            print ("Terimakasih sudah menggunakan program ini!")
            break
        else:
            print ("Input tidak tersedia")
main()