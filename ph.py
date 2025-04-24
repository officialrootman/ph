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
        # Sosyal Medya Platformları
        "GitHub": "https://github.com/{username}",
        "Twitter": "https://twitter.com/{username}",
        "Instagram": "https://www.instagram.com/{username}",
        "Pinterest": "https://www.pinterest.com/{username}",
        "Reddit": "https://www.reddit.com/user/{username}",
        "Facebook": "https://www.facebook.com/{username}",
        "LinkedIn": "https://www.linkedin.com/in/{username}",
        "TikTok": "https://www.tiktok.com/@{username}",
        "Tumblr": "https://{username}.tumblr.com",
        
        # İçerik ve Video Platformları
        "YouTube": "https://www.youtube.com/{username}",
        "Vimeo": "https://vimeo.com/{username}",
        "Flickr": "https://www.flickr.com/people/{username}",
        "Dailymotion": "https://www.dailymotion.com/{username}",
        "Twitch": "https://www.twitch.tv/{username}",
        
        # Geliştirici Platformları
        "Dev.to": "https://dev.to/{username}",
        "Medium": "https://medium.com/@{username}",
        "HackerRank": "https://www.hackerrank.com/{username}",
        "CodePen": "https://codepen.io/{username}",
        "Stack Overflow": "https://stackoverflow.com/users/{username}",
        "Replit": "https://replit.com/@{username}",
        "GitLab": "https://gitlab.com/{username}",
        
        # Yaratıcı Platformlar
        "Dribbble": "https://dribbble.com/{username}",
        "Behance": "https://www.behance.net/{username}",
        "SoundCloud": "https://soundcloud.com/{username}",
        "Spotify": "https://open.spotify.com/user/{username}",
        
        # Diğer Platformlar
        "Goodreads": "https://www.goodreads.com/{username}",
        "Last.fm": "https://www.last.fm/user/{username}",
        "AngelList": "https://angel.co/u/{username}",
        "Product Hunt": "https://www.producthunt.com/@{username}",
        "Kaggle": "https://www.kaggle.com/{username}",
        "Bandcamp": "https://bandcamp.com/{username}"
    }

    check_username(args.username, platforms)

if __name__ == "__main__":
    main()