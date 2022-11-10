#The Imports
import os
os.system("pip install py-cord==2.0.0b1") #When run remove this line
import discord
import asyncio


bot = discord.Bot()


@bot.event
async def on_ready():
  print(f'Working as {bot.user} rubycord owner')
  
@bot.slash_command(description="Hi) # description defines what bot description is
async def hello(ctx): #async defines the command, #hello defines the bot command name
  await ctx.respond(f'Hello There {ctx.author.mention})
           
                    
                    
#Helping Stuff_______
#Make A Embed
embed = discord.Embed(title="Rubycord") #optional stuff
embed.add_field(name="rubycord, value="rubycord")
embed.add_footer(text="Rubycord")
                #sendinf
await ctx.respond(embed=embed)
 #If this errors create a report in my server or this git, with your discord username, i can also help
                #Add more commands
  
  bot.run('token')
