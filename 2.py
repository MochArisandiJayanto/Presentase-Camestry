import random
import time
from termcolor import cprint

# Noted!
# Jangan lupa instal termcolor, untuk bisa menggunakan fitur warna
# pip install termcolor


cprint('''
------------------------------------
|    selamat datang di program     |
|   presentase chemistry antara    |
|        Eluwh dan bliaw           |
------------------------------------
'''.upper(), "cyan")

a = 0
while a == 0:
    nama_eluwh = input("\nMasukkan Nama Eluwih: ")
    nama_bliaw = input("Masukkan Nama Bliaw: ")
    random_eluwh = random.randint(0, 100)
    random_bliaw = 100 - random_eluwh
    cprint(f"Eluwh, {nama_eluwh}, [{random_eluwh}%]", "blue")
    cprint(f"Bliaw, {nama_bliaw}, [{random_bliaw}%]", "yellow")

    if random_eluwh < random_bliaw:
        tes = f"Wahhh Bliaw({nama_bliaw}) Ternyata Lebih Peka, dari pada Eluwh({nama_eluwh})"
        for j in tes:
            cprint(j, "green", end='',flush=True)
            time.sleep(0.1)
    elif random_eluwh > random_bliaw:
        tes = f"Wahhh Eluwh({nama_eluwh}) Ternyata Lebih Peka, dari pada Bliaw({nama_bliaw})"
        for j in tes:
            cprint(j, "green", end='',flush=True)
            time.sleep(0.1)
    elif random_eluwh == random_bliaw:
        # print(f"Wahhh Ternyata Eluwh({nama_eluwh}) dan Bliaw({nama_bliaw}) Sama-sama Peka")

        tes = f"Wahhh Ternyata Eluwh({nama_eluwh}) dan Bliaw({nama_bliaw}) Sama-sama Peka"
        for j in tes:
            cprint(j, "green", end='',flush=True)
            time.sleep(0.1)
    else:
        continue
    
    tanya = input("\nApakah ingin mengulang? [y/t] ")

    if tanya == "y" or tanya == "Y":
        continue
    elif tanya == "t" or tanya == "T":
        a += 1
    else:
        cprint("Masukan yang anda inputkan tidak sesuai dengan perintah yang ada.".upper(), "red")
        break