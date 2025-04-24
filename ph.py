import requests
import argparse
from colorama import Fore, Style

def check_username(username, platforms):
    print(f"{Fore.CYAN}[*] Kullanıcı Adı Aranıyor: {username}{Style.RESET_ALL}")
    for platform, url in platforms.items():
        try:
            response = requests.get(url.format(username=username))
            if response.status_code == 200:
                print(f"{Fore.GREEN}[+] Bulundu: {platform} -> {url.format(username=username)}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[-] Bulunamadı: {platform}{Style.RESET_ALL}")
        except requests.ConnectionError:
            print(f"{Fore.YELLOW}[!] Hata: {platform} sitesine bağlanılamadı.{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description="Kullanıcı Adı Arama Aracı")
    parser.add_argument("username", help="Aranacak kullanıcı adı")
    args = parser.parse_args()

    platforms = {
        "GitHub": "https://github.com/{username}",
        "Twitter": "https://twitter.com/{username}",
        "Instagram": "https://www.instagram.com/{username}",
        "Pinterest": "https://www.pinterest.com/{username}",
        "Reddit": "https://www.reddit.com/user/{username}",
    }

    check_username(args.username, platforms)

if __name__ == "__main__":
    main()