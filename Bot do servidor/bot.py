import discord
from secret import TOKEN

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logado com sucesso como {client.user}')


# esta função é executada em todo novo usuário que entra nos servidores onde o bot está
@client.event
async def on_member_join(member):
    
    if not member.bot:
        await client.get_channel(1051004621264523358).send(f'Bem-vindo usuário {member.name}!')
        cargo_id = 1051022995067519006
    else:
        cargo_id = 1051023074142715974
        
    await member.add_roles(client.get_guild(1051004621264523355).get_role(cargo_id)) # Adiciona cargo "Humanos" ou "Máquinas de Turing"


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!hehe'):
        await message.channel.send(f'HMM alguém olhou o github do minicurso e achou um comando escondido! {message.author.mention}')

client.run(TOKEN)
