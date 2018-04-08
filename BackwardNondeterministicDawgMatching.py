#  kodun calismasi icin kodun bulundugu adres de 'metin.txt' dosyasi mevcut olmalidir
from tkinter import *
from tkinter.filedialog import askopenfilename


def d_bul(kelime, harf):
    print("")
    print("-----------------D BUL-----------------")
    print(str(harf) + "  " + str(kelime))
    d = ""
    toplam = 0
    for h in kelime:
        if h == harf:
            d += "1"
            toplam += 1
        else:
            d += "0"
    print("d: ", d)
    print("---------------------------------------")
    print("")
    return d, toplam


def shift_left(d):
    shifted_d = ""
    i = 1
    while i < len(d):
        shifted_d += str(d[i])
        i += 1
    shifted_d += "0"
    return shifted_d


def d_and_shifted_d(d, shifted_d):
    tmp = ""
    for i in range(len(d)):
        if str(d[i]) == "1" and str(shifted_d[i]) == "1":
            tmp += "1"
        else:
            tmp += "0"
    print("AND isleminin sonucunda elde edilen d: ", tmp)
    print("")
    return tmp


def main():
    import time
    tic = time.clock()
    metin_dosyasi = open("metin.txt", "r")
    metin = metin_dosyasi.read()
    metin_dosyasi.close()

    log_dosyasi = open("log.txt", "a")
    sonuc_dosyasi = open("sonuc.txt", "r+")
    sonuc_dosyasi.truncate()

    import datetime
    log_dosyasi.write(str(datetime.datetime.now()) + "\n\n")
    sonuc_dosyasi.write(str(datetime.datetime.now()) + "\n\n")

    log_dosyasi.write("------------------------------METIN------------------------------\n\n")
    log_dosyasi.write(metin + "\n")
    log_dosyasi.write("-----------------------------------------------------------------\n\n")

    sonuc_dosyasi.write("------------------------------METIN------------------------------\n\n")
    sonuc_dosyasi.write(metin + "\n\n")
    sonuc_dosyasi.write("-----------------------------------------------------------------\n\n")

    kelime = E1.get()  # input("Arayacaginiz kelimeyi girin...\n=> ")
    log_dosyasi.write("Aranan kelime:  " + str(kelime) + "\n\n")
    sonuc_dosyasi.write("Aranan kelime:  " + str(kelime) + "\n\n")

    kelime_bulundu = False
    konum = 0  # kelimenin metin de yerlestirildigi konum

    while not kelime_bulundu and konum + len(kelime) <= len(metin):
        shift = len(kelime)  # kayma durumunda kelimenin metin de kac harf kaydirilmasi gerektigini tutan degisken
        indeks = 1  # inceledigimiz alt dizide sagdan kacinci harfe baktigimizi gosteren degisken
        sonuc_dosyasi.write("Ana metinde inceledigimiz alt metin: " +
                            str(metin[konum:konum + (len(kelime) - indeks + 1)]) + "\n")
        log_dosyasi.write("Ana metinde inceledigimiz alt metin: " +
                            str(metin[konum:konum + (len(kelime) - indeks + 1)]) + "\n")
        sonuc_dosyasi.write("Bir sonraki shift miktari:  " + str(shift) + "\n")
        log_dosyasi.write("Bir sonraki shift miktari:  " + str(shift) + "\n")
        print("Ana metinde inceledigimiz alt metin: " + str(metin[konum:konum + (len(kelime) - indeks + 1)]))
        print("")
        print("Bir sonraki shift miktari: ", shift)
        print("")
        d, d_toplam = d_bul(kelime, metin[konum + (len(kelime) - indeks)])
        #  d nin ne oldugunu anlamak icin alttaki link den bakabilirsiniz, sayfa 18-25
        #  d_toplam degiskeni d de 1 rakami var mi yok mu kontrol etmek icin tutuluyor
        #  http://www.powershow.com/view/134a6-OWQ0N/Master_Course_powerpoint_ppt_presentation
        sonuc_dosyasi.write("Bakilan harf:  " + str(metin[konum + (len(kelime) - indeks)]) + "\n")
        sonuc_dosyasi.write("Hesaplanan d:  " + str(d) + "\n")
        log_dosyasi.write("Bakilan harf:  " + str(metin[konum + (len(kelime) - indeks)]) + "\n")
        log_dosyasi.write("Hesaplanan d:  " + str(d) + "\n")
        while d_toplam != 0 and indeks <= len(kelime):
            # d yi Shift etme islemi
            print("d: "+d)
            if int(d[0]):  # d deki ilk rakam 1 ise
                shift = len(kelime) - indeks
                print("Bir sonraki kaydirma miktari: ", shift)
                sonuc_dosyasi.write("Bir sonraki shift miktari:  " + str(shift) + "\n")
                log_dosyasi.write("Bir sonraki shift miktari:  " + str(shift) + "\n")
            shifted_d = shift_left(d)
            #  shifted_d, bir onceki d nin bir sola kaymis hali
            print("Shifted d: "+shifted_d)
            print("")
            sonuc_dosyasi.write("Eski d'nin bir sola kaydirilmis hali:  " + shifted_d + "\n")
            log_dosyasi.write("Eski d'nin bir sola kaydirilmis hali:  " + shifted_d + "\n")
            # d yi Shift etme isleminin sonu
            indeks += 1
            d, d_toplam = d_bul(kelime, metin[konum + (len(kelime) - indeks)])
            d = d_and_shifted_d(d, shifted_d)
            #  yeni d yi hesaplamak icin onceki d nin kaydirilmis hali ile yeni harfin d sini AND leme islemi
            sonuc_dosyasi.write("Bakilan harf:  " + str(metin[konum + (len(kelime) - indeks)]) + "\n")
            sonuc_dosyasi.write("Hesaplanan yeni d:  " + str(d) + "\n")
            log_dosyasi.write("Bakilan harf:  " + str(metin[konum + (len(kelime) - indeks)]) + "\n")
            log_dosyasi.write("Hesaplanan yeni d:  " + str(d) + "\n")
            d_toplam = 0
            #  yeni d deki 1 lerin sayisini bulmak icin yeni d deki rakamlarin toplamini hesapliyoruz
            for i in d:
                if str(i) == "1":
                    d_toplam += 1
        if indeks > len(kelime):
            kelime_bulundu = True
        if not kelime_bulundu:
            konum += shift  # Kelime metinin icinde kaydiriliyor
            print(str(shift) + " HARF KAYDIRMA GERCEKLESTI")
            print("_______________________________________")
            print("_______________________________________")
            print("\n\n")
            sonuc_dosyasi.write("\n" + str(shift) + " HARF KAYDIRMA GERCEKLESTI\n\n"
                                                    "-----------------------------------------------------------------"
                                                    "\n\n")
            log_dosyasi.write("\n" + str(shift) + " HARF KAYDIRMA GERCEKLESTI\n\n"
                                                  "-----------------------------------------------------------------"
                                                  "\n\n")
    toc = time.clock()
    if kelime_bulundu:
        # Kelime metin de mevcut ise konumu yaziliyor
        print("Kelime bulundu, konum: " + str(konum))
        sonuc_dosyasi.write("Kelime bulundu, konum: " + str(konum) + "\n\nKodun calima suresi:  " + str(toc - tic))
        log_dosyasi.write("Kelime bulundu, konum: " + str(konum) + "\n\nKodun calima suresi:  " + str(toc - tic) +
                                                                   "\n\n_______________________________________________"
                                                                   "_________________________________________________\n"
                                                                   "___________________________________________________"
                                                                   "_____________________________________________\n"
                                                                   "_______________________________________________"
                                                                   "_________________________________________________"
                                                                   "\n\n\n")
    else:
        print("Kelime bulunamadi")
        sonuc_dosyasi.write("Kelime bulunamadi" + "\n\nKodun calima suresi:  " + str(toc - tic))
        log_dosyasi.write("Kelime bulunamadi" + "\n\nKodun calima suresi:  " + str(toc - tic) +
                                                "\n\n_______________________________________________"
                                                "_________________________________________________\n"
                                                "___________________________________________________"
                                                "_____________________________________________\n"
                                                "_______________________________________________"
                                                "_________________________________________________\n\n\n")
    sonuc_dosyasi.close()
    log_dosyasi.close()
    print("\nKodun calisma suresi(saniye):  " + str(toc - tic))


def refresh():
    sonuc_frame = Frame(top, width=100, height=300).grid(row=1, column=3, rowspan=4)
    sonuc = Text(sonuc_frame, borderwidth=3, relief="sunken")
    sonuc.config(font=("consolas", 10), undo=True, wrap='word')
    sonuc.grid(row=0, column=3, rowspan=3, sticky="nsew", padx=2, pady=2)

    sonuc_dosyasi = open("sonuc.txt", "r")
    sonuc.insert(INSERT, sonuc_dosyasi.read())
    sonuc_dosyasi.close()


def botton():
    main()
    refresh()


def newtext():
    fname = askopenfilename(filetypes=(("Template files", "*.txt"), ("All files", "*.*")))
    try:
        metin_okuma_dosyasi = open(fname, "r")
        metin = metin_okuma_dosyasi.read()
        metin_okuma_dosyasi.close()
        metin_dosyasi = open("metin.txt", "w")
        metin_dosyasi.write(metin)
        metin_dosyasi.close()
    except IOError:
        print("metin dosyasi acilamadi!!")
    sonuc_frame = Frame(top, width=100, height=300).grid(row=1, column=3, rowspan=4)
    sonuc = Text(sonuc_frame, borderwidth=3, relief="sunken")
    sonuc.config(font=("consolas", 10), undo=True, wrap='word')
    sonuc.grid(row=0, column=3, rowspan=3, sticky="nsew", padx=2, pady=2)
    sonuc.insert(INSERT, metin)


top = Tk()
top.title("BACKWARD NON-DETERMINISTIC DAWG MATCHING")
top.geometry('930x376')

L1 = Label(top, text="Pattern", borderwidth=1).grid(row=0, column=0)

E1 = Entry(top, bd=3, bg='yellow', fg='red')
E1.grid(row=0, column=1)

B = Button(top, text="GO", command=botton, activebackground='lightblue1', bg='white')
B.grid(row=0, column=2)

B2 = Button(top, text="NEW", command=newtext, activebackground='lightblue1', bg='white')
B2.grid(row=1, column=2)

B3 = Button(top, text="QUIT", command=quit, activebackground='lightblue1', bg='white')
B3.grid(row=2, column=2)

#fname = askopenfilename(filetypes=(("Template files", "*.txt"), ("All files", "*.*")))
#try:
#    metin_okuma_dosyasi = open(fname, "r")
#    metin = metin_okuma_dosyasi.read()
#    metin_okuma_dosyasi.close()
#    metin_dosyasi = open("metin.txt", "w")
#    metin_dosyasi.write(metin)
#    metin_dosyasi.close()
#except IOError:
#    print("metin dosyasi acilamadi!!")

sonuc_frame = Frame(top, width=100, height=300).grid(row=1, column=3, rowspan=4)
sonuc = Text(sonuc_frame, borderwidth=3, relief="sunken")
sonuc.config(font=("consolas", 10), undo=True, wrap='word')
sonuc.grid(row=0, column=3, rowspan=3, sticky="nsew", padx=2, pady=2)

#sonuc.insert(INSERT, metin)

top.mainloop()

