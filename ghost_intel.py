import os
import sys
import asyncio
import aiohttp

# Nettoyage de l'écran automatique
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. SCANNER DE PSEUDONYME ULTRA-RAPIDE
async def check_site(session, site_name, url_template, username):
    url = url_template.format(username)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        timeout = aiohttp.ClientTimeout(total=8)
        async with session.get(url, headers=headers, timeout=timeout, ssl=False) as response:
            if response.status == 200:
                print(f"[\033[92m+\033[0m] {site_name}: {url}")
            elif response.status == 404:
                print(f"[\033[91m-\033[0m] {site_name}: Introuvable")
            else:
                print(f"[\033[93m?\033[0m] {site_name}: Code {response.status}")
    except Exception:
        print(f"[\033[91m!\033[0m] {site_name}: Erreur de connexion")

async def scan_username(username):
    platforms = {
        "GitHub": "https://github.com{}",
        "Instagram": "https://instagram.com{}",
        "TikTok": "https://tiktok.com@{}",
        "Pinterest": "https://pinterest.com{}",
        "Twitter-X": "https://x.com{}",
        "YouTube": "https://youtube.com@{}"
    }
    
    print(f"\n[\033[94m*\033[0m] Recherche globale pour : {username}...\n")
    async with aiohttp.ClientSession() as session:
        tasks = [check_site(session, name, template, username) for name, template in platforms.items()]
        await asyncio.gather(*tasks)
    input("\nAppuyez sur Entrée pour revenir au menu...")

# 2. TRACKER D'ADRESSE IP (Nouveau outil fonctionnel)
async def track_ip():
    print(f"\n[\033[94m*\033[0m] Initialisation du Tracker IP...")
    target_ip = input("Entrez l'adresse IP à tracker (ou Entrée pour votre propre IP) : ").strip()
    
    url = f"http://ip-api.com/json/{target_ip}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                res = await response.json()
                
                if res.get("status") == "success":
                    print(f"\n\033[92m[+] Informations récoltées pour l'IP {res.get('query')} :\033[0m")
                    print(f"[-] Pays         : {res.get('country')} ({res.get('countryCode')})")
                    print(f"[-] Région       : {res.get('regionName')}")
                    print(f"[-] Ville        : {res.get('city')}")
                    print(f"[-] Code Postal  : {res.get('zip')}")
                    print(f"[-] Opérateur    : {res.get('isp')}")
                    print(f"[-] Organisation : {res.get('org')}")
                    print(f"[-] Latitude     : {res.get('lat')}")
                    print(f"[-] Longitude    : {res.get('lon')}")
                    print(f"[-] Fuseau Hor.  : {res.get('timezone')}")
                else:
                    print(f"[\033[91m!\033[0m] Impossible de récupérer les infos : {res.get('message')}")
    except Exception as e:
        print(f"[\033[91m!\033[0m] Erreur lors de la requête : {e}")
        
    input("\nAppuyez sur Entrée pour revenir au menu principal...")

# 3. MENU PRINCIPAL
def main_menu():
    while True:
        clear_screen()
        print("""
\033[95m  ________ __                     __     .___        __   
 /  _____//  |__   ____  _______/  |_   |   | _____/  |_  
/   \  __\  |  \ /  _ \/  ___/\   __\  |   |/    \   __\ 
\   \_\  \   Y  (  <_> )___ \  |  |    |   |   |  \  |   
 \______  /__|_  /\____/____  > |__|    |___|___|  /__|   
        \/     \/           \/                   \/      \033[0m
==========================================================
        \033[94m=== GHOST INTEL PRO - MULTI-TOOL v2 ===\033[0m
==========================================================
1. Scanner un pseudonyme (Ultra-Fast OSINT)
2. Tracker une adresse IP (Géolocalisation)
3. Analyser un numéro (À venir)
4. Quitter le script
==========================================================
        """)
        choix = input("Choisissez une option (1-4) : ").strip()
        
        if choix == "1":
            pseudo = input("\nEntrez le pseudonyme à rechercher : ").strip()
            if pseudo:
                asyncio.run(scan_username(pseudo))
        elif choix == "2":
            asyncio.run(track_ip())
        elif choix == "3":
            print("\nOption Téléphone bientôt prête...")
            input("\nAppuyez sur Entrée...")
        elif choix == "4":
            print("\n\033[93mFermeture. Au revoir !\033[0m")
            sys.exit()
        else:
            input("\nOption invalide ! Appuyez sur Entrée...")

if __name__ == "__main__":
    main_menu()
