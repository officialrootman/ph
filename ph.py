import requests
import argparse
from colorama import Fore, Style, init
import concurrent.futures
import time
from urllib.parse import urlparse
import json
from datetime import datetime
import os

# Initialize colorama
init(autoreset=True)

class UsernameFinder:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.results = []
        self.load_platforms()

    def load_platforms(self):
        self.platforms = {
            # Sosyal Medya Platformları
            "GitHub": {
                "url": "https://github.com/{username}",
                "error_type": "404",
                "category": "Geliştirici"
            },
            "Twitter": {
                "url": "https://twitter.com/{username}",
                "error_type": "404",
                "category": "Sosyal Medya"
            },
            # ... (mevcut platformlar aynı formatta devam eder)
            
            # Yeni Türk Platformları
            "Ekşi Sözlük": {
                "url": "https://eksisozluk.com/biri/{username}",
                "error_type": "404",
                "category": "Türk Platformları"
            },
            "GittiGidiyor": {
                "url": "https://profil.gittigidiyor.com/{username}",
                "error_type": "404",
                "category": "Türk Platformları"
            },
            "Onedio": {
                "url": "https://onedio.com/{username}",
                "error_type": "404",
                "category": "Türk Platformları"
            }
        }

    def check_single_username(self, platform_name, platform_data, username):
        start_time = time.time()
        result = {
            "platform": platform_name,
            "url": platform_data["url"].format(username=username),
            "category": platform_data["category"],
            "status": "Bulunamadı",
            "response_time": 0
        }

        try:
            response = self.session.get(
                result["url"], 
                timeout=10,
                allow_redirects=False
            )
            result["response_time"] = round(time.time() - start_time, 2)

            if response.status_code == 200:
                result["status"] = "Bulundu"
                self.print_result(result, Fore.GREEN)
            else:
                self.print_result(result, Fore.RED)

        except requests.RequestException as e:
            result["status"] = f"Hata: {str(e)}"
            self.print_result(result, Fore.YELLOW)

        self.results.append(result)
        return result

    def print_result(self, result, color):
        print(f"{color}[{result['status']}] {result['platform']} ({result['category']}) - "
              f"Response Time: {result['response_time']}s{Style.RESET_ALL}")

    def save_results(self, username):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"results_{username}_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                "username": username,
                "scan_date": datetime.now().isoformat(),
                "results": self.results
            }, f, indent=4, ensure_ascii=False)
        
        print(f"\n{Fore.CYAN}[*] Sonuçlar kaydedildi: {filename}{Style.RESET_ALL}")

    def search(self, username, max_workers=10):
        print(f"\n{Fore.CYAN}[*] Kullanıcı Adı Taranıyor: {username}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Toplam Platform Sayısı: {len(self.platforms)}{Style.RESET_ALL}\n")

        start_time = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_platform = {
                executor.submit(
                    self.check_single_username, 
                    platform_name, 
                    platform_data, 
                    username
                ): platform_name 
                for platform_name, platform_data in self.platforms.items()
            }

            concurrent.futures.wait(future_to_platform)

        total_time = round(time.time() - start_time, 2)
        
        # İstatistikleri hesapla
        found_count = len([r for r in self.results if r["status"] == "Bulundu"])
        error_count = len([r for r in self.results if r["status"].startswith("Hata")])
        
        print(f"\n{Fore.CYAN}=== Tarama Sonuçları ==={Style.RESET_ALL}")
        print(f"Toplam Süre: {total_time} saniye")
        print(f"Bulunan Hesaplar: {found_count}")
        print(f"Bulunamayan Hesaplar: {len(self.results) - found_count - error_count}")
        print(f"Hata Sayısı: {error_count}")
        
        self.save_results(username)

def main():
    parser = argparse.ArgumentParser(description="Gelişmiş Kullanıcı Adı Arama Aracı")
    parser.add_argument("username", help="Aranacak kullanıcı adı")
    parser.add_argument("-w", "--workers", type=int, default=10, help="Maksimum eşzamanlı işlem sayısı")
    args = parser.parse_args()

    finder = UsernameFinder()
    finder.search(args.username, max_workers=args.workers)

if __name__ == "__main__":
    main()