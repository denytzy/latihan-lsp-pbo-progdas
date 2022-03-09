def garis():
    print("------------------------------")

#tampilan menu
print("------------------ Hotel Smk Jakarta Pusat 1 -------------------")
print("-- Lama Inap ----- Superior ------- Deluxe ------ Premium-")
print("- 1 s.d 2 Hari  - 100.000/Night- 150.000/Night - 200.000/Night -")
print("- 3 s.d 4 Hari  - 90.000/Night - 135.000/Night - 180.000/Night -")
print("- 5 Hari Keatas - 80.000/Night - 120.000/Night - 160.000/Night -")

#input data
tipe_kamar = input("Masukkan Tipe Kamar : ")
lama_inap = int(input("Masukkan Lama Menginap : "))



#tipe_superior
if tipe_kamar == "Superior":
    if lama_inap <= 2:
        total_harga = 1000000*lama_inap
    elif lama_inap <= 4:
        total_harga = 90000*lama_inap
    else:
        total_harga = 80000*lama_inap

#tipe_deluxe
elif tipe_kamar == "Deluxe":
    if lama_inap <= 2:
        total_harga = 150000*lama_inap
    elif lama_inap <= 4:
        total_harga = 135000*lama_inap
    else:
        total_harga = 120000*lama_inap

#tipe_premium
elif tipe_kamar == "Premium":
    if lama_inap <= 2:
        total_harga = 200000*lama_inap
    elif lama_inap <= 4:
        total_harga = 180000*lama_inap
    else:
        total_harga = 160000*lama_inap

#total harga menginap
garis()
print("Tipe Kamar Yang Dipilih : ", (tipe_kamar))
print("Lama Menginap : ", (lama_inap), "Hari")
print("Total Harga Yang Dibayar : Rp. ", (total_harga))

