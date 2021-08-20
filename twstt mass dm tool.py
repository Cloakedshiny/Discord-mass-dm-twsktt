import discord
from discord.ext import commands
import colorama 
import os
from colorama import Fore
client = commands.Bot(command_prefix = 'a niglet', help_command = None)
# this made me attract 100 gurls at my door 

colorama.init()
token = input("Input Token>>")
@client.event
async def on_ready():
 os.system('cls')
 print(f'''
{Fore.CYAN}                        
{Fore.RED}     
{Fore.RED}                                                       
{Fore.RED}                   ████████╗██╗    ██╗   ███████╗   ██╗  ██╗████████╗████████╗
{Fore.RED}                   ╚══██╔══╝██║    ██║   ██╔════╝   ██║ ██╔╝╚══██╔══╝╚══██╔══╝
{Fore.RED}                      ██║   ██║ █╗ ██║   ███████╗   █████╔╝    ██║      ██║   
{Fore.RED}                      ██║   ██║███╗██║   ╚════██║   ██╔═██╗    ██║      ██║   
{Fore.RED}                      ██║██╗╚███╔███╔╝██╗███████║██╗██║  ██╗██╗██║██╗   ██║   
{Fore.RED}                      ╚═╝╚═╝ ╚══╝╚══╝ ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝   ╚═╝   
{Fore.RED}                          
{Fore.RED}                                        By Wakii™#0001             
{Fore.RED}                                         [1] Mass Dm 
{Fore.RED}                                         [2] Mass Friend [Soon]                                                 
''')
 fuck = input(f"{Fore.RED}Select>>")
 if fuck == '1':
  input2 = input(f"{Fore.WHITE}What Should I Send?>>")
  for user in client.user.friends:                
   await user.send(f"{input2}")
   print(f"{Fore.RED}[+] Sent{Fore.WHITE} {input2} To {user}")

client.run(token, bot = False)