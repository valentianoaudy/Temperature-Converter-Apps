# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 18:49:10 2022

@author: asus
"""
#Import the Tkinter module
#Tkinter adalah antarmuka Python ke toolkit GUI Tk yang dikirimkan bersama Python
from tkinter import *

#Membuat window utama baru untuk aplikasi GUI dengan nama variabel window
window = Tk()

#Membuat title untuk window utama baru untuk aplikasi GUI dengan nama 'Temperature Converter Apps'
window.title('Temperature Converter Apps')
#Membuat size untuk window utama baru untuk aplikasi GUI dengan ukuran "400x300"
window.geometry("400x300")
#Membuat background untuk window utama baru untuk aplikasi GUI dengan warna "lightgreen"
window.config(bg="lightgreen")

#Membuat sebuah variabel bernama nilaiTemperatur dengan tipe DoubleVar
nilaiTemperatur = DoubleVar()

#Membuat sebuah label untuk window utama GUI dengan nama variabel label_nilai_temperatur dimana pada label tersebut terletak pada window dengan nama "Nilai Temperature", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "lightgreen", dengan batas atas dan bawah 10
label_nilai_temperatur = Label(window, text="Nilai Temperature", font=("Times New Roman", 17), bg="lightgreen", pady=10)
#Mengatur posisi widget pada grid label_nilai_temperatur di window utama
label_nilai_temperatur.grid(row=0, column=0, padx=10, pady=10, sticky=W)

#Membuat sebuah label untuk window utama GUI dengan nama variabel label_titik_dua_1 dimana pada label tersebut terletak pada window dengan nama ":", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "lightgreen"
label_titik_dua_1 = Label(window, text=":", font=("Times New Roman", 17), bg="lightgreen")
#Mengatur posisi widget pada grid label_titik_dua_1 di window utama
label_titik_dua_1.grid(row=0, column=1)

#Membuat sebuah textfield(entry) untuk window utama GUI dengan nama variabel text_entry dimana pada label tersebut terletak pada window dengan nama "", dengan jenis font "Times New Roman", dengan ukuran 17 dengan panjang text 5, dengan isi dari entry adalah nilai dari variabel nilaiTemperatur
text_entry = Entry(window, text="", font=("Times New Roman", 17), width=15, textvariable=nilaiTemperatur)
#Mengatur posisi widget pada grid text_entry di window utama
text_entry.grid(row=0, column=2, padx=10, pady=10)

#Membuat sebuah label untuk window utama GUI dengan nama variabel label_dari dimana pada label tersebut terletak pada window dengan nama "Dari", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "lightgreen"
label_dari = Label(window, text="Dari", font=("Times New Roman", 17), bg="lightgreen")
#Mengatur posisi widget pada grid label_dari di window utama
label_dari.grid(row=1, column=0, padx=10, pady=10, sticky=W)

#Membuat sebuah label untuk window utama GUI dengan nama variabel label_titik_dua_2 dimana pada label tersebut terletak pada window dengan nama ":", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "lightgreen"
label_titik_dua_2 = Label(window, text=":", font=("Times New Roman", 17), bg="lightgreen")
#Mengatur posisi widget pada grid label_titik_dua_2 di window utama
label_titik_dua_2.grid(row=1, column=1)

#Method dengan nama perhitungan dengan isi perhitungan untuk setiap konversi suhu
def perhitungan():
    #Membuat variabel baru bernama buttonDari dengan menampung nilai dari user setelah memilih button_dari untuk pilihan suhu yang akan dikonversi ke
    buttonDari = button_dari.get()
    #Membuat variabel baru bernama buttonKe dengan menampung nilai dari user setelah memilih button_ke untuk pilihan suhu yang ingin di dikonversi setelah memilih button_dari
    buttonKe = button_ke.get()
    #Membuat variabel baru bernama nilai_tempereatur dengan menampung nilai dari variabel nilaiTemperatur
    nilai_tempereatur = int(nilaiTemperatur.get())

    #Membuat perulangan ketika user mengisi buttonDari yaitu °C dan user mengisi buttonKe yaitu °F, maka akan menjalankan perintah if ini
    if buttonDari == "°C" and buttonKe == "°F":
        #Membuat variabel baru bernama hitungan yang menampung nilai dari celcius ke fahrenheit
        hitungan = (nilai_tempereatur * 9/5) + 32
    #Membuat perulangan ketika user mengisi buttonDari yaitu °C dan user mengisi buttonKe yaitu °R, maka akan menjalankan perintah if ini
    elif buttonDari == "°C" and buttonKe == "°R":
        #Membuat variabel baru bernama hitungan yang menampung nilai dari celcius ke reamur
        hitungan = (4/5 * nilai_tempereatur)
    #Membuat perulangan ketika user mengisi buttonDari yaitu °F dan user mengisi buttonKe yaitu °C, maka akan menjalankan perintah if ini
    elif buttonDari == "°F" and buttonKe == "°C":
        #Membuat variabel baru bernama hitungan yang menampung nilai dari fahrenheit ke celcius
        hitungan = (nilai_tempereatur - 32) * 5/9
    #Membuat perulangan ketika user mengisi buttonDari yaitu °F dan user mengisi buttonKe yaitu °R, maka akan menjalankan perintah if ini
    elif buttonDari == "°F" and buttonKe == "°R":
        #Membuat variabel baru bernama hitungan yang menampung nilai dari fahrenheit ke reamur
        hitungan = (nilai_tempereatur - 32) * 4/9
    #Membuat perulangan ketika user mengisi buttonDari yaitu °R dan user mengisi buttonKe yaitu °C, maka akan menjalankan perintah if ini
    elif buttonDari == "°R" and buttonKe == "°C":
        #Membuat variabel baru bernama hitungan yang menampung nilai dari reamur ke celcius
        hitungan = (5/4 * nilai_tempereatur)
    #Membuat perulangan ketika user mengisi buttonDari yaitu °R dan user mengisi buttonKe yaitu °F, maka akan menjalankan perintah if ini
    elif buttonDari == "°R" and buttonKe == "°F":
        #Membuat variabel baru bernama hitungan yang menampung nilai dari reamur ke fahrenheit
        hitungan = (9/4 * nilai_tempereatur) + 32
    #Membuat perulangan ketika user mengisi buttonDari yaitu °C dan user mengisi buttonKe yaitu °C atau mengisi buttonDari yaitu °F dan user mengisi buttonKe yaitu °F atau mengisi buttonDari yaitu °R dan user mengisi buttonKe yaitu °R, maka akan menjalankan perintah if ini
    elif buttonDari == "°C" and buttonKe == "°C" or buttonDari == "°F" and buttonKe == "°F" or  buttonDari == "°R" and buttonKe == "°R":
        #Membuat variabel baru bernama hitungan yang menampung nilai dari variabel nilai_tempereatur
        hitungan = nilai_tempereatur
    #Membuat variabel baru bernama hasil yang akan menampung nilai dari variabel hitungan
    hasil = hitungan
    #Membuat variabel baru bernama label_hasil yang akan menampung nilai dari variabel hasil
    label_hasil.config(text="" + str(hasil))

#Membuat sebuah variabel bertipe Array baru bernama pilihan yang berisi sebuah string yaitu "°C","°F","°R"
pilihan = ["°C","°F","°R"]
#Membuat variabel baru bernama button_dari yang bertipe StringVar()
button_dari = StringVar()
#Mendeklrasikan nilai dari variabel button_dari adalah isi dari variabel pilihan
button_dari.set(pilihan[0])
#Membuat sebuah Menu pilihan dari dengan nama variabel drop dengan isi menu dari isi variabel pilihan dan nilai dari tiap menu adalah dari method perhitungan yang berisikan perhitungan tiap konversi suhu
drop = OptionMenu(window, button_dari, *pilihan, command=perhitungan)
#Mengatur panjang dari Menu pilihan dari yaitu 16, dengan font "Times New Roman" dengan ukuran 12 dan background "yellow"
drop.config(width=16, font=("Times New Roman", 12), bg="yellow")
#Mengatur posisi widget grid dari Menu pilihan dari di window utama
drop.grid(row=1, column=2, padx=10, pady=10)

#Membuat variabel baru bernama button_ke yang bertipe StringVar()
button_ke = StringVar()
#Mendeklrasikan nilai dari variabel button_ke adalah isi dari variabel pilihan
button_ke.set(pilihan[1])
#Membuat sebuah Menu pilihan ke dengan nama variabel drop dengan isi menu dari isi variabel pilihan dan nilai dari tiap menu adalah dari method perhitungan yang berisikan perhitungan tiap konversi suhu
drop = OptionMenu(window, button_ke, *pilihan, command=perhitungan)
#Mengatur panjang dari Menu pilihan ke yaitu 16, dengan font "Times New Roman" dengan ukuran 12 dan background "yellow"
drop.config(width=16, font=("Times New Roman", 12), bg="yellow")
#Mengatur posisi widget grid dari Menu pilihan ke di window utama
drop.grid(row=2, column=2, padx=10, pady=10)

#Membuat sebuah label dari window utama GUI dengan nama variabel label_ke dimana pada label tersebut terletak pada window dengan nama "Ke", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "lightgreen"
label_ke = Label(window, text="Ke", font=("Times New Roman", 17), bg="lightgreen")
#Mengatur posisi widget pada grid label_ke di window utama
label_ke.grid(row=2, column=0, padx=10, pady=10, sticky=W)

#Membuat sebuah label dari window utama GUI dengan nama variabel label_titik_dua_3 dimana pada label tersebut terletak pada window dengan nama ":", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "lightgreen"
label_titik_dua_3 = Label(window, text=":", font=("Times New Roman", 17), bg="lightgreen")
#Mengatur posisi widget pada grid label_titik_dua_3 di window utama
label_titik_dua_3.grid(row=2, column=1)

#Membuat sebuah button dengan nama variabel button_hitung dimana pada button tersebut terletak pada window dengan nama "Hitung", dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "blue"
button_hitung = Button(window, text="Hitung", font=("Times New Roman", 17), bg="blue", command=perhitungan)
#Mengatur posisi widget pada grid button_hitung di window utama
button_hitung.grid(row=3, columnspan=3, padx=10, pady=10)

#Membuat sebuah label dengan nama variabel label_hasil dimana pada label tersebut terletak pada window dengan jenis font "Times New Roman", dengan ukuran 17 dengan background "salmon" yang akan menampung hasil tiap konversi
label_hasil = Label(window, font=("Times New Roman", 17), bg="salmon")
#Mengatur posisi widget pada grid label_hasil di window utama
label_hasil.grid(row=4, columnspan=3, padx=10, pady=10)

#Ada metode yang dikenal dengan nama mainloop() yang digunakan saat aplikasi Anda siap dijalankan yaitu mainloop() adalah infinite loop yang digunakan untuk menjalankan aplikasi, menunggu event terjadi dan memproses event tersebut selama window tidak ditutup
window.mainloop()