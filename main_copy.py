
# IMPORT DISCORD.PY and others
import discord
import random
import os
import datetime
import asyncio
import pytz
from discord.ext import commands, tasks

# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv

# Loads the .env file that resides on the same level as the script.
load_dotenv()

# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL = os.getenv("CHANNEL")
USER_ID = os.getenv("USER_ID")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()
bot = commands.Bot("$") #idk too lol

# roger timezone
timezone = pytz.timezone("Asia/Singapore")
print(timezone.localize(datetime.datetime.now()))


# create the 727 alarm
@tasks.loop(hours=12)
async def called_twice_a_day():
    await bot.wait_until_ready()
    c = bot.get_channel(CHANNEL)
    await c.send("@everyone 727 WYSI")

@called_twice_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    
    while True:
        now = timezone.localize(datetime.datetime.now())
        if now.strftime("%I:%M") == "07:27":
            break
        await asyncio.sleep(15)
    print("Finished waiting")

called_twice_a_day.start()


# create the skill issue alarm
@tasks.loop(minutes=180)
async def skill_issue_call():
    # checks that the time isnt ungodly lol i aint that evil
    now = timezone.localize(datetime.datetime.now())
    if not (int(now.strftime("%H")) < 8 or int(now.strftime("%H")) > 22):
        await bot.wait_until_ready()
        c = bot.get_channel(CHANNEL)
        USER_IDS = "<@" + USER_ID + ">"
        await c.send(f"{USER_IDS} has skill issue")
    
    # edit the interval
    n = random.randint(150, 300)
    skill_issue_call.change_interval(minutes=n)
    #print(n)

skill_issue_call.start()


# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")


# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    # checks if author is the bot
    if message.author == bot.user:
        return

    # sets up the 727 quotes
    seventwentyseven_quotes = [
        "STOP POSTING ABOUT 727 IM TIRED OF SEEING IT, my friend's on tik tok send me memes on discord it's fucking memes, I was in a server right, and ALL of the channels were just 727 stuff, I showed my clock to my girlfriend and it was the number and I said. \"Hey babe, When you see it\" insert blue zenith I looked at the Boeing 727 and I said that's a bit familiar, I looked at the Railway Battalion in Camp Shelby, Mississippi from ww2 and I think about shigetora and i was like Camp Shelby more like 727 AAAAAAAAAAAAAAAAAAAAAAAA",
        "I can't fucking take it. I see an image of a random score posted and then I see it, I fucking see it. \"Oh that looks kinda like the Blue Zenith 727 score\" it started as. That's funny, that's a cool reference. But I kept going, I'd see a clock with time that showed 7:27, I'd see that I'm on the 7/27 page on my school homework, my last notice to pay my electricity bill is 727$ , I'd notice that it's been 727 days since the last time I touched a woman. And every time I'd burst into an insane, breath deprived laugh staring at the image as the number 727 ran through my head. I'm scared to look at the time when someone asks me what time is it. It's torment, psychological torture, I am being conditioned to laugh maniacly any time I see an 3-digit number which is anywhere close to 727. I can't fucking live like this... I can't I can't I can't I can't I can't! And don't get me fucking started on the words! I'll never hear the phrase \"when you see it\" again without thinking of 727. Someone does pretty cool and respectable score and I can't say anything other than \"WYSI.\" I could watch a man Fc hard underweighted map I love and all I would be able to say is \"WYSI\" and laugh like a fucking insane person. And the phrase \"when you see it\" is ruined. I can't live anymore. 727 has destroyed my fucking life. I want to eject myself from this plane of existence.",
        "Help I'm seeing 727 everywhere around me. While checking the time I coincidentally happen to see it at 7:27 it happens like 3-4 times a week. I usually wake up at 9:00 but few days ago I woke up early and checked the time, it was 7:27 AM. I was playing clash of clans and collected my dark elixir, it happened to be fucking 727. I'm not kidding this shit is making my mind crazy."
    ]
    
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    if message.content.lower() == "$wysi good bot":
        # SENDS BACK A MESSAGE TO THE CHANNEL.
        await message.channel.send("<3")

    elif message.content.lower() == "$wysi bad bot":
        await message.channel.send(f"Fuck you {message.author.mention}")
    
    #elif message.content == "$wysi help":
        #await message.channel.send("$wysi good bot\n$wysi bad bot\n$wysi 727\n$wysi link")

    elif message.content.lower() == "$wysi 727":
        response727 = random.choice(seventwentyseven_quotes)
        await message.channel.send(response727)

    elif message.content.lower() == "$wysi link":
        await message.channel.send("https://youtu.be/AaAF51Gwbxo")
    
    elif message.content.lower() == "$wysi skill issue":
        USER_IDS = "<@" + USER_ID + ">" 
        await message.channel.send(f"{USER_IDS} has skill issue")

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. 
bot.run(DISCORD_TOKEN)







