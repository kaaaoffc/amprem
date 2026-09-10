import os
import sys
import time
import requests

# Color Palette (ANSI Escape Codes)
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
WHITE = "\033[1;37m"
GRAY = "\033[0;90m"
RESET = "\033[0m"

BASE_URL = "https://aliicia.my.id/api/amprem"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def draw_header(title, subtitle=""):
    clear_screen()
    width = 54
    print(f"{MAGENTA}┌" + "─" * (width - 2) + f"┐{RESET}")
    print(f"{MAGENTA}│{WHITE}" + title.center(width - 2) + f"{MAGENTA}│{RESET}")
    if subtitle:
        print(f"{MAGENTA}│{CYAN}" + subtitle.center(width - 2) + f"{MAGENTA}│{RESET}")
    print(f"{MAGENTA}└" + "─" * (width - 2) + f"┘{RESET}\n")

def print_contact():
    print(f"{CYAN}◆ INFORMASI KONTAK{RESET}")
    print(f"{GRAY}──────────────────────────────────────────────────────{RESET}")
    print(f" {WHITE}WhatsApp {RESET}: 085126041172")
    print(f" {WHITE}Telegram {RESET}: t.me/saturn07officiall")
    print(f" {WHITE}TikTok   {RESET}: @kaaaoffc")
    print(f"{GRAY}──────────────────────────────────────────────────────{RESET}\n")

def magic_link_v1():
    draw_header("MAGIC LINK", "Method V1 - Email & Verification")
    
    print(f"{CYAN}◆ STEP 1 - EMAIL{RESET}")
    print(f"{GRAY}──────────────────────────────────────────────────────{RESET}")
    email = input(f"{WHITE}Gmail            >{RESET} ").strip()
    
    if not email:
        print(f"{RED}x Email tidak boleh kosong!{RESET}")
        time.sleep(2)
        return

    print(f"\n{GRAY}Memproses permintaan magic link...{RESET}")
    try:
        res = requests.get(f"{BASE_URL}?action=send&email={email}", timeout=15).json()
        if res.get("status"):
            print(f"{GREEN}✓ Permintaan magic link berhasil diproses.{RESET}")
            print(f"{GREEN}  Periksa inbox Gmail Anda.{RESET}\n")
        else:
            print(f"{RED}x {res.get('message', 'Gagal mengirim email verifikasi.')}{RESET}\n")
            time.sleep(2)
            return
    except Exception as e:
        print(f"{RED}x Error koneksi API: {e}{RESET}\n")
        time.sleep(2)
        return

    print(f"{CYAN}◆ STEP 2 - VERIFIKASI{RESET}")
    print(f"{GRAY}──────────────────────────────────────────────────────{RESET}")
    print(f"{GRAY}Salin URL magic link dari email Anda.{RESET}")
    link = input(f"{WHITE}Magic link       >{RESET} ").strip()

    if not link:
        print(f"{RED}x Link verifikasi tidak boleh kosong!{RESET}")
        time.sleep(2)
        return

    print(f"\n{GRAY}Verifikasi akun...{RESET}")
    try:
        res_verif = requests.get(f"{BASE_URL}?action=verif&email={email}&link={link}", timeout=15).json()
        if res_verif.get("status"):
            print(f"{GREEN}✓ Verifikasi berhasil.{RESET}\n")
            print(f"{GREEN}┌" + "─" * 52 + f"┐{RESET}")
            print(f"{GREEN}│ Operation completed successfully.".ljust(53) + f"│{RESET}")
            print(f"{GREEN}└" + "─" * 52 + f"┘{RESET}\n")
        else:
            print(f"{RED}x {res_verif.get('message', 'Verifikasi gagal.')}{RESET}\n")
    except Exception as e:
        print(f"{RED}x Error koneksi API: {e}{RESET}\n")

    ans = input(f"{CYAN}Kembali ke menu utama? [Y/n] >{RESET} ").strip().lower()
    if ans == 'n':
        sys.exit()

def magic_link_v2():
    draw_header("MAGIC LINK", "Method V2 - Bulk Account Generator")
    
    print(f"{CYAN}◆ BULK GENERATOR{RESET}")
    print(f"{GRAY}──────────────────────────────────────────────────────{RESET}")
    try:
        amount = int(input(f"{WHITE}Jumlah Akun      >{RESET} ").strip())
    except ValueError:
        print(f"{RED}x Jumlah harus berupa angka!{RESET}")
        time.sleep(2)
        return

    print(f"\n{GRAY}Memproses generate bulk account...{RESET}")
    try:
        res = requests.get(f"{BASE_URL}?action=bulk&amount={amount}", timeout=30).json()
        if res.get("status"):
            result = res.get("result", {})
            print(f"{GREEN}✓ Berhasil membuat {result.get('success_count')} akun.{RESET}\n")
            for acc in result.get("accounts", []):
                print(f" {WHITE}Email:{RESET} {acc.get('email')} | {WHITE}Paket:{RESET} {acc.get('package')}")
            print(f"\n{GREEN}┌" + "─" * 52 + f"┐{RESET}")
            print(f"{GREEN}│ Operation completed successfully.".ljust(53) + f"│{RESET}")
            print(f"{GREEN}└" + "─" * 52 + f"┘{RESET}\n")
        else:
            print(f"{RED}x {res.get('message', 'Gagal generate bulk akun.')}{RESET}\n")
    except Exception as e:
        print(f"{RED}x Error koneksi API: {e}{RESET}\n")

    ans = input(f"{CYAN}Kembali ke menu utama? [Y/n] >{RESET} ").strip().lower()
    if ans == 'n':
        sys.exit()

def menu_magic_link():
    while True:
        draw_header("MAGIC LINK", "Alight Motion")
        print(f"{CYAN}◆ PILIH METODE{RESET}")
        print(f"{GRAY}──────────────────────────────────────────────────────{RESET}")
        print(f"  {WHITE}1{RESET}  {WHITE}V1{RESET}                  GET - API Single (Verif)")
        print(f"  {WHITE}2{RESET}  {WHITE}V2{RESET}                  POST - API Bulk Generator")
        print(f"  {WHITE}0{RESET}  {WHITE}KEMBALI{RESET}             Menu utama\n")

        pilihan = input(f"{WHITE}Pilih > {RESET}").strip()
        if pilihan == "1":
            magic_link_v1()
        elif pilihan == "2":
            magic_link_v2()
        elif pilihan == "0":
            break

def main():
    while True:
        draw_header("X-SATURN TOOLKIT", "Toolkit v1.0")
        print_contact()
        print(f"{CYAN}◆ CATEGORY MENU{RESET}")
        print(f"{GRAY}──────────────────────────────────────────────────────{RESET}")
        print(f"  {WHITE}1{RESET}  {WHITE}TOOLS{RESET}               Encode / Decode file")
        print(f"  {WHITE}2{RESET}  {WHITE}MAGIC LINK{RESET}          Alight Motion V1 / V2")
        print(f"  {WHITE}3{RESET}  {WHITE}WEB TOOLS{RESET}           Web TO APK / Source / ZIP")
        print(f"  {WHITE}4{RESET}  {WHITE}AI TOOLS{RESET}            Strom-Ai interactive chat")
        print(f"  {WHITE}5{RESET}  {WHITE}DOWNLOADER{RESET}          TikTok public media")
        print(f"  {WHITE}0{RESET}  {WHITE}EXIT{RESET}                Tutup aplikasi\n")

        pilihan = input(f"{WHITE}Pilih kategori > {RESET}").strip()

        if pilihan == "1":
            print(f"\n{GRAY}[!] Fitur TOOLS sedang dikembangkan.{RESET}")
            time.sleep(1.5)
        elif pilihan == "2":
            menu_magic_link()
        elif pilihan == "3":
            print(f"\n{GRAY}[!] Fitur WEB TOOLS sedang dikembangkan.{RESET}")
            time.sleep(1.5)
        elif pilihan == "4":
            print(f"\n{GRAY}[!] Fitur AI TOOLS sedang dikembangkan.{RESET}")
            time.sleep(1.5)
        elif pilihan == "5":
            print(f"\n{GRAY}[!] Fitur DOWNLOADER sedang dikembangkan.{RESET}")
            time.sleep(1.5)
        elif pilihan == "0":
            clear_screen()
            print(f"{CYAN}Terima kasih telah menggunakan X-Saturn Toolkit!{RESET}\n")
            sys.exit()

if __name__ == "__main__":
    main()
    
