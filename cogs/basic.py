import discord
from discord.ext import commands
import random

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined a server.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            pass
        
        if message.content.upper().startswith('I AM') or message.content.upper().startswith("I'M") or message.content.upper().startswith("IM"):
            l = message.content.upper()
            mapping = [('I AM',''), ("I'M",''), ('IM','')]
            #message.author
            for k, v in mapping:
                c = l.replace(k, v, 1)
                if len(c) < len(l):
                    l = c
                    break
            if len(l) == 0:
                await message.channel.send("Hi no name, I'm Stove!")
                await message.author.edit(nick="no name")
            elif len(l) > 31:
                await message.channel.send("Hi " +  message.content[-len(l):31] + ", I'm Stove!")
                await message.author.edit(nick="{}".format(message.content[-len(l):31]))            
            else:
                await message.channel.send('Hi ' + message.content[-len(l):] + ", I'm Dr. Bot!")
                await message.author.edit(nick="{}".format(message.content[-len(l):]))

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes - definitely.',
                    'You may rely on it.',
                    'Most likely.',
                    'Outlook good.',
                    'Yes.',
                    'Signs point to yes.',
                    'Reply hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    'Dont count on it.',
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Very doubtful.']
        await ctx.send('Question: {}\nAnswer: {}'.format(question,random.choice(responses)))

    @commands.command()
    async def joined(self, ctx, *, member: discord.Member):
        await ctx.send('{0} joined on {0.joined_at}'.format(member))
    
    @commands.command()
    async def ppsize(self, ctx, member: discord.Member):
        print(member.id)
        await ctx.send('The size of your pp is: {}cm'.format((random.uniform(1,6))))
    
    @commands.command()
    async def brainsize(self, ctx, member: discord.Member):
        print(member.id)
        await ctx.send('The size of your brain is: {}cm³'.format((random.uniform(1000,1400))))

def setup(client):
    client.add_cog(Basic(client))