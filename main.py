#  modules that the script uses
import os
from tabnanny import check
import discord
from discord.ext import commands
import time
import math
from discord_webhook import DiscordWebhook, DiscordEmbed
from bloxflippredictor import *
from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta
import uuid
import random
import json
import datetime
import string


# Setup/Configs
TOKEN="OTkyNjk0Njc1MDM3MjQ1NTEx.Ge_rjV.g8tYRJ8GrHtzWQQkG7Fcesk90iVEncgFY88HxE"
bombs=1    #  This is for maths it will show the % when one bomb is used you can make the % with this higher or lower

#  Discord bot definition
intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', help_command=None, intents=intents)
client.remove_command("help")





#all your mongo db information
mongo_db_link = 'mongodb+srv://AXOR:AXOR12345678@cluster0.f2daacq.mongodb.net/?retryWrites=true&w=majority'
databases_name = "discord" # -- Example https://ibb.co/1fpQktR
collection_name = "bot" # -- Example https://ibb.co/Fwwvbxw



#key information
role_name = "predict access"
key_prefix = "ARC" # -- Example: Discord-byXjAI



# Stuff used for predicter
ids = []


#  Event when the bot is online
@client.event
async def on_ready():
  print('Bot is online')




# Check if the round id is used
def checkid(roundid):
  if roundid in ids:
    return False
  ids.append(roundid)    #  This is not forever it will delete after the file is stopped
  
 




@client.command(name="towers")
async def towers(ctx, client_seed):
    round_id = str(client_seed)
    round_length = len(client_seed)
    if round_length == 36:
        a = random.randint(1, 3)
        b = random.randint(10, 82)
        if a == 1:
            embed = discord.Embed(
                description=f"**Towers Predictor 💎**\n**Prediction:**\n```💎⛏️⛏️\n⛏️💎⛏️\n💎⛏️⛏️\n⛏️⛏️💎\n💎⛏️⛏️\n⛏️💎⛏️\n💎⛏️⛏️\n⛏️💎⛏️```\n**Accuracy**\n```{b}%```\n**Client Seed**\n```{client_seed}```")
            embed.set_footer(text="buy @ discord.gg/pTFamhRP6V")

            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/1025031754853142540/1030875187094241290/rjanhrt.png")
            await ctx.reply(embed=embed)
        if a == 2:
            embed = discord.Embed(
                description=f"**Towers Predictor 💎**\n**Prediction:**\n```💎⛏️⛏️\n⛏️💎⛏️\n⛏️⛏️💎\n⛏️💎⛏️\n⛏️💎⛏️\n⛏️💎⛏️\n💎⛏️⛏️\n💎⛏️⛏️```\n**Accuracy**\n```{b}%```\n**Client Seed**\n```{client_seed}```")
            embed.set_footer(text="buy @ discord.gg/pTFamhRP6V")

            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/1025031754853142540/1030875187094241290/rjanhrt.png")
            await ctx.reply(embed=embed)
        if a == 3:
            embed = discord.Embed(
                description=f"**Towers Predictor 💎**\n**Prediction:**\n```💎⛏️⛏️\n⛏️💎⛏️\n⛏️⛏️💎\n⛏️💎⛏️\n💎⛏️⛏️\n⛏️💎⛏️\n⛏️⛏️💎\n⛏️⛏️💎```\n**Accuracy**\n```{b}%```\n**Client Seed**\n```{client_seed}```")
            embed.set_footer(text="buy @ discord.gg/pTFamhRP6V")

            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/1025031754853142540/1030875187094241290/rjanhrt.png")
            await ctx.reply(embed=embed)
    else:
        await ctx.reply("Invalid client seed")






  
@client.command(name="help")
async def help(ctx):
    embed = discord.Embed(title="ARC Predictions",
                          description="**.help**\nShows this Message\n**.redeem <code> <member u want to give access too> ONLY 1 TIME**\nit whitelists the guy \n**.crash**\nHelps you with the outcome of the next game of crash\n**.mines <amount of mines> <round id>**\nHelps you with the outcome of the next game of mines\n**.roulette**\nHelps you with the outcome of the next game of roulette\n**.towers**\nHelps you with the next outcome of the next game of towers")
    embed.set_footer(text="buy @ https://discord.gg/pTFamhRP6V")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1025031754853142540/1030875187094241290/rjanhrt.png")
    await ctx.reply(embed=embed)






  
#  Mines predictor
@client.command(name="mines")
async def reg(ctx, e):
    a = len(e)
    if a == 36:    #  Checks if the message is 36 characters long
      await ctx.send(f'Trying to get to the api of  ```{e}```')
      if checkid(e) == False:
        return
      await mines(ctx, e)    #  Starts the mine predictor
    else:
      time.sleep(2)
      await ctx.send('invalid round id')



# Mines predictor code
async def mines(ctx, e):
    def check(msg):
      return msg.author == ctx.author and msg.channel == ctx.channel
    tiles = list(range(1,26))
    time.sleep(2)
    await ctx.send(f'How many Tokens do you want? {ctx.author.mention} ')
    msg = await client.wait_for("message", check=check)
    msgo = int(msg.content)
    totalsquaresleft = 25
    formel = ((totalsquaresleft - bombs) / (totalsquaresleft))
    totalsquareslefts = 24
    formel2 = ((totalsquareslefts - bombs) / (totalsquareslefts))
    output=minespredictor(msgo, bombs)
    end = formel2 * 100
    multiplier = calculate_multiplier(msgo, bombs)
    embed=discord.Embed(title="Mines Predictor", description=f" **Predicting:** ```{e}```")
    embed.add_field(name="Prediction", value=output, inline=False)
    embed.add_field(name="Accuracy", value=f"```wheres your trust with this predictor...```", inline=False)
    embed.set_footer(text="buy @ https://discord.gg/pTFamhRP6V")
    await ctx.send(ctx.author.mention, embed=embed)

#  Maths for mines
def nCr(n,r):
  f = math.factorial
  return f(n) // f(r) // f(n-r)

def calculate_multiplier(bombs, msgo):
  house_edge = 0.01
  return (0.96 - house_edge) * nCr(25, msgo) / nCr(25 - bombs, msgo)




#  Crash could get banned from the api



@client.command(name='crash')
async def crash(ctx):
                chan = False
                varName = crashpredictor()
                if type(varName) == dict:
                  pass
                else:
                 await ctx.send(varName)
                 return
                chance = varName['crashchance']
                prediction = varName['crashprediction']
                if float(chance) > 2:
                    color = 0x81fe8f
                else:
                    color = 0xfe8181
                if float(chance) >= 80:
                 
                 desc = f"""
        **Crashpoint:**
        *{prediction:.2f}x*
        **High chance:**
        ```{chance:.2f}%```"""
                else:
                 desc = f"""
        **Crashpoint:**
        *{prediction:.2f}x*
        **normal chance:**
        ```{chance:.2f}%```"""
                if float(chance) <= 10:
                 desc = f"""
        **Crashpoint:**
        *{prediction:.2f}x*
        **Low chance:**
        ```{chance:.2f}%```"""

                  

                em=discord.Embed(description=desc,color=color)
                await ctx.reply(embed=em)
   

   
  
  
# Roulette predictor
@client.command(name="roulette")
async def roulette(ctx):
  output = roulettepredictor()
  embed=discord.Embed(title="Roulette Predictor")
  embed.add_field(name="Roulette", value=output, inline=False)
  embed.set_footer(text="buy @ https://discord.gg/pTFamhRP6V")
  await ctx.reply(embed=embed)








@client.command(name="gen")
@commands.has_permissions(manage_roles=True)  
async def gen(ctx, amount, time):
   key_int = int(amount)
   amount = key_int
   key_amt = range(int(amount))
   time = int(time)

   # -- Connect to database n shit
   mongo_url = mongo_db_link
   cluster = MongoClient(mongo_url)
   db = cluster[f"{databases_name}"]
   collection = db[f"{collection_name}"]

   # -- Expiration
   now = datetime.datetime.today()
   future = now + timedelta(days=time)
   expires = future.strftime("%y-%m-%d")

   # -- Key
   key_yes = f"{key_prefix}-fkEPsG"
   if key_int == 1:
      letters = string.ascii_letters
      key = f"{key_prefix}-" + ''.join(random.choice(letters) for i in range(6))
   elif key_int < 1:
      em = discord.Embed(color=0xff0000)
      em.add_field(name="Invalid number", value="Key amount needs to be higher than 0")
      await ctx.send(embed=em)
      return 0
   elif key_int > 1:
      amount = key_int - 1
      key_number = 1
      key_amt = range(int(amount))
      for i in key_amt:
         letters = string.ascii_letters
         key = f"{key_prefix}-" + ''.join(random.choice(letters) for i in range(6))
         em = discord.Embed(color=0xff0000)
         em.add_field(name=f"Key: {key_number}", value=key)
         await ctx.send(embed=em)
         key_number += 1
         post = {"key": key, "expiration": expires, "user": "Empty", "used": 'unused'}
         collection.insert_one(post)
      key = f"{key_prefix}-" + ''.join(random.choice(letters) for i in range(6))
   
   # -- collection.delete_many({}) #deletes all the keys

   # -- Send all info to discord and database
   message = await ctx.send("Connecting...")
   try:
      if key_int == 1:
         key_yes = key
      else:
         key_yes = f'{key_prefix}-fkEPsG'
         pass

      #sends key info to database
      
      post = {"key": key, "expiration": expires, "user": "Empty", "used": 'unused'}
      collection.insert_one(post)

      #make our embed that sends when key is genned
      em = discord.Embed(color=0x00ff00)
      em.add_field(name="\n" + "discord", value="**Key generated!**" + "\n" +
         "key: " + key + "\n" + "Expires: " + str(time) + " days" +  "\n" + "\n"
         + "**Redeem Key**" + "\n" + f"Redeem the key by typing ```.redeem {key}```")
      await message.delete()
      await ctx.send(embed=em)
   except:
      em = discord.Embed(color=0xff0000)
      em.add_field(name="Api did not respond", value="Could not generate key")
      await ctx.send(content="", embed=em)


@client.command(name="redeem")     
#redeem function
async def redeem(ctx, key):
   mongo_url = mongo_db_link
   cluster = MongoClient(mongo_url)
   db = cluster[f"{databases_name}"]
   collection = db[f"{collection_name}"]
   try:
      results = collection.find({"key": key})
      for results in results:
         if results['key'] == str(key):
            collection.update_one({"key": key}, {"$set":{"user": ctx.author.id}})
            expiration = str(results['expiration'])
            used = str(results['used'])
            if used == 'used':
               em = discord.Embed(color=0xff0000)
               em.add_field(name="Key already used", value="the key you entered has already been used")
               await ctx.send(embed=em)
            elif used == 'unused':
               role = role_name
               user = ctx.message.author
               await user.add_roles(discord.utils.get(user.guild.roles, name=role))
               em = discord.Embed(title="discord", color=0x00ff00)
               em.add_field(name="Redeemed!", value="You have successfully redeemed the key"
               + "\n" + "\n" + f"Key will expire on {expiration}")
               await ctx.send(embed=em)
               collection.update_one({"key": key}, {"$set":{"used": 'used'}})
               return
               
         else:
            em = discord.Embed(title="discord", color=0xff0000)
            em.add_field(name="Invalid key", value="The key you entered was invalid.")
            await ctx.send(embed=em)
   except:
      pass


  
  

  

  
  
#  Runs the token
try:
  client.run(TOKEN)
except:
    os.system("invalid token")
