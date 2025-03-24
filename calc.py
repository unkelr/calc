# Author: Unk?
import requests
import json
from colorama import Fore, Style
import os
import time
import random
import sys
# Author: Unk?

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def title():
    if os.name == 'nt':
        os.system("title github.com/unkelr")
title()
clearscreen()

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
api_base = 'https://discord.com/api/v9'

random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=4))


def mainscreen():
    print(f'''{Fore.GREEN}
                                             --------------------------------
                                                       {Fore.RESET}ᵍᶦᵗʰᵘᵇ ᵘⁿᵏᵉˡʳ{Fore.GREEN}
                                            {Fore.RESET}           ╔═╗╔═╗╦  ╔═╗{Fore.GREEN}
                                            {Fore.RESET}           ║  ╠═╣║  ║  {Fore.GREEN}
                                            {Fore.RESET}           ╚═╝╩ ╩╩═╝╚═╝{Fore.GREEN}
                                             --------------------------------
                                                    {Fore.RESET}1. {Fore.GREEN}Get Servers
                                                    {Fore.RESET}2. {Fore.GREEN}Get Friends
                                                    {Fore.RESET}3. {Fore.GREEN}Get Info
                                                    {Fore.RESET}4. {Fore.GREEN}MassDM
                                                    {Fore.RESET}5. {Fore.GREEN}Change Activity
                                                    {Fore.RESET}6. {Fore.GREEN}Exit
''')

if token == "":
    print(f"{Fore.GREEN}Enter your token{Fore.RESET} (it will save in config.)")
    token = input(f"{Fore.RESET}Token ->{Fore.GREEN} ")
    config['token'] = token
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)
    print(f"{Fore.RESET}Token saved to {Fore.GREEN}config.json{Fore.RESET}")
else:
    print(f"{Fore.RESET}Token loaded from {Fore.GREEN}config.json{Fore.RESET}")
time.sleep(1)
clearscreen()

def tokenresolve_todiscordname():
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(f'{api_base}/users/@me', headers=headers)
    data = response.json()
    print(f"Welcome. {Fore.GREEN}{data['username']}{Fore.RESET} To CALC.")

tokenresolve_todiscordname()
time.sleep(2)
clearscreen()

def create_progress_bar(duration=2.5, width=50):

    for i in range(width + 1):
        percent = i / width * 100
        
        bar = f'                                   [{"#" * i}{" " * (width - i)}]'
        
        clearscreen()
        
        if i % 3 == 0:
            print(f'''{Fore.GREEN}
                                             --------------------------------
                                                       {Fore.RESET}ᵍᶦᵗʰᵘᵇ ᵘⁿᵏᵉˡʳ{Fore.GREEN}
                                            {Fore.RESET}           ╔═╗╔═╗╦  ╔═╗{Fore.GREEN}
                                            {Fore.RESET}           ║  ╠═╣║  ║  {Fore.GREEN}
                                            {Fore.RESET}           ╚═╝╩ ╩╩═╝╚═╝{Fore.GREEN}
                                             --------------------------------
                                                        {Fore.RESET}Loading.{Fore.GREEN}                                   
''')
        elif i % 3 == 1:
            print(f'''{Fore.GREEN}
                                             --------------------------------
                                                       {Fore.RESET}ᵍᶦᵗʰᵘᵇ ᵘⁿᵏᵉˡʳ{Fore.GREEN}
                                            {Fore.RESET}           ╔═╗╔═╗╦  ╔═╗{Fore.GREEN}
                                            {Fore.RESET}           ║  ╠═╣║  ║  {Fore.GREEN}
                                            {Fore.RESET}           ╚═╝╩ ╩╩═╝╚═╝{Fore.GREEN}
                                             --------------------------------
                                                        {Fore.RESET}Loading..{Fore.GREEN}                                   
''')
        else:
            print(f'''{Fore.GREEN}
                                             --------------------------------
                                                       {Fore.RESET}ᵍᶦᵗʰᵘᵇ ᵘⁿᵏᵉˡʳ{Fore.GREEN}
                                            {Fore.RESET}           ╔═╗╔═╗╦  ╔═╗{Fore.GREEN}
                                            {Fore.RESET}           ║  ╠═╣║  ║  {Fore.GREEN}
                                            {Fore.RESET}           ╚═╝╩ ╩╩═╝╚═╝{Fore.GREEN}
                                             --------------------------------
                                                        {Fore.RESET}Loading...{Fore.GREEN}                                   
''')
        
        print(f'{Fore.GREEN}{bar} {Fore.RESET}{percent:.0f}%')
        time.sleep(duration / width)
    clearscreen()
    print(f'''{Fore.GREEN}
                                             --------------------------------
                                                       {Fore.RESET}ᵍᶦᵗʰᵘᵇ ᵘⁿᵏᵉˡʳ{Fore.GREEN}
                                            {Fore.RESET}           ╔═╗╔═╗╦  ╔═╗{Fore.GREEN}
                                            {Fore.RESET}           ║  ╠═╣║  ║  {Fore.GREEN}
                                            {Fore.RESET}           ╚═╝╩ ╩╩═╝╚═╝{Fore.GREEN}
                                             --------------------------------
                                                    {Fore.RESET}Loading Complete!{Fore.GREEN}                                   
''')

create_progress_bar()
clearscreen()
mainscreen()

def get_user_servers():
    output_dir = 'outputs/servers'
    os.makedirs(output_dir, exist_ok=True)

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(f'{api_base}/users/@me/guilds', headers=headers)
    data = response.json()
    for i in data:
        print(f"{Fore.RESET}Server -:{Fore.GREEN}  {i['name']}{Fore.RESET} | {Fore.RESET}ID -:{Fore.GREEN}  {i['id']}{Fore.RESET} | {Fore.RESET}Owner -:{Fore.GREEN}  {i['owner']}{Fore.RESET}")
    print(f"--------------------------------\nsave all servers to a file? {Fore.GREEN}(y/n)")
    save = input().lower()
    
    if save == 'y':
        filename = os.path.join(output_dir, f'{random_string}_servers.txt')
        with open(filename, 'w', encoding='utf-8') as f:
            for i in data:
                f.write(f"{i['name']} | {i['id']} | {i['owner']}\n")
        print(f"{Fore.RESET}All servers saved to {Fore.GREEN}{filename}")
    else:
        print(f"{Fore.RESET}Not saved{Fore.GREEN}")


def get_user_friends():
    output_dir = 'outputs/friends'
    os.makedirs(output_dir, exist_ok=True)

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(f'{api_base}/users/@me/relationships', headers=headers)
    data = response.json()
    for i in data:
        print(f"{Fore.RESET}Friend -:{Fore.GREEN}  {i['user']['username']}#{i['user']['discriminator']}{Fore.RESET} | {Fore.RESET}ID -:{Fore.GREEN}  {i['id']}{Fore.RESET} | {Fore.RESET}Type -:{Fore.GREEN}  {i['type']}{Fore.RESET}")
    print(f"--------------------------------\nsave all friends to a file? {Fore.GREEN}(y/n)")
    save = input().lower()

    if save == 'y':
        filename = os.path.join(output_dir, f'{random_string}_friends.txt')
        with open(filename,
                    'w', encoding='utf-8') as f:
                for i in data:
                    f.write(f"{i['user']['username']}#{i['user']['discriminator']} | {i['id']} | {i['type']}\n")
        print(f"{Fore.RESET}All friends saved to {Fore.GREEN}{filename}")
    else:
        print(f"{Fore.RESET}Not saved{Fore.GREEN}")

def get_user_info():
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(f'{api_base}/users/@me', headers=headers)
    data = response.json()
    print(f"                                                    {Fore.RESET}Username -:{Fore.GREEN}  {data['username']}#{data['discriminator']}{Fore.RESET}\n                                                    {Fore.RESET}ID -:{Fore.GREEN}  {data['id']}{Fore.RESET}\n                                                    {Fore.RESET}Email -:{Fore.GREEN}  {data['email']}{Fore.RESET}\n                                                    {Fore.RESET}Phone -:{Fore.GREEN}  {data['phone']}{Fore.RESET}\n                                                    {Fore.RESET}MFA -:{Fore.GREEN}  {data['mfa_enabled']}{Fore.RESET}")

def user_massdm_friends():
    content = input(f"{Fore.RESET}                                              msg? ->{Fore.GREEN} ")
    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v10/users/@me/channels", headers=headers).json()
    if content == "":
        print(f"{Fore.RESET}                                         Message cannot be empty{Fore.GREEN}")
    for channel in channelIds:
        try:
            requests.post(
                f'https://discord.com/api/v9/channels/{channel["id"]}/messages',
                headers=headers,
                data={"content": f"{content}"}
            )
            time.sleep(2)
            print(f"{Fore.RESET}                                         ✅ | {Fore.GREEN}User: {Fore.RESET}{channel['id']}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RESET}                                         ✖️ | {Fore.RED}User: {channel['id']} | {e}{Fore.RESET}")

def user_change_activity():
    url = f'{api_base}/users/@me/settings'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    activity = input(f"{Fore.RESET}                                         activity? ->{Fore.GREEN} ")
    payload = json.dumps({
        'custom_status': {
            'text': activity
        }
    })
    response = requests.patch(url, headers=headers, data=payload)
    if activity == "":
        print("You removed your activity.")
        pass
    if response.status_code == 200:
        print(f"{Fore.RESET}                                         Activity changed to {Fore.GREEN}{activity}{Fore.RESET}")
    else:
        print(f"{Fore.RESET}                                         Failed to change activity{Fore.GREEN}")


if __name__ == '__main__':
    while True:
        option = input(f"{Fore.RESET}                                                   ->{Fore.GREEN} ")
        if option == '1':
            clearscreen()
            get_user_servers()
        elif option == '2':
            clearscreen()
            get_user_friends()
        elif option == '3':
            get_user_info()
            input(f"                                                    {Fore.RESET}Press enter to continue")
        elif option == '4':
            user_massdm_friends()
        elif option == '5':
            user_change_activity()
        elif option == '6':
            break
        else:
            print(f"                                                    {Fore.RESET}Invalid option{Fore.GREEN}")
        time.sleep(1)
        clearscreen()
        mainscreen()