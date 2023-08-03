import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)

class Question :
    acak = True
    def __init__(self,pertanyaan,opsi,jawaban):
        self.pertanyaan=pertanyaan
        self.opsi=opsi
        self.jawaban=jawaban
    def cetak_pertanyaan(self):
        print(self.pertanyaan)
    @property

    def cetak_opsi(self) :
        if self.acak:
            random.shuffle(self.opsi)
        c = 0
        for x in self.opsi:
            print (str(c)+"."+x)
            c+=1
        pilihan = int(input("\nMASUKKAN JAWABAN (DENGAN ANGKA) : "))

        if self.opsi[pilihan] == self.jawaban :
            return True
        else:
            return False
