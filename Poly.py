import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ">")

words = {
    "Fuck": "Fridge",
    "Shit": "Salamanders",
    "Bitch": "Beach Ball",
    "Asshole": "Aviator",
    "Motherfucking": "Mountain Top",
}
patterns = []

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    global patterns
    global poli
    global new_xic
    global words
    global the_message
    global sec_message
    global q
    q = "False"
    for word in words:
        new_word = word.lower()
        Polop = message.content.lower()
        if new_word in Polop:
            old_message = Polop
            new_message = old_message.split(new_word)
            a_message = new_message[1]
            for x in a_message:
                if x.isspace():
                    a_message.split(x)
                    break
            the_message = new_message[0]
            sec_message = a_message[1:]
            await message.delete()
            await message.channel.send(the_message + words[word] + " " + sec_message)
            patterns.append(the_message + " " + sec_message)
            q = "True"

    if q == "False":
        Zircon = message.content
        for pattern in patterns:
            if pattern in Zircon:
                for content in Zircon:
                    if content.isspace():
                        cons = Zircon.split(content)
                        for con in cons:
                            if not con in pattern:
                                leta = con[0]
                                words[con] = leta + "alloon"
                                break
                        
    
client.run(token)
