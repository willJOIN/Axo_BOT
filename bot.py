import discord
from discord.ext import commands
import dotenv
import os

client = commands.Bot(command_prefix=".")


@client.command()
async def oi(ctx):
    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await ctx.send("Oiiie!")
    voice_client.play(discord.FFmpegOpusAudio("assets\som1.mp3"))


@client.command()
async def meme(ctx):
    voice_channel = ctx.author.voice.channel
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await ctx.send(file=discord.File("assets\meme.gif"))
    voice_client.play(discord.FFmpegOpusAudio("assets\som2.mp3"))


@client.command()
async def love(ctx):
    voice_channel = ctx.author.voice.channel
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await ctx.send(
        "while(true){Te amo! :blue_heart: :white_heart: :smiling_face_with_3_hearts: :white_heart: :blue_heart:;}"
    )
    voice_client.play(discord.FFmpegOpusAudio("assets\som3.mp3"))


@client.command()
async def desenho(ctx):
    voice_channel = ctx.author.voice.channel
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await ctx.send(file=discord.File("assets\desenho.png"))
    voice_client.play(discord.FFmpegOpusAudio("assets\som3.mp3"))


@client.command()
async def tchau(ctx):
    voice_channel = ctx.author.voice.channel
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    try:
        if voice_client.is_connected():
            await ctx.send("Tchau tchau!")
            await voice_client.disconnect()
    except:
        await ctx.send("Não estou no canal agora!")


dotenv.load_dotenv(dotenv.find_dotenv())
token = os.getenv("token")
client.run(token)
