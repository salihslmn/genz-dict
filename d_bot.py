import discord
from discord.ext import commands
import os
import random
import requests

print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
img_name = random.choice(os.listdir('images'))

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    # Dosya adını bir değişkenden bu şekilde değiştirebilirsiniz!
    with open(f'images/{img_name}', 'rb') as f:
         picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)
    

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']


@bot.command('fox')
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)

def get_tokyo_anime_image_url():    
    url = 'https://kitsu.io/api/edge/anime?filter[text]=tokyo'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('tokyo_anime')
async def tokyo_anime(ctx):
    image_url = get_tokyo_anime_image_url()
    await ctx.send(image_url)


def get_çevre_image_url():    
    url = 'https://cevre.mersin.bel.tr/cevre-icin-neler-yapabiliriz/'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('çevre')
async def çevre(ctx):
    image_url = "https://cevre.mersin.bel.tr/cevre-icin-neler-yapabiliriz/"
    await ctx.send(image_url)
































bot.run("MTQ2NzE4MzUzNTI1MjE4MTA0NQ.GARVRG.vXMEcuikFSGfU_MLhK5StfHDI__1qMEiUxCjg8")
