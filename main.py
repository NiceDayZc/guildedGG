import threading
import httpx, random, itertools, os
from colorama import Fore

os.system("cls")

INVITE = input("INVITE > ")
USERNAME = input("USERNAME > ")

with open("data/proxies.txt", encoding="utf-8") as s:
    proxies = itertools.cycle([i.strip() for i in s if i])

def gen():
    username = USERNAME + " | "+ "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=4))
    email =  f"NiceDayZc" + "_" + "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8)) + random.choice(["@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com", "@protonmail.com"])
    proxy = {
        "http://": "http://" + next(proxies),
        "https://": "http://" + next(proxies),
    }
    client = httpx.Client(proxies=proxy)
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'fr-FR,fr;q=0.9',
        'content-type': 'application/json',
        'guilded-device-type': 'desktop',
        'origin': 'https://www.guilded.gg',
        'referer': 'https://www.guilded.gg/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'dnt': '1',
        "Sec-Ch-Ua": '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        "Sec-Ch-Ua-Mobile": '?0',
        "Sec-Ch-Ua-Platform": "macOS",
        }
    try:
        response = client.post("https://www.guilded.gg/api/users?type=email", headers=headers, 
        json={"extraInfo": {"platform": "desktop","referrerId": ""},"name": username,"email": email,"password": "NiceDayZc#1001","fullName": username})
        if "email" in response.json()["user"]:
            print(f"({Fore.GREEN}!{Fore.RESET}) Make This ({username}{response.cookies['hmac_signed_session'][:40]})")
            client.cookies.set('hmac_signed_session', response.cookies['hmac_signed_session'])
            client.put(f"https://www.guilded.gg/api/invites/{INVITE}", headers=headers)
            with open("data/cookies.txt", "a") as f:
                f.write(f"{response.cookies['hmac_signed_session']}\n")
                f.close()
        else:
            pass
    except Exception:
        pass

def start_thread():
    threading.Thread(target=gen).start()

def run():
    Threadz = int("10000000") #best Thread lol
    for i in range(Threadz):
        threading.Thread(target=start_thread).start()

run()