class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Baju :
    def __init__ (self,warna,ukuran,stok,harga,jeniskelamin):
        self.warna = warna
        self.ukuran = ukuran
        self.stok = stok
        self.harga = harga
        self.jeniskelamin = jeniskelamin

class Stokk :
    def __init__(self):
        self.head = None
    def kriet(self, warna,ukuran,stok,harga,jeniskelamin):
        node_baru  = Node(Baju(warna,ukuran,stok,harga,jeniskelamin ))
        keriet = input("Mau menambah node dari depan/belakang : ")
        if keriet == "depan" :
            node_baru.next = self.head 
            self.head = node_baru
        elif keriet == "belakang" :
            if self.head == None :
                self.head = node_baru
            else:
                noderil = self.head
                while noderil.next is not None:
                    noderil =  noderil.next
                noderil.next = node_baru
        else :
            print ("Pilihan tidak tersedia")
    def delet(self):
        if self.head == None : 
            print ("Node Kosong")
            pass
        else:
            self.head = self.head.next
    def readd(self):
        noderil = self.head
        if noderil == None:
            print ("List kosong")
        else:
            index = 0
            while noderil :
                print(f"\nBaju {index + 1}:")
                self.read(noderil.data)
                noderil = noderil.next
                index += 1
    def read(self,baju):
        print("======================================")
        print("Warna:",baju.warna)
        print("Ukuran:",baju.ukuran)
        print("Stok:",baju.stok)
        print("Harga:",baju.harga)
        print("Jenis Kelamin:", baju.jeniskelamin)
        print("======================================")
    def updet(self):
        print ("==================================================")
        tanya = int(input("Masukkan Nomor baju yang mau diganti : "))
        print ("==================================================")
        index = tanya -1
        noderil = self.head
        while noderil is not None and index >= 1:
            noderil = noderil.next
            index -= 1
        if noderil is not None:
            print ("==================================================")
            warnabaru = input("Masukkan Warna Baru : ")
            ukuranbaru =input ("Masukkan ukuran baju baru : ")
            stokbaru =int(input ("Masukkan jumlah stok baju : "))
            hargabaru = int(input("Masukkan harga baju : "))
            jkbaru = input ("Masukkan jenis kelamin baju : ")
            print ("==================================================")
            noderil.data = Baju(warnabaru,ukuranbaru,stokbaru,hargabaru,jkbaru)
            print ("Data sudah diubah")
        else:
            print ("Data tidak ada")

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
            tes.updet()
        elif mau == 4:
            print ("==================================================")
            hapus = int(input ("Masukkan nomor baju yang ingin dihapus : "))
            print ("==================================================")
            if hapus >= 1 :
                tes.delet()
                print ("Data berhasil dihapus")
            else :
                print ("Silahkan input angka yang valid")
        elif mau == 5:
            print ("Terimakasih sudah menggunakan program ini!")
            break
        else:
            print ("Input tidak tersedia")
main()