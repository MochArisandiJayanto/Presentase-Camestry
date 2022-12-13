import random
import time
from colorama import Fore, Style

teks = f'''
{Fore.LIGHTYELLOW_EX}------------------------------------{Style.RESET_ALL}
{Fore.LIGHTYELLOW_EX}|{Style.RESET_ALL}    {Fore.LIGHTCYAN_EX}SELAMAT DATANG DI PROGRAM{Style.RESET_ALL}     {Fore.LIGHTYELLOW_EX}|{Style.RESET_ALL}
{Fore.LIGHTYELLOW_EX}|{Style.RESET_ALL}   {Fore.LIGHTCYAN_EX}PRESENTASE CHEMISTRY ANTARA{Style.RESET_ALL}    {Fore.LIGHTYELLOW_EX}|{Style.RESET_ALL}
{Fore.LIGHTYELLOW_EX}|{Style.RESET_ALL}        {Fore.LIGHTCYAN_EX}ELUWH DAN BLIAW{Style.RESET_ALL}           {Fore.LIGHTYELLOW_EX}|{Style.RESET_ALL}
{Fore.LIGHTYELLOW_EX}------------------------------------{Style.RESET_ALL}
'''

for huruf in teks:
  print(huruf,end='',flush=True)
  time.sleep(0.02)

while True:
    eluwh = input(f"\n{Fore.MAGENTA}Masukkan Nama Eluwh: {Style.RESET_ALL}")
    bliaw = input(f"{Fore.YELLOW}Masukkan Nama Bliaw: {Style.RESET_ALL}")
    random_eluwh = random.randint(0, 100)
    random_bliaw = 100 - random_eluwh
    print(f"Eluwh, {Fore.MAGENTA}{eluwh}{Style.RESET_ALL}, [{Fore.BLUE}{random_eluwh}%{Style.RESET_ALL}]")
    print(f"Bliaw, {Fore.YELLOW}{bliaw}{Style.RESET_ALL}, [{Fore.BLUE}{random_bliaw}%{Style.RESET_ALL}]")

    if random_eluwh < random_bliaw:
        print(f"Wahhh {Fore.YELLOW}Bliaw({bliaw}){Style.RESET_ALL} Ternyata Lebih Peka, dari pada {Fore.MAGENTA}Eluwh({eluwh}){Style.RESET_ALL}")
    elif random_eluwh > random_bliaw:
        print(f"Wahhh {Fore.MAGENTA}Eluwh({eluwh}){Style.RESET_ALL} Ternyata Lebih Peka, dari pada {Fore.YELLOW}Bliaw({bliaw}){Style.RESET_ALL}")
    elif random_eluwh == random_bliaw:
        print(f"Wahhh Ternyata {Fore.MAGENTA}Eluwh({eluwh}){Style.RESET_ALL} dan {Fore.YELLOW}Bliaw({bliaw}){Style.RESET_ALL} Sama-sama Peka")
    else:
        continue
    

    pembantu = "True"
    while pembantu=="True":
        tanya = input(f"\nApakah ingin mengulang? [{Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}t{Style.RESET_ALL}] ")

        if tanya == "y" or tanya == "Y":
            pembantu="False"
            continue
        elif tanya == "t" or tanya == "T":
            pembantu = "Berhenti"
            print(f"{Fore.RED}Sistem Berhenti{Style.RESET_ALL}, {Fore.GREEN}Terimakasih Sudah Mengguanakan Program Prsentase Chemistry.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Error! Masukan yang anda inputkan tidak sesuai dengan perintah yang ada. Silahkan masukkan lagi.{Style.RESET_ALL}")
    
    if pembantu == "Berhenti":
        break