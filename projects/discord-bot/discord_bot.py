import discord

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in')

@client.event
async def on_message(message):
  '''
  This function is called whenever any message is sent on the server, including those sent by the
  bot itself!

  Docs for `message`: https://discordpy.readthedocs.io/en/latest/api.html#discord.Message
  '''
  # Ignore messages sent by the bot
  if message.author == client.user:
    return
  await message.channel.send('Hello!')

client.run('<YOUR DISCORD BOT TOKEN HERE>')
