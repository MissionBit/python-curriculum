import discord

client = discord.Client()

names = {}

@client.event
async def on_ready():
  print('Logged in')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  await message.channel.send("Hi there! Replace we with your favorite greeting.")

client.run('YOUR_CLIENT_HERE')

##To run your bot and try it out, go to the shell on the right and type: 

## python3 projects/discord/discord_bot.py

##Try out the bot by adding it to your server and interact!


'''
Week 3:
Create a discord bot and add the client ID in the “YOUR_CLIENT_HERE” section of discord_bot.py

Instructions to create the bot and find the client ID: https://discord.com/developers/docs/intro

Extra instructions here: https://www.freecodecamp.org/news/create-a-discord-bot-with-python/

Send a message from the channel in the on_message method
Play around with on_message and explore the discord variables

Week 4:
Send a message prompt in on_message asking for a name and score

Use string parsing to store the name and score in the names dictionary

Print out the names dictionary in a clear format

'''
