import discord
from cards import cartas
from discord.ext import commands
import asyncio
import random

id_do_server = 1096549820421902458
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix="!")


@bot.event
async def on_ready():
  print('Bot is ready!')


@bot.command(name='DMzinha')
async def secret(ctx):
  try:
    name = ctx.author.name
    await ctx.author.send(f'O {name} testou a DM')
  except discord.errors.Forbidden:
    await ctx.send(
        'Não consigo te enviar a DM, habilite a opção de receber mensagem de todos em Privacidade'
    )


@bot.command(name='foto')
async def get_random_image(ctx):
  url_image = 'https://picsum.photos/200/300'
  embed = discord.Embed(
      title='Teste de procura de imagens',
      description=
      'A imagem é aleatória',
      color=discord.Color.blue())
  embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
  embed.add_field(name='Imagem', value=url_image)
  embed.add_field(name='Link', value='https://picsum.photos/200/300')
  embed.add_field(name='Teste',
                  value='Teste texto',
                  inline=False)
  embed.set_footer(text=ctx.bot.user.name, icon_url=ctx.bot.user.avatar.url)
  embed.set_image(url=url_image)
  await ctx.send(embed=embed)


total_probabilidade = sum(cartas[carta]['probabilidade'] for carta in cartas)
for carta in cartas:
  cartas[carta]['probabilidade'] /= total_probabilidade


def sortear_carta():
  carta_sorteada = random.choices(
      list(cartas.keys()),
      weights=[carta['probabilidade'] for carta in cartas.values()],
      k=1)
  return carta_sorteada[0]


@bot.command(name='pack_test')
async def pack_test(ctx):
  await ctx.send('Abrindo o pack...')
  await asyncio.sleep(5)
  carta_sorteada = sortear_carta()

  embed = discord.Embed(
      title='Teste de pack',
      description=
      f'PARABÉNS {ctx.author.mention} PELA CARTA DO: {carta_sorteada}\n probailidade: {cartas[carta_sorteada]["probabilidade"]*100}',
      color=discord.Color.blue())
  embed.set_image(url=cartas[carta_sorteada]['Imagem_da_carta'])
  await ctx.send(embed=embed)

#O código abaixo foi feito pelo bem do humor
@bot.command(name='Lula')
async def Lula_Neymar(ctx):
  try:
    name = ctx.author.name
    await ctx.author.send(
        'https://tenor.com/view/lula-da-silva-jair-bolsonaro-presidente-2022-elenao-gif-26628518'
    )
  except discord.errors.Forbidden:
    await ctx.send(f'Vai tomar no cu {name}')


bot.run(
    'TOKEN')
