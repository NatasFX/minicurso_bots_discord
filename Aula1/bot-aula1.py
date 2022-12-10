import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logado com sucesso como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!oi'):
        await message.channel.send(f'Oii {message.author.mention}!')

client.run('COLE SEU TOKEN AQUI DENTRO, NÃO REMOVA AS ASPAS SIMPLES')
