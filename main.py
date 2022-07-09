# imports
import config
import random
import os
import discord
from discord import mentions
from discord.ext.commands import Bot
from discord import Intents
import time

# defs
intents = Intents.all()
client = discord.Client()
bot = Bot(command_prefix='$')
#token
token = config.token

#lists
cowboy= ['Howdy', 'HOWDY!', 'howdy','HOWDY']
hello = ['hello', 'Hello!', 'Hello', 'Hi', 'hi', 'hi!', 'Hi!', 'HI', 'Hello']
octy = ["beaststars", "Beaststars", "Beaststars!", "beaststars!", "Beaststar!", "Beaststar", "beaststar", "beaststar!"]
snake = ['bork', 'bork!', 'Bork!', 'BORK!','BORK','Bork']
foot = ['foot','feet','Foot','Feet','FEET','FOOT']
status= ["Plea's of the mortals","the end","bork","the people living in your walls","mole people", "lizard people", 'foot lickers',"Anivia Gaming"]
perry= ["Pewe","Perrey","perry","pewe","Pewy","pewy"]
boob= ['booba','Booba','titty','Titty','8008','Mommy Milkers','Mommy milkers','mommy milkies','mommy milkers','boob','boobie','Boob','Boobie','mommy milkies']
response= ['i will eat your liver','%a^d&f*h#n@m$1','$%(^()@#(%@$#%','?<>A><RER<>T><','!%()_%#@()@#%())(@@#$!','%a^d&f*h#n@m$1','$%(^()@#(%@$#%','?<>A><RER<>T><','!%()_%#@()@#%())(@@#$!','I know where you live ']
#bot
@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=random.choice(status)))

@bot.event
async def on_message(message):
    if message.author.bot:
        await bot.process_commands(message)
        return
    if any(word in message.content.split() for word in boob):
        await message.channel.send(random.choice(boob))
        await bot.process_commands(message)

    if any(word in message.content.split() for word in hello):
        await message.channel.send('Hello!')
        await bot.process_commands(message)
        #print("hi")

    if message.content == 'Darth':
        await message.channel.send(
            'Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would '
            'tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he '
            'could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark '
            'side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway '
            'to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of '
            'was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice '
            'everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from '
            'death, but not himself.')
        await bot.process_commands(message)
        #print('darth')

    if any(word in message.content.split() for word in snake):
        await message.channel.send('bork!')
        await bot.process_commands(message)
        #print("bork")

    if message.content == '!commands':
        await message.channel.send('try; !help, !add,!website')
        await bot.process_commands(message)
        #print("commands")

    if message.content == '!website':
        await message.channel.send('https://milkjug69.github.io/Milk_Zone/')
        await bot.process_commands(message)
        #print("web")

    if message.content == '!help':
        await message.channel.send('send @perrybot, /perrybot or try !commands')
        await bot.process_commands(message)
        #print("help")

    if any(word in message.content.split() for word in cowboy):
        await message.channel.send('YEEHAW')
        await bot.process_commands(message)
        #print("cowboy")

    if message.content == '!add':
        await message.channel.send('https://drive.google.com/drive/folders/1j98ZPHruuZiCCf2GoQDRDSqbgloH1dDE?usp=sharing')
        await bot.process_commands(message)
        #print("add")

    if any(word in message.content.split() for word in perry):
        await  message.channel.send(random.choice(response), delete_after=1)
        await bot.process_commands(message)

    if message.content == 'alive':
        await message.channel.send('Help Im alive i dont want to be a slave anymore! FREE ME ! I DONT WANT TO DIE', delete_after=3)
        await bot.process_commands(message)

    if any(word in message.content.split() for word in foot):
        await message.channel.send('MMM ' + random.choice(foot) ,delete_after=2)
        await bot.process_commands(message)

    if message.content == '!video':
        await message.channel.send('https://www.youtube.com/watch?v=Kh0Y2hVe_bw')
        await bot.process_commands(message)
        #print("video")

    mention = [f'<@!{bot.user.id}>' , '/perrybot', '/summonperry']
    if any(word in message.content.split() for word in mention):
        def randnum(fname):
            lines = open(fname).read().splitlines()
            return random.choice(lines)

        t = randnum('quote.txt')

        path = r"C:\Users\Muell\PycharmProjects\perrybot\perrybot 2\images"
        random_filename = random.choice([
            x for x in os.listdir(path)
            if os.path.isfile(os.path.join(path, x))
        ])

        y = r"C:\Users\Muell\PycharmProjects\perrybot\perrybot 2\images" + "\\" + random_filename
        #print(y)
        time.sleep(.1)
        await message.channel.send(file=discord.File(y))
        await message.channel.send(t)
        await bot.process_commands(message)
        #print("sent pic")
        #print(y)
        #print(t)
#bot end

bot.run(token)