import os, json, socket, time, subprocess, sys
from turtle import back
from colorama import Fore
from ipaddress import IPv4Network
import requests

# Copyright (c) 2022 IP4 Attack By TryWarz Inc.
# @uthor : TryWarz
# Company : Codex
# Attack IP4
# chang files json
# I am not responsible for your actions
os.system('title IP4 Attack')
def center(var:str, space:int=None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())



def banner():
    os.system('cls')
    print(center(f"""
    ██╗██████╗ ██╗  ██╗     █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗
    ██║██╔══██╗██║  ██║    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
    ██║██████╔╝███████║    ███████║   ██║      ██║   ███████║██║     █████╔╝ 
    ██║██╔═══╝ ╚════██║    ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ 
    ██║██║          ██║    ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
    ╚═╝╚═╝          ╚═╝    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝""").replace('█', Fore.RED+'█'+Fore.RESET))
    print(Fore.LIGHTGREEN_EX + '                                                → Copyright (c) TryWarz ;) ←' + Fore.RESET)
    print()

def inputs():
    try:
        choice = input(Fore.LIGHTBLACK_EX + 'ENTER : ' + Fore.RESET)
    except:
        pass
    return choice

def CIDR():
    z = 0
    fu = 0
    banner()
    with open('config.json', 'r') as f: # Import Json
        config = json.load(f)

    for addr in IPv4Network(config['IP']['Host']):
        z += 1
        with open(config['file_name']['file_CIDR'] + '.txt', 'a') as fx:
            fx.write(str(addr) + '\n')
            fx.close()
        banner()
        print(center(Fore.RED + f"""
    008 Generated     >   {z}
    088 OUTPUT FILE   >   {config['file_name']['file_CIDR']}
    888 CIDR          >   {config['IP']['Host']}
    800 IP            >   {addr}""").replace('>', Fore.LIGHTBLACK_EX+'>'+Fore.RED))
        
        if config['Discord']['opt'] == "True":
            embeds = [] # Embed Discord
            embed0 = {
                "color": 0xFF0000,
                "fields": [
                            {
                            "name": "INFO", # Title
                            "value": f"Generated {z} \n File Name : {config['file_name']['file_CIDR']} \n CIDR : {config['IP']['Host']} \n IP : {addr}" # description
                            },
                        ]
                    }
            embeds.append(embed0)
            requests.post(config['Discord']['url'],headers={"content-type": "application/json"}, data=json.dumps({"content": "","embeds": embeds,"username": "IP4 Attack","avatar_url": "https://cdn.discordapp.com/avatars/922450497074495539/a_c1738e5280f6e70487ef02d307c62a07?size=1024"}).encode()) # Send Embed

        time.sleep(3)
        

def ScanPort():
    timeout_seconds = 0.5 # timeout
    z = 0
    fu = 0
    banner()
    with open('config.json', 'r') as f: # Import Json
        config = json.load(f)


    with open(str(config['file_name']['file_CIDR'] + '.txt'), 'r') as filehosts:
        for host in filehosts:
            z += 1
            host = host.rstrip("\n")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout_seconds)
            result = sock.connect_ex((host, int(config['IP']['Port'])))
            if result == 0:
                fu += 1
                print(f"""{Fore.GREEN}Successful Connect : {host} {config['IP']['Port']} ---- TRUE""")
                with open(config['IP']['Host'] + "_output_scan.txt", "a") as fc:
                    fc.write('\n' + str(host) + ':' + str(config['IP']['Port']))
                    fc.close()
                    if config['Discord']['opt'] == "True":
                        embeds = [] # Embed Discord
                        embed2 = {
                    "color": 0x27FF00,
                    "fields": [
                            {
                            "name": "Success", # Title
                            "value": f"Successful Connect : {host} {config['IP']['Port']} ---- TRUE" # description
                            },
                        ]
                    }
                        embeds.append(embed2)
                        requests.post(config['Discord']['url'],headers={"content-type": "application/json"}, data=json.dumps({"content": "","embeds": embeds,"username": "IP4 Attack","avatar_url": "https://cdn.discordapp.com/avatars/922450497074495539/a_c1738e5280f6e70487ef02d307c62a07?size=1024"}).encode()) # Send Embed
                        
            else:
                print(f"""                                  {Fore.LIGHTBLACK_EX}Scan : {z} {Fore.LIGHTBLACK_EX}Total Found : {fu} {Fore.LIGHTBLACK_EX}PORT : {config['IP']['Port']} {Fore.LIGHTBLACK_EX}IP : {host}""".replace(':', Fore.RED+":"))

                if config['Discord']['opt'] == "True":
                    embeds = [] # Embed Discord
                    embed = {
                        "color": 0xFF0000,
                        "fields": [
                            {
                            "name": "INFO", # Title
                            "value": f"`🔨` Scan : {z} \n `🔧` Total Found: {fu} \n `📡` PORT : {config['IP']['Port']} \n `🏠` IP: {host}" # description
                            },
                        ]
                    }
                    embeds.append(embed)
                    requests.post(config['Discord']['url'],headers={"content-type": "application/json"}, data=json.dumps({"content": "","embeds": embeds,"username": "IP4 Attack","avatar_url": "https://cdn.discordapp.com/avatars/922450497074495539/a_c1738e5280f6e70487ef02d307c62a07?size=1024"}).encode()) # Send Embed

def help():
    os.system('cls')
    banner()

    print(Fore.RED + """
                            ┍━━━━━━━━━━━━━━━━━━━━━┰━━━━━━━━━━━━━━━━━━━━━━━━━━┰━━━━━━━━━━━━━━━━━┑
                            ┃ -- help             ┃ help command             ┃ Command : True  ┃
                            ┃ -- cidr             ┃ Search IP                ┃ Command : True  ┃
                            ┃ -- scanport         ┃ Start Attack             ┃ Command : True  ┃
                            ┃ -- back             ┃ Back Home                ┃ Command : True  ┃
                            ┗━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━┛""".replace('--', Fore.LIGHTBLACK_EX+'--'+Fore.RED))
    choicee = inputs()
    #Command
    if choicee == "cidr":
        CIDR()
    elif choicee == "scanport":
        ScanPort()
    elif choicee == "help":
        help()
    elif choicee == "back":
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    else:
        print('ERROR..')
        time.sleep(2)
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])





def main():
    banner()
    choicee = inputs()
    

    if choicee == "cidr":
        CIDR()
    elif choicee == "scanport":
        ScanPort()
    elif choicee == "help":
        help()
    elif choicee == "back":
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    else:
        print('ERROR..')
        time.sleep(2)
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
        

main()
