from Question import *
from colorama import Fore ,Style


mengetik(Style.BRIGHT +"BERIKUT ADALAH CONTOH\nPROGRAM PYTHON 3.9 SOAL TANYA JAWAB :\nMARSHALL SETIAN PROGRAMING")

soal = [Question(Fore.LIGHTYELLOW_EX + "\n1.BAHASA INGGRIS MERAH ADALAH :\n",["GREEN","BLUE","RED","YELLOW","PURPLE"],"RED"),
        Question(Fore.LIGHTYELLOW_EX + "\n2.BAHASA INGGRIS BIRU ADALAH :\n",["GREEN","BLUE","RED","YELLOW","PURPLE"],"BLUE"),
        Question(Fore.LIGHTYELLOW_EX + "\n3.BAHASA INGGRIS KUNING ADALAH :\n",["GREEN","BLUE","RED","YELLOW","PURPLE"],"YELLOW")]

score = 0
for x in soal:
    x.cetak_pertanyaan()
    benar = x.cetak_opsi
    if benar:
        mengetik(Fore.LIGHTGREEN_EX + "JAWABAN KAMU BENAR!!!")
    else:
        mengetik(Fore.RED + "JAWABAN KAMU SALAH!!!")
    if benar:score+=1
    mengetik(Fore.CYAN + "\nJUMLAH JAWABAN YANG BENAR ADALAH : " + str(score))


mengetik(str("\nini adalah akhir dari program....."))





