import os

import discord
import asyncio
import random

from dotenv import load_dotenv
from collections import Counter

intents = discord.Intents.default()
intents.members = True
intents.presences = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.change_nicknames())

    async def on_ready(self):
        print('--------------------------------------------------')
        print(f'Logged in as: {self.user.name} {self.user.id}')
        print('--------------------------------------------------')

    async def change_nicknames(self):
        baseNick = 'kingchris'
        nicknames = ['xX_EdgeGod69_Xx', 'Stephen', 'Gus', 'Matt', 'Cam', 'Josie', 'Poop Sock', 'UwU', 'OwO', 'HewWo?', 'Gus\'s Ex Wife', 'Bryce', 'Higoo', 'kingchris69', 'Herman',
                     'Hubert', 'Garret', ' ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽', 'oops', 'Groovy', 'Dynamic Channel Name Bot', 'a',
                     'Why have you done this', 'Inigo Montoya', 'bjork', 'gub', '#1undisputedbestadcinworld', 'team green', 'skrillecks', '#1undisputedworstadcinworld', 'Bot', 'z',
                     'Help a bot changed my name', 'surprise', "I have clinical depression", 'FAKER WHAT WAS THAT?!?', 'LOOK AT THE CLEANSE', 'LOOK AT THE MOVES', 'I\'m bored',
                     'PHREAK, YOU HAVE NO MANA', 'Moment De La Bruh', 'Why are we here? Just to suffer?', 'MONKE', 'SEJUANI??', 'make soup', 'mojo jojo this pack I power puff',
                     '10 Hours of Sea Shanties', 'Mii Channel Music - 10 Hours', 'zed is not melee', 'it me maro', 'Green Team 4Ever', 'Unregistered Hypercam 2', 'dont talk me angy']
        await self.wait_until_ready()
        while not self.is_closed():
            for guild in self.guilds:
                tempNickList = nicknames.copy()
                modifier = 234
                chrisTime = random.randint(0, 49)
                for user in guild.members:
                    if(user.name == 'Groovy'):
                        await user.edit(nick = 'Groovy')
                    elif(user.name == 'Dynamic Channel Name Bot'):
                        await user.edit(nick = 'DCN Bot')
                    elif(user.guild_permissions.administrator != True):
                        if(chrisTime == 0):
                            tempNick = f'kingchris{modifier}'
                            modifier += 1
                        else:
                            if(len(tempNickList) > 0):
                                tempNick = random.choice(tempNickList)
                                tempNickList.remove(tempNick)
                            else:
                                if(user.name == 'kingchris233'):
                                    tempNick = 'kingchris233'
                                else:
                                    tempNick = f'kingchris{modifier}'
                                    modifier += 1
                        await user.edit(nick=tempNick)
                await asyncio.sleep(86400) #Randomizes Once a day

client = MyClient(intents = intents)
client.run(TOKEN)