import os
import random
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

mensajes = [
    "¡Sos un grande, rey! Ninguna mala racha dura para siempre. 👑",
    "Recordatorio diario: Valés un Perú y se vienen cosas mejores. 🔥",
    "¡El terroncito de azúcar no se derrite por nadie! 💪",
    "Hoy es un buen día para jugar unas partidas y olvidarse del resto. 🎮"
]

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def animar(ctx):
    frase = random.choice(mensajes)
    await ctx.send(frase)

bot.run(TOKEN)
