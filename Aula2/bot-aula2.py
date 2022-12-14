import discord
from discord.ext import commands

client = commands.Bot(intents=discord.Intents.all(), command_prefix='COLOQUE AQUI O PREFIXO QUE VOCÊ GANHOU DO BOT')

@client.event
async def on_ready():
    print(f'Logado com sucesso como {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    await client.process_commands(message)


@client.command()
async def oi(context, *nome):
    if len(nome) == 0:
        await context.reply('Ei, cadê seu nome? Eu sei que você tem!! 👀')
    else:
        await context.channel.send(f'Oii {" ".join(nome)}!')

client.run('SEU TOKEN')
