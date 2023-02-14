import os
import random, discord
from discord.ext import commands, tasks
from discord import app_commands
from itertools import cycle
import csv




intents = discord.Intents.all()
intents.members = True
client = commands.Bot(
command_prefix = ".", 
intents=intents,
case_insensitive=True)

client.remove_command('help')
# tree = app_commands.CommandTree(client)

token = "[ENTER TOKEN HERE]"


# Bot is activated and ready to be man-handled
@client.event
async def on_ready():
  print("Bot is activated properly")
  status_change.start()
  try:
    synced = await client.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)


status = cycle(['We\'re next.', 'Titans'])
# trusted users have access to the following:
  # shutdown the bot (kill)
  # yep thats about it.
Trusted = [135932078486192128]

@tasks.loop(seconds = 10)
async def status_change():


  await client.change_presence(activity=discord.Game(next(status)))

for guild in client.guilds:
  print(guild)
  print(guild.id)


@client.command(name= 'connect',aliases = ['join', 'play'], pass_context = True)
async def connect(ctx):
  if ctx.author.voice is None:
    await ctx.reply('You\'re not in a Voice Channel.')
  voice_channel = ctx.author.voice.channel
  if ctx.voice_client is None:
    await voice_channel.connect()
  else:
    await ctx.voice_client.move_to(voice_channel)


@client.command(name = 'disconnect', aliases = ['leave'])
async def disconnect(ctx):
  await ctx.voice_client.disconnect()


@client.tree.command(name="coinflip", description="Flip a coin!")

async def coinflip(interaction:discord.Interaction):
    heads_or_tails = ['<:tails:903489344185172009>','<:heads:903489327361818654> ']
    # await ctx.channel.trigger_typing()
    await interaction.response.send_message(random.choice(heads_or_tails))
    # await interaction.response.send_message("test2", ephemeral=True)





# @client.command(name="coinflip", aliases=["cf", "headsortails"], pass_context = True)
 # COIN FLIP COMMAND START---------------------------------



@client.command(name="avatar", aliases=['av'], pass_context=True)
async def avatar(ctx, member : discord.Member = None):
    avEmbed = discord.Embed(title = 'Avatar', color = 2763306)
    if member == None:
      member = ctx.author
    link = member.avatar_url
    avEmbed.set_author(name = ctx.author, icon_url = link)
    avEmbed.set_image(url = link)
    await ctx.channel.send(embed = avEmbed)





@client.command(name="purge", aliases= ['delete'])
    #check user role
async def purge(ctx, number=1):

  if ctx.author.id in Trusted:
    access = True
  else:
    access = False

  if access == True:
    print("Access Granted:", number, "messages purged successfully.")
    await ctx.channel.purge(limit = int(number)+1)
  else:
    print("Access Denied: No approved role.")



@client.command(name="ping", aliases=["latency"], pass_context=True)
async def ping(ctx):
    await ctx.channel.send('``Latency: ' + str(round(client.latency*1000)) + 'ms``')



# KEEPS THE BOT ALIVE FUNCTION CALL

#RUNS BOT WITH SECRET TOKEN

# client.run(os.environ['TOKEN']) 
client.run(token) 