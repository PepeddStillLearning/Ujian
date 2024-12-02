nama_mr = input("Masukkan Nama :") #nama pemesan
nomor_mr = int(input("Masukkan Nomor Antrian :")) #nomor antrian
jumlah_order = int(input("Masukkan Jumlah Pesanan :")) #jumlah pesanan

try:
            with open("Cafe.txt", "w", encoding="utf-8") as file_gwejh:
                width = 87
                file_gwejh.write(f"{' ' * ((width - len('Cafe Sigma Skibidi')) // 2)}Cafe Sigma Skibidi\n")
                file_gwejh.write(f"{' ' * ((width - len('Daily Order')) // 2)}Daily Order\n\n")

                file_gwejh.write(f"Nomor : {nomor_mr:02d}\n")
                file_gwejh.write(f"Nama Pemesan : {nama_mr}\n")
                file_gwejh.write(f"Monday, 12 December 2024\n")
                file_gwejh.write("=" * 70 + "\n")
                file_gwejh.write("Item" + " " * (50) + "AMT(Rp)\n")

                for x in range (1, jumlah_order + 1):
                    FnB = input("Masukkan Makanan atau Minuman yang ingin dipesan :") #makanan dan minuman
                    price = int(input("Masukkan Harga makanan atau minuman yang ingin dipesan :")) #harga makanan dan minuman
                    jumlah_beli = int(input("Masukkan Jumlah makanan atau minuman yang ingin dipesan :")) #harga makanan dan minuman

                    file_gwejh.write(f"{FnB} {price}\n")
                file_gwejh.write("=" * 70 + "\n")    

except ValueError:
        print ("Input Tidak Valid")
