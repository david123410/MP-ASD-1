
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Baju:
    def __init__(self, warna, ukuran, stok, harga, jeniskelamin):
        self.warna = warna
        self.ukuran = ukuran
        self.stok = stok
        self.harga = harga
        self.jeniskelamin = jeniskelamin

class Stokk:
    def __init__(self):
        self.head = None
        self.recorddata()
    
    def recorddata(self):
        self.head = Node(Baju ("hijau","l",1,100000,"L"))
        self.head.next = Node(Baju("kuning","s",15,200000,"L"))
        self.head.next.next = Node(Baju ("merah","xl",9,300000,"P"))
        self.head.next.next.next = Node(Baju("biru","xxl",2,500000,"L"))
    
    def kriet(self, warna, ukuran, stok, harga, jeniskelamin):
        node_baru = Node(Baju(warna, ukuran, stok, harga, jeniskelamin))
        keriet = input("Mau menambah node dari depan/tengah/belakang : ")
        if keriet == "depan":
            node_baru.next = self.head
            self.head = node_baru
        elif keriet == "tengah":
            tambahnomor = int(input("Mau tambah di nomor berapa : "))
            pilihan = tambahnomor - 1
            if pilihan < 0:
                print("Pilihan tidak tersedia")
            else:
                index = 0
                noderil = self.head
                while noderil is not None and index < pilihan:
                    noderil = noderil.next
                    index = +1
                    if noderil is not None:
                        node_baru.next = noderil.next
                        noderil.next = node_baru
                    else:
                        print("Data tidak ada")
        elif keriet == "belakang":
            if self.head == None:
                self.head = node_baru
            else:
                noderil = self.head
                while noderil.next is not None:
                    noderil = noderil.next
                noderil.next = node_baru
                print("Baju berhasil ditambahkan")
        else:
            print("Pilihan tidak tersedia")

    def delet(self):
        hapus = input("Mau hapus dari depan/tengah/belakang? : ")
        if hapus == "depan":
            if self.head == None:
                print("Node Kosong")
                pass
            else:
                self.head = self.head.next
        if hapus == "tengah":
            nohapus = int(input("Masukkan nomor baju yang mau dihapus : "))
            ppp = nohapus - 1
            if self.head is None:
                print("Node kosong")
            else:
                if nohapus == 1:
                    self.head = self.head.next
                else:
                    noderil = self.head
                    index = 0
                    while noderil.next is not None and index < ppp:
                        noderil = noderil.next
                        index += 1
                        if noderil.next is not None:
                            hapusnode = noderil.next
                            noderil.next = hapusnode.next
                        else:
                            print("Nomor baju tidak ditemukan")
        if hapus == "belakang":
            prev = None
            noderil = self.head
            while noderil.next is not None:
                noderil = noderil.next
                prev = noderil
                noderil = noderil.next
            prev.next = None

    def sorting(self, nodes,sorting):
        if sorting == "harga":
            if len(nodes) <= 1:
                print("data tidak ada / kurang banyak")
            else:
                apasih = input("mau ascending / descending : ")
                if apasih == "ascending":
                    nodes.sort(key=lambda x: x.data.harga)
                elif apasih == "descending":
                    nodes.sort(key=lambda x: x.data.harga, reverse=True)
        elif sorting == "stok":
            if len(nodes) <= 1:
                print("data tidak ada / kurang banyak")
            else:
                apasih = input("mau ascending / descending : ")
                if apasih == "ascending":
                    nodes.sort(key=lambda x: x.data.stok)
                elif apasih == "descending":
                    nodes.sort(key=lambda x: x.data.stok, reverse=True)
        self.head = nodes[0]
        noderil = self.head
        for node in nodes[1:]:
            noderil.next = node
            noderil = noderil.next
        noderil.next = None

    def readd(self):
        noderil = self.head
        if noderil == None:
            print("List kosong")
        else:
            index = 0
            while noderil:
                print(f"\nBaju {index + 1}:")
                self.read(noderil.data)
                noderil = noderil.next
                index += 1

    def read(self, baju):
        print("======================================")
        print("Warna:", baju.warna)
        print("Ukuran:", baju.ukuran)
        print("Stok:", baju.stok)
        print("Harga:", baju.harga)
        print("Jenis Kelamin:", baju.jeniskelamin)
        print("======================================")

    def updet(self):
        print("==================================================")
        tanya = int(input("Masukkan Nomor baju yang mau diganti : "))
        print("==================================================")
        index = tanya - 1
        noderil = self.head
        while noderil is not None and index >= 1:
            noderil = noderil.next
            index -= 1
        if noderil is not None:
            print("==================================================")
            warnabaru = input("Masukkan Warna Baru : ")
            ukuranbaru = input("Masukkan ukuran baju baru : ")
            stokbaru = int(input("Masukkan jumlah stok baju : "))
            hargabaru = int(input("Masukkan harga baju : "))
            jkbaru = input("Masukkan jenis kelamin baju L/P : ")
            print("==================================================")
            noderil.data = Baju(warnabaru, ukuranbaru, stokbaru, hargabaru, jkbaru)
            print("Data sudah diubah")
        else:
            print("Data tidak ada")

    def cariharga(self,nodes,charga):
        a = len(nodes)
        jump = int(a ** 0.5)
        prev = 0
        noderil = self.head
        while noderil:
            while prev in range (a) and nodes [min(jump,a)-1].data.harga < charga:
                prev = jump
                jump += int (a ** 0.5)
                if prev >= a:
                    return -1
            while prev < min(jump, a) and nodes[prev].data.harga < charga: 
                prev += 1
            if prev in range (a) and nodes[prev].data.harga == charga:
                return prev
            noderil = noderil.next
        return -1

    def caristok(cstok,nodes,self):
        a = len(nodes)
        jump = int(a ** 0.5)
        prev = 0
        noderil = self.head
        while noderil:
            while prev in range (a) and nodes [min(jump,a)-1].data.stok < cstok:
                prev = jump
                jump += int (a ** 0.5)
                if prev >= a:
                    return -1
            while prev < min(jump, a) and nodes[prev].data.stok < cstok: 
                prev += 1
            if prev in range (a) and nodes[prev].data.stok == cstok:
                return prev
            noderil = noderil.next
        return -1

def main():
    tes = Stokk()
    while True:
        print("+========================================================+")
        print("| Selamat datang di toko baju david, silahkan pilih menu |")
        print("|                1. Buat barang baru                     |")
        print("|                2. Lihat daftar barang                  |")
        print("|                3. Update list barang                   |")
        print("|                4. Hapus barang                         |")
        print("|                5. Sorting list barang                  |")
        print("|                6. Searching (Gunakan Setelah Sorting)  |")
        print("|                7. Keluar Program                       |")
        print("+========================================================+")
        mau = int(input("Silahkan pilih menu 1/2/3/4/5 : "))
        if mau == 1:
            print("======================================")
            print("|          MEMBUAT DATA BARU         |")
            print("======================================")
            print("|        SILAHKAN MASUKKAN DATA      |")
            print("======================================")
            warna = input("Masukkan Warna Baju : ")
            ukuran = input("Masukkan Ukuran Baju : ")
            stok = int(input("Masukkan Jumlah Stock : "))
            harga = int(input("Masukkan Harga Baju : "))
            jeniskelamin = input("Masukkan Jenis Kelamin Baju L/P : ")
            tes.kriet(warna, ukuran, stok, harga, jeniskelamin)
            print("Penambahan Stok Berhasil!")
        elif mau == 2:
            tes.readd()
        elif mau == 3:
            tes.updet()
        elif mau == 4:
            tes.delet()
        elif mau == 5:
            sorting = input("Mau sorting berdasarkan apa? harga / stok : ")
            if sorting in ["harga", "stok"]:
                nodes = []
                noderil = tes.head
                while noderil:
                    nodes.append(noderil)
                    noderil = noderil.next
                tes.sorting(nodes,sorting)
                print("Sorting berhasil dilakukan!")
            else:
                print("Pilihan tidak tersedia")
        elif mau == 6:
            cari = input("Mau cari berdasarkan harga / stok : ")
            if cari == "harga":
                charga = int(input("Mau cari harga berapa : "))
                ketemu = tes.cariharga(nodes,charga)
                print("Searching berhasil dilakukan!")
                if ketemu !=-1:
                    print (f"Baju ada di node ke-{ketemu}")
                else : 
                    print ("Tidak ada")
            elif cari == "stok":
                cstok = int(input ("Masukkan jumlah stok yang dicari : "))
                ketemu = tes.cstok(nodes,cstok)
                print("Searching berhasil dilakukan!")
                if ketemu !=-1:
                    print (f"Baju ada di node ke-{ketemu}")
                else : 
                    print ("Tidak ada")
        elif mau == 7:
            print("Terimakasih sudah menggunakan program ini!")
            break
        else:
            print("Input tidak tersedia")

main()