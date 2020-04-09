# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:40:42 2020

@author: steve
"""
import discord
import token
from discord.ext import commands
import os
print(discord.__version__)

import os

client = commands.Bot(command_prefix = '.')

@client.command()
async def load(ctx, extension):
    client.load_extension('cogs.{}'.format(extension))

@client.command()
async def unload(ctx, extension):
    client.unload_extension('cogs.{}'.format(extension))

@client.command()
async def reload(ctx, extension):
    client.unload_extension('cogs.{}'.format(extension))
    client.load_extension('cogs.{}'.format(extension))

for filename in os.listdir(r'./cogs'):
    print(filename)
    if filename.endswith('.py'):
        client.load_extension('cogs.{}'.format(filename[:-3]))

client.run(os.getenv('TOKEN'))