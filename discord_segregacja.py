import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Umożliwia botowi odczytywanie treści wiadomości


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} jest gotowy!')

@bot.command()
async def segregacja(ctx, typ_odpadu):
    odpady = {
        'plastik': 'Plastik wrzucamy do żółtego pojemnika.',
        'plastik_rozklad': 'Plastik rozkłada się od 100 do 1000 lat.',
        'papier': 'Papier wrzucamy do niebieskiego pojemnika.',
        'papier_rozklad': 'Papier rozkłada się 6 miesięcy.',
        'metal': 'Metal wrzucamy do żółtego pojemnika.',
        'metal_rozklad': 'Metal rozkłada się od 10 do 200 lat.',
        'zmieszane': 'Zmieszane wrzucamy do czarnego pojemnika.',
        'zmieszane_rozklad': 'Zmieszane rozkładają się średnio od 6 miesięcy do 80 lat.',
        'szklo': 'Szkło wrzucamy do zielonego pojemnika.',
        'szklo_rozklad': 'Szkło rozkłada się od 4 tysięcy do około 1 miliona lat, zależy to od temperatury czy także warunków pogodowych.'
    }
    odpowiedz = odpady.get(typ_odpadu.lower(), 'Nie znam tego typu odpadu lub komendy.')
    await ctx.send(odpowiedz)

bot.run("TOKEN")
