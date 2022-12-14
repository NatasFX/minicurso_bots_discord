from discord.ext import commands
from os.path import exists
import discord
import pickle
import random
import asyncio

from secret import TOKEN


client = commands.Bot(intents=discord.Intents.all(), command_prefix=',')

####################################

# funções utilitárias para utilizar o Pickle, assunto da aula 3
def load_pickle(default, filename):
    if exists(f'./db/{filename}.pickle'):
        with open(f'./db/{filename}.pickle', 'rb') as f:
            return pickle.load(f)
    else:
        with open(f'./db/{filename}.pickle', 'wb') as f:
            pickle.dump(default, f)
            return default

def save_pickle(obj, filename):
    with open(f'./db/{filename}.pickle', 'wb') as f:
        pickle.dump(obj, f)

#####################################


#####################################

# variáveis para utilizar nos comandos
prefixos_disponiveis = [
    '.',
    ';',
    ';;',
    '?',
    '??',
    '!',
    '$',
    '$$',
    '%',
    '%%',
    '+',
    '++',
    '<',
    '>',
    '&',
    '-',
    '--',
    ':',
    '@',
    '@@',
    '=',
    '==',
    '_'
]

prefixos_designados = load_pickle({}, 'used_prefixes')

# quem adicionou qual bot
user_add_bot = load_pickle({}, 'user_add_bot')

######################################


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
        async for entry in member.guild.audit_logs(action=discord.AuditLogAction.bot_add):
            if entry.target == member:
                print(f'Usuário {entry.user.name} adicionou o bot {entry.target.name}')
                if entry.user.id not in user_add_bot:
                    user_add_bot[entry.user.id] = entry.target.id
                    save_pickle(user_add_bot, 'user_add_bot')
                elif entry.target.id not in user_add_bot.values() and entry.user.id != 283345376231292929:
                    await member.kick()
                    await client.get_channel(1051004621264523358).send(f'{entry.user.mention}, você não pode adicionar mais de 1 bot neste servidor!')
                    return
                
                break

        cargo_id = 1051023074142715974


    await member.add_roles(client.get_guild(1051004621264523355).get_role(cargo_id)) # Adiciona cargo "Humanos" ou "Máquinas de Turing"


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)


@client.command()
async def prefixo(context):
    
    random.shuffle(prefixos_disponiveis)

    if len(prefixos_disponiveis) == len(prefixos_designados):
        await context.reply('Poxa, eu não conheço tantos prefixos assim... Pede ajuda pro Natã escolher um pra ti')
        return

    if context.author.id in prefixos_designados:
        await context.reply(f'Eii {context.author.mention}, eu já escolhi um prefixo pra você! Use `{prefixos_designados[context.author.id]}`')
        return

    if context.author.id not in user_add_bot:
        await context.reply(f'Eii {context.author.mention}, você ainda não adicionou seu bot neste servidor!')
        return

    for prefix in prefixos_disponiveis:
        if prefix not in prefixos_designados.values():

            m = context.guild.get_member(user_add_bot[context.author.id])
            await m.edit(nick=f'[ {prefix} ] {m.name}')

            prefixos_designados[context.author.id] = prefix
            save_pickle(prefixos_designados, 'used_prefixes')
            break

    await context.typing()

    await asyncio.sleep(2)

    embed = discord.Embed(
        title=f'Prefixo de {context.author.name if context.author.nick == None else context.author.nick}',
        description=f'Seu prefixo é `{prefix}`, parabéns!!\n\nVocê já pode utilizar em seu bot <@{user_add_bot[context.author.id]}>',
        color=discord.Color.blue()
    )

    mensagem = await context.reply(embed=embed)

    await mensagem.pin()


@client.command()
async def par(context, num):
    if not num.isdigit():
        await context.reply('Digite um número!')
    else:
        num = int(num)
        await context.channel.send(f'{num} é {"PAR" if num%2 == 0 else "ÍMPAR"}!')
   

@client.command()
async def oi(context, *nome):
    if len(nome) == 0:
        await context.reply('Ei, cadê seu nome? Eu sei que você tem!! 👀')
    else:
        await context.channel.send(f'Oii {" ".join(nome)}!')

client.run(TOKEN)
